import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
MARKER = "<!-- vitalbloom-week1-internal-authority-v1 -->"

POST_LINKS = {
    "seasonal-wellness-tips": [
        ("Daily Wellness Routine for Beginners", "/daily-wellness-routine-beginners"),
        ("Daily Wellness Checklist", "/daily-wellness-checklist"),
        ("Simple Wellness Plan", "/how-to-build-a-simple-wellness-plan"),
        ("Sustainable Wellness Routine", "/sustainable-wellness-routine"),
    ],
    "small-healthy-habits": [
        ("Daily Wellness Routine for Beginners", "/daily-wellness-routine-beginners"),
        ("Daily Wellness Checklist", "/daily-wellness-checklist"),
        ("How to Stay Consistent With Healthy Habits", "/how-to-stay-consistent-with-healthy-habits"),
        ("Simple Self-Care Checklist", "/simple-self-care-checklist"),
    ],
    "sustainable-wellness-routine": [
        ("Daily Wellness Routine for Beginners", "/daily-wellness-routine-beginners"),
        ("Daily Wellness Checklist", "/daily-wellness-checklist"),
        ("Simple Wellness Plan", "/how-to-build-a-simple-wellness-plan"),
        ("Healthy Habits When Life Feels Busy", "/healthy-habits-when-life-feels-busy"),
    ],
    "beginner-meditation-guide": [
        ("Stress Management Guide", "/stress-management-guide"),
        ("Stress Reset Checklist Printable", "/stress-reset-checklist-printable"),
        ("Practice Mindfulness Simply", "/practice-mindfulness-simply"),
        ("Simple Relaxation Techniques", "/simple-relaxation-techniques"),
    ],
    "healthy-habits-remote-workers": [
        ("Daily Wellness Routine for Beginners", "/daily-wellness-routine-beginners"),
        ("Remote Worker Wellness Checklist", "/remote-worker-wellness-checklist"),
        ("Better Breaks for Remote Work", "/better-breaks-remote-work"),
        ("Digital Wellness Routine", "/digital-wellness-routine"),
    ],
    "recover-after-stressful-day": [
        ("Stress Management Guide", "/stress-management-guide"),
        ("Stress Reset Checklist Printable", "/stress-reset-checklist-printable"),
        ("How to Wind Down After Work", "/how-to-wind-down-after-work"),
        ("Simple Relaxation Techniques", "/simple-relaxation-techniques"),
    ],
    "strength-training-basics": [
        ("Beginner Home Workout Guide", "/beginner-home-workout-guide"),
        ("Remote Worker Wellness Checklist", "/remote-worker-wellness-checklist"),
        ("How to Start Strength Training at Home", "/how-to-start-strength-training-at-home"),
        ("Rest Day Routine for Beginners", "/rest-day-routine-for-beginners"),
    ],
    "simple-hydration-guide": [
        ("Balanced Plate Guide", "/balanced-plate-guide"),
        ("Balanced Plate Printable Guide", "/balanced-plate-printable-guide"),
        ("Hydration Tracker Printable", "/hydration-tracker-printable"),
        ("Simple Energy-Boosting Habits", "/simple-energy-boosting-habits"),
    ],
    "sleep-routine-for-parents-caregivers": [
        ("Better Sleep Routine Guide", "/better-sleep-routine-guide"),
        ("Sleep Hygiene Checklist Printable", "/sleep-hygiene-checklist-printable"),
        ("Sleep-Friendly Evening Routine", "/sleep-friendly-evening-routine"),
        ("Bedroom Environment Checklist", "/bedroom-environment-checklist"),
    ],
    "weekend-sleep-schedule": [
        ("Better Sleep Routine Guide", "/better-sleep-routine-guide"),
        ("Sleep Hygiene Checklist Printable", "/sleep-hygiene-checklist-printable"),
        ("Weekend Reset for Better Sleep", "/weekend-reset-for-better-sleep"),
        ("How to Reset After a Bad Night's Sleep", "/how-to-reset-after-a-bad-night-sleep"),
    ],
    "work-stress-reset-routine": [
        ("Stress Management Guide", "/stress-management-guide"),
        ("Stress Reset Checklist Printable", "/stress-reset-checklist-printable"),
        ("How to Wind Down After Work", "/how-to-wind-down-after-work"),
        ("Simple Relaxation Techniques", "/simple-relaxation-techniques"),
    ],
    "high-fiber-breakfast-ideas": [
        ("Balanced Plate Guide", "/balanced-plate-guide"),
        ("Balanced Plate Printable Guide", "/balanced-plate-printable-guide"),
        ("Fiber-Rich Carbohydrates Guide", "/fiber-rich-carbohydrates-guide"),
        ("Simple Breakfast Meal Prep", "/simple-breakfast-meal-prep"),
    ],
    "low-sugar-snack-ideas": [
        ("Balanced Plate Guide", "/balanced-plate-guide"),
        ("Balanced Plate Printable Guide", "/balanced-plate-printable-guide"),
        ("Healthy Snack Plate Ideas", "/healthy-snack-plate-ideas"),
        ("Healthy Snacks for Work", "/healthy-snacks-for-work"),
    ],
    "better-sleep-routine": [
        ("Better Sleep Routine Guide", "/better-sleep-routine-guide"),
        ("Sleep Hygiene Checklist Printable", "/sleep-hygiene-checklist-printable"),
        ("Sleep-Friendly Evening Routine", "/sleep-friendly-evening-routine"),
        ("Phone-Free Bedtime Routine", "/phone-free-bedtime-routine"),
    ],
    "journaling-mental-clarity": [
        ("Stress Management Guide", "/stress-management-guide"),
        ("Stress Reset Checklist Printable", "/stress-reset-checklist-printable"),
        ("Stress Journaling Prompts", "/stress-journaling-prompts"),
        ("Journaling for Mental Clarity", "/journaling-for-mental-clarity"),
    ],
    "mindful-morning-routine": [
        ("Stress Management Guide", "/stress-management-guide"),
        ("Stress Reset Checklist Printable", "/stress-reset-checklist-printable"),
        ("Morning Routine for Low-Energy Days", "/morning-routine-for-low-energy-days"),
        ("Practice Mindfulness Simply", "/practice-mindfulness-simply"),
    ],
    "daily-wellness-checklist": [
        ("Daily Wellness Routine for Beginners", "/daily-wellness-routine-beginners"),
        ("Simple Wellness Plan", "/how-to-build-a-simple-wellness-plan"),
        ("Simple Self-Care Checklist", "/simple-self-care-checklist"),
        ("Healthy Habits When Life Feels Busy", "/healthy-habits-when-life-feels-busy"),
    ],
    "daily-wellness-routine-beginners": [
        ("Daily Wellness Checklist", "/daily-wellness-checklist"),
        ("Simple Wellness Plan", "/how-to-build-a-simple-wellness-plan"),
        ("Beginner Guide to Balanced Living", "/beginner-guide-to-balanced-living"),
        ("Weekly Reset Routine", "/how-to-build-a-weekly-reset-routine"),
    ],
    "remote-worker-wellness-checklist": [
        ("Daily Wellness Routine for Beginners", "/daily-wellness-routine-beginners"),
        ("Healthy Habits for Remote Workers", "/healthy-habits-remote-workers"),
        ("Better Breaks for Remote Work", "/better-breaks-remote-work"),
        ("Digital Wellness Routine", "/digital-wellness-routine"),
    ],
    "beginner-stretching-routine": [
        ("Beginner Home Workout Guide", "/beginner-home-workout-guide"),
        ("Remote Worker Wellness Checklist", "/remote-worker-wellness-checklist"),
        ("Daily Mobility Routine", "/daily-mobility-routine"),
        ("Stretching Routine for Desk Workers", "/stretching-routine-desk-workers"),
    ],
    "how-to-start-strength-training-at-home": [
        ("Beginner Home Workout Guide", "/beginner-home-workout-guide"),
        ("Remote Worker Wellness Checklist", "/remote-worker-wellness-checklist"),
        ("Strength Training Basics", "/strength-training-basics"),
        ("Post-Workout Recovery Tips", "/post-workout-recovery-tips"),
    ],
    "low-impact-cardio-for-beginners": [
        ("Beginner Home Workout Guide", "/beginner-home-workout-guide"),
        ("Remote Worker Wellness Checklist", "/remote-worker-wellness-checklist"),
        ("10-Minute Walking Routine", "/10-minute-walking-routine"),
        ("Walking for Weight Management", "/walking-for-weight-management"),
    ],
    "rest-day-routine-for-beginners": [
        ("Beginner Home Workout Guide", "/beginner-home-workout-guide"),
        ("Remote Worker Wellness Checklist", "/remote-worker-wellness-checklist"),
        ("Post-Workout Recovery Tips", "/post-workout-recovery-tips"),
        ("Daily Mobility Routine", "/daily-mobility-routine"),
    ],
    "healthy-snacks-for-work": [
        ("Balanced Plate Guide", "/balanced-plate-guide"),
        ("Balanced Plate Printable Guide", "/balanced-plate-printable-guide"),
        ("Healthy Snack Plate Ideas", "/healthy-snack-plate-ideas"),
        ("Add Protein to Every Meal", "/add-protein-to-every-meal"),
    ],
    "simple-breakfast-meal-prep": [
        ("Balanced Plate Guide", "/balanced-plate-guide"),
        ("Balanced Plate Printable Guide", "/balanced-plate-printable-guide"),
        ("High-Fiber Breakfast Ideas", "/high-fiber-breakfast-ideas"),
        ("Healthy Breakfast Ideas", "/healthy-breakfast-ideas"),
    ],
}

PILLAR_LINKS = {
    "better-sleep-routine-guide": [
        ("Sleep-Friendly Evening Routine", "/sleep-friendly-evening-routine"),
        ("Phone-Free Bedtime Routine", "/phone-free-bedtime-routine"),
        ("Weekend Reset for Better Sleep", "/weekend-reset-for-better-sleep"),
        ("How to Reset After a Bad Night's Sleep", "/how-to-reset-after-a-bad-night-sleep"),
        ("Sleep Hygiene Checklist Printable", "/sleep-hygiene-checklist-printable"),
    ],
    "stress-management-guide": [
        ("Stress Reset Checklist Printable", "/stress-reset-checklist-printable"),
        ("Simple Relaxation Techniques", "/simple-relaxation-techniques"),
        ("How to Wind Down After Work", "/how-to-wind-down-after-work"),
        ("Beginner Meditation Guide", "/beginner-meditation-guide"),
        ("Work Stress Reset Routine", "/work-stress-reset-routine"),
    ],
    "balanced-plate-guide": [
        ("Balanced Plate Printable Guide", "/balanced-plate-printable-guide"),
        ("Simple Grocery List for Healthy Eating", "/simple-grocery-list-for-healthy-eating"),
        ("Simple Breakfast Meal Prep", "/simple-breakfast-meal-prep"),
        ("Healthy Snacks for Work", "/healthy-snacks-for-work"),
        ("Fiber-Rich Carbohydrates Guide", "/fiber-rich-carbohydrates-guide"),
    ],
    "beginner-home-workout-guide": [
        ("Beginner Stretching Routine", "/beginner-stretching-routine"),
        ("Low-Impact Cardio for Beginners", "/low-impact-cardio-for-beginners"),
        ("How to Start Strength Training at Home", "/how-to-start-strength-training-at-home"),
        ("Daily Mobility Routine", "/daily-mobility-routine"),
        ("Rest Day Routine for Beginners", "/rest-day-routine-for-beginners"),
    ],
    "daily-wellness-routine-beginners": [
        ("Daily Wellness Checklist", "/daily-wellness-checklist"),
        ("Simple Wellness Plan", "/how-to-build-a-simple-wellness-plan"),
        ("Healthy Habits When Life Feels Busy", "/healthy-habits-when-life-feels-busy"),
        ("Simple Self-Care Checklist", "/simple-self-care-checklist"),
        ("Digital Wellness Routine", "/digital-wellness-routine"),
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
  <h2>Related VitalBloom Guides</h2>
  <p>Use these related guides to keep exploring this topic and connect the next practical step.</p>
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

    if MARKER in content:
        updated = content.rstrip() + "\n" + link_section(to_add).strip() + "\n"
    else:
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
