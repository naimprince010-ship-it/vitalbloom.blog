import json
import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
IMAGE_DIR = Path("/tmp/vitalbloom-nutrition-pillar")
TODAY = "2026-05-31"
SLUG = "balanced-plate-guide"
MARKER = "<!-- vitalbloom-nutrition-pillar-link-v1 -->"

POST = {
    "title": "Balanced Plate Guide: How to Build Healthy Meals Without Counting Calories",
    "slug": SLUG,
    "category": "Nutrition",
    "keyword": "balanced plate method",
    "meta_title": "Balanced Plate Guide: Healthy Meals Made Simple",
    "meta_description": "Use the balanced plate method to build simple meals with vegetables, protein, fiber-rich carbs, healthy fats, and realistic examples.",
    "excerpt": "A practical balanced plate guide for building healthy meals without counting calories, with examples, swaps, meal prep tips, and credible sources.",
    "image": "balanced-plate-guide.png",
    "image_alt": "balanced plate guide with vegetables protein grains and healthy fats",
    "sources": [
        {
            "title": "MyPlate",
            "url": "https://www.myplate.gov/",
            "publisher": "U.S. Department of Agriculture",
            "accessedAt": TODAY,
        },
        {
            "title": "The Healthy Eating Plate",
            "url": "https://www.hsph.harvard.edu/nutritionsource/healthy-eating-plate/",
            "publisher": "Harvard T.H. Chan School of Public Health",
            "accessedAt": TODAY,
        },
        {
            "title": "Healthy Eating for a Healthy Weight",
            "url": "https://www.cdc.gov/healthy-weight-growth/healthy-eating/index.html",
            "publisher": "Centers for Disease Control and Prevention",
            "accessedAt": TODAY,
        },
        {
            "title": "DASH Eating Plan",
            "url": "https://www.nhlbi.nih.gov/education/dash-eating-plan",
            "publisher": "National Heart, Lung, and Blood Institute",
            "accessedAt": TODAY,
        },
    ],
    "content": """
<p>The balanced plate method is a simple way to build healthier meals without tracking every calorie or weighing every ingredient. Instead of starting with strict rules, you start with a visual pattern: more plants, enough protein, fiber-rich carbohydrates, healthy fats, and water or another low-sugar drink.</p>
<p>This guide explains how to use the balanced plate method for everyday breakfasts, lunches, dinners, and meal prep. It is for general education, not personal medical nutrition advice. If you have diabetes, kidney disease, food allergies, pregnancy-related nutrition needs, eating disorder history, or a medically prescribed diet, work with a qualified clinician or registered dietitian.</p>
<h2>Start Here: The Simple Balanced Plate Formula</h2>
<p>For many meals, use this basic structure:</p>
<ul>
  <li>Half the plate: non-starchy vegetables or vegetables plus fruit.</li>
  <li>One quarter: protein such as fish, poultry, eggs, beans, lentils, tofu, yogurt, or lean meat.</li>
  <li>One quarter: fiber-rich carbohydrates such as whole grains, potatoes, oats, brown rice, quinoa, beans, or fruit.</li>
  <li>Add a small amount of healthy fat, such as olive oil, avocado, nuts, seeds, or nut butter.</li>
  <li>Choose water most often, or another drink without a lot of added sugar.</li>
</ul>
<p>This method is flexible. A balanced bowl, soup, sandwich, or breakfast plate can follow the same idea even when food is not arranged in neat sections.</p>
<h2>What Is the Balanced Plate Method?</h2>
<p>The balanced plate method is a visual meal planning tool. It helps you include different food groups and nutrients without turning every meal into a math problem. The goal is not perfection. The goal is to make meals more satisfying, colorful, and steady.</p>
<p>A useful plate usually includes protein for fullness and repair, fiber-rich carbohydrates for energy, vegetables and fruits for micronutrients, and fats for flavor and satiety. This combination may help reduce the habit of building meals around only refined starches or snacks that leave you hungry soon after.</p>
<p>For a shorter overview, read <a href="/balanced-plate-method">Balanced Plate Method for Simple Healthy Meals</a>.</p>
<h2>Balanced Plate Components</h2>
<table>
  <thead>
    <tr>
      <th>Plate part</th>
      <th>Examples</th>
      <th>Simple tip</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Vegetables and fruit</td>
      <td>Leafy greens, broccoli, carrots, peppers, tomatoes, berries, apples</td>
      <td>Choose color and variety when possible.</td>
    </tr>
    <tr>
      <td>Protein</td>
      <td>Beans, lentils, tofu, eggs, fish, chicken, Greek yogurt, lean meat</td>
      <td>Add one clear protein source to most meals.</td>
    </tr>
    <tr>
      <td>Fiber-rich carbohydrates</td>
      <td>Oats, brown rice, quinoa, whole-grain bread, potatoes, corn, fruit</td>
      <td>Choose less refined options most often.</td>
    </tr>
    <tr>
      <td>Healthy fats</td>
      <td>Olive oil, avocado, nuts, seeds, nut butter</td>
      <td>Use enough for flavor and satisfaction.</td>
    </tr>
    <tr>
      <td>Drinks</td>
      <td>Water, sparkling water, unsweetened tea</td>
      <td>Watch added sugar in drinks.</td>
    </tr>
  </tbody>
</table>
<h2>Balanced Breakfast Ideas</h2>
<p>Breakfast does not have to be complicated. Try pairing protein, fiber, and color:</p>
<ul>
  <li>Greek yogurt with berries, oats, and nuts.</li>
  <li>Eggs with whole-grain toast and fruit.</li>
  <li>Oatmeal with peanut butter, chia seeds, and sliced banana.</li>
  <li>Tofu scramble with vegetables and potatoes.</li>
  <li>Whole-grain wrap with eggs, beans, spinach, and salsa.</li>
</ul>
<p>For more ideas, see <a href="/healthy-breakfast-ideas">Healthy Breakfast Ideas for Busy Mornings</a> and <a href="/high-fiber-breakfast-ideas">High-Fiber Breakfast Ideas for Steady Energy</a>.</p>
<h2>Balanced Lunch and Dinner Examples</h2>
<p>Use these examples as templates, not rules:</p>
<ul>
  <li>Salmon, roasted vegetables, brown rice, and olive oil dressing.</li>
  <li>Bean chili with vegetables, avocado, and a side salad.</li>
  <li>Chicken or tofu bowl with quinoa, greens, peppers, and tahini sauce.</li>
  <li>Lentil soup with whole-grain bread and fruit.</li>
  <li>Turkey, hummus, or veggie sandwich with raw vegetables and yogurt.</li>
</ul>
<p>If you meal prep, read <a href="/simple-meal-prep-healthy-lunches">Simple Meal Prep for Healthy Lunches</a>. If you eat plant-based meals, see <a href="/high-protein-vegetarian-meals">High-Protein Vegetarian Meals</a>.</p>
<h2>How to Use the Balanced Plate on a Budget</h2>
<p>A balanced plate does not require expensive foods. Budget-friendly staples can work well:</p>
<ul>
  <li>Frozen vegetables and fruit.</li>
  <li>Beans, lentils, chickpeas, and peas.</li>
  <li>Oats, potatoes, brown rice, and whole-grain pasta.</li>
  <li>Eggs, canned fish, tofu, or yogurt when they fit your preferences.</li>
  <li>Peanut butter, sunflower seeds, or olive oil for affordable fats.</li>
</ul>
<p>Build meals around the foods you already like and can repeat. Consistency usually matters more than chasing perfect ingredients.</p>
<h2>Common Balanced Plate Mistakes</h2>
<ul>
  <li><strong>Skipping protein.</strong> Meals built only on starch or salad may not keep you satisfied.</li>
  <li><strong>Forgetting fiber.</strong> Whole grains, beans, vegetables, fruit, nuts, and seeds help make meals more filling.</li>
  <li><strong>Making vegetables boring.</strong> Use herbs, spices, sauces, roasting, or crunchy textures.</li>
  <li><strong>Trying to be perfect.</strong> A balanced eating pattern is built across many meals, not one meal.</li>
  <li><strong>Ignoring personal needs.</strong> Some conditions require specific nutrition guidance.</li>
</ul>
<h2>Snacks Can Be Balanced Too</h2>
<p>A useful snack often combines two elements: protein or fat plus fiber. Examples include apple with peanut butter, yogurt with berries, hummus with vegetables, nuts with fruit, or whole-grain crackers with tuna or cottage cheese.</p>
<p>For lower added sugar ideas, read <a href="/low-sugar-snack-ideas">Low-Sugar Snack Ideas That Still Feel Satisfying</a>.</p>
<h2>Digestive Comfort and the Balanced Plate</h2>
<p>If you are adding more fiber, increase it gradually and drink enough fluid. A sudden jump in beans, vegetables, or whole grains can feel uncomfortable for some people. Your body may need time to adjust.</p>
<p>For gentle food ideas, see <a href="/foods-support-better-digestion">Foods That Support Better Digestion</a>.</p>
<h2>When to Personalize Your Plate</h2>
<p>The balanced plate method is a general framework. You may need a personalized plan if you have a medical condition, take medication affected by food, have a history of disordered eating, are pregnant, are an athlete with high training demands, or have specific cultural, religious, or budget needs that change how you eat.</p>
<p>A registered dietitian can help adapt the plate method without making food feel stressful or unrealistic.</p>
<h2>Balanced Plate Checklist</h2>
<ul>
  <li>Do I have a protein source?</li>
  <li>Do I have a vegetable, fruit, or both?</li>
  <li>Do I have a fiber-rich carbohydrate?</li>
  <li>Do I have a fat source for flavor and satisfaction?</li>
  <li>Is my drink mostly low in added sugar?</li>
  <li>Does this meal fit my real schedule and budget?</li>
</ul>
<h2>Common Questions</h2>
<h3>Do I need to count calories to eat healthy?</h3>
<p>Not always. Many people can improve meal quality by using a balanced plate structure, focusing on whole foods, and noticing hunger and fullness. Some medical or performance goals may need more specific guidance.</p>
<h3>Can the balanced plate method help with weight management?</h3>
<p>It may help some people build more satisfying meals with protein, fiber, and less reliance on highly refined foods. Weight is influenced by many factors, so personal guidance may be helpful.</p>
<h3>What if I do not like vegetables?</h3>
<p>Start with one vegetable prepared in a way you enjoy. Roasting, seasoning, soups, sauces, and mixed dishes can make vegetables easier to include.</p>
<h3>Is rice or bread allowed on a balanced plate?</h3>
<p>Yes. The goal is balance, not banning foods. Choose fiber-rich options often and pair them with protein and vegetables.</p>
<h3>How do I make a balanced vegetarian plate?</h3>
<p>Use beans, lentils, tofu, tempeh, eggs, dairy, nuts, seeds, or other protein-rich foods, then add vegetables, fruit, whole grains or starches, and fats.</p>
<h3>What is the easiest first step?</h3>
<p>Add one clear protein source and one fruit or vegetable to a meal you already eat. Small upgrades are easier to repeat.</p>
""",
}

BACKLINK_POSTS = [
    "balanced-plate-method",
    "healthy-breakfast-ideas",
    "high-fiber-breakfast-ideas",
    "simple-meal-prep-healthy-lunches",
    "high-protein-vegetarian-meals",
    "low-sugar-snack-ideas",
    "foods-support-better-digestion",
]

BACKLINK_HTML = f"""
{MARKER}
<section>
  <h2>Complete Balanced Plate Guide</h2>
  <p>For a deeper meal-building guide, read <a href="/{SLUG}">Balanced Plate Guide: How to Build Healthy Meals Without Counting Calories</a>.</p>
</section>
"""


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
    return result.stdout.strip()


def get_or_create_category(name: str) -> str:
    existing = run_wp("term", "list", "category", f"--name={name}", "--field=term_id")
    if existing:
        return existing.splitlines()[0]
    return run_wp("term", "create", "category", name, "--porcelain")


def find_post_id(slug: str) -> str | None:
    found = run_wp("post", "list", f"--name={slug}", "--post_type=post", "--field=ID")
    return found.splitlines()[0] if found else None


def existing_attachment_id(slug: str) -> str | None:
    attachments_json = run_wp(
        "post",
        "list",
        "--post_type=attachment",
        "--post_mime_type=image",
        "--fields=ID,post_name",
        "--format=json",
    )
    attachments = json.loads(attachments_json or "[]")
    for attachment in attachments:
        post_name = str(attachment.get("post_name", ""))
        if post_name == slug or post_name.startswith(f"{slug}-"):
            return str(attachment["ID"])
    return None


def set_featured_image(post_id: str) -> None:
    attachment_id = existing_attachment_id(POST["slug"])
    if not attachment_id:
        attachment_id = run_wp(
            "media",
            "import",
            str(IMAGE_DIR / POST["image"]),
            f"--title={POST['title']}",
            f"--alt={POST['image_alt']}",
            "--porcelain",
        )
    run_wp("post", "meta", "update", post_id, "_thumbnail_id", attachment_id)


def publish_pillar() -> str:
    category_id = get_or_create_category(POST["category"])
    existing_id = find_post_id(POST["slug"])
    args = [
        f"--post_title={POST['title']}",
        f"--post_name={POST['slug']}",
        f"--post_content={POST['content'].strip()}",
        f"--post_excerpt={POST['excerpt']}",
        "--post_status=publish",
        f"--post_category={category_id}",
    ]
    if existing_id:
        run_wp("post", "update", existing_id, *args)
        post_id = existing_id
        action = "updated"
    else:
        post_id = run_wp("post", "create", *args, "--porcelain")
        action = "created"

    run_wp("post", "meta", "update", post_id, "_yoast_wpseo_title", POST["meta_title"])
    run_wp("post", "meta", "update", post_id, "_yoast_wpseo_metadesc", POST["meta_description"])
    run_wp("post", "meta", "update", post_id, "_yoast_wpseo_focuskw", POST["keyword"])
    run_wp("post", "meta", "update", post_id, "_vitalbloom_sources", json.dumps(POST["sources"], ensure_ascii=True))
    run_wp("post", "meta", "update", post_id, "_vitalbloom_fact_checked_by", "VitalBloom Editorial Team")
    run_wp("post", "meta", "update", post_id, "_vitalbloom_fact_checked_at", TODAY)
    set_featured_image(post_id)
    return f"{action}: {post_id} {POST['slug']}"


def add_backlinks() -> None:
    for slug in BACKLINK_POSTS:
        post_id = find_post_id(slug)
        if not post_id:
            print(f"missing-backlink-target: {slug}")
            continue
        content = run_wp("post", "get", post_id, "--field=post_content")
        if MARKER in content:
            print(f"backlink-exists: {slug}")
            continue
        updated = content.rstrip() + "\n\n" + BACKLINK_HTML.strip()
        run_wp("post", "update", post_id, f"--post_content={updated}")
        print(f"backlink-added: {slug}")


def main() -> None:
    print(publish_pillar())
    add_backlinks()


if __name__ == "__main__":
    main()
