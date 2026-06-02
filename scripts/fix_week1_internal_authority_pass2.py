import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
MARKER = "<!-- vitalbloom-week1-internal-authority-v2 -->"

POST_LINKS = {
    "healthy-routine-after-travel": [
        ("Daily Wellness Routine for Beginners", "/daily-wellness-routine-beginners"),
        ("Daily Wellness Checklist", "/daily-wellness-checklist"),
    ],
    "how-to-stay-consistent-with-healthy-habits": [
        ("Daily Wellness Routine for Beginners", "/daily-wellness-routine-beginners"),
        ("Daily Wellness Checklist", "/daily-wellness-checklist"),
    ],
    "recover-after-stressful-day": [
        ("Stress Management Guide", "/stress-management-guide"),
        ("Stress Reset Checklist Printable", "/stress-reset-checklist-printable"),
    ],
    "simple-energy-boosting-habits": [
        ("Daily Wellness Routine for Beginners", "/daily-wellness-routine-beginners"),
        ("Daily Wellness Checklist", "/daily-wellness-checklist"),
    ],
    "sleep-hygiene-checklist-printable": [
        ("Better Sleep Routine Guide", "/better-sleep-routine-guide"),
        ("Sleep Hygiene Checklist Printable", "/sleep-hygiene-checklist-printable"),
    ],
    "beginner-evening-routine-better-sleep": [
        ("Better Sleep Routine Guide", "/better-sleep-routine-guide"),
        ("Sleep Hygiene Checklist Printable", "/sleep-hygiene-checklist-printable"),
    ],
    "budget-friendly-healthy-meals": [
        ("Balanced Plate Guide", "/balanced-plate-guide"),
        ("Balanced Plate Printable Guide", "/balanced-plate-printable-guide"),
    ],
    "easy-balanced-dinner-formula": [
        ("Balanced Plate Guide", "/balanced-plate-guide"),
        ("Balanced Plate Printable Guide", "/balanced-plate-printable-guide"),
    ],
    "healthy-pantry-staples-for-beginners": [
        ("Balanced Plate Guide", "/balanced-plate-guide"),
        ("Balanced Plate Printable Guide", "/balanced-plate-printable-guide"),
    ],
    "how-to-build-a-filling-salad": [
        ("Balanced Plate Guide", "/balanced-plate-guide"),
        ("Balanced Plate Printable Guide", "/balanced-plate-printable-guide"),
    ],
    "how-to-eat-more-vegetables": [
        ("Balanced Plate Guide", "/balanced-plate-guide"),
        ("Balanced Plate Printable Guide", "/balanced-plate-printable-guide"),
    ],
    "mindful-eating-for-beginners": [
        ("Balanced Plate Guide", "/balanced-plate-guide"),
        ("Balanced Plate Printable Guide", "/balanced-plate-printable-guide"),
    ],
    "bedtime-anxiety-racing-thoughts": [
        ("Better Sleep Routine Guide", "/better-sleep-routine-guide"),
        ("Sleep Hygiene Checklist Printable", "/sleep-hygiene-checklist-printable"),
    ],
    "nap-timing-guide": [
        ("Better Sleep Routine Guide", "/better-sleep-routine-guide"),
        ("Sleep Hygiene Checklist Printable", "/sleep-hygiene-checklist-printable"),
    ],
    "shift-work-sleep-basics": [
        ("Better Sleep Routine Guide", "/better-sleep-routine-guide"),
        ("Sleep Hygiene Checklist Printable", "/sleep-hygiene-checklist-printable"),
    ],
    "morning-stress-reset": [
        ("Stress Management Guide", "/stress-management-guide"),
        ("Stress Reset Checklist Printable", "/stress-reset-checklist-printable"),
    ],
    "stress-and-screen-time": [
        ("Stress Management Guide", "/stress-management-guide"),
        ("Stress Reset Checklist Printable", "/stress-reset-checklist-printable"),
    ],
    "10-minute-walking-routine": [
        ("Beginner Home Workout Guide", "/beginner-home-workout-guide"),
        ("Remote Worker Wellness Checklist", "/remote-worker-wellness-checklist"),
    ],
    "walking-for-weight-management": [
        ("Beginner Home Workout Guide", "/beginner-home-workout-guide"),
        ("Remote Worker Wellness Checklist", "/remote-worker-wellness-checklist"),
        ("10-Minute Walking Routine", "/10-minute-walking-routine"),
    ],
    "simple-meal-prep-healthy-lunches": [
        ("Balanced Plate Guide", "/balanced-plate-guide"),
        ("Balanced Plate Printable Guide", "/balanced-plate-printable-guide"),
    ],
    "foods-drinks-affect-sleep": [
        ("Better Sleep Routine Guide", "/better-sleep-routine-guide"),
        ("Sleep Hygiene Checklist Printable", "/sleep-hygiene-checklist-printable"),
    ],
    "how-to-reset-after-a-bad-night-sleep": [
        ("Better Sleep Routine Guide", "/better-sleep-routine-guide"),
        ("Sleep Hygiene Checklist Printable", "/sleep-hygiene-checklist-printable"),
    ],
    "phone-free-bedtime-routine": [
        ("Better Sleep Routine Guide", "/better-sleep-routine-guide"),
        ("Sleep Hygiene Checklist Printable", "/sleep-hygiene-checklist-printable"),
    ],
    "weekend-reset-for-better-sleep": [
        ("Better Sleep Routine Guide", "/better-sleep-routine-guide"),
        ("Sleep Hygiene Checklist Printable", "/sleep-hygiene-checklist-printable"),
    ],
    "daily-stress-relief-routine": [
        ("Stress Management Guide", "/stress-management-guide"),
        ("Stress Reset Checklist Printable", "/stress-reset-checklist-printable"),
    ],
    "beginner-guide-to-balanced-living": [
        ("Daily Wellness Routine for Beginners", "/daily-wellness-routine-beginners"),
        ("Daily Wellness Checklist", "/daily-wellness-checklist"),
    ],
    "exercise-sustainable-habit": [
        ("Beginner Home Workout Guide", "/beginner-home-workout-guide"),
        ("Remote Worker Wellness Checklist", "/remote-worker-wellness-checklist"),
    ],
    "post-workout-recovery-tips": [
        ("Beginner Home Workout Guide", "/beginner-home-workout-guide"),
        ("Remote Worker Wellness Checklist", "/remote-worker-wellness-checklist"),
    ],
    "stretching-routine-desk-workers": [
        ("Beginner Home Workout Guide", "/beginner-home-workout-guide"),
        ("Remote Worker Wellness Checklist", "/remote-worker-wellness-checklist"),
    ],
    "balanced-plate-method": [
        ("Balanced Plate Guide", "/balanced-plate-guide"),
        ("Balanced Plate Printable Guide", "/balanced-plate-printable-guide"),
    ],
    "balanced-plate-printable-guide": [
        ("Balanced Plate Guide", "/balanced-plate-guide"),
        ("Balanced Plate Printable Guide", "/balanced-plate-printable-guide"),
    ],
    "foods-support-better-digestion": [
        ("Balanced Plate Guide", "/balanced-plate-guide"),
        ("Balanced Plate Printable Guide", "/balanced-plate-printable-guide"),
    ],
    "healthy-breakfast-ideas": [
        ("Balanced Plate Guide", "/balanced-plate-guide"),
        ("Balanced Plate Printable Guide", "/balanced-plate-printable-guide"),
    ],
    "better-breaks-remote-work": [
        ("Daily Wellness Routine for Beginners", "/daily-wellness-routine-beginners"),
        ("Remote Worker Wellness Checklist", "/remote-worker-wellness-checklist"),
    ],
    "healthy-habits-remote-workers": [
        ("Remote Worker Wellness Checklist", "/remote-worker-wellness-checklist"),
    ],
    "remote-worker-wellness-checklist": [
        ("Remote Worker Wellness Checklist", "/remote-worker-wellness-checklist"),
    ],
    "daily-mobility-routine": [
        ("Beginner Home Workout Guide", "/beginner-home-workout-guide"),
        ("Remote Worker Wellness Checklist", "/remote-worker-wellness-checklist"),
    ],
    "stress-reset-checklist-printable": [
        ("Stress Management Guide", "/stress-management-guide"),
        ("Stress Reset Checklist Printable", "/stress-reset-checklist-printable"),
    ],
    "digital-wellness-routine": [
        ("Daily Wellness Routine for Beginners", "/daily-wellness-routine-beginners"),
        ("Daily Wellness Checklist", "/daily-wellness-checklist"),
    ],
    "healthy-habits-when-life-feels-busy": [
        ("Daily Wellness Routine for Beginners", "/daily-wellness-routine-beginners"),
        ("Daily Wellness Checklist", "/daily-wellness-checklist"),
    ],
    "meal-planning-for-busy-weeks": [
        ("Balanced Plate Guide", "/balanced-plate-guide"),
    ],
    "bedroom-environment-checklist": [
        ("Better Sleep Routine Guide", "/better-sleep-routine-guide"),
    ],
    "how-to-wind-down-after-work": [
        ("Stress Management Guide", "/stress-management-guide"),
    ],
    "stress-journaling-prompts": [
        ("Stress Management Guide", "/stress-management-guide"),
    ],
    "how-to-build-a-weekly-reset-routine": [
        ("Daily Wellness Routine for Beginners", "/daily-wellness-routine-beginners"),
    ],
    "fiber-rich-carbohydrates-guide": [
        ("Balanced Plate Guide", "/balanced-plate-guide"),
    ],
    "healthy-snack-plate-ideas": [
        ("Balanced Plate Guide", "/balanced-plate-guide"),
    ],
    "hydration-tracker-printable": [
        ("Balanced Plate Guide", "/balanced-plate-guide"),
    ],
    "simple-grocery-list-for-healthy-eating": [
        ("Balanced Plate Guide", "/balanced-plate-guide"),
    ],
    "evening-stress-reset": [
        ("Better Sleep Routine Guide", "/better-sleep-routine-guide"),
    ],
    "sleep-friendly-evening-routine": [
        ("Better Sleep Routine Guide", "/better-sleep-routine-guide"),
    ],
    "why-you-wake-up-tired": [
        ("Better Sleep Routine Guide", "/better-sleep-routine-guide"),
    ],
    "grounding-techniques-for-stress": [
        ("Stress Management Guide", "/stress-management-guide"),
    ],
    "simple-relaxation-techniques": [
        ("Stress Management Guide", "/stress-management-guide"),
    ],
    "simple-self-care-checklist": [
        ("Stress Management Guide", "/stress-management-guide"),
    ],
}

PILLAR_LINKS = {
    "daily-wellness-routine-beginners": [
        ("Healthy Routine After Travel", "/healthy-routine-after-travel"),
        ("How to Stay Consistent With Healthy Habits", "/how-to-stay-consistent-with-healthy-habits"),
        ("Simple Energy-Boosting Habits", "/simple-energy-boosting-habits"),
        ("Seasonal Wellness Tips", "/seasonal-wellness-tips"),
    ],
    "balanced-plate-guide": [
        ("Budget-Friendly Healthy Meals", "/budget-friendly-healthy-meals"),
        ("Healthy Pantry Staples for Beginners", "/healthy-pantry-staples-for-beginners"),
        ("How to Eat More Vegetables", "/how-to-eat-more-vegetables"),
        ("Mindful Eating for Beginners", "/mindful-eating-for-beginners"),
    ],
    "better-sleep-routine-guide": [
        ("Beginner Evening Routine for Better Sleep", "/beginner-evening-routine-better-sleep"),
        ("Nap Timing Guide", "/nap-timing-guide"),
        ("Shift Work Sleep Basics", "/shift-work-sleep-basics"),
        ("Weekend Sleep Schedule", "/weekend-sleep-schedule"),
    ],
    "stress-management-guide": [
        ("Morning Stress Reset", "/morning-stress-reset"),
        ("Daily Stress Relief Routine", "/daily-stress-relief-routine"),
        ("Stress and Screen Time", "/stress-and-screen-time"),
        ("Stress Journaling Prompts", "/stress-journaling-prompts"),
    ],
    "beginner-home-workout-guide": [
        ("10-Minute Walking Routine", "/10-minute-walking-routine"),
        ("Walking for Weight Management", "/walking-for-weight-management"),
        ("Exercise as a Sustainable Habit", "/exercise-sustainable-habit"),
        ("Stretching Routine for Desk Workers", "/stretching-routine-desk-workers"),
    ],
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


def missing_links(content: str, links: list[tuple[str, str]]) -> list[tuple[str, str]]:
    return [(label, href) for label, href in links if f'href="{href}"' not in content]


def link_section(links: list[tuple[str, str]]) -> str:
    items = "\n".join(f'  <li><a href="{href}">{label}</a></li>' for label, href in links)
    return f"""
<section>
  <h2>Related Authority Guides</h2>
  <p>These hub and checklist resources help connect this guide to the broader VitalBloom topic cluster.</p>
  <ul>
{items}
  </ul>
</section>
"""


def update_post(slug: str, links: list[tuple[str, str]]) -> str:
    pid = post_id(slug)
    content = run_wp("post", "get", pid, "--field=post_content")
    to_add = missing_links(content, links)
    if not to_add:
        return f"already-linked: {slug}"
    updated = content.rstrip() + "\n\n" + MARKER + "\n" + link_section(to_add).strip() + "\n"
    run_wp("post", "update", pid, f"--post_content={updated}")
    return f"linked: {slug} +{len(to_add)}"


def main() -> None:
    for slug, links in POST_LINKS.items():
        print(update_post(slug, links))
    for slug, links in PILLAR_LINKS.items():
        print(update_post(slug, links))


if __name__ == "__main__":
    main()
