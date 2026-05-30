import type { Author, Category, Post, Tag } from "@/types/blog";

export const categories: Category[] = [
  {
    id: "cat-health",
    name: "Health",
    slug: "health",
    description: "Evidence-based guidance for building healthier routines."
  },
  {
    id: "cat-mental-wellness",
    name: "Mental Wellness",
    slug: "mental-wellness",
    description: "Mindfulness, stress management, and emotional resilience."
  },
  {
    id: "cat-nutrition",
    name: "Nutrition",
    slug: "nutrition",
    description: "Simple and practical nutrition advice for daily life."
  },
  {
    id: "cat-lifestyle",
    name: "Lifestyle",
    slug: "lifestyle",
    description: "Balanced living habits for long-term wellbeing."
  }
];

export const tags: Tag[] = [
  { id: "tag-mindfulness", name: "Mindfulness", slug: "mindfulness" },
  { id: "tag-fitness", name: "Fitness", slug: "fitness" },
  { id: "tag-meal-prep", name: "Meal Prep", slug: "meal-prep" },
  { id: "tag-sleep", name: "Sleep", slug: "sleep" },
  { id: "tag-productivity", name: "Productivity", slug: "productivity" }
];

export const authors: Author[] = [
  {
    id: "author-ava-mitchell",
    name: "Ava Mitchell",
    bio: "Certified wellness coach focused on daily habit design.",
    avatar: "/images/authors/ava-mitchell.jpg",
    expertise: ["Habit Building", "Lifestyle"]
  },
  {
    id: "author-liam-hayes",
    name: "Liam Hayes",
    bio: "Nutrition researcher writing practical food and recovery guides.",
    avatar: "/images/authors/liam-hayes.jpg",
    expertise: ["Nutrition", "Recovery"]
  }
];

export const posts: Post[] = [
  {
    id: "post-morning-reset-5-minutes",
    title: "5-Minute Morning Reset for a Calmer Day",
    slug: "5-minute-morning-reset-calmer-day",
    excerpt:
      "A simple morning routine to reduce stress and improve focus before work.",
    content:
      "Start with deep breathing for one minute, then light mobility and hydration. Keep your phone away for the first five minutes to reduce cognitive overload.",
    featuredImage: "/images/posts/morning-reset.jpg",
    readingTime: 5,
    status: "published",
    publishedAt: "2026-05-20T08:00:00.000Z",
    updatedAt: "2026-05-22T08:00:00.000Z",
    authorId: "author-ava-mitchell",
    categoryId: "cat-mental-wellness",
    tagIds: ["tag-mindfulness", "tag-productivity"],
    seo: {
      metaTitle: "5-Minute Morning Reset for a Calmer Day",
      metaDescription:
        "Build a calmer, focused morning with a quick and practical 5-minute reset routine.",
      canonicalUrl:
        "https://vitalbloom.blog/mental-wellness/5-minute-morning-reset-calmer-day",
      ogImage: "/images/og/morning-reset-og.jpg",
      focusKeyword: "morning wellness routine"
    },
    sources: [],
    editorialReview: {}
  },
  {
    id: "post-balanced-breakfast-us",
    title: "Balanced Breakfast Ideas for Busy Mornings",
    slug: "balanced-breakfast-ideas-busy-mornings",
    excerpt:
      "High-protein, fiber-rich breakfast options that support stable energy levels.",
    content:
      "Use a simple plate formula: protein + fiber + healthy fat. Examples include Greek yogurt bowls, egg wraps, and overnight oats.",
    featuredImage: "/images/posts/balanced-breakfast.jpg",
    readingTime: 6,
    status: "published",
    publishedAt: "2026-05-25T09:30:00.000Z",
    authorId: "author-liam-hayes",
    categoryId: "cat-nutrition",
    tagIds: ["tag-meal-prep", "tag-fitness"],
    seo: {
      metaTitle: "Balanced Breakfast Ideas for Busy Mornings",
      metaDescription:
        "Discover quick and balanced breakfast ideas designed for sustained energy and focus.",
      canonicalUrl:
        "https://vitalbloom.blog/nutrition/balanced-breakfast-ideas-busy-mornings",
      ogImage: "/images/og/balanced-breakfast-og.jpg",
      focusKeyword: "balanced breakfast ideas"
    },
    sources: [],
    editorialReview: {}
  },
  {
    id: "post-better-sleep-habits",
    title: "7 Evening Habits That Improve Sleep Quality",
    slug: "7-evening-habits-improve-sleep-quality",
    excerpt:
      "Small evening shifts that help you fall asleep faster and wake up refreshed.",
    content:
      "Set a wind-down alarm, dim bright lights, avoid late caffeine, and keep your room cool and dark. Consistency is more important than perfection.",
    featuredImage: "/images/posts/sleep-habits.jpg",
    readingTime: 7,
    status: "scheduled",
    publishedAt: "2026-06-05T01:00:00.000Z",
    authorId: "author-ava-mitchell",
    categoryId: "cat-lifestyle",
    tagIds: ["tag-sleep"],
    seo: {
      metaTitle: "7 Evening Habits That Improve Sleep Quality",
      metaDescription:
        "Improve your sleep quality with seven practical evening habits backed by behavior science.",
      canonicalUrl:
        "https://vitalbloom.blog/lifestyle/7-evening-habits-improve-sleep-quality",
      ogImage: "/images/og/sleep-habits-og.jpg",
      focusKeyword: "improve sleep quality"
    },
    sources: [],
    editorialReview: {}
  }
];
