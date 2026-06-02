import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
MARKER = "<!-- vitalbloom-nutrition-support-batch1-expanded-v1 -->"

EXPANSIONS = {
    "beginner-meal-prep-checklist": """
<h2>One-Hour Beginner Meal Prep Plan</h2>
<p>If you have one hour, keep the plan focused. Start one carbohydrate, prepare one protein, wash or chop one produce option, and make one sauce. For example, cook rice, roast tofu or chicken, chop cucumbers, and mix yogurt sauce. That is enough to build several meals without spending the whole day in the kitchen.</p>
<h2>Meal Prep Without Cooking</h2>
<p>You can meal prep even when you do not want to cook. Use canned beans, rotisserie chicken, tuna packets, microwave grains, frozen vegetables, bagged salad, yogurt, fruit, nuts, hummus, and whole-grain bread. Assembly still counts. The point is to make meals easier when you are tired.</p>
<h2>How to Avoid Food Boredom</h2>
<p>Use the same ingredients with different formats. Rice, beans, vegetables, and sauce can become a bowl, wrap, salad, or side plate. Change the sauce or seasoning before changing the whole plan. This keeps prep simple while still giving variety.</p>
""",
    "hydration-tracker-printable": """
<h2>Hydration for Workdays</h2>
<p>Workdays can make hydration easy to forget. Meetings, errands, calls, and deadlines can push water into the background. Try placing water where you start work, refilling during a natural break, and pairing water with lunch. If you work remotely, keep water away from the desk sometimes so refilling creates a movement break.</p>
<h2>Hydration for Students</h2>
<p>Students may forget water between classes, labs, commuting, and studying. Carry a bottle if allowed, drink with meals, and refill before long study blocks. If you rely heavily on caffeine during exams, add water and food cues so caffeine is not carrying the whole day.</p>
<h2>Hydration and Exercise</h2>
<p>Activity, heat, and sweating can change fluid needs. Use thirst, urine color, climate, and how you feel as general clues, while remembering that medical conditions can change what is appropriate. For intense exercise or heat exposure, follow trusted guidance.</p>
<h2>Make the Tracker Printable</h2>
<p>Draw four boxes: morning, midday, afternoon, evening. In each box, write what you drank and one note about energy or thirst. At the bottom, write the cue that worked best. This printable format keeps tracking simple and low-pressure.</p>
""",
    "add-protein-to-every-meal": """
<h2>How Much Protein Is Enough?</h2>
<p>There is no single answer for everyone. Needs vary by body size, activity, age, health, and goals. Instead of starting with numbers, many beginners can start by including a protein source at meals and noticing fullness, energy, and meal satisfaction. For specific targets, ask a qualified professional.</p>
<h2>Protein for Busy Mornings</h2>
<p>Busy mornings are easier with repeatable options. Keep Greek yogurt, eggs, cottage cheese, nut butter, tofu, milk, or protein-rich leftovers available. A simple breakfast with protein and fiber can reduce the need to snack immediately afterward.</p>
<h2>Protein on a Budget</h2>
<p>Budget-friendly protein can include beans, lentils, eggs, canned fish, peanut butter, tofu, yogurt, and bulk nuts or seeds. Frozen fish or poultry may also help. Build meals around affordable anchors, then add produce and fiber-rich carbohydrates.</p>
<h2>Protein and the Balanced Plate</h2>
<p>Protein is only one part of the plate. A meal with protein but no produce or fiber-rich carbohydrate may still feel incomplete. Use the balanced plate formula: protein, produce, carbohydrate, and flavor. That structure makes meals easier to repeat.</p>
<h2>Simple Protein Prep Ideas</h2>
<ul>
  <li>Boil eggs for snacks or breakfast.</li>
  <li>Cook lentils for bowls and soups.</li>
  <li>Bake tofu for wraps and salads.</li>
  <li>Portion yogurt with fruit.</li>
  <li>Prepare beans with spices for tacos or rice bowls.</li>
</ul>
""",
    "fiber-rich-carbohydrates-guide": """
<h2>Fiber-Rich Carbs for Breakfast</h2>
<p>Breakfast is a simple place to add fiber-rich carbohydrates. Try oats with fruit, whole-grain toast with eggs, potatoes with vegetables, or yogurt with berries and granola. Pairing fiber with protein can make breakfast more satisfying.</p>
<h2>Fiber-Rich Carbs for Lunch</h2>
<p>Lunch options include brown rice bowls, bean salads, lentil soup, whole-grain wraps, sweet potatoes, or quinoa with vegetables. If you use convenience foods, add a fiber-rich side such as fruit, carrots, beans, or whole-grain crackers.</p>
<h2>Fiber-Rich Carbs for Dinner</h2>
<p>Dinner can include potatoes, whole grains, beans, lentils, or whole-grain pasta. Add protein and produce to make the meal feel complete. For example, lentil pasta with vegetables, salmon with potatoes and broccoli, or tofu with brown rice and stir-fried vegetables.</p>
<h2>How to Reduce Digestive Discomfort</h2>
<p>If you are increasing fiber, go gradually. Add one serving at a time, drink fluids, and notice what your body tolerates. Some people need individualized advice, especially with digestive conditions.</p>
<h2>Carbohydrates Are Not the Enemy</h2>
<p>Carbohydrates are often oversimplified. Instead of labeling foods as good or bad, ask how the meal works as a whole. Fiber-rich carbohydrates can be part of steady, satisfying meals when paired with protein, produce, and flavor.</p>
""",
    "healthy-snack-plate-ideas": """
<h2>Snack Plates for Different Needs</h2>
<p>If you need quick energy, pair fruit with yogurt or nuts. If you need something filling, include protein and fiber. If you want a calming evening snack, choose something satisfying but not overly stimulating. The best snack depends on the gap it is filling.</p>
<h2>Snack Plates for Kids and Families</h2>
<p>Family snack plates can be simple: fruit, vegetables, cheese, hummus, crackers, yogurt, or nut butter if appropriate. Let people choose from a few options. Snack plates can reduce pressure because they do not require one perfect food.</p>
<h2>Snack Plates for Work</h2>
<p>At work, keep shelf-stable options ready: nuts, roasted chickpeas, whole-grain crackers, fruit, tuna packets, or nut butter. If you have a fridge, add yogurt, cheese, hummus, vegetables, or boiled eggs. A planned snack can prevent the afternoon crash from turning into random grazing.</p>
<h2>When Snacks Do Not Feel Satisfying</h2>
<p>If snacks never satisfy you, look at meals. You may need more food, more protein, more fiber, or a better meal schedule. Snacks help between meals, but they should not be responsible for fixing meals that are consistently too small.</p>
<h2>Keep a Snack List</h2>
<p>Write down five snack plates you actually like. Keep the list near your grocery list. Decision fatigue is often the reason snack habits fall apart, not lack of knowledge.</p>
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
