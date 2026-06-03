import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import JsonLd from "@/components/JsonLd";
import PostImage from "@/components/PostImage";
import { noindexDuplicateSlugs } from "@/config/content-quality";
import { categoryPillarGuideSlugs } from "@/config/pillar-guides";
import { siteConfig } from "@/config/site";
import { getCategoryBySlug, getPostsByCategorySlug } from "@/lib/api";
import { breadcrumbSchema, collectionPageSchema } from "@/lib/schema";

type CategoryPageProps = {
  params: Promise<{
    slug: string;
  }>;
};

const formatDate = (dateString: string): string => {
  return new Date(dateString).toLocaleDateString("en-US", {
    month: "short",
    day: "numeric",
    year: "numeric"
  });
};

export async function generateMetadata({ params }: CategoryPageProps): Promise<Metadata> {
  const { slug } = await params;
  const category = await getCategoryBySlug(slug);

  if (!category) {
    return {
      title: "Category Not Found",
      description: "The requested category could not be found.",
      robots: {
        index: false,
        follow: false
      }
    };
  }

  const title = `${category.name} Articles`;
  const description =
    category.description || `Explore the latest ${category.name.toLowerCase()} posts.`;
  const canonical = `${siteConfig.url}/category/${category.slug}`;

  return {
    title,
    description,
    alternates: {
      canonical
    },
    openGraph: {
      type: "website",
      title,
      description,
      url: canonical,
      siteName: siteConfig.name,
      images: [siteConfig.defaultOgImage]
    },
    twitter: {
      card: "summary_large_image",
      title,
      description,
      images: [siteConfig.defaultOgImage]
    }
  };
}

export default async function CategoryPage({ params }: CategoryPageProps) {
  const { slug } = await params;
  const category = await getCategoryBySlug(slug);

  if (!category) {
    notFound();
  }

  const posts = (await getPostsByCategorySlug(slug)).filter(
    (post) => !noindexDuplicateSlugs.has(post.slug)
  );
  const pillarSlugs = categoryPillarGuideSlugs[category.slug] || [];
  const pillarPosts = pillarSlugs
    .map((pillarSlug) => posts.find((post) => post.slug === pillarSlug))
    .filter((post): post is NonNullable<typeof post> => Boolean(post));
  const regularPosts = posts.filter((post) => !pillarSlugs.includes(post.slug));
  const breadcrumbs = [
    { name: "Home", url: "/" },
    { name: category.name, url: `/category/${category.slug}` }
  ];

  return (
    <main className="flex flex-1 flex-col gap-8 py-10 sm:py-12">
      <JsonLd data={[collectionPageSchema(category, posts), breadcrumbSchema(breadcrumbs)]} />
      <header className="space-y-3 border-b border-zinc-200 pb-6">
        <p className="text-sm font-medium uppercase tracking-[0.12em] text-zinc-500">
          Category
        </p>
        <h1 className="text-3xl font-semibold tracking-tight text-zinc-900 sm:text-4xl">
          {category.name}
        </h1>
        {category.description ? (
          <p className="max-w-3xl text-base leading-7 text-zinc-600 sm:text-lg">
            {category.description}
          </p>
        ) : null}
      </header>

      {pillarPosts.length > 0 ? (
        <section aria-labelledby="category-featured-guides" className="space-y-4">
          <div>
            <p className="text-sm font-medium uppercase tracking-[0.12em] text-zinc-500">
              Essential Guides
            </p>
            <h2 id="category-featured-guides" className="text-2xl font-semibold text-zinc-900">
              Start with These {category.name} Guides
            </h2>
          </div>
          <div className="grid gap-4 sm:grid-cols-2">
            {pillarPosts.map((post, index) => (
              <article
                key={post.id}
                className="overflow-hidden rounded-lg border border-zinc-200 bg-white"
              >
                <PostImage
                  imageUrl={post.featuredImage}
                  alt={post.title}
                  className="aspect-[16/9] w-full object-cover"
                  priority={index === 0}
                />
                <div className="p-5">
                  <div className="mb-2 flex items-center gap-3 text-sm text-zinc-500">
                    <span>{post.readingTime} min guide</span>
                    <span aria-hidden="true">|</span>
                    <time dateTime={post.publishedAt}>{formatDate(post.publishedAt)}</time>
                  </div>
                  <h3 className="text-xl font-semibold tracking-tight text-zinc-900">
                    <Link
                      href={`/${post.slug}`}
                      className="hover:text-zinc-700 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-zinc-400"
                    >
                      {post.title}
                    </Link>
                  </h3>
                  <p className="mt-2 text-base leading-7 text-zinc-600">{post.excerpt}</p>
                </div>
              </article>
            ))}
          </div>
        </section>
      ) : null}

      <section aria-labelledby="category-posts" className="space-y-4">
        <h2 id="category-posts" className="text-2xl font-semibold text-zinc-900">
          Latest in {category.name}
        </h2>
        {regularPosts.length > 0 ? (
          <div className="space-y-4">
            {regularPosts.map((post) => (
              <article
                key={post.id}
                className="grid overflow-hidden rounded-lg border border-zinc-200 bg-white sm:grid-cols-[220px_1fr]"
              >
                <PostImage
                  imageUrl={post.featuredImage}
                  alt={post.title}
                  className="aspect-[16/9] h-full w-full object-cover"
                />
                <div className="p-5">
                  <div className="mb-2 flex items-center gap-3 text-sm text-zinc-500">
                    <span>{post.readingTime} min read</span>
                    <span aria-hidden="true">|</span>
                    <time dateTime={post.publishedAt}>{formatDate(post.publishedAt)}</time>
                  </div>
                  <h3 className="text-xl font-semibold tracking-tight text-zinc-900">
                    <Link
                      href={`/${post.slug}`}
                      className="hover:text-zinc-700 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-zinc-400"
                    >
                      {post.title}
                    </Link>
                  </h3>
                  <p className="mt-2 text-base leading-7 text-zinc-600">{post.excerpt}</p>
                </div>
              </article>
            ))}
          </div>
        ) : (
          <p className="text-zinc-600">No published posts in this category yet.</p>
        )}
      </section>
    </main>
  );
}
