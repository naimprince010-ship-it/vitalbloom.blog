from generate_featured_images import make_image


IMAGES = [
    {
        "filename": "beginner-stretching-routine.png",
        "title": "Beginner Stretching Routine",
        "subtitle": "Gentle flexibility habits for everyday comfort",
        "palette": ("#eef8f7", "#bee7e2", "#3f8f86", "#193b38"),
    },
    {
        "filename": "low-impact-cardio-for-beginners.png",
        "title": "Low-Impact Cardio",
        "subtitle": "Beginner movement that feels approachable",
        "palette": ("#eef6f8", "#badde3", "#2f7785", "#18333a"),
    },
    {
        "filename": "how-to-start-strength-training-at-home.png",
        "title": "Strength Training at Home",
        "subtitle": "Simple beginner steps without a gym",
        "palette": ("#f1f6f1", "#c8dfc8", "#4f8555", "#213424"),
    },
    {
        "filename": "daily-mobility-routine.png",
        "title": "Daily Mobility Routine",
        "subtitle": "Small joint-friendly movement breaks",
        "palette": ("#f0f8f4", "#c6e3d2", "#4b8a63", "#1f3527"),
    },
    {
        "filename": "rest-day-routine-for-beginners.png",
        "title": "Rest Day Routine",
        "subtitle": "Recover well and keep momentum steady",
        "palette": ("#f7f4ee", "#e7d9bf", "#9a7344", "#3b2b1d"),
    },
]


def main() -> None:
    for config in IMAGES:
        make_image(config)
        print(config["filename"])


if __name__ == "__main__":
    main()
