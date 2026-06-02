import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
MARKER = "<!-- vitalbloom-nutrition-support-batch2-expanded-v1 -->"

EXPANSIONS = {
    "simple-grocery-list-for-healthy-eating": """
<h2>Make a Two-Level Grocery List</h2>
<p>A two-level grocery list can make shopping easier. The first level is your core list: foods you use almost every week, such as oats, eggs, yogurt, beans, rice, potatoes, frozen vegetables, fruit, and one or two sauces. The second level is your flexible list: foods that change based on sales, recipes, season, or appetite.</p>
<p>This structure helps you avoid starting from scratch. When you are tired, shop the core list. When you have more energy, add one flexible ingredient that brings variety. For example, the core list might stay the same while the flexible item changes from broccoli to peppers or from lentils to tofu.</p>
<h2>Use the List After Shopping</h2>
<p>When you get home, make the groceries easier to use. Wash fruit, put vegetables where you can see them, freeze anything you will not use soon, and choose one protein to prepare first. A grocery list is only helpful if the food becomes visible and convenient.</p>
<p>Before the week begins, choose three combinations from the foods you bought. That might be yogurt bowls, bean bowls, and egg toast. These simple defaults make the list feel connected to real meals instead of sitting as separate ingredients in the kitchen.</p>
""",
    "meal-planning-for-busy-weeks": """
<h2>Choose Your Cooking Energy Level</h2>
<p>Busy weeks are not all the same. Some weeks allow one cooking session. Other weeks need mostly assembly meals. Before planning, choose your cooking energy level: no-cook, low-cook, or cook-once. This keeps the plan honest.</p>
<p>No-cook meals might include yogurt bowls, hummus plates, sandwiches, salads, and canned bean bowls. Low-cook meals might use eggs, microwave grains, frozen vegetables, or quick soups. Cook-once weeks might include a pot of lentils, roasted vegetables, or a grain that can support several meals.</p>
<h2>Build a Plan B Into the Plan</h2>
<p>A meal plan without a Plan B often breaks on the first hard day. Write the backup directly into the plan. For example, if Tuesday dinner is a stir-fry, the backup might be frozen vegetables, beans, rice, and salsa. If lunch prep does not happen, the backup might be yogurt, fruit, oats, and nuts.</p>
<p>This makes flexibility part of the system instead of a sign that you failed. The more realistic your backup meals are, the more likely you are to stay nourished during weeks that do not follow the calendar neatly.</p>
""",
    "how-to-eat-more-vegetables": """
<h2>Pair Vegetables With Foods You Already Like</h2>
<p>Vegetables are easier to eat when they are connected to foods you already enjoy. Add peppers to tacos, spinach to pasta, carrots to hummus, tomatoes to toast, or roasted vegetables to potatoes. Familiar foods make the vegetable feel like part of the meal rather than an extra assignment.</p>
<p>This approach also helps with picky eating or vegetable fatigue. Instead of forcing a large serving of a vegetable you do not like, try small amounts with a sauce, seasoning, or texture that feels more appealing.</p>
<h2>Use a Vegetable Rotation</h2>
<p>A simple rotation can keep vegetables from feeling repetitive. Choose one leafy option, one crunchy option, one frozen option, and one cooked option for the week. For example: spinach, carrots, frozen broccoli, and roasted peppers.</p>
<p>The rotation gives variety while keeping the list short. It also helps you use vegetables in different ways: greens in eggs, carrots as snacks, frozen broccoli in rice bowls, and roasted peppers in wraps. Small variety is easier to sustain than buying many vegetables without a plan.</p>
""",
    "budget-friendly-healthy-meals": """
<h2>Use Cost Per Meal, Not Just Cost Per Item</h2>
<p>A food can look expensive but still be useful if it supports several meals. A container of Greek yogurt can become breakfast, sauce, snack, and a protein add-on. A bag of potatoes can become breakfast hash, dinner sides, bowls, and soup. A bag of frozen vegetables can support many quick meals.</p>
<p>Thinking in cost per meal helps you compare foods more fairly. It also helps you decide where convenience is worth paying for. If prewashed greens help you actually eat vegetables before they spoil, they may save money compared with cheaper produce that goes unused.</p>
<h2>Repeat Meals With Small Changes</h2>
<p>Repeating meals is one of the simplest budget strategies. You can eat beans and rice more than once without making it taste identical. Change the sauce, add different vegetables, use a wrap one day and a bowl the next, or turn leftovers into soup.</p>
<p>This reduces the number of ingredients you need to buy. It also makes cooking easier because you learn the rhythm of a few reliable meals. A budget-friendly routine does not need endless novelty; it needs enough variety to stay enjoyable.</p>
""",
    "mindful-eating-for-beginners": """
<h2>Practice the Pause Before Changing Anything</h2>
<p>Beginners often want to change their eating right away, but mindful eating starts with noticing. Before adjusting portions, timing, or food choices, practice a pause. Ask what you notice in your body, what emotion is present, and what kind of meal or snack would feel supportive.</p>
<p>This pause can be brief. It might happen while opening the refrigerator, sitting down with lunch, or reaching for an afternoon snack. The purpose is not to stop yourself from eating. The purpose is to make the moment less automatic.</p>
<h2>Notice Patterns Across the Day</h2>
<p>Mindful eating becomes more useful when you look at patterns, not isolated meals. If you often feel overly hungry at night, breakfast or lunch may need more attention. If snacks feel chaotic, the gap between meals may be too long. If meals feel unsatisfying, flavor or variety may be missing.</p>
<p>Patterns give you practical next steps. You might add a protein source at breakfast, pack a more complete snack, reduce one distraction at lunch, or plan a dinner that feels more satisfying. Small adjustments are easier when they come from observation instead of guilt.</p>
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
