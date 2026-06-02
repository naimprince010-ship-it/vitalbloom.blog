from generate_featured_images import make_image


IMAGES = [
    {
        "filename": "simple-grocery-list-for-healthy-eating.png",
        "title": "Simple Grocery List",
        "subtitle": "Healthy eating staples without overbuying",
        "palette": ("#f6f8ef", "#d8e7bd", "#789044", "#303b1f"),
    },
    {
        "filename": "meal-planning-for-busy-weeks.png",
        "title": "Meal Planning for Busy Weeks",
        "subtitle": "Flexible meals when time is tight",
        "palette": ("#fff7ed", "#f0d4a7", "#b96f2f", "#3b2618"),
    },
    {
        "filename": "how-to-eat-more-vegetables.png",
        "title": "Eat More Vegetables",
        "subtitle": "Simple ways to add color to daily meals",
        "palette": ("#f0f8f4", "#c6e3d2", "#4b8a63", "#1f3527"),
    },
    {
        "filename": "budget-friendly-healthy-meals.png",
        "title": "Budget-Friendly Healthy Meals",
        "subtitle": "Balanced plates with practical pantry staples",
        "palette": ("#f7f4ee", "#e7d9bf", "#9a7344", "#3b2b1d"),
    },
    {
        "filename": "mindful-eating-for-beginners.png",
        "title": "Mindful Eating for Beginners",
        "subtitle": "A calmer way to notice meals and hunger",
        "palette": ("#eef8f7", "#bee7e2", "#3f8f86", "#193b38"),
    },
]


def main() -> None:
    for config in IMAGES:
        make_image(config)
        print(config["filename"])


if __name__ == "__main__":
    main()
