export const pillarGuideSlugs = [
  "stress-management-guide",
  "beginner-home-workout-guide",
  "balanced-plate-guide",
  "journaling-for-mental-clarity",
  "better-sleep-routine-guide"
] as const;

export const categoryPillarGuideSlugs: Record<string, string[]> = {
  fitness: [
    "beginner-home-workout-guide",
    "how-to-start-strength-training-at-home",
    "low-impact-cardio-for-beginners",
    "beginner-stretching-routine",
    "walking-for-weight-management"
  ],
  mindfulness: [
    "stress-management-guide",
    "journaling-for-mental-clarity",
    "beginner-meditation-guide",
    "simple-breathing-exercises",
    "simple-relaxation-techniques"
  ],
  nutrition: [
    "balanced-plate-guide",
    "beginner-meal-prep-checklist",
    "healthy-breakfast-ideas",
    "high-protein-vegetarian-meals",
    "simple-grocery-list-for-healthy-eating"
  ],
  sleep: ["better-sleep-routine-guide"],
  wellness: ["stress-management-guide", "balanced-plate-guide"]
};
