import type { Author, Category, Post } from "@/types/blog";
import { authors, categories, posts } from "@/lib/mock-data";
import {
  WP_CATEGORIES_QUERY,
  WP_POST_BY_SLUG_QUERY,
  WP_POSTS_BY_CATEGORY_QUERY,
  WP_POSTS_QUERY
} from "@/lib/queries";

const cmsApiUrl = process.env.NEXT_PUBLIC_CMS_API_URL?.trim();
const cmsAuthorCache = new Map<string, Author>();
const cmsFetchTimeoutMs = Number(process.env.CMS_FETCH_TIMEOUT_MS || 8000);

type GraphQLResponse<TData> = {
  data?: TData;
  errors?: Array<{ message: string }>;
};

type WpAuthorNode = {
  id?: string | null;
  name?: string | null;
  description?: string | null;
  avatar?: { url?: string | null } | null;
};

type WpCategoryNode = {
  id?: string | null;
  name?: string | null;
  slug?: string | null;
  description?: string | null;
  count?: number | null;
};

type WpTagNode = {
  id?: string | null;
  name?: string | null;
  slug?: string | null;
};

type WpPostNode = {
  id?: string | null;
  title?: string | null;
  slug?: string | null;
  excerpt?: string | null;
  content?: string | null;
  date?: string | null;
  modified?: string | null;
  featuredImage?: { node?: { sourceUrl?: string | null } | null } | null;
  author?: { node?: WpAuthorNode | null } | null;
  categories?: { nodes?: WpCategoryNode[] | null } | null;
  tags?: { nodes?: WpTagNode[] | null } | null;
  seo?: {
    title?: string | null;
    metaDesc?: string | null;
    canonical?: string | null;
    focuskw?: string | null;
    opengraphImage?: { sourceUrl?: string | null } | null;
  } | null;
};

type WpPostsQueryData = {
  posts?: { nodes?: WpPostNode[] | null } | null;
};

type WpPostBySlugQueryData = {
  post?: WpPostNode | null;
};

type WpCategoriesQueryData = {
  categories?: { nodes?: WpCategoryNode[] | null } | null;
};

const sortByPublishedDateDesc = (items: Post[]): Post[] => {
  return [...items].sort(
    (a, b) =>
      new Date(b.publishedAt).getTime() - new Date(a.publishedAt).getTime()
  );
};

const getMockPosts = (): Post[] => {
  return sortByPublishedDateDesc(
    posts.filter((post) => post.status === "published")
  );
};

const stripHtml = (value: string | undefined | null): string => {
  if (!value) {
    return "";
  }

  return value
    .replace(/<[^>]+>/g, " ")
    .replace(/\s+/g, " ")
    .trim();
};

const estimateReadingTime = (content: string): number => {
  const words = content.split(/\s+/).filter(Boolean).length;
  return Math.max(1, Math.ceil(words / 220));
};

const mapWpCategory = (category: WpCategoryNode): Category | null => {
  const slug = category.slug?.trim();
  const name = category.name?.trim();

  if (!slug || !name || slug === "uncategorized" || category.count === 0) {
    return null;
  }

  return {
    id: category.id?.trim() || slug,
    slug,
    name,
    description: stripHtml(category.description)
  };
};

const mapWpAuthor = (author: WpAuthorNode | null | undefined): Author => {
  const authorId = author?.id?.trim() || "author-unknown";

  return {
    id: authorId,
    name: author?.name?.trim() || "VitalBloom Editorial Team",
    bio:
      stripHtml(author?.description) ||
      "Editorial contributor for VitalBloom.blog.",
    avatar: author?.avatar?.url?.trim() || ""
  };
};

const mapWpPost = (post: WpPostNode): Post | null => {
  const slug = post.slug?.trim();
  const title = stripHtml(post.title);

  if (!slug || !title) {
    return null;
  }

  const mappedAuthor = mapWpAuthor(post.author?.node);
  cmsAuthorCache.set(mappedAuthor.id, mappedAuthor);

  const mappedCategories = (post.categories?.nodes || [])
    .map(mapWpCategory)
    .filter((category): category is Category => Boolean(category));
  const primaryCategory = mappedCategories[0];

  const mappedTags = (post.tags?.nodes || [])
    .map((tag) => {
      const slugValue = tag.slug?.trim();
      if (!slugValue) {
        return null;
      }

      return tag.id?.trim() || slugValue;
    })
    .filter((tag): tag is string => Boolean(tag));

  const rawContent = post.content?.trim() || "";
  const cleanedContent = stripHtml(rawContent);
  const cleanedExcerpt = stripHtml(post.excerpt) || cleanedContent.slice(0, 180);
  const canonicalUrl = post.seo?.canonical?.trim();
  const derivedCanonicalUrl =
    canonicalUrl || (cmsApiUrl ? `${cmsApiUrl.replace(/\/graphql\/?$/, "")}/${slug}` : undefined);

  return {
    id: post.id?.trim() || slug,
    title,
    slug,
    excerpt: cleanedExcerpt,
    content: rawContent,
    featuredImage: post.featuredImage?.node?.sourceUrl?.trim() || "",
    readingTime: estimateReadingTime(cleanedContent),
    status: "published",
    publishedAt: post.date?.trim() || new Date().toISOString(),
    updatedAt: post.modified?.trim() || undefined,
    authorId: mappedAuthor.id,
    categoryId: primaryCategory?.id || "cat-uncategorized",
    tagIds: mappedTags,
    seo: {
      metaTitle: post.seo?.title?.trim() || title,
      metaDescription: stripHtml(post.seo?.metaDesc) || cleanedExcerpt,
      canonicalUrl: derivedCanonicalUrl,
      ogImage: post.seo?.opengraphImage?.sourceUrl?.trim() || post.featuredImage?.node?.sourceUrl?.trim() || undefined,
      focusKeyword: post.seo?.focuskw?.trim() || undefined
    }
  };
};

const fetchFromCms = async <TData, TVariables extends Record<string, unknown>>(
  query: string,
  variables?: TVariables
): Promise<TData | null> => {
  if (!cmsApiUrl) {
    return null;
  }

  const controller = new AbortController();
  const timeoutId = setTimeout(() => {
    controller.abort("CMS request timed out");
  }, cmsFetchTimeoutMs);

  let response: Response;

  try {
    response = await fetch(cmsApiUrl, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ query, variables }),
      signal: controller.signal,
      next: { revalidate: 60, tags: ["cms-content"] }
    });
  } catch (error) {
    if (error instanceof Error && error.name === "AbortError") {
      throw new Error(`CMS request timeout after ${cmsFetchTimeoutMs}ms`);
    }

    throw new Error(
      `CMS network request failed: ${error instanceof Error ? error.message : "Unknown error"}`
    );
  } finally {
    clearTimeout(timeoutId);
  }

  if (!response.ok) {
    throw new Error(`CMS request failed with status ${response.status}`);
  }

  const json = (await response.json()) as GraphQLResponse<TData>;

  if (json.errors?.length) {
    throw new Error(json.errors.map((error) => error.message).join("; "));
  }

  return json.data ?? null;
};

export const getPosts = async (): Promise<Post[]> => {
  if (!cmsApiUrl) {
    return getMockPosts();
  }

  try {
    const data = await fetchFromCms<WpPostsQueryData, { first: number }>(
      WP_POSTS_QUERY,
      { first: 24 }
    );
    const mappedPosts = (data?.posts?.nodes || [])
      .map(mapWpPost)
      .filter((post): post is Post => Boolean(post));

    if (mappedPosts.length > 0) {
      return sortByPublishedDateDesc(mappedPosts);
    }
  } catch (error) {
    console.error("Failed to load posts from CMS.", error);
  }

  return getMockPosts();
};

export const getPostBySlug = async (slug: string): Promise<Post | undefined> => {
  if (!cmsApiUrl) {
    return posts.find(
      (post) => post.slug === slug && post.status === "published"
    );
  }

  try {
    const data = await fetchFromCms<WpPostBySlugQueryData, { slug: string }>(
      WP_POST_BY_SLUG_QUERY,
      { slug }
    );
    const cmsPost = mapWpPost(data?.post || {});

    if (cmsPost) {
      return cmsPost;
    }
  } catch (error) {
    console.error(`Failed to load post '${slug}' from CMS.`, error);
  }

  return posts.find((post) => post.slug === slug && post.status === "published");
};

export const getCategories = async (): Promise<Category[]> => {
  if (!cmsApiUrl) {
    return [...categories];
  }

  try {
    const data = await fetchFromCms<WpCategoriesQueryData, { first: number }>(
      WP_CATEGORIES_QUERY,
      { first: 100 }
    );
    const cmsCategories = (data?.categories?.nodes || [])
      .map(mapWpCategory)
      .filter((category): category is Category => Boolean(category));

    if (cmsCategories.length > 0) {
      return cmsCategories;
    }
  } catch (error) {
    console.error("Failed to load categories from CMS.", error);
  }

  return [...categories];
};

export const getCategoryById = async (
  categoryId: string
): Promise<Category | undefined> => {
  const allCategories = await getCategories();
  return allCategories.find((category) => category.id === categoryId);
};

export const getCategoryBySlug = async (
  slug: string
): Promise<Category | undefined> => {
  const allCategories = await getCategories();
  return allCategories.find((category) => category.slug === slug);
};

export const getPostsByCategorySlug = async (slug: string): Promise<Post[]> => {
  if (cmsApiUrl) {
    try {
      const data = await fetchFromCms<
        WpPostsQueryData,
        { categorySlug: string; first: number }
      >(WP_POSTS_BY_CATEGORY_QUERY, {
        categorySlug: slug,
        first: 24
      });
      const cmsPosts = (data?.posts?.nodes || [])
        .map(mapWpPost)
        .filter((post): post is Post => Boolean(post));

      if (cmsPosts.length > 0) {
        return sortByPublishedDateDesc(cmsPosts);
      }
    } catch (error) {
      console.error(`Failed to load posts for category '${slug}' from CMS.`, error);
    }
  }

  const category = await getCategoryBySlug(slug);

  if (!category) {
    return [];
  }

  const allPosts = await getPosts();
  return allPosts.filter((post) => post.categoryId === category.id);
};

export const getAuthorById = (authorId: string): Author | undefined => {
  const cmsAuthor = cmsAuthorCache.get(authorId);
  if (cmsAuthor) {
    return cmsAuthor;
  }

  return authors.find((author) => author.id === authorId);
};

export const getRelatedPosts = async (
  currentPostId: string,
  categoryId: string
): Promise<Post[]> => {
  const publishedPosts = await getPosts();

  const sameCategory = publishedPosts.filter(
    (post) => post.id !== currentPostId && post.categoryId === categoryId
  );

  if (sameCategory.length >= 3) {
    return sameCategory.slice(0, 3);
  }

  const fallback = publishedPosts.filter(
    (post) => post.id !== currentPostId && post.categoryId !== categoryId
  );

  return [...sameCategory, ...fallback].slice(0, 3);
};
