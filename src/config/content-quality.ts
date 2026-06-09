import { siteConfig } from "@/config/site";

export const canonicalSlugOverrides: Record<string, string> = {
  "better-sleep-routine": "better-sleep-routine-guide",
  "balanced-plate-method": "balanced-plate-guide"
};

export const noindexDuplicateSlugs = new Set(Object.keys(canonicalSlugOverrides));

export const getCanonicalUrlForSlug = (slug: string): string => {
  const canonicalSlug = canonicalSlugOverrides[slug] || slug;
  return `${siteConfig.url}/${canonicalSlug}`;
};

export const maxInlineInternalLinksPerArticle = 10;

type SearchFocusedSeo = {
  title: string;
  description: string;
};

export const searchFocusedPostSeo: Record<string, SearchFocusedSeo> = {
  "high-fiber-breakfast-ideas": {
    title: "High-Fiber Breakfast Ideas for Steady Energy",
    description:
      "Simple high-fiber breakfast ideas with oats, beans, fruit, seeds, and balanced pairings to help you build filling morning meals."
  },
  "low-sugar-snack-ideas": {
    title: "Low-Sugar Snack Ideas for Work, Home, and Busy Days",
    description:
      "Practical low-sugar snack ideas with protein, fiber, and simple prep tips for steadier energy between meals."
  },
  "how-to-build-a-simple-wellness-plan": {
    title: "How to Build a Simple Wellness Plan That Actually Fits",
    description:
      "A practical guide to building a simple wellness plan with realistic habits for sleep, nutrition, movement, stress, and consistency."
  },
  "journaling-for-mental-clarity": {
    title: "Journaling for Mental Clarity: Prompts and Simple Steps",
    description:
      "Use journaling for mental clarity with simple prompts, weekly reflection, and practical ways to sort thoughts without overcomplicating it."
  },
  "healthy-breakfast-ideas": {
    title: "Healthy Breakfast Ideas for Busy Mornings",
    description:
      "Easy healthy breakfast ideas with balanced protein, fiber, and flexible meal prep options for busy mornings."
  },
  "beginner-home-workout-guide": {
    title: "Beginner Home Workout Guide: Simple At-Home Fitness",
    description:
      "A beginner home workout guide with simple movements, realistic routines, and recovery tips for starting fitness at home."
  },
  "beginner-meditation-guide": {
    title: "Beginner Meditation Guide: Simple Practice for Calm",
    description:
      "A beginner meditation guide with simple breathing, short sessions, and practical tips for building a calmer daily habit."
  }
};
