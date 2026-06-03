import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
TODAY = "2026-06-03"
MARKER = "<!-- vitalbloom-top20-quality-final-two-v1 -->"

SECTIONS = {
    "rest-day-routine-for-beginners": """
<section>
  <h2>Sample Week With Beginner Rest Days</h2>
  <p>A simple week might use strength training on Monday, a walk on Tuesday, full or active rest on Wednesday, strength training on Thursday, and gentle movement on Saturday. Friday or Sunday can stay flexible depending on soreness, sleep, and schedule.</p>
  <p>This sample is only a starting point. If soreness is high, sleep is poor, or pain appears, move the rest day earlier instead of forcing the plan.</p>
</section>
""",
    "beginner-meal-prep-checklist": """
<section>
  <h2>When to Personalize Meal Prep With a Professional</h2>
  <p>A checklist can make everyday meals easier, but it is not a medical nutrition plan. If you manage diabetes, kidney disease, digestive conditions, food allergies, pregnancy-related nutrition needs, or a history of disordered eating, personalize meal prep with a registered dietitian or clinician.</p>
  <p>Professional guidance can help you keep the checklist practical while matching your health needs, food access, culture, budget, and preferences.</p>
</section>
""",
}


def run_wp(*args: str) -> str:
    result = subprocess.run(["wp", *args, "--allow-root"], cwd=WP_PATH, text=True, capture_output=True, check=False)
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip())
    return result.stdout


def post_id(slug: str) -> str:
    found = run_wp("post", "list", f"--name={slug}", "--post_type=post", "--field=ID").strip()
    if not found:
        raise RuntimeError(f"Post not found: {slug}")
    return found.splitlines()[0]


def main() -> None:
    for slug, section in SECTIONS.items():
        pid = post_id(slug)
        content = run_wp("post", "get", pid, "--field=post_content")
        if MARKER not in content:
            run_wp("post", "update", pid, f"--post_content={content.rstrip()}\n\n{MARKER}\n{section.strip()}\n")
            action = "section-added"
        else:
            action = "section-exists"
        run_wp("post", "meta", "update", pid, "_vitalbloom_fact_checked_at", TODAY)
        run_wp("post", "meta", "update", pid, "_vitalbloom_reviewed_at", TODAY)
        print(f"{action}: {pid} {slug}")


if __name__ == "__main__":
    main()
