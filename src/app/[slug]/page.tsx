import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { getAuthorById, getCategoryById, getPostBySlug, getRelatedPosts } from "@/lib/api";
import { siteConfig } from "@/config/site";

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

  const seoTitle = post.seo.metaTitle || post.title;
  const seoDescription = post.seo.metaDescription || post.excerpt;
  const seoImage = post.seo.ogImage || siteConfig.defaultOgImage;
  const canonicalUrl =
    post.seo.canonicalUrl || `${siteConfig.url}/${post.slug}`;

  return {
    title: seoTitle,
    description: seoDescription,
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

  return (
    <main className="flex flex-1 flex-col gap-10 py-10 sm:py-12">
      <aside
        aria-label="Advertising placeholder top banner"
        className="flex min-h-[120px] items-center justify-center rounded-lg border-2 border-dashed border-zinc-300 bg-zinc-100 px-4 text-center text-sm font-medium text-zinc-600"
      >
        [AdSense Placement - Top Banner]
      </aside>

      <article className="rounded-xl border border-zinc-200 bg-white p-6 sm:p-8">
        <header className="space-y-4 border-b border-zinc-200 pb-6">
          <p className="text-sm font-medium uppercase tracking-[0.12em] text-zinc-500">
            {category?.name ?? "Wellness"}
          </p>
          <h1 className="max-w-3xl text-3xl font-semibold tracking-tight text-zinc-900 sm:text-4xl">
            {post.title}
          </h1>
          <div className="flex flex-wrap items-center gap-3 text-sm text-zinc-600">
            <span>{post.readingTime} min read</span>
            <span aria-hidden="true">•</span>
            <time dateTime={post.publishedAt}>{formatDate(post.publishedAt)}</time>
            {author ? (
              <>
                <span aria-hidden="true">•</span>
                <span>By {author.name}</span>
              </>
            ) : null}
          </div>
        </header>

        <section
          className="prose prose-zinc mt-6 max-w-none"
          dangerouslySetInnerHTML={{ __html: post.content }}
        />

        <aside
          aria-label="Advertising placeholder mid article"
          className="mt-8 flex min-h-[120px] items-center justify-center rounded-lg border-2 border-dashed border-zinc-300 bg-zinc-100 px-4 text-center text-sm font-medium text-zinc-600"
        >
          [AdSense Placement - Mid Article]
        </aside>
      </article>

      {author ? (
        <section aria-labelledby="author-details" className="rounded-lg border border-zinc-200 bg-white p-5">
          <h2 id="author-details" className="text-lg font-semibold text-zinc-900">
            About the Author
          </h2>
          <p className="mt-2 text-sm leading-6 text-zinc-600">{author.bio}</p>
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
                className="rounded-lg border border-zinc-200 bg-white p-5"
              >
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
              </article>
            ))}
          </div>
        </section>
      ) : null}
    </main>
  );
}
