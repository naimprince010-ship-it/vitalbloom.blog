import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
IMAGE_DIR = Path("/tmp/vitalbloom-drafts")

POST_IMAGES = {
    "daily-wellness-checklist": "daily-wellness-checklist.png",
    "sustainable-wellness-routine": "sustainable-wellness-routine.png",
    "healthy-breakfast-ideas": "healthy-breakfast-ideas.png",
    "beginner-home-workout-plan": "beginner-home-workout-plan.png",
    "better-sleep-routine": "better-sleep-routine.png",
    "high-protein-vegetarian-meals": "high-protein-vegetarian-meals.png",
    "walking-for-weight-management": "walking-for-weight-management.png",
    "sleep-hygiene-checklist": "sleep-hygiene-checklist.png",
    "simple-breathing-exercises": "simple-breathing-exercises.png",
    "healthy-habits-remote-workers": "healthy-habits-remote-workers.png",
}

CATEGORY_DESCRIPTIONS = {
    "wellness": "Simple routines, daily habits, and practical guidance for building a healthier lifestyle.",
    "nutrition": "Balanced eating ideas, meal tips, and everyday nutrition guidance for real life.",
    "fitness": "Beginner-friendly movement, home workouts, walking, stretching, and recovery tips.",
    "sleep": "Sleep routines, evening habits, and rest-friendly guidance for better daily energy.",
    "mindfulness": "Breathing exercises, stress support, journaling, and simple practices for a calmer mind.",
}


def run_wp(*args: str) -> str:
    result = subprocess.run(
        ["wp", *args, "--allow-root"],
        cwd=WP_PATH,
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip())
    return result.stdout.strip()


def post_id(slug: str) -> str:
    found = run_wp("post", "list", f"--name={slug}", "--post_type=post", "--field=ID")
    if not found:
        raise RuntimeError(f"Post not found: {slug}")
    return found.splitlines()[0]


def set_featured_images() -> None:
    for slug, filename in POST_IMAGES.items():
        image_path = IMAGE_DIR / filename
        attachment_id = run_wp(
            "media",
            "import",
            str(image_path),
            f"--title={slug.replace('-', ' ').title()}",
            f"--alt={slug.replace('-', ' ')}",
            "--porcelain",
        )
        run_wp("post", "meta", "update", post_id(slug), "_thumbnail_id", attachment_id)
        print(f"featured-image: {slug} -> {attachment_id}")


def update_categories() -> None:
    for slug, description in CATEGORY_DESCRIPTIONS.items():
        term_id = run_wp("term", "list", "category", f"--slug={slug}", "--field=term_id")
        if term_id:
            run_wp("term", "update", "category", term_id.splitlines()[0], f"--description={description}")
            print(f"category-description: {slug}")


def main() -> None:
    set_featured_images()
    update_categories()


if __name__ == "__main__":
    main()
