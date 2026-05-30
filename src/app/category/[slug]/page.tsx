import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import PostImage from "@/components/PostImage";
import { getCategoryBySlug, getPostsByCategorySlug } from "@/lib/api";
import { siteConfig } from "@/config/site";

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

  const posts = await getPostsByCategorySlug(slug);

  return (
    <main className="flex flex-1 flex-col gap-8 py-10 sm:py-12">
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

      <section aria-labelledby="category-posts" className="space-y-4">
        <h2 id="category-posts" className="text-2xl font-semibold text-zinc-900">
          Latest in {category.name}
        </h2>
        {posts.length > 0 ? (
          <div className="space-y-4">
            {posts.map((post) => (
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
                    <span aria-hidden="true">•</span>
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
