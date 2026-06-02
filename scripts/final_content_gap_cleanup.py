import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
REFRESH_MARKER = "<!-- vitalbloom-final-content-gap-cleanup-v1 -->"
INBOUND_MARKER = "<!-- vitalbloom-final-inbound-boost-v1 -->"

EXPANSIONS = {
    "balanced-plate-printable-guide": """
<h2>Turn the Printable Into a Weekly Habit</h2>
<p>The printable becomes more useful when it is part of a weekly routine. Use it before grocery shopping, before meal prep, or when you are choosing two default dinners for a busy week. Pick one protein, one produce option, one fiber-rich carbohydrate, and one flavor cue for each meal idea.</p>
<p>Keep the printable somewhere visible instead of saving it only for perfect planning days. A simple visual reminder can make balanced meals easier when you are tired or rushed.</p>
""",
    "better-sleep-routine": """
<h2>Keep One Sleep Cue Consistent</h2>
<p>If changing your whole sleep routine feels overwhelming, choose one cue to keep consistent. That might be dimming lights, charging your phone away from bed, writing tomorrow's first task, or using the same calming activity before sleep.</p>
<p>One cue repeated often can become the anchor for the rest of the routine. Once that cue feels natural, add another habit gradually.</p>
""",
    "screen-time-and-sleep-quality": """
<h2>Replace the Final Scroll</h2>
<p>Screen time before bed is often hardest to change because it fills a real need: decompression, distraction, connection, or entertainment. Instead of simply removing the phone, choose a replacement that answers the same need with less stimulation.</p>
<p>Try reading, music, stretching, journaling, a warm shower, or a short phone-free wind-down. The replacement should be easy enough that you can choose it when you are already tired.</p>
""",
    "sleep-hygiene-checklist-printable": """
<h2>Use the Checklist as a Troubleshooting Tool</h2>
<p>The printable is not meant to make bedtime perfect. Use it to identify one sleep friction point at a time. Maybe the room is too bright, caffeine is too late, the phone is too close, or tomorrow's tasks are still floating in your head.</p>
<p>Choose one item from the checklist for a week. A focused experiment is easier to learn from than changing every sleep habit at once.</p>
""",
    "practice-mindfulness-simply": """
<h2>Use Mindfulness During Ordinary Transitions</h2>
<p>Mindfulness is easier to practice when it attaches to ordinary transitions: before opening email, after washing hands, before eating, after getting into the car, or before bed. These small moments give you a natural pause.</p>
<p>You do not need a quiet room or long session. One breath, one sensation, or one moment of noticing can help you return to the present before moving into the next task.</p>
""",
    "add-protein-to-every-meal": """
<h2>Use a Protein Backup List</h2>
<p>Keep a short list of protein backups for busy days: eggs, Greek yogurt, cottage cheese, canned beans, lentils, tuna packets, tofu, hummus, nuts, seeds, or nut butter. The best backup is one you can use without much cooking.</p>
<p>This makes protein easier to add when the original meal plan falls apart. A backup list turns the advice into something practical.</p>
""",
}

INBOUND_LINKS = {
    "balanced-plate-guide": [
        ("Easy Balanced Dinner Formula", "/easy-balanced-dinner-formula"),
        ("Healthy Pantry Staples for Beginners", "/healthy-pantry-staples-for-beginners"),
    ],
    "simple-grocery-list-for-healthy-eating": [
        ("Healthy Pantry Staples for Beginners", "/healthy-pantry-staples-for-beginners"),
        ("Easy Balanced Dinner Formula", "/easy-balanced-dinner-formula"),
    ],
    "meal-planning-for-busy-weeks": [
        ("Easy Balanced Dinner Formula", "/easy-balanced-dinner-formula"),
        ("Healthy Routine After Travel", "/healthy-routine-after-travel"),
    ],
    "sleep-friendly-evening-routine": [
        ("Shift Work Sleep Basics", "/shift-work-sleep-basics"),
    ],
    "sleep-hygiene-checklist": [
        ("Shift Work Sleep Basics", "/shift-work-sleep-basics"),
    ],
    "student-stress-management-checklist": [
        ("Stress Management Guide", "/stress-management-guide"),
    ],
    "daily-stress-relief-routine": [
        ("Student Stress Management Checklist", "/student-stress-management-checklist"),
    ],
    "healthy-habits-when-life-feels-busy": [
        ("Healthy Routine After Travel", "/healthy-routine-after-travel"),
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


def link_section(links: list[tuple[str, str]]) -> str:
    items = "\n".join(f'  <li><a href="{href}">{label}</a></li>' for label, href in links)
    return f"""
<section>
  <h2>Related Practical Guides</h2>
  <p>Use these related guides to continue the next practical step in this topic cluster.</p>
  <ul>
{items}
  </ul>
</section>
"""


def refresh_content() -> None:
    for slug, expansion in EXPANSIONS.items():
        pid = post_id(slug)
        content = run_wp("post", "get", pid, "--field=post_content")
        if REFRESH_MARKER in content:
            print(f"already-refreshed: {slug}")
            continue
        run_wp("post", "update", pid, f"--post_content={content.rstrip()}\n\n{REFRESH_MARKER}\n{expansion.strip()}\n")
        print(f"refreshed: {pid} {slug}")


def boost_inbound() -> None:
    for slug, links in INBOUND_LINKS.items():
        pid = post_id(slug)
        content = run_wp("post", "get", pid, "--field=post_content")
        missing = [(label, href) for label, href in links if f'href="{href}"' not in content]
        if not missing:
            print(f"already-boosted: {slug}")
            continue
        run_wp("post", "update", pid, f"--post_content={content.rstrip()}\n\n{INBOUND_MARKER}\n{link_section(missing).strip()}\n")
        print(f"boosted: {pid} {slug} +{len(missing)}")


def main() -> None:
    refresh_content()
    boost_inbound()


if __name__ == "__main__":
    main()
