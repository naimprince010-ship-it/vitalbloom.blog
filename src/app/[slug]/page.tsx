import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import JsonLd from "@/components/JsonLd";
import PostImage from "@/components/PostImage";
import {
  canonicalSlugOverrides,
  getCanonicalUrlForSlug,
  noindexDuplicateSlugs
} from "@/config/content-quality";
import { categoryPillarGuideSlugs } from "@/config/pillar-guides";
import { getAuthorById, getCategoryById, getPostBySlug, getRelatedPosts } from "@/lib/api";
import { prepareArticleHtml } from "@/lib/article-html";
import { siteConfig } from "@/config/site";
import { articleSchema, breadcrumbSchema } from "@/lib/schema";

type PostPageProps = {
  params: Promise<{
    slug: string;
  }>;
};

const formatDate = (dateString: string): string => {
  return new Date(dateString).toLocaleDateString("en-US", {
    month: "long",
    day: "numeric",
    year: "numeric"
  });
};

const isDefined = <T,>(value: T | undefined): value is T => Boolean(value);

const getReviewDate = (post: Awaited<ReturnType<typeof getPostBySlug>>): string | undefined => {
  if (!post) {
    return undefined;
  }

  return (
    post.editorialReview.reviewedAt ||
    post.editorialReview.factCheckedAt ||
    post.updatedAt ||
    post.publishedAt
  );
};

const needsCrisisSupportBox = (content: string): boolean => {
  const normalizedContent = content.toLowerCase();

  return [
    "self-harm",
    "suicide",
    "unsafe",
    "immediate danger",
    "crisis support"
  ].some((phrase) => normalizedContent.includes(phrase));
};

export async function generateMetadata({ params }: PostPageProps): Promise<Metadata> {
  const { slug } = await params;
  const post = await getPostBySlug(slug);

  if (!post) {
    return {
      title: "Post Not Found",
      description: "The requested article could not be found.",
      robots: {
        index: false,
        follow: false
      }
    };
  }

  const seoTitle = post.title;
  const seoDescription = post.seo.metaDescription || post.excerpt;
  const seoImage = post.seo.ogImage || siteConfig.defaultOgImage;
  const canonicalUrl = post.seo.canonicalUrl || getCanonicalUrlForSlug(post.slug);
  const isDuplicateSupportPage = noindexDuplicateSlugs.has(post.slug);

  return {
    title: seoTitle,
    description: seoDescription,
    robots: isDuplicateSupportPage
      ? {
          index: false,
          follow: true
        }
      : undefined,
    alternates: {
      canonical: canonicalUrl
    },
    openGraph: {
      type: "article",
      url: canonicalUrl,
      title: seoTitle,
      description: seoDescription,
      images: [seoImage],
      siteName: siteConfig.name,
      publishedTime: post.publishedAt
    },
    twitter: {
      card: "summary_large_image",
      title: seoTitle,
      description: seoDescription,
      images: [seoImage]
    }
  };
}

export default async function PostPage({ params }: PostPageProps) {
  const { slug } = await params;
  const post = await getPostBySlug(slug);

  if (!post) {
    notFound();
  }

  const author = getAuthorById(post.authorId);
  const relatedPosts = await getRelatedPosts(post.id, post.categoryId);
  const category = await getCategoryById(post.categoryId);
  const pillarGuideSlugs = category
    ? categoryPillarGuideSlugs[category.slug] ?? []
    : [];
  const pillarGuides = (
    await Promise.all(
      pillarGuideSlugs
        .filter((pillarSlug) => pillarSlug !== post.slug)
        .map((pillarSlug) => getPostBySlug(pillarSlug))
    )
  ).filter(isDefined);
  const reviewDate = getReviewDate(post);
  const reviewByline =
    post.editorialReview.reviewedBy ||
    post.editorialReview.factCheckedBy ||
    author?.name ||
    "VitalBloom Editorial Team";
  const articleHtml = prepareArticleHtml(
    post.content,
    post.slug,
    canonicalSlugOverrides
  );
  const showCrisisSupportBox = needsCrisisSupportBox(post.content);
  const isDuplicateSupportPage = noindexDuplicateSlugs.has(post.slug);
  const breadcrumbs = [
    { name: "Home", url: "/" },
    ...(category
      ? [{ name: category.name, url: `/category/${category.slug}` }]
      : []),
    { name: post.title, url: `/${post.slug}` }
  ];

  return (
    <main className="flex flex-1 flex-col gap-10 py-10 sm:py-12">
      <JsonLd data={[articleSchema(post, author, category), breadcrumbSchema(breadcrumbs)]} />
      <aside
        aria-label="Advertising placeholder top banner"
        className="ad-slot"
      />

      <article className="rounded-lg border border-zinc-200 bg-white p-5 sm:p-8">
        <header className="space-y-4 border-b border-zinc-200 pb-6">
          <p className="text-sm font-medium uppercase tracking-[0.12em] text-zinc-500">
            {category?.name ?? "Wellness"}
          </p>
          <h1 className="max-w-3xl text-3xl font-semibold tracking-tight text-zinc-900 sm:text-4xl">
            {post.title}
          </h1>
          <div className="flex flex-wrap items-center gap-3 text-sm text-zinc-600">
            <span>{post.readingTime} min read</span>
            <span aria-hidden="true">|</span>
            <time dateTime={post.publishedAt}>{formatDate(post.publishedAt)}</time>
            {author ? (
              <>
                <span aria-hidden="true">|</span>
                <span>By {author.name}</span>
              </>
            ) : null}
          </div>
          <div className="flex flex-wrap gap-2 text-sm text-zinc-600">
            <span className="rounded-md bg-zinc-100 px-2.5 py-1">
              {reviewDate ? `Updated ${formatDate(reviewDate)}` : "Editorially reviewed"}
            </span>
            <span className="rounded-md bg-emerald-50 px-2.5 py-1 text-emerald-800">
              {post.sources.length > 0
                ? `${post.sources.length} credible source${post.sources.length === 1 ? "" : "s"}`
                : "Editorial source review"}
            </span>
            <span className="rounded-md bg-zinc-100 px-2.5 py-1">
              Checked by {reviewByline}
            </span>
            <span className="rounded-md bg-zinc-100 px-2.5 py-1">
              Professional medical review not claimed
            </span>
          </div>
        </header>

        <PostImage
          imageUrl={post.featuredImage}
          alt={post.title}
          className="mt-6 aspect-[16/9] w-full rounded-lg object-cover"
          priority
        />

        <aside className="mt-6 rounded-lg border border-amber-200 bg-amber-50 p-4 text-sm leading-6 text-amber-950">
          <p className="font-semibold">General wellness information only</p>
          <p className="mt-1">
            This article is for education and everyday habit-building. It is not
            personal medical, nutrition, mental health, or fitness advice. If you
            have symptoms, a diagnosis, medication questions, or urgent concerns,
            work with a qualified professional.
          </p>
        </aside>

        {showCrisisSupportBox ? (
          <aside className="mt-4 rounded-lg border border-rose-200 bg-rose-50 p-4 text-sm leading-6 text-rose-950">
            <p className="font-semibold">If you feel unsafe or may harm yourself</p>
            <p className="mt-1">
              Contact local emergency services now. In the United States, call or
              text{" "}
              <a
                href="https://988lifeline.org/"
                className="font-medium underline underline-offset-4"
                rel="noreferrer"
                target="_blank"
              >
                988 Suicide &amp; Crisis Lifeline
              </a>
              . You can also text HOME to 741741 through{" "}
              <a
                href="https://www.crisistextline.org/"
                className="font-medium underline underline-offset-4"
                rel="noreferrer"
                target="_blank"
              >
                Crisis Text Line
              </a>
              . Outside the United States, use{" "}
              <a
                href="https://findahelpline.com/"
                className="font-medium underline underline-offset-4"
                rel="noreferrer"
                target="_blank"
              >
                Find A Helpline
              </a>
              .
            </p>
          </aside>
        ) : null}

        {isDuplicateSupportPage ? (
          <aside className="mt-4 rounded-lg border border-zinc-200 bg-zinc-50 p-4 text-sm leading-6 text-zinc-700">
            This page is kept as a supporting article, while the main version is
            canonicalized for search engines to reduce topic overlap.
          </aside>
        ) : null}

        <section
          className="article-content mt-6 max-w-none"
          dangerouslySetInnerHTML={{ __html: articleHtml }}
        />

        {(post.sources.length > 0 ||
          post.editorialReview.factCheckedBy ||
          post.editorialReview.reviewedBy) ? (
          <section
            aria-labelledby="sources-and-review"
            className="mt-8 border-t border-zinc-200 pt-6"
          >
            <h2 id="sources-and-review" className="text-lg font-semibold text-zinc-900">
              Sources &amp; Editorial Review
            </h2>
            <div className="mt-3 space-y-2 text-sm leading-6 text-zinc-700">
              <p>
                This article is maintained by the VitalBloom editorial process:
                source alignment, practical context, and reader safety are checked
                before publication and during updates.
              </p>
              <p>
                VitalBloom does not present this article as reviewed by a doctor,
                dietitian, therapist, or other licensed clinician unless a named
                qualified reviewer is listed here.
              </p>
              {post.editorialReview.factCheckedBy ? (
                <p>
                  Fact-checked by {post.editorialReview.factCheckedBy}
                  {post.editorialReview.factCheckedAt
                    ? ` on ${formatDate(post.editorialReview.factCheckedAt)}`
                    : ""}
                  .
                </p>
              ) : null}
              {post.editorialReview.reviewedBy ? (
                <p>
                  Reviewed by {post.editorialReview.reviewedBy}
                  {post.editorialReview.reviewedAt
                    ? ` on ${formatDate(post.editorialReview.reviewedAt)}`
                    : ""}
                  .
                </p>
              ) : null}
              {post.sources.length > 0 ? (
                <ol className="list-decimal space-y-2 pl-5">
                  {post.sources.map((source) => (
                    <li key={source.url}>
                      <a
                        href={source.url}
                        className="font-medium text-green-700 underline underline-offset-4 hover:text-green-800"
                        rel="noreferrer"
                        target="_blank"
                      >
                        {source.title}
                      </a>
                      {source.publisher ? (
                        <span className="text-zinc-500"> - {source.publisher}</span>
                      ) : null}
                      {source.accessedAt ? (
                        <span className="text-zinc-500">
                          {" "}
                          (accessed {formatDate(source.accessedAt)})
                        </span>
                      ) : null}
                    </li>
                  ))}
                </ol>
              ) : null}
            </div>
          </section>
        ) : null}

        <aside
          aria-label="Advertising placeholder mid article"
          className="ad-slot mt-8"
        />
      </article>

      {author ? (
        <section aria-labelledby="author-details" className="rounded-lg border border-zinc-200 bg-white p-5">
          <h2 id="author-details" className="text-lg font-semibold text-zinc-900">
            About the Author
          </h2>
          <p className="mt-2 text-sm leading-6 text-zinc-600">{author.bio}</p>
          <p className="mt-2 text-sm leading-6 text-zinc-600">
            Author names and review labels are shown for transparency. Clinical
            credentials are not implied unless they are explicitly listed.
          </p>
        </section>
      ) : null}

      {pillarGuides.length > 0 ? (
        <section
          aria-labelledby="essential-guides"
          className="rounded-lg border border-emerald-100 bg-emerald-50/60 p-5"
        >
          <h2 id="essential-guides" className="text-lg font-semibold text-zinc-900">
            Essential Guides
          </h2>
          <div className="mt-3 grid gap-3 sm:grid-cols-2">
            {pillarGuides.map((pillarGuide) => (
              <Link
                key={pillarGuide.slug}
                href={`/${pillarGuide.slug}`}
                className="rounded-md border border-emerald-100 bg-white p-4 text-sm leading-6 text-zinc-700 transition hover:border-emerald-200 hover:text-zinc-950 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-emerald-500"
              >
                <span className="block font-semibold text-zinc-900">
                  {pillarGuide.title}
                </span>
                <span className="mt-1 block">{pillarGuide.excerpt}</span>
              </Link>
            ))}
          </div>
        </section>
      ) : null}

      {relatedPosts.length > 0 ? (
        <section aria-labelledby="related-posts" className="space-y-4">
          <h2 id="related-posts" className="text-2xl font-semibold text-zinc-900">
            Related Posts
          </h2>
          <div className="grid gap-4 sm:grid-cols-2">
            {relatedPosts.map((relatedPost) => (
              <article
                key={relatedPost.id}
                className="overflow-hidden rounded-lg border border-zinc-200 bg-white"
              >
                <PostImage
                  imageUrl={relatedPost.featuredImage}
                  alt={relatedPost.title}
                  className="aspect-[16/9] w-full object-cover"
                />
                <div className="p-5">
                  <h3 className="text-lg font-semibold text-zinc-900">
                    <Link
                      href={`/${relatedPost.slug}`}
                      className="hover:text-zinc-700 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-zinc-400"
                    >
                      {relatedPost.title}
                    </Link>
                  </h3>
                  <p className="mt-2 text-sm leading-6 text-zinc-600">
                    {relatedPost.excerpt}
                  </p>
                </div>
              </article>
            ))}
          </div>
        </section>
      ) : null}
    </main>
  );
}
