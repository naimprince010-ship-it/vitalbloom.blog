from generate_featured_images import make_image


IMAGES = [
    {
        "filename": "healthy-pantry-staples-for-beginners.png",
        "title": "Healthy Pantry Staples",
        "subtitle": "Beginner basics for fast balanced meals",
        "palette": ("#f7f4ee", "#e6d8bd", "#9a7344", "#3b2b1d"),
    },
    {
        "filename": "easy-balanced-dinner-formula.png",
        "title": "Balanced Dinner Formula",
        "subtitle": "A simple structure for weeknight meals",
        "palette": ("#f6f8ef", "#d8e7bd", "#789044", "#303b1f"),
    },
    {
        "filename": "simple-breakfast-meal-prep.png",
        "title": "Breakfast Meal Prep",
        "subtitle": "Simple morning options for busy weeks",
        "palette": ("#fff7ed", "#f0d4a7", "#b96f2f", "#3b2618"),
    },
    {
        "filename": "how-to-build-a-filling-salad.png",
        "title": "Build a Filling Salad",
        "subtitle": "Protein, fiber, texture, and flavor",
        "palette": ("#f0f8f4", "#c6e3d2", "#4b8a63", "#1f3527"),
    },
    {
        "filename": "healthy-snacks-for-work.png",
        "title": "Healthy Snacks for Work",
        "subtitle": "Steady energy between busy tasks",
        "palette": ("#eef8f7", "#bee7e2", "#3f8f86", "#193b38"),
    },
]


def main() -> None:
    for config in IMAGES:
        make_image(config)
        print(config["filename"])


if __name__ == "__main__":
    main()
