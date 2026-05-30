from pathlib import Path
from PIL import Image, ImageDraw, ImageFont


OUTPUT_DIR = Path("content-plan/featured-images")
WIDTH = 1600
HEIGHT = 900


IMAGES = [
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
