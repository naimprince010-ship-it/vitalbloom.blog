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

export type SearchOpportunityBlock = {
  eyebrow: string;
  title: string;
  summary: string;
  links: Array<{
    label: string;
    href: string;
    description: string;
  }>;
  faqs: Array<{
    question: string;
    answer: string;
  }>;
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
  "balanced-plate-guide": {
    title: "Balanced Plate Guide: Simple Healthy Meal Formula",
    description:
      "Use the balanced plate guide to build simple meals with protein, produce, fiber-rich carbohydrates, and healthy fats."
  },
  "better-sleep-routine-guide": {
    title: "Better Sleep Routine Guide for Calmer Evenings",
    description:
      "Build a better sleep routine with evening habits, screen boundaries, caffeine timing, and realistic wind-down steps."
  },
  "stress-management-guide": {
    title: "Stress Management Guide: Practical Relief Tools",
    description:
      "Learn practical stress management tools including breathing, grounding, journaling, burnout prevention, and safety support."
  },
  "7-day-wellness-reset-checklist": {
    title: "7-Day Wellness Reset Checklist for Simple Habits",
    description:
      "Use this 7-day wellness reset checklist to organize simple sleep, nutrition, movement, hydration, and stress habits."
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

export const searchOpportunityBlocks: Record<string, SearchOpportunityBlock> = {
  "high-fiber-breakfast-ideas": {
    eyebrow: "Breakfast Search Guide",
    title: "Make a High-Fiber Breakfast More Filling",
    summary:
      "A useful high-fiber breakfast usually pairs fiber-rich carbohydrates with protein, fluid, and a little fat so the meal feels satisfying instead of just bulky.",
    links: [
      {
        label: "Healthy Breakfast Ideas",
        href: "/healthy-breakfast-ideas",
        description:
          "Use this for balanced breakfast examples when fiber is only one part of the morning meal."
      },
      {
        label: "Balanced Plate Guide",
        href: "/balanced-plate-guide",
        description:
          "See how to combine carbohydrates, protein, produce, and fats in a simple visual format."
      },
      {
        label: "Fiber-Rich Carbohydrates Guide",
        href: "/fiber-rich-carbohydrates-guide",
        description:
          "Compare oats, beans, fruit, whole grains, and starchy vegetables for everyday meals."
      }
    ],
    faqs: [
      {
        question: "What is a simple high-fiber breakfast?",
        answer:
          "A simple high-fiber breakfast can be oatmeal with fruit and seeds, whole-grain toast with beans or eggs, or yogurt with berries and nuts."
      },
      {
        question: "How can I add fiber to breakfast without making it complicated?",
        answer:
          "Start with one easy add-on such as berries, chia seeds, oats, beans, lentils, whole-grain bread, or a piece of fruit."
      }
    ]
  },
  "low-sugar-snack-ideas": {
    eyebrow: "Snack Search Guide",
    title: "Choose Low-Sugar Snacks That Still Feel Satisfying",
    summary:
      "The most useful low-sugar snacks are not just low in sugar; they also include protein, fiber, or healthy fats so you are less likely to keep grazing.",
    links: [
      {
        label: "Healthy Snack Plate Ideas",
        href: "/healthy-snack-plate-ideas",
        description:
          "Build snack plates with produce, protein, and crunchy add-ons for home or work."
      },
      {
        label: "Healthy Snacks for Work",
        href: "/healthy-snacks-for-work",
        description:
          "Plan portable snacks that fit busy days without relying on high-sugar convenience foods."
      },
      {
        label: "Simple Grocery List for Healthy Eating",
        href: "/simple-grocery-list-for-healthy-eating",
        description:
          "Keep low-sugar snack staples ready with a practical grocery list."
      }
    ],
    faqs: [
      {
        question: "What makes a snack low sugar but filling?",
        answer:
          "A filling low-sugar snack usually combines protein or healthy fat with fiber, such as nuts with fruit, yogurt with seeds, or vegetables with hummus."
      },
      {
        question: "Are low-sugar snacks only for weight loss?",
        answer:
          "No. Low-sugar snacks can also help with steadier energy, fewer afternoon crashes, and simpler meal planning."
      }
    ]
  },
  "healthy-breakfast-ideas": {
    eyebrow: "Breakfast Search Guide",
    title: "Build a Breakfast That Is Healthy and Realistic",
    summary:
      "A healthy breakfast is easier to repeat when it has a simple structure: protein, fiber-rich carbohydrates, color from fruit or vegetables, and a prep method that fits your morning.",
    links: [
      {
        label: "High-Fiber Breakfast Ideas",
        href: "/high-fiber-breakfast-ideas",
        description:
          "Use these ideas when you want breakfast to feel more filling and steady."
      },
      {
        label: "Simple Breakfast Meal Prep",
        href: "/simple-breakfast-meal-prep",
        description:
          "Prep a few breakfast pieces ahead so busy mornings are easier."
      },
      {
        label: "Add Protein to Every Meal",
        href: "/add-protein-to-every-meal",
        description:
          "Find simple protein options that make breakfast more balanced."
      }
    ],
    faqs: [
      {
        question: "What should a healthy breakfast include?",
        answer:
          "A healthy breakfast often includes protein, fiber-rich carbohydrates, fruit or vegetables, and enough fluid to support a steady morning routine."
      },
      {
        question: "What is a quick healthy breakfast for busy mornings?",
        answer:
          "Quick options include overnight oats, yogurt with fruit and seeds, whole-grain toast with eggs, or a smoothie paired with a protein source."
      }
    ]
  },
  "balanced-plate-guide": {
    eyebrow: "Meal Planning Search Guide",
    title: "Use the Balanced Plate Method Without Overthinking Meals",
    summary:
      "The balanced plate method is most useful when it stays flexible: choose a protein, add colorful produce, include a fiber-rich carbohydrate, and finish with a small amount of fat or flavor.",
    links: [
      {
        label: "High-Fiber Breakfast Ideas",
        href: "/high-fiber-breakfast-ideas",
        description:
          "Apply the balanced plate idea to morning meals that feel filling and steady."
      },
      {
        label: "Easy Balanced Dinner Formula",
        href: "/easy-balanced-dinner-formula",
        description:
          "Turn the same plate structure into simple dinners for busy nights."
      },
      {
        label: "Simple Grocery List for Healthy Eating",
        href: "/simple-grocery-list-for-healthy-eating",
        description:
          "Stock flexible staples so balanced meals are easier to repeat."
      }
    ],
    faqs: [
      {
        question: "What are the parts of a balanced plate?",
        answer:
          "A balanced plate usually includes protein, vegetables or fruit, fiber-rich carbohydrates, and a small amount of healthy fat or flavor."
      },
      {
        question: "Do I need to measure every meal?",
        answer:
          "No. The balanced plate method is a visual guide, so it can work without strict measuring or calorie tracking."
      }
    ]
  },
  "better-sleep-routine-guide": {
    eyebrow: "Sleep Search Guide",
    title: "Make a Better Sleep Routine Easier to Repeat",
    summary:
      "A better sleep routine works best when it starts before bedtime: reduce bright screens, keep caffeine timing realistic, choose a short wind-down cue, and keep wake time steady when possible.",
    links: [
      {
        label: "Sleep Hygiene Checklist",
        href: "/sleep-hygiene-checklist-printable",
        description:
          "Use a practical checklist to review light, temperature, caffeine, and bedtime habits."
      },
      {
        label: "Phone-Free Bedtime Routine",
        href: "/phone-free-bedtime-routine",
        description:
          "Build a realistic screen boundary when late scrolling keeps pushing sleep later."
      },
      {
        label: "How to Reset After a Bad Night of Sleep",
        href: "/how-to-reset-after-a-bad-night-sleep",
        description:
          "Recover the next day without overcorrecting or making the next night harder."
      }
    ],
    faqs: [
      {
        question: "How long should a sleep routine take?",
        answer:
          "A useful sleep routine can be short. Even 15 to 30 minutes of repeatable wind-down cues may help your body transition toward rest."
      },
      {
        question: "What is the first sleep habit to fix?",
        answer:
          "Start with a consistent wake time or a simple evening screen boundary, because both can shape the rest of the routine."
      }
    ]
  },
  "stress-management-guide": {
    eyebrow: "Stress Search Guide",
    title: "Choose Stress Tools Based on What You Feel",
    summary:
      "Stress management is easier when the tool matches the moment: slow breathing for racing thoughts, grounding for overwhelm, movement for restless energy, and journaling for repeated worry loops.",
    links: [
      {
        label: "Grounding Techniques for Stress",
        href: "/grounding-techniques-for-stress",
        description:
          "Use sensory grounding when stress feels intense or hard to organize."
      },
      {
        label: "Work Stress Reset Routine",
        href: "/work-stress-reset-routine",
        description:
          "Try a short reset for overloaded workdays and transition moments."
      },
      {
        label: "Stress Journaling Prompts",
        href: "/stress-journaling-prompts",
        description:
          "Separate facts, feelings, worries, and next actions with structured prompts."
      }
    ],
    faqs: [
      {
        question: "What is a quick way to manage stress?",
        answer:
          "A quick stress reset can start with slower exhales, naming what is in your control, or taking a brief walk to discharge restless energy."
      },
      {
        question: "When should stress get professional support?",
        answer:
          "Consider professional support when stress disrupts sleep, work, relationships, safety, or daily functioning, or when symptoms feel unmanageable."
      }
    ]
  },
  "7-day-wellness-reset-checklist": {
    eyebrow: "Wellness Reset Search Guide",
    title: "Use the 7-Day Reset as a Simple Weekly Starting Point",
    summary:
      "A short reset works best when it focuses on a few repeatable basics: hydration, sleep cues, easy meals, light movement, and one stress-support habit per day.",
    links: [
      {
        label: "How to Build a Simple Wellness Plan",
        href: "/how-to-build-a-simple-wellness-plan",
        description:
          "Turn the checklist into a longer-term plan that fits your week."
      },
      {
        label: "Daily Wellness Checklist",
        href: "/daily-wellness-checklist",
        description:
          "Use a daily version when you want a repeatable habit tracker."
      },
      {
        label: "Simple Hydration Guide",
        href: "/simple-hydration-guide",
        description:
          "Make the hydration part of the reset easier and more realistic."
      }
    ],
    faqs: [
      {
        question: "What is a 7-day wellness reset?",
        answer:
          "A 7-day wellness reset is a short, practical way to restart simple habits around sleep, hydration, meals, movement, and stress support."
      },
      {
        question: "Should I restart if I miss a day?",
        answer:
          "No. Continue with the next small step instead of restarting the whole week, because consistency grows from recovery, not perfection."
      }
    ]
  }
};
