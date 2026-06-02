import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
MARKER = "<!-- vitalbloom-nutrition-support-batch3-expanded-v1 -->"

EXPANSIONS = {
    "healthy-pantry-staples-for-beginners": """
<h2>Create a Pantry Refill Rule</h2>
<p>A pantry works best when you replace the foods you use most often before they run out completely. Choose a simple refill rule: when there is one serving left of oats, rice, beans, pasta, nut butter, or your favorite sauce, add it to the shopping list. This prevents the pantry from becoming empty right when you need an easy meal.</p>
<p>The rule also helps you avoid buying too many duplicates. Instead of guessing at the store, you know which staples truly need replacing. Over time, your pantry becomes more reliable and less cluttered.</p>
<h2>Pair Pantry Staples With Fresh Food</h2>
<p>Pantry staples are strongest when they pair with one or two fresh or frozen foods. Beans become a meal with greens and salsa. Oats become breakfast with fruit and yogurt. Pasta becomes dinner with canned tomatoes, frozen spinach, and lentils.</p>
<p>This pairing keeps meals from feeling like emergency food. It also helps you stretch fresh groceries because the pantry provides the structure and the fresh food adds color, texture, and variety.</p>
""",
    "easy-balanced-dinner-formula": """
<h2>Use the Formula for Different Cooking Times</h2>
<p>The same dinner formula can work whether you have five minutes or forty minutes. With five minutes, use canned beans, microwave rice, frozen vegetables, and salsa. With twenty minutes, cook eggs, potatoes, and greens. With forty minutes, roast vegetables, cook a grain, and prepare a protein.</p>
<p>Thinking this way helps you avoid abandoning balanced meals when time is short. You are not choosing between perfect dinner and no plan. You are choosing the version of the formula that fits the night.</p>
<h2>Keep One Sauce Ready</h2>
<p>A ready sauce can make dinner feel finished. It might be hummus, salsa, pesto, yogurt with herbs, tahini lemon dressing, vinaigrette, or a simple tomato sauce. One sauce can connect ingredients that otherwise feel random.</p>
<p>If weeknight dinners often feel repetitive, rotate the sauce before changing every ingredient. The same rice, beans, and vegetables can feel different with salsa one night, lemon yogurt another night, and curry sauce later in the week.</p>
""",
    "simple-breakfast-meal-prep": """
<h2>Prepare Breakfast Cues, Not Just Food</h2>
<p>Breakfast prep is easier when the cue is visible. Put oats on the counter, keep yogurt at eye level, place fruit where you can see it, or set a container near the coffee maker. A visible cue reduces the chance that breakfast becomes an afterthought.</p>
<p>This matters on rushed mornings because decisions are harder when you are tired. If the first step is already obvious, you are more likely to follow through with the breakfast you planned.</p>
<h2>Make a Two-Minute Breakfast List</h2>
<p>Write down three breakfasts you can make in two minutes. Examples include yogurt with fruit and oats, toast with nut butter and banana, cottage cheese with fruit, a smoothie with oats and protein, or boiled eggs with crackers and fruit.</p>
<p>Keep this list near the kitchen or in your phone. When mornings feel scattered, choose from the list instead of inventing a new plan. A small menu can make breakfast meal prep feel much more useful.</p>
""",
    "how-to-build-a-filling-salad": """
<h2>Make Salads Warm or Cold</h2>
<p>A filling salad does not have to be cold. Warm grains, roasted vegetables, lentils, potatoes, tofu, or chicken can make a salad feel more satisfying, especially in cooler weather. You can place warm ingredients over sturdy greens or cabbage so the meal feels hearty without becoming heavy.</p>
<p>Warm salad bowls are also useful for leftovers. Add dressing after reheating the warm ingredients, then combine with greens, herbs, or crunchy toppings. This turns yesterday's dinner into a new lunch.</p>
<h2>Build the Dressing Around the Main Ingredient</h2>
<p>Choosing dressing becomes easier when you match it to the protein or carbohydrate. Beans often work well with salsa, lime, cumin, or vinaigrette. Eggs and potatoes work well with yogurt-herb dressing. Tofu and rice work well with sesame, peanut, or ginger flavors.</p>
<p>This keeps the salad from tasting like disconnected ingredients. Dressing is the bridge that helps the whole bowl make sense.</p>
""",
    "healthy-snacks-for-work": """
<h2>Pack Snacks the Night Before</h2>
<p>Work snacks are easier when they are packed before the morning rush. Put shelf-stable snacks in your bag, portion refrigerated snacks into containers, and place anything that needs an ice pack near the front of the refrigerator. The less you need to decide in the morning, the more likely the snack will leave with you.</p>
<p>If packing every night feels unrealistic, pack two or three days at once. Keep the options simple and repeatable. A reliable snack routine is better than a complicated one that only happens once.</p>
<h2>Use Snacks to Protect Lunch and Dinner</h2>
<p>A planned snack can make main meals calmer. If you arrive at lunch or dinner extremely hungry, it can be harder to notice what you actually want or need. A snack with protein and fiber can bridge the gap so meals feel less rushed.</p>
<p>This is especially useful on long workdays, commute days, or days with back-to-back meetings. Snacks are part of the rhythm of the day, not a sign that your meals failed.</p>
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
