from generate_featured_images import make_image


IMAGES = [
    {
        "filename": "how-to-wind-down-after-work.png",
        "title": "Wind Down After Work",
        "subtitle": "A calmer transition from work to evening",
        "palette": ("#eef6fa", "#c2dce8", "#3f7892", "#1d3540"),
    },
    {
        "filename": "sleep-friendly-evening-routine.png",
        "title": "Sleep-Friendly Evening Routine",
        "subtitle": "Simple cues for a more restful night",
        "palette": ("#f4f2fb", "#d2c9eb", "#6d5c9e", "#2f2946"),
    },
    {
        "filename": "phone-free-bedtime-routine.png",
        "title": "Phone-Free Bedtime Routine",
        "subtitle": "Gentler nights with clearer boundaries",
        "palette": ("#f1f1f8", "#c9cae8", "#555c96", "#252840"),
    },
    {
        "filename": "simple-relaxation-techniques.png",
        "title": "Simple Relaxation Techniques",
        "subtitle": "Breathing, release, and calm attention",
        "palette": ("#eef8f7", "#bee7e2", "#3f8f86", "#193b38"),
    },
    {
        "filename": "how-to-reset-after-a-bad-night-sleep.png",
        "title": "Reset After Bad Sleep",
        "subtitle": "A steady day after a rough night",
        "palette": ("#f3f1fa", "#d3caea", "#675a9d", "#2b2944"),
    },
]


def main() -> None:
    for config in IMAGES:
        make_image(config)
        print(config["filename"])


if __name__ == "__main__":
    main()
