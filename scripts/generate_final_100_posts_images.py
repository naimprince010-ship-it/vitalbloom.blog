from generate_featured_images import make_image


IMAGES = [
    {
        "filename": "how-to-build-a-simple-wellness-plan.png",
        "title": "Simple Wellness Plan",
        "subtitle": "A realistic map for sleep, meals, movement, and stress",
        "palette": ("#f0f8f4", "#c6e3d2", "#4b8a63", "#1f3527"),
    },
    {
        "filename": "healthy-routine-after-travel.png",
        "title": "Healthy Routine After Travel",
        "subtitle": "Reset gently after disrupted schedules",
        "palette": ("#eef6fa", "#c2dce8", "#3f7892", "#1d3540"),
    },
    {
        "filename": "how-to-stay-consistent-with-healthy-habits.png",
        "title": "Stay Consistent With Habits",
        "subtitle": "Small systems that survive real life",
        "palette": ("#f7f4ee", "#e7d9bf", "#9a7344", "#3b2b1d"),
    },
    {
        "filename": "weekend-reset-for-better-sleep.png",
        "title": "Weekend Reset for Sleep",
        "subtitle": "Rest without losing your weekday rhythm",
        "palette": ("#f4f2fb", "#d2c9eb", "#6d5c9e", "#2f2946"),
    },
    {
        "filename": "simple-energy-boosting-habits.png",
        "title": "Simple Energy Habits",
        "subtitle": "Steadier days with practical basics",
        "palette": ("#fff7ed", "#f0d4a7", "#b96f2f", "#3b2618"),
    },
    {
        "filename": "beginner-guide-to-balanced-living.png",
        "title": "Balanced Living Guide",
        "subtitle": "A beginner framework for everyday wellness",
        "palette": ("#eef8f7", "#bee7e2", "#3f8f86", "#193b38"),
    },
]


def main() -> None:
    for config in IMAGES:
        make_image(config)
        print(config["filename"])


if __name__ == "__main__":
    main()
