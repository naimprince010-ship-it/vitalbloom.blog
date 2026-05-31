export const pillarGuideSlugs = [
  "stress-management-guide",
  "beginner-home-workout-guide",
  "balanced-plate-guide",
  "journaling-for-mental-clarity",
  "better-sleep-routine-guide"
] as const;

export const categoryPillarGuideSlugs: Record<string, string[]> = {
  fitness: ["beginner-home-workout-guide"],
  mindfulness: ["stress-management-guide", "journaling-for-mental-clarity"],
  nutrition: ["balanced-plate-guide"],
  sleep: ["better-sleep-routine-guide"],
  wellness: ["stress-management-guide", "balanced-plate-guide"]
};
