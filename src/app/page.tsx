import Link from "next/link";
import PostImage from "@/components/PostImage";
import { siteConfig } from "@/config/site";
import { getCategories, getPosts } from "@/lib/api";

export default async function Home() {
  const posts = await getPosts();
  const categories = await getCategories();
  const heroPost = posts[0];

  return (
    <main className="flex flex-1 flex-col gap-12 py-10 sm:py-12">
      <header className="space-y-3 border-b border-zinc-200 pb-6">
        <p className="text-sm font-medium uppercase tracking-[0.12em] text-zinc-500">
          Wellness Publishing Platform
        </p>
        <h1 className="max-w-3xl text-3xl font-semibold tracking-tight text-zinc-900 sm:text-4xl">
          {siteConfig.title}
        </h1>
        <p className="max-w-3xl text-base leading-7 text-zinc-600 sm:text-lg">
          {siteConfig.description}
        </p>
      </header>

      <aside aria-label="Advertising placeholder top banner" className="ad-slot" />

      <section aria-labelledby="hero-featured-post" className="space-y-5">
        <h2 id="hero-featured-post" className="text-2xl font-semibold text-zinc-900">
          Featured Post
        </h2>
        {heroPost ? (
          <article className="overflow-hidden rounded-lg border border-zinc-200 bg-white shadow-sm">
            <PostImage
              imageUrl={heroPost.featuredImage}
              alt={heroPost.title}
              className="aspect-[16/7] w-full object-cover"
              priority
            />
            <div className="p-5 sm:p-6">
              <p className="mb-2 text-sm font-medium text-zinc-500">
                {heroPost.readingTime} min read
              </p>
              <h3 className="text-2xl font-semibold tracking-tight text-zinc-900">
                <Link
                  href={`/${heroPost.slug}`}
                  className="hover:text-zinc-700 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-zinc-400"
                >
                  {heroPost.title}
                </Link>
              </h3>
              <p className="mt-3 max-w-2xl text-base leading-7 text-zinc-600">
                {heroPost.excerpt}
              </p>
            </div>
          </article>
        ) : (
          <p className="text-zinc-600">No featured content available yet.</p>
        )}
      </section>

      <section aria-labelledby="category-grid" className="space-y-5">
        <h2 id="category-grid" className="text-2xl font-semibold text-zinc-900">
          Explore Categories
        </h2>
        <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
          {categories.map((category) => (
            <article
              key={category.id}
              className="rounded-lg border border-zinc-200 bg-white p-5"
            >
              <h3 className="text-lg font-semibold text-zinc-900">
                <Link
                  href={`/category/${category.slug}`}
                  className="hover:text-zinc-700 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-zinc-400"
                >
                  {category.name}
                </Link>
              </h3>
              <p className="mt-2 text-sm leading-6 text-zinc-600">
                {category.description}
              </p>
            </article>
          ))}
        </div>
      </section>

      <section aria-labelledby="latest-posts" className="space-y-5">
        <aside aria-label="Advertising placeholder mid page" className="ad-slot mb-2" />
        <h2 id="latest-posts" className="text-2xl font-semibold text-zinc-900">
          Latest Posts
        </h2>
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
                  <span aria-hidden="true">|</span>
                  <time dateTime={post.publishedAt}>
                    {new Date(post.publishedAt).toLocaleDateString("en-US", {
                      month: "short",
                      day: "numeric",
                      year: "numeric"
                    })}
                  </time>
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
    </main>
  );
}
