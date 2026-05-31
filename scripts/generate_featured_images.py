from pathlib import Path
from PIL import Image, ImageDraw, ImageFont


OUTPUT_DIR = Path("content-plan/featured-images")
WIDTH = 1600
HEIGHT = 900


IMAGES = [
    {
        "filename": "beginner-home-workout-guide.png",
        "title": "Beginner Home Workout Guide",
        "subtitle": "Simple strength and movement without a gym",
        "palette": ("#eef6f8", "#badde3", "#2f7785", "#18333a"),
    },
    {
        "filename": "balanced-plate-guide.png",
        "title": "Balanced Plate Guide",
        "subtitle": "Build simple meals with protein, plants, and fiber",
        "palette": ("#f6f8ef", "#d8e7bd", "#789044", "#303b1f"),
    },
    {
        "filename": "journaling-for-mental-clarity.png",
        "title": "Journaling for Mental Clarity",
        "subtitle": "Benefits, prompts, and a simple starter routine",
        "palette": ("#f7f4ee", "#e7d9bf", "#9a7344", "#3b2b1d"),
    },
    {
        "filename": "better-sleep-routine-guide.png",
        "title": "Better Sleep Routine Guide",
        "subtitle": "A complete beginner plan for calmer nights",
        "palette": ("#f2f1fa", "#c9d8f0", "#596aa4", "#252844"),
    },
    {
        "filename": "10-minute-walking-routine.png",
        "title": "10-Minute Walking Routine",
        "subtitle": "Short movement for busy days",
        "palette": ("#eef8f2", "#c7e7d2", "#43835a", "#1f3527"),
    },
    {
        "filename": "simple-meal-prep-healthy-lunches.png",
        "title": "Simple Healthy Lunch Meal Prep",
        "subtitle": "Flexible meals for weekday energy",
        "palette": ("#fff7ed", "#f0d4a7", "#b96f2f", "#3b2618"),
    },
    {
        "filename": "beginner-evening-routine-better-sleep.png",
        "title": "Beginner Evening Routine",
        "subtitle": "Gentle cues for better sleep",
        "palette": ("#f3f1fa", "#d3caea", "#675a9d", "#2b2944"),
    },
    {
        "filename": "better-breaks-remote-work.png",
        "title": "Better Breaks for Remote Work",
        "subtitle": "Movement, eyes, and energy resets",
        "palette": ("#eef6fa", "#c2dce8", "#3f7892", "#1d3540"),
    },
    {
        "filename": "high-fiber-breakfast-ideas.png",
        "title": "High-Fiber Breakfast Ideas",
        "subtitle": "Simple mornings with more staying power",
        "palette": ("#f6f8ef", "#d8e7bd", "#789044", "#303b1f"),
    },
    {
        "filename": "daily-wellness-checklist.png",
        "title": "Daily Wellness Checklist",
        "subtitle": "Simple habits for a healthier routine",
        "palette": ("#f7f4ee", "#d8ead7", "#436850", "#1f2d26"),
    },
    {
        "filename": "sustainable-wellness-routine.png",
        "title": "Sustainable Wellness Routine",
        "subtitle": "Realistic habits that fit everyday life",
        "palette": ("#f3f6f1", "#c8d8c1", "#5f7f63", "#243126"),
    },
    {
        "filename": "healthy-breakfast-ideas.png",
        "title": "Healthy Breakfast Ideas",
        "subtitle": "Balanced options for busy mornings",
        "palette": ("#fff7ed", "#f7d8a8", "#b7652c", "#3b2418"),
    },
    {
        "filename": "beginner-home-workout-plan.png",
        "title": "Beginner Home Workout Plan",
        "subtitle": "Build consistency with simple movement",
        "palette": ("#eef6f8", "#badde3", "#2f7785", "#18333a"),
    },
    {
        "filename": "better-sleep-routine.png",
        "title": "Better Sleep Routine",
        "subtitle": "Calmer evenings and more consistent rest",
        "palette": ("#f1f1f8", "#c8c7e3", "#585489", "#25243d"),
    },
    {
        "filename": "high-protein-vegetarian-meals.png",
        "title": "High-Protein Vegetarian Meals",
        "subtitle": "Balanced meal ideas for everyday eating",
        "palette": ("#f4f8ef", "#cfe5b8", "#5d8a3f", "#26351f"),
    },
    {
        "filename": "walking-for-weight-management.png",
        "title": "Walking for Weight Management",
        "subtitle": "Simple movement for energy and consistency",
        "palette": ("#eef7f5", "#b7ded8", "#347f77", "#183a37"),
    },
    {
        "filename": "sleep-hygiene-checklist.png",
        "title": "Sleep Hygiene Checklist",
        "subtitle": "Everyday habits for a calmer night",
        "palette": ("#f4f2fb", "#d2c9eb", "#6d5c9e", "#2f2946"),
    },
    {
        "filename": "simple-breathing-exercises.png",
        "title": "Simple Breathing Exercises",
        "subtitle": "Gentle resets for everyday stress",
        "palette": ("#eef8f7", "#bee7e2", "#3f8f86", "#193b38"),
    },
    {
        "filename": "healthy-habits-remote-workers.png",
        "title": "Healthy Habits for Remote Workers",
        "subtitle": "Better breaks, boundaries, and workday energy",
        "palette": ("#f5f6f2", "#d8dfc8", "#68764d", "#2d3324"),
    },
    {
        "filename": "foods-support-better-digestion.png",
        "title": "Foods for Better Digestion",
        "subtitle": "Gentle everyday choices for gut comfort",
        "palette": ("#f7f5ee", "#d8e6c6", "#6f8f4e", "#29351e"),
    },
    {
        "filename": "stretching-routine-desk-workers.png",
        "title": "Desk Worker Stretching Routine",
        "subtitle": "Simple movement for long sitting days",
        "palette": ("#eef6fa", "#c3dce8", "#417993", "#1d3641"),
    },
    {
        "filename": "evening-habits-better-rest.png",
        "title": "Evening Habits for Better Rest",
        "subtitle": "A calmer transition into the night",
        "palette": ("#f5f2fa", "#d6c8eb", "#755aa0", "#302640"),
    },
    {
        "filename": "beginner-meditation-guide.png",
        "title": "Beginner Meditation Guide",
        "subtitle": "Simple practice for a calmer mind",
        "palette": ("#f0f8f4", "#c6e3d2", "#4b8a63", "#1f3527"),
    },
    {
        "filename": "how-to-avoid-burnout.png",
        "title": "How to Avoid Burnout",
        "subtitle": "Daily boundaries for sustainable energy",
        "palette": ("#f8f4ef", "#ead1bc", "#a25f3b", "#3d281d"),
    },
    {
        "filename": "simple-hydration-guide.png",
        "title": "Simple Hydration Guide",
        "subtitle": "Steady fluid habits for everyday wellness",
        "palette": ("#edf8fb", "#bfe3ee", "#3d8aa4", "#1d3b47"),
    },
    {
        "filename": "strength-training-basics.png",
        "title": "Strength Training Basics",
        "subtitle": "Beginner movement patterns and progress",
        "palette": ("#f1f6f1", "#c8dfc8", "#4f8555", "#213424"),
    },
    {
        "filename": "foods-drinks-affect-sleep.png",
        "title": "Foods and Drinks That Affect Sleep",
        "subtitle": "Evening choices for better rest",
        "palette": ("#f3f1f8", "#ccc8e5", "#5b5890", "#272640"),
    },
    {
        "filename": "journaling-mental-clarity.png",
        "title": "Journaling for Mental Clarity",
        "subtitle": "Simple reflection prompts for busy minds",
        "palette": ("#f7f4ee", "#e6d8bd", "#9a7344", "#3b2b1d"),
    },
    {
        "filename": "seasonal-wellness-tips.png",
        "title": "Seasonal Wellness Tips",
        "subtitle": "Balanced habits through changing seasons",
        "palette": ("#f3f8ef", "#d4e6c5", "#6f914a", "#2d3b1f"),
    },
    {
        "filename": "low-sugar-snack-ideas.png",
        "title": "Low-Sugar Snack Ideas",
        "subtitle": "Satisfying options for steady energy",
        "palette": ("#fff7ed", "#f2d6aa", "#b97935", "#3d2818"),
    },
    {
        "filename": "post-workout-recovery-tips.png",
        "title": "Post-Workout Recovery Tips",
        "subtitle": "Rest, hydration, and smarter progress",
        "palette": ("#eef7f8", "#b9dde2", "#3b8290", "#1b3940"),
    },
    {
        "filename": "screen-time-and-sleep-quality.png",
        "title": "Screen Time and Sleep Quality",
        "subtitle": "Calmer evenings with less stimulation",
        "palette": ("#f1f1f8", "#c9cae8", "#555c96", "#252840"),
    },
    {
        "filename": "mindful-morning-routine.png",
        "title": "Mindful Morning Routine",
        "subtitle": "Start the day with calm and focus",
        "palette": ("#f2f8ef", "#d5e7c7", "#6a914d", "#29391e"),
    },
    {
        "filename": "small-healthy-habits.png",
        "title": "Small Healthy Habits",
        "subtitle": "Simple actions that improve your day",
        "palette": ("#f6f4ef", "#ded4bd", "#7b6b4a", "#312b20"),
    },
    {
        "filename": "balanced-plate-method.png",
        "title": "Balanced Plate Method",
        "subtitle": "Simple meals without counting calories",
        "palette": ("#f6f8ef", "#d8e8bd", "#789447", "#303b1f"),
    },
    {
        "filename": "exercise-sustainable-habit.png",
        "title": "Exercise as a Sustainable Habit",
        "subtitle": "Movement that fits real life",
        "palette": ("#eef6f7", "#c0dfe3", "#447f8a", "#1f3940"),
    },
    {
        "filename": "stress-affects-sleep.png",
        "title": "Stress and Sleep",
        "subtitle": "Gentle ways to calm the night",
        "palette": ("#f2f1f8", "#cac8e4", "#5d5a91", "#282641"),
    },
    {
        "filename": "practice-mindfulness-simply.png",
        "title": "Practice Mindfulness Simply",
        "subtitle": "Awareness in ordinary moments",
        "palette": ("#eff8f4", "#c7e5d5", "#4f8a68", "#203729"),
    },
    {
        "filename": "daily-wellness-routine-beginners.png",
        "title": "Daily Wellness Routine for Beginners",
        "subtitle": "Simple habits for a steady start",
        "palette": ("#f8f5ef", "#e4d7bf", "#8d744d", "#352b1f"),
    },
]


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    candidates = [
        "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
        "C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf",
    ]
    for candidate in candidates:
        try:
            return ImageFont.truetype(candidate, size)
        except OSError:
            continue
    return ImageFont.load_default()


def rounded_rectangle(draw: ImageDraw.ImageDraw, xy, radius: int, fill: str) -> None:
    draw.rounded_rectangle(xy, radius=radius, fill=fill)


def make_image(config: dict) -> None:
    background, accent_light, accent, ink = config["palette"]
    image = Image.new("RGB", (WIDTH, HEIGHT), background)
    draw = ImageDraw.Draw(image)

    for index in range(0, WIDTH, 48):
        color = accent_light if index % 96 == 0 else "#ffffff"
        draw.line([(index, 0), (index - 520, HEIGHT)], fill=color, width=2)

    rounded_rectangle(draw, (96, 96, WIDTH - 96, HEIGHT - 96), 42, "#ffffff")
    rounded_rectangle(draw, (118, 118, WIDTH - 118, HEIGHT - 118), 30, background)

    for offset, alpha_color in [
        (0, accent),
        (34, accent_light),
        (68, "#ffffff"),
    ]:
        draw.ellipse((WIDTH - 540 + offset, 120 + offset, WIDTH - 90 + offset, 570 + offset), fill=alpha_color)

    draw.rectangle((96, HEIGHT - 210, WIDTH - 96, HEIGHT - 96), fill=accent)

    label_font = font(30, bold=True)
    title_font = font(76, bold=True)
    subtitle_font = font(34)

    draw.text((150, 160), "VITALBLOOM", fill=accent, font=label_font)

    title_lines = wrap_text(draw, config["title"], title_font, 900)
    y = 270
    for line in title_lines:
        draw.text((150, y), line, fill=ink, font=title_font)
        y += 88

    draw.text((150, y + 18), config["subtitle"], fill="#4b5563", font=subtitle_font)
    draw.text((150, HEIGHT - 170), "Evidence-informed wellness guidance", fill="#ffffff", font=subtitle_font)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    image.save(OUTPUT_DIR / config["filename"], "PNG", optimize=True)


def wrap_text(draw: ImageDraw.ImageDraw, text: str, selected_font, max_width: int) -> list[str]:
    words = text.split()
    lines = []
    current = ""
    for word in words:
        candidate = f"{current} {word}".strip()
        bbox = draw.textbbox((0, 0), candidate, font=selected_font)
        if bbox[2] <= max_width:
            current = candidate
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def main() -> None:
    for config in IMAGES:
        make_image(config)


if __name__ == "__main__":
    main()
