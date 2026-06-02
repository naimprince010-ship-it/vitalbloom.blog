from generate_featured_images import make_image


IMAGES = [
    {
        "filename": "morning-routine-for-low-energy-days.png",
        "title": "Low-Energy Morning Routine",
        "subtitle": "Gentle first steps for slower days",
        "palette": ("#f7f4ee", "#e7d9bf", "#9a7344", "#3b2b1d"),
    },
    {
        "filename": "healthy-habits-when-life-feels-busy.png",
        "title": "Healthy Habits for Busy Life",
        "subtitle": "Small routines when time feels tight",
        "palette": ("#f0f8f4", "#c6e3d2", "#4b8a63", "#1f3527"),
    },
    {
        "filename": "how-to-build-a-weekly-reset-routine.png",
        "title": "Weekly Reset Routine",
        "subtitle": "A calmer way to start the next week",
        "palette": ("#eef6fa", "#c2dce8", "#3f7892", "#1d3540"),
    },
    {
        "filename": "simple-self-care-checklist.png",
        "title": "Simple Self-Care Checklist",
        "subtitle": "Practical care without perfection pressure",
        "palette": ("#f5f2fa", "#d6c8eb", "#755aa0", "#302640"),
    },
    {
        "filename": "digital-wellness-routine.png",
        "title": "Digital Wellness Routine",
        "subtitle": "Healthier screen boundaries for everyday life",
        "palette": ("#eef8f7", "#bee7e2", "#3f8f86", "#193b38"),
    },
]


def main() -> None:
    for config in IMAGES:
        make_image(config)
        print(config["filename"])


if __name__ == "__main__":
    main()
