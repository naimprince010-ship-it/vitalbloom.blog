import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
MARKER = "<!-- vitalbloom-authority-expansion-v1 -->"

AUTHORITY_SECTIONS: dict[str, str] = {
    "foods-support-better-digestion": """
<section>
  <h2>How to Build a Digestion-Friendly Plate</h2>
  <p>A digestion-friendly plate is usually balanced, familiar, and not overloaded with too many new foods at once. Start with one fiber source, one protein source, and one cooked or raw produce option that your body already tolerates well. Then add variety slowly.</p>
  <p>For example, breakfast might be oatmeal with yogurt and berries. Lunch might be lentils with rice, cooked vegetables, and water. Dinner might be fish, potatoes, and zucchini. These meals are not magic fixes, but they combine fiber, fluids, protein, and steady meal timing in a practical way.</p>
  <p>If you are increasing fiber, give your body time. Adding beans, bran, seeds, and large salads all at once can backfire and make bloating worse. A better approach is to add one higher-fiber food for several days, drink enough fluids, and notice how you feel.</p>
</section>
<section>
  <h2>Simple Meal Ideas for Better Digestion</h2>
  <ul>
    <li>Oatmeal with banana, chia seeds, and plain yogurt.</li>
    <li>Rice bowl with lentils, cooked carrots, spinach, and olive oil.</li>
    <li>Whole-grain toast with eggs and a side of fruit.</li>
    <li>Soup with beans, vegetables, and enough broth for hydration.</li>
    <li>Greek yogurt with berries and ground flaxseed.</li>
  </ul>
  <p>Keep portions comfortable. Feeling overly full can make digestion feel harder, even when the foods themselves are nutritious.</p>
</section>
""",
    "journaling-mental-clarity": """
<section>
  <h2>A 10-Minute Journaling Structure</h2>
  <p>If open-ended journaling feels too vague, use a simple structure. Spend three minutes writing everything on your mind, three minutes sorting those thoughts into categories, two minutes choosing what needs action, and two minutes closing with one realistic next step.</p>
  <p>This structure helps prevent journaling from becoming endless rumination. The point is not to solve every problem in one sitting. The point is to move thoughts out of a crowded mental space and into a format you can review calmly.</p>
  <p>You can also keep separate pages for decisions, worries, gratitude, and ideas. Separating categories makes patterns easier to see over time.</p>
</section>
<section>
  <h2>Journaling Prompts for Different Needs</h2>
  <ul>
    <li>For stress: What is the real concern underneath this feeling?</li>
    <li>For decisions: What are the facts, assumptions, and tradeoffs?</li>
    <li>For focus: What would make today feel successful enough?</li>
    <li>For sleep: What can wait until tomorrow?</li>
    <li>For confidence: What evidence shows I handled something difficult before?</li>
  </ul>
  <p>Use one prompt at a time. Too many prompts can turn a calming habit into another task list.</p>
</section>
""",
    "low-sugar-snack-ideas": """
<section>
  <h2>How to Read Snack Labels Without Overthinking</h2>
  <p>When choosing packaged snacks, look first at added sugar, protein, fiber, and serving size. A snack can look healthy on the front of the package while still being mostly refined starch or sweetener. The nutrition label gives a clearer picture.</p>
  <p>Added sugar is different from the natural sugar found in whole fruit or plain dairy. If a snack is sweetened with syrup, cane sugar, honey, or concentrated fruit juice, it may still raise the total added sugar even when the branding sounds natural.</p>
  <p>A practical rule is to pair sweetness with staying power. Fruit with yogurt, apple with peanut butter, or berries with cottage cheese usually feels more satisfying than a sweet snack eaten by itself.</p>
</section>
<section>
  <h2>Low-Sugar Snacks by Situation</h2>
  <ul>
    <li>For work: nuts, boiled eggs, plain yogurt, hummus cups, or roasted chickpeas.</li>
    <li>For evenings: cottage cheese, herbal tea with a small whole-grain snack, or Greek yogurt with cinnamon.</li>
    <li>For kids or family snacks: apple slices with nut butter, cheese with fruit, or popcorn with seeds.</li>
    <li>For travel: tuna packets, unsweetened trail mix, whole-grain crackers, or protein-rich snack bars with low added sugar.</li>
  </ul>
  <p>The best snack is the one you can prepare before hunger gets intense. Planning ahead makes lower-sugar choices much easier.</p>
</section>
""",
    "daily-wellness-routine-beginners": """
<section>
  <h2>A Simple 7-Day Starter Plan</h2>
  <p>If you are not sure where to begin, use the first week as a light experiment. Day one can be water with breakfast. Day two can add a short walk. Day three can include a balanced lunch. Day four can add a two-minute breathing break. Day five can include a screen-free wind-down cue.</p>
  <p>On days six and seven, review what felt easiest and what created friction. Keep the habits that fit your life and shrink the ones that felt too big. This makes the routine personal instead of copied from someone else's schedule.</p>
  <p>A beginner plan should also include recovery. If you are tired, sick, or overloaded, the minimum version still counts. Drinking water, stepping outside for light, or preparing one simple meal can be enough to keep the routine alive.</p>
</section>
<section>
  <h2>How to Know Your Routine Is Working</h2>
  <ul>
    <li>You can repeat it on normal busy days.</li>
    <li>It supports energy without creating guilt.</li>
    <li>You have a minimum version for stressful days.</li>
    <li>You are improving sleep, meals, movement, or stress awareness gradually.</li>
    <li>You recover quickly after missing a day.</li>
  </ul>
  <p>Progress should feel steady, not dramatic. The goal is a routine that quietly supports your life for months, not a perfect week that disappears.</p>
</section>
""",
    "exercise-sustainable-habit": """
<section>
  <h2>Build a Weekly Exercise Menu</h2>
  <p>A weekly exercise menu gives you options instead of a rigid plan. Choose two or three main workouts, then keep several smaller backup options ready. This helps you keep moving when weather, energy, time, or motivation changes.</p>
  <p>Your main menu might include a 30-minute walk, a beginner strength session, and a mobility routine. Your backup menu might include a five-minute walk, one set of squats and wall pushups, or gentle stretching before bed.</p>
  <p>This approach works because it protects the habit identity. Even when the full workout is not possible, you still practice being someone who returns to movement.</p>
</section>
<section>
  <h2>When to Make Exercise Harder</h2>
  <p>Increase difficulty only after the routine feels repeatable. You might add five minutes to a walk, one extra set to strength training, or one additional workout day per week. Small increases are usually easier to sustain than sudden jumps.</p>
  <p>Watch for warning signs such as unusual pain, poor sleep, low motivation, or soreness that does not improve. Those signs may mean you need more recovery, less intensity, or professional guidance.</p>
  <ul>
    <li>Add time before adding intensity.</li>
    <li>Increase one variable at a time.</li>
    <li>Keep at least one easy movement day in the week.</li>
    <li>Choose consistency before chasing fast results.</li>
  </ul>
</section>
""",
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
    return result.stdout


def post_id(slug: str) -> str:
    found = run_wp("post", "list", f"--name={slug}", "--post_type=post", "--field=ID").strip()
    if not found:
        raise RuntimeError(f"Post not found: {slug}")
    return found.splitlines()[0]


def main() -> None:
    for slug, section in AUTHORITY_SECTIONS.items():
        pid = post_id(slug)
        content = run_wp("post", "get", pid, "--field=post_content")
        if MARKER in content:
            print(f"already-expanded: {slug}")
            continue

        updated = content.rstrip() + "\n\n" + MARKER + "\n" + section.strip() + "\n"
        run_wp("post", "update", pid, f"--post_content={updated}")
        print(f"expanded: {pid} {slug}")


if __name__ == "__main__":
    main()
