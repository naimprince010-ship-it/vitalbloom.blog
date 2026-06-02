import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
REFRESH_MARKER = "<!-- vitalbloom-content-refresh-eat-v2 -->"
INBOUND_MARKER = "<!-- vitalbloom-inbound-boost-v1 -->"

EXPANSIONS = {
    "exercise-sustainable-habit": """
<h2>Use a Minimum Movement Version</h2>
<p>A sustainable exercise habit needs a minimum version for difficult days. That might be a five-minute walk, one set of bodyweight exercises, a short stretch, or a mobility break. The minimum version keeps the habit alive when the full routine is unrealistic.</p>
<p>This matters because consistency is built through returns, not perfect streaks. When you practice the small version, you keep the identity of being someone who moves regularly without forcing your body or schedule past its limit.</p>
""",
    "post-workout-recovery-tips": """
<h2>Match Recovery to the Workout</h2>
<p>Recovery should match the kind of workout you did. A hard strength session may need more sleep, protein, and rest between sessions. A long walk may need hydration, food, and comfortable footwear. A mobility session may simply need consistency and gentle pacing.</p>
<p>Instead of using the same recovery checklist for every day, ask what the workout asked from your body. Then choose the recovery habit that answers that demand.</p>
""",
    "stretching-routine-desk-workers": """
<h2>Add a Midday Reset</h2>
<p>Desk workers often wait until the end of the day to stretch, but a midday reset can prevent stiffness from building. Stand up, roll the shoulders, stretch the chest, move the ankles, and take a short walk if possible.</p>
<p>Even two minutes can change how the afternoon feels. Pair the reset with lunch, a meeting ending, or a water refill so it becomes easier to remember.</p>
""",
    "balanced-plate-method": """
<h2>Use the Plate Method Without Perfection</h2>
<p>The balanced plate method is a guide, not a rulebook. Some meals will have more carbohydrates, some will have more vegetables, and some will be assembled quickly from leftovers. The goal is to return to the structure often enough that meals feel steadier.</p>
<p>If a meal is missing one part, add the easiest option. Fruit can add produce, yogurt can add protein, beans can add both protein and fiber-rich carbohydrates, and salsa or herbs can add flavor.</p>
""",
    "balanced-plate-printable-guide": """
<h2>How to Use the Printable During Meal Planning</h2>
<p>The printable works best when it is visible before the week begins. Use it while making a grocery list or planning two default meals. Choose one protein, one produce option, one fiber-rich carbohydrate, and one flavor item for each meal idea.</p>
<p>You do not need to fill every line perfectly. The printable is meant to reduce decisions, not create another strict food rule.</p>
""",
    "foods-support-better-digestion": """
<h2>Build Digestive Support Gradually</h2>
<p>Foods that support digestion often work best when added gradually. If you suddenly add large amounts of beans, raw vegetables, or high-fiber grains, your body may need time to adjust. Start with one change and drink fluids consistently.</p>
<p>Notice comfort, appetite, and routine. If digestive symptoms are persistent, painful, or unusual, seek professional guidance instead of trying to solve everything with food changes alone.</p>
""",
    "healthy-breakfast-ideas": """
<h2>Choose a Breakfast Backup</h2>
<p>A healthy breakfast routine becomes easier with one backup option. Keep oats, yogurt, eggs, nut butter, fruit, or whole-grain toast available so mornings do not depend on cooking motivation.</p>
<p>The backup does not need to be exciting. It needs to be fast, satisfying, and realistic enough that you will use it before the day becomes rushed.</p>
""",
    "low-sugar-snack-ideas": """
<h2>Pair Sweetness With Staying Power</h2>
<p>A lower-sugar snack can still include sweetness. The key is pairing sweet foods with protein, fat, or fiber so the snack feels more satisfying. Fruit with yogurt, apple with peanut butter, or berries with cottage cheese can feel both practical and enjoyable.</p>
<p>This approach avoids making snacks feel restrictive. The goal is steady energy and satisfaction, not removing pleasure from food.</p>
""",
}

INBOUND_LINKS = {
    "beginner-home-workout-guide": [
        ("Low-Impact Cardio for Beginners", "/low-impact-cardio-for-beginners"),
    ],
    "balanced-plate-guide": [
        ("Easy Balanced Dinner Formula", "/easy-balanced-dinner-formula"),
        ("Healthy Pantry Staples for Beginners", "/healthy-pantry-staples-for-beginners"),
        ("How to Build a Filling Salad", "/how-to-build-a-filling-salad"),
        ("Mindful Eating for Beginners", "/mindful-eating-for-beginners"),
    ],
    "better-sleep-routine-guide": [
        ("Nap Timing Guide", "/nap-timing-guide"),
        ("Shift Work Sleep Basics", "/shift-work-sleep-basics"),
        ("Sleep Routine for Parents and Caregivers", "/sleep-routine-for-parents-caregivers"),
    ],
    "stress-management-guide": [
        ("Recover After a Stressful Day", "/recover-after-stressful-day"),
        ("Student Stress Management Checklist", "/student-stress-management-checklist"),
    ],
    "daily-wellness-routine-beginners": [
        ("Healthy Routine After Travel", "/healthy-routine-after-travel"),
    ],
    "healthy-habits-remote-workers": [
        ("Low-Impact Cardio for Beginners", "/low-impact-cardio-for-beginners"),
        ("Recover After a Stressful Day", "/recover-after-stressful-day"),
    ],
    "sleep-friendly-evening-routine": [
        ("Nap Timing Guide", "/nap-timing-guide"),
        ("Sleep Routine for Parents and Caregivers", "/sleep-routine-for-parents-caregivers"),
    ],
    "healthy-snack-plate-ideas": [
        ("Mindful Eating for Beginners", "/mindful-eating-for-beginners"),
        ("How to Build a Filling Salad", "/how-to-build-a-filling-salad"),
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


def section(title: str, body: str, marker: str) -> str:
    return f"\n\n{marker}\n{body.strip()}\n"


def link_section(links: list[tuple[str, str]]) -> str:
    items = "\n".join(f'  <li><a href="{href}">{label}</a></li>' for label, href in links)
    return f"""
<section>
  <h2>More Helpful VitalBloom Guides</h2>
  <p>These related guides add practical next steps and strengthen this topic cluster.</p>
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
        run_wp("post", "update", pid, f"--post_content={content.rstrip()}{section('refresh', expansion, REFRESH_MARKER)}")
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
