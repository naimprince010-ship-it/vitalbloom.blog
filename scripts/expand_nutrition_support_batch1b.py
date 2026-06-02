import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
MARKER = "<!-- vitalbloom-nutrition-support-batch1-expanded-v1b -->"

EXPANSIONS = {
    "beginner-meal-prep-checklist": """
<h2>Keep a Backup Meal</h2>
<p>Every beginner meal prep plan needs a backup meal. This might be eggs and toast, beans and rice, yogurt with oats and fruit, soup and bread, or a frozen meal with added vegetables. Backup meals prevent one missed prep day from turning into a week of stress.</p>
<h2>Review Before You Shop Again</h2>
<p>At the end of the week, ask what you actually ate. Keep the meals that worked and remove anything that stayed untouched. Meal prep improves through feedback, not by forcing yourself to like a plan that does not fit.</p>
""",
    "hydration-tracker-printable": """
<h2>Hydration and Sleep</h2>
<p>Hydration timing can affect sleep for some people. If you forget water all day and drink a lot late at night, bathroom trips may interrupt sleep. Try spreading fluids earlier and drinking comfortably in the evening rather than catching up all at once.</p>
<h2>Hydration and Hunger</h2>
<p>Thirst and hunger are different, but busy people may miss both signals. If you feel tired or snacky, check when you last ate and drank. A balanced snack plus water may work better than water alone or food alone.</p>
<h2>Common Tracker Mistakes</h2>
<p>One mistake is setting a goal that ignores your real day. Another is tracking perfectly for two days and then quitting. Keep the tracker flexible. Three check-ins per day may be enough. The tool should support awareness, not create guilt.</p>
<h2>Make Water More Appealing</h2>
<p>If plain water is hard to drink, try temperature changes, a straw, fruit, herbs, sparkling water, or a bottle that is easy to carry. Small preference changes can make the habit easier to repeat.</p>
""",
    "add-protein-to-every-meal": """
<h2>How to Add Protein Without Cooking More</h2>
<p>Use ready-to-eat options when cooking energy is low. Greek yogurt, cottage cheese, canned beans, canned tuna or salmon, hummus, nuts, seeds, rotisserie chicken, tofu, or boiled eggs can make meals easier. Convenience can still support balanced eating.</p>
<h2>Protein Pairing Examples</h2>
<ul>
  <li>Toast plus eggs and fruit.</li>
  <li>Rice plus beans and vegetables.</li>
  <li>Pasta plus lentils and greens.</li>
  <li>Crackers plus hummus and carrots.</li>
  <li>Oats plus yogurt and nuts.</li>
</ul>
<h2>If You Do Not Like Typical Protein Foods</h2>
<p>Start with foods you already tolerate. Add small portions instead of forcing a large serving. You might blend Greek yogurt into a smoothie, add beans to soup, use nut butter on toast, or add tofu to a stir-fry with a sauce you like.</p>
<h2>When to Get Personalized Advice</h2>
<p>People with kidney disease, digestive conditions, eating disorder history, athletic goals, pregnancy-related needs, or medical conditions may need individualized guidance. A registered dietitian or clinician can help tailor protein choices safely.</p>
""",
    "fiber-rich-carbohydrates-guide": """
<h2>Fiber-Rich Snacks</h2>
<p>Snacks can include fiber too. Try fruit with nuts, hummus with vegetables and whole-grain crackers, oats with yogurt, roasted chickpeas, or a small bean dip. Pairing fiber with protein often feels more satisfying than a snack made from only refined carbohydrates.</p>
<h2>Fiber and Hydration</h2>
<p>Fiber works best with enough fluid. If you add more beans, oats, whole grains, fruits, or vegetables, pay attention to hydration. Increase slowly so your digestive system has time to adjust.</p>
<h2>Fiber on a Budget</h2>
<p>Budget-friendly fiber-rich foods include oats, beans, lentils, potatoes, brown rice, frozen vegetables, apples, bananas, and whole-grain bread. You do not need expensive specialty foods to build a fiber-rich plate.</p>
<h2>Simple Weekly Fiber Plan</h2>
<p>Choose one breakfast fiber, one lunch fiber, and one dinner fiber. For example: oats at breakfast, beans at lunch, potatoes or brown rice at dinner. Repeat the plan until it feels easy, then add variety.</p>
""",
    "healthy-snack-plate-ideas": """
<h2>Sweet Snack Plates</h2>
<p>Sweet snack plates can still be balanced. Try yogurt with berries and granola, apple with peanut butter, cottage cheese with fruit, or toast with nut butter and banana. Sweetness does not have to mean the snack lacks staying power.</p>
<h2>Savory Snack Plates</h2>
<p>Savory options include hummus with vegetables, cheese with whole-grain crackers, boiled eggs with fruit, edamame with rice cakes, or avocado toast with tomatoes. Add color and texture so the snack feels satisfying.</p>
<h2>Snack Plates for Late Afternoons</h2>
<p>Late afternoon snacks often need protein and fiber because dinner may still be hours away. A balanced snack can prevent arriving at dinner overly hungry, which can make choices feel more urgent and less intentional.</p>
<h2>Use Snacks to Fill Gaps</h2>
<p>Look at what your meals are missing. If lunch had little protein, choose a protein-rich snack. If the day had little produce, add fruit or vegetables. If you are low on energy, include a fiber-rich carbohydrate.</p>
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
    for slug, expansion in EXPANSIONS.items():
        pid = post_id(slug)
        content = run_wp("post", "get", pid, "--field=post_content")
        if MARKER in content:
            print(f"already-expanded: {slug}")
            continue
        updated = content.rstrip() + "\n\n" + MARKER + "\n" + expansion.strip() + "\n"
        run_wp("post", "update", pid, f"--post_content={updated}")
        print(f"expanded: {pid} {slug}")


if __name__ == "__main__":
    main()
