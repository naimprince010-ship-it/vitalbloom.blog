from generate_featured_images import make_image


MISSING_IMAGES = [
    {
        "filename": "healthy-snack-plate-ideas.png",
        "title": "Healthy Snack Plate Ideas",
        "subtitle": "Balanced snacks for steady everyday energy",
        "palette": ("#fff7ed", "#f2d6aa", "#b97935", "#3d2818"),
    },
    {
        "filename": "fiber-rich-carbohydrates-guide.png",
        "title": "Fiber-Rich Carbohydrates",
        "subtitle": "Simple choices for balanced plates",
        "palette": ("#f6f8ef", "#d8e7bd", "#789044", "#303b1f"),
    },
    {
        "filename": "add-protein-to-every-meal.png",
        "title": "Add Protein to Every Meal",
        "subtitle": "Easy ways to build more satisfying plates",
        "palette": ("#f4f8ef", "#cfe5b8", "#5d8a3f", "#26351f"),
    },
    {
        "filename": "hydration-tracker-printable.png",
        "title": "Hydration Tracker Printable",
        "subtitle": "Notice your water habits with less guesswork",
        "palette": ("#edf8fb", "#bfe3ee", "#3d8aa4", "#1d3b47"),
    },
    {
        "filename": "beginner-meal-prep-checklist.png",
        "title": "Beginner Meal Prep Checklist",
        "subtitle": "Plan balanced meals without overthinking",
        "palette": ("#fff7ed", "#f0d4a7", "#b96f2f", "#3b2618"),
    },
    {
        "filename": "weekend-sleep-schedule.png",
        "title": "Weekend Sleep Schedule",
        "subtitle": "Rest well without wrecking Monday",
        "palette": ("#f1f1f8", "#c9cae8", "#555c96", "#252840"),
    },
    {
        "filename": "sleep-routine-for-parents-caregivers.png",
        "title": "Sleep Routine for Parents",
        "subtitle": "Small habits that support real-life rest",
        "palette": ("#f3f1fa", "#d3caea", "#675a9d", "#2b2944"),
    },
    {
        "filename": "shift-work-sleep-basics.png",
        "title": "Shift Work Sleep Basics",
        "subtitle": "Practical habits for irregular schedules",
        "palette": ("#eef6fa", "#c2dce8", "#3f7892", "#1d3540"),
    },
    {
        "filename": "bedroom-environment-checklist.png",
        "title": "Bedroom Environment Checklist",
        "subtitle": "Simple changes for a calmer sleep space",
        "palette": ("#f4f2fb", "#d2c9eb", "#6d5c9e", "#2f2946"),
    },
    {
        "filename": "nap-timing-guide.png",
        "title": "Nap Timing Guide",
        "subtitle": "Rest without ruining night sleep",
        "palette": ("#f2f1fa", "#c9d8f0", "#596aa4", "#252844"),
    },
    {
        "filename": "bedtime-anxiety-racing-thoughts.png",
        "title": "Bedtime Anxiety",
        "subtitle": "Quiet racing thoughts at night",
        "palette": ("#f5f2fa", "#d6c8eb", "#755aa0", "#302640"),
    },
    {
        "filename": "caffeine-and-sleep-cutoff.png",
        "title": "Caffeine and Sleep",
        "subtitle": "Find your cutoff time for better rest",
        "palette": ("#f3f1f8", "#ccc8e5", "#5b5890", "#272640"),
    },
    {
        "filename": "morning-light-and-sleep.png",
        "title": "Morning Light and Sleep",
        "subtitle": "A simple habit for better rhythm",
        "palette": ("#eef7f5", "#b7ded8", "#347f77", "#183a37"),
    },
    {
        "filename": "why-you-wake-up-tired.png",
        "title": "Why You Wake Up Tired",
        "subtitle": "Common causes and simple fixes",
        "palette": ("#f1f1f8", "#c8c7e3", "#585489", "#25243d"),
    },
    {
        "filename": "sleep-debt-recovery-guide.png",
        "title": "Sleep Debt Recovery Guide",
        "subtitle": "Reset gently after short nights",
        "palette": ("#f2f1fa", "#c9d8f0", "#596aa4", "#252844"),
    },
    {
        "filename": "recover-after-stressful-day.png",
        "title": "Recover After a Stressful Day",
        "subtitle": "A calmer reset for body and mind",
        "palette": ("#f8f4ef", "#ead1bc", "#a25f3b", "#3d281d"),
    },
    {
        "filename": "stress-journaling-prompts.png",
        "title": "Stress Journaling Prompts",
        "subtitle": "Simple reflection for mental clutter",
        "palette": ("#f7f4ee", "#e6d8bd", "#9a7344", "#3b2b1d"),
    },
    {
        "filename": "stress-and-screen-time.png",
        "title": "Stress and Screen Time",
        "subtitle": "Create calmer digital boundaries",
        "palette": ("#eef6fa", "#c3dce8", "#417993", "#1d3641"),
    },
    {
        "filename": "evening-stress-reset.png",
        "title": "Evening Stress Reset",
        "subtitle": "Stop carrying the day into bed",
        "palette": ("#f5f2fa", "#d6c8eb", "#755aa0", "#302640"),
    },
    {
        "filename": "morning-stress-reset.png",
        "title": "Morning Stress Reset",
        "subtitle": "Start the day with more calm",
        "palette": ("#eff8f4", "#c7e5d5", "#4f8a68", "#203729"),
    },
    {
        "filename": "daily-stress-relief-routine.png",
        "title": "Daily Stress Relief Routine",
        "subtitle": "Small resets that fit real life",
        "palette": ("#f0f8f4", "#c6e3d2", "#4b8a63", "#1f3527"),
    },
    {
        "filename": "student-stress-management-checklist.png",
        "title": "Student Stress Checklist",
        "subtitle": "Steady support for busy weeks",
        "palette": ("#f7f4ee", "#e7d9bf", "#9a7344", "#3b2b1d"),
    },
    {
        "filename": "work-stress-reset-routine.png",
        "title": "Work Stress Reset",
        "subtitle": "A practical routine for busy days",
        "palette": ("#eef6fa", "#c2dce8", "#3f7892", "#1d3540"),
    },
    {
        "filename": "grounding-techniques-for-stress.png",
        "title": "Grounding Techniques for Stress",
        "subtitle": "Simple ways to feel present again",
        "palette": ("#eef8f7", "#bee7e2", "#3f8f86", "#193b38"),
    },
    {
        "filename": "calm-down-when-stress-feels-overwhelming.png",
        "title": "Calm Down When Stress Feels Overwhelming",
        "subtitle": "Gentle steps for intense moments",
        "palette": ("#f5f2fa", "#d6c8eb", "#755aa0", "#302640"),
    },
    {
        "filename": "stress-reset-checklist-printable.png",
        "title": "Stress Reset Checklist Printable",
        "subtitle": "A simple one-page calm reset tool",
        "palette": ("#f5f2fa", "#d6c8eb", "#755aa0", "#302640"),
    },
    {
        "filename": "remote-worker-wellness-checklist.png",
        "title": "Remote Worker Wellness Checklist",
        "subtitle": "Better breaks, posture, and workday energy",
        "palette": ("#eef6fa", "#c2dce8", "#3f7892", "#1d3540"),
    },
    {
        "filename": "balanced-plate-printable-guide.png",
        "title": "Balanced Plate Printable Guide",
        "subtitle": "Build simple meals with more confidence",
        "palette": ("#f6f8ef", "#d8e7bd", "#789044", "#303b1f"),
    },
    {
        "filename": "sleep-hygiene-checklist-printable.png",
        "title": "Sleep Hygiene Checklist Printable",
        "subtitle": "A practical checklist for calmer nights",
        "palette": ("#f4f2fb", "#d2c9eb", "#6d5c9e", "#2f2946"),
    },
]


def main() -> None:
    for config in MISSING_IMAGES:
        make_image(config)
        print(config["filename"])


if __name__ == "__main__":
    main()
