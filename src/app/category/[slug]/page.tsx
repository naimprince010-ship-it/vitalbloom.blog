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
  searchParams?: Promise<{
    topic?: string;
    page?: string;
  }>;
};

const POSTS_PER_PAGE = 12;

const categorySeoCopy: Record<string, { title: string; description: string; ogImage: string }> = {
  nutrition: {
    title: "Nutrition Guides: Balanced Eating, Meal Planning & Healthy Habits",
    description:
      "Explore practical nutrition guides for balanced eating, meal planning, healthy breakfasts, snacks, hydration, protein, fiber, digestion, and everyday food habits.",
    ogImage: "https://backend.vitalbloom.blog/wp-content/uploads/2026/05/balanced-plate-guide.png"
  },
  fitness: {
    title: "Fitness Guides: Beginner Workouts, Walking & Recovery",
    description:
      "Beginner-friendly fitness guides for home workouts, walking, stretching, mobility, strength training, cardio, recovery, and realistic movement habits.",
    ogImage: "https://backend.vitalbloom.blog/wp-content/uploads/2026/05/beginner-home-workout-guide.png"
  },
  mindfulness: {
    title: "Mindfulness Guides: Stress Support, Journaling & Calm Habits",
    description:
      "Mindfulness and stress-support guides for breathing, journaling, relaxation, mental clarity, calmer routines, and everyday emotional wellness.",
    ogImage: "https://backend.vitalbloom.blog/wp-content/uploads/2026/05/stress-management-guide.png"
  },
  sleep: {
    title: "Sleep Guides: Better Routines, Rest & Evening Habits",
    description:
      "Sleep guides for bedtime routines, sleep hygiene, evening habits, screen boundaries, sleep debt, shift work, naps, and better daily rest.",
    ogImage: "https://backend.vitalbloom.blog/wp-content/uploads/2026/05/better-sleep-routine-guide.png"
  },
  stress: {
    title: "Stress Guides: Relief Tools, Burnout Prevention & Resets",
    description:
      "Stress support guides for quick resets, burnout prevention, work stress, student stress, breathing, journaling, and calming daily routines.",
    ogImage: "https://backend.vitalbloom.blog/wp-content/uploads/2026/05/stress-management-guide.png"
  },
  lifestyle: {
    title: "Lifestyle Guides: Daily Routines, Digital Wellness & Resets",
    description:
      "Lifestyle guides for daily routines, digital wellness, travel resets, remote work habits, weekly planning, consistency, and balanced living.",
    ogImage: "https://backend.vitalbloom.blog/wp-content/uploads/2026/05/daily-wellness-routine-beginners.png"
  }
};

const categoryTopicFilters: Record<string, Array<{ label: string; value: string; keywords: string[] }>> = {
  fitness: [
    { label: "Beginner Workouts", value: "beginner-workouts", keywords: ["beginner", "home-workout", "workout"] },
    { label: "Strength", value: "strength", keywords: ["strength", "training"] },
    { label: "Walking & Cardio", value: "walking-cardio", keywords: ["walking", "cardio"] },
    { label: "Stretching & Mobility", value: "stretching-mobility", keywords: ["stretching", "mobility"] },
    { label: "Recovery", value: "recovery", keywords: ["recovery", "rest-day", "post-workout"] }
  ],
  mindfulness: [
    { label: "Stress Relief", value: "stress-relief", keywords: ["stress", "relaxation", "self-care"] },
    { label: "Journaling", value: "journaling", keywords: ["journal", "journaling"] },
    { label: "Meditation", value: "meditation", keywords: ["meditation", "mindfulness"] },
    { label: "Breathing", value: "breathing", keywords: ["breathing", "breath"] },
    { label: "Wind Down", value: "wind-down", keywords: ["wind-down", "morning", "after-work"] }
  ],
  nutrition: [
    { label: "Meal Prep", value: "meal-prep", keywords: ["meal-prep", "meal-planning", "grocery"] },
    { label: "Breakfast", value: "breakfast", keywords: ["breakfast", "morning"] },
    { label: "Snacks", value: "snacks", keywords: ["snack", "snacks"] },
    { label: "Balanced Plates", value: "balanced-plates", keywords: ["balanced-plate", "dinner", "salad"] },
    { label: "Hydration", value: "hydration", keywords: ["hydration", "water"] }
  ],
  stress: [
    { label: "Quick Resets", value: "quick-resets", keywords: ["reset", "calm-down", "grounding"] },
    { label: "Work Stress", value: "work-stress", keywords: ["work", "busy-days"] },
    { label: "Student Support", value: "student-support", keywords: ["student"] },
    { label: "Journaling", value: "journaling", keywords: ["journal", "journaling", "overthinking"] },
    { label: "Digital Boundaries", value: "digital-boundaries", keywords: ["screen", "digital"] }
  ]
};

const formatDate = (dateString: string): string => {
  return new Date(dateString).toLocaleDateString("en-US", {
    month: "short",
    day: "numeric",
    year: "numeric"
  });
};

const getDisplayDate = (post: { publishedAt: string; updatedAt?: string }) => {
  return {
    published: post.publishedAt,
    updated: post.updatedAt
  };
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

  const seoCopy = categorySeoCopy[category.slug];
  const title = seoCopy?.title || `${category.name} Articles`;
  const description = seoCopy?.description || category.description || `Explore the latest ${category.name.toLowerCase()} posts.`;
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
      images: [seoCopy?.ogImage || siteConfig.defaultOgImage]
    },
    twitter: {
      card: "summary_large_image",
      title,
      description,
      images: [seoCopy?.ogImage || siteConfig.defaultOgImage]
    }
  };
}

const matchesTopic = (
  post: { slug: string; title: string },
  topic?: { keywords: string[] }
): boolean => {
  if (!topic) {
    return true;
  }

  const haystack = `${post.slug} ${post.title}`.toLowerCase();
  return topic.keywords.some((keyword) => haystack.includes(keyword));
};

export default async function CategoryPage({ params, searchParams }: CategoryPageProps) {
  const { slug } = await params;
  const query = (await searchParams) || {};
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
  const topicFilters = categoryTopicFilters[category.slug] || [];
  const selectedTopic = topicFilters.find((topic) => topic.value === query.topic);
  const filteredRegularPosts = posts
    .filter((post) => !pillarSlugs.includes(post.slug))
    .filter((post) => matchesTopic(post, selectedTopic));
  const requestedPage = Number.parseInt(query.page || "1", 10);
  const currentPage = Number.isFinite(requestedPage) && requestedPage > 0 ? requestedPage : 1;
  const totalPages = Math.max(1, Math.ceil(filteredRegularPosts.length / POSTS_PER_PAGE));
  const visiblePage = Math.min(currentPage, totalPages);
  const regularPosts = filteredRegularPosts.slice(
    (visiblePage - 1) * POSTS_PER_PAGE,
    visiblePage * POSTS_PER_PAGE
  );
  const pageHref = (page: number) => {
    const params = new URLSearchParams();
    if (selectedTopic) {
      params.set("topic", selectedTopic.value);
    }
    if (page > 1) {
      params.set("page", String(page));
    }
    const suffix = params.toString();
    return `/category/${category.slug}${suffix ? `?${suffix}` : ""}`;
  };
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
              (() => {
                const displayDate = getDisplayDate(post);

                return (
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
                    <time dateTime={displayDate.published}>
                      Published {formatDate(displayDate.published)}
                    </time>
                    {displayDate.updated ? (
                      <>
                        <span aria-hidden="true">|</span>
                        <time dateTime={displayDate.updated}>
                          Updated {formatDate(displayDate.updated)}
                        </time>
                      </>
                    ) : null}
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
                );
              })()
            ))}
          </div>
        </section>
      ) : null}

      <section aria-labelledby="category-posts" className="space-y-4">
        <div className="flex flex-col gap-3 sm:flex-row sm:items-end sm:justify-between">
          <div>
            <h2 id="category-posts" className="text-2xl font-semibold text-zinc-900">
              Latest in {category.name}
            </h2>
            <p className="mt-1 text-sm text-zinc-600">
              Showing {regularPosts.length} of {filteredRegularPosts.length} posts
              {selectedTopic ? ` for ${selectedTopic.label}` : ""}.
            </p>
          </div>
          {topicFilters.length > 0 ? (
            <div className="flex flex-wrap gap-2">
              <Link
                href={`/category/${category.slug}`}
                className={`rounded-md border px-3 py-1.5 text-sm font-medium ${
                  selectedTopic
                    ? "border-zinc-200 text-zinc-700 hover:border-zinc-300"
                    : "border-green-700 bg-green-700 text-white"
                }`}
              >
                All
              </Link>
              {topicFilters.map((topic) => (
                <Link
                  key={topic.value}
                  href={`/category/${category.slug}?topic=${topic.value}`}
                  className={`rounded-md border px-3 py-1.5 text-sm font-medium ${
                    selectedTopic?.value === topic.value
                      ? "border-green-700 bg-green-700 text-white"
                      : "border-zinc-200 text-zinc-700 hover:border-zinc-300"
                  }`}
                >
                  {topic.label}
                </Link>
              ))}
            </div>
          ) : null}
        </div>
        {regularPosts.length > 0 ? (
          <div className="space-y-4">
            {regularPosts.map((post) => (
              (() => {
                const displayDate = getDisplayDate(post);

                return (
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
                    <time dateTime={displayDate.published}>
                      Published {formatDate(displayDate.published)}
                    </time>
                    {displayDate.updated ? (
                      <>
                        <span aria-hidden="true">|</span>
                        <time dateTime={displayDate.updated}>
                          Updated {formatDate(displayDate.updated)}
                        </time>
                      </>
                    ) : null}
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
                );
              })()
            ))}
          </div>
        ) : (
          <p className="text-zinc-600">No published posts in this category yet.</p>
        )}
        {totalPages > 1 ? (
          <nav aria-label={`${category.name} pagination`} className="flex items-center justify-between gap-3 pt-2">
            {visiblePage > 1 ? (
              <Link
                href={pageHref(visiblePage - 1)}
                className="rounded-md border border-zinc-200 px-4 py-2 text-sm font-medium text-zinc-700 hover:border-zinc-300"
              >
                Previous
              </Link>
            ) : (
              <span />
            )}
            <span className="text-sm text-zinc-600">
              Page {visiblePage} of {totalPages}
            </span>
            {visiblePage < totalPages ? (
              <Link
                href={pageHref(visiblePage + 1)}
                className="rounded-md border border-zinc-200 px-4 py-2 text-sm font-medium text-zinc-700 hover:border-zinc-300"
              >
                Next
              </Link>
            ) : (
              <span />
            )}
          </nav>
        ) : null}
      </section>
    </main>
  );
}
