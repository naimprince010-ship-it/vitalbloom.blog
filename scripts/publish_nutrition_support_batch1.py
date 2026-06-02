import json
import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
TODAY = "2026-06-02"

COMMON_SOURCES = [
    {
        "title": "MyPlate Plan",
        "url": "https://www.myplate.gov/myplate-plan",
        "publisher": "U.S. Department of Agriculture",
        "accessedAt": TODAY,
    },
    {
        "title": "Dietary Guidelines for Americans",
        "url": "https://www.dietaryguidelines.gov/",
        "publisher": "U.S. Department of Health and Human Services and U.S. Department of Agriculture",
        "accessedAt": TODAY,
    },
    {
        "title": "Healthy Eating Plate",
        "url": "https://www.health.harvard.edu/plate/healthy-eating-plate",
        "publisher": "Harvard Health Publishing",
        "accessedAt": TODAY,
    },
]

POSTS = [
    {
        "title": "Beginner Meal Prep Checklist for Balanced Meals",
        "slug": "beginner-meal-prep-checklist",
        "category": "Nutrition",
        "keyword": "beginner meal prep checklist",
        "meta_title": "Beginner Meal Prep Checklist",
        "meta_description": "Use this beginner meal prep checklist to plan balanced meals with protein, produce, fiber-rich carbs, and flexible flavor.",
        "excerpt": "A beginner-friendly meal prep checklist for balanced meals without complicated rules or all-day cooking.",
        "content": """
<p>Meal prep can sound like a huge weekend project, but it does not have to be. For beginners, the best meal prep is simple, flexible, and easy to repeat. You do not need matching containers, a perfect plan, or a refrigerator full of identical meals.</p>
<p>This checklist uses the balanced plate method: protein, produce, fiber-rich carbohydrates, and flavor. It is for general education and is not a medical nutrition plan. If you have a medical condition, eating disorder history, allergies, pregnancy-related needs, or special dietary requirements, follow professional guidance.</p>
<h2>Step 1: Choose the Meal You Actually Need Help With</h2>
<p>Do not prep everything at once. Choose the meal that causes the most stress. For many people, that is lunch on workdays, breakfast on rushed mornings, or dinner after a long day.</p>
<ul>
  <li>If lunch is the problem, prep one protein and one grain or starch.</li>
  <li>If breakfast is the problem, prep a grab-and-go option.</li>
  <li>If dinner is the problem, prep ingredients instead of full meals.</li>
  <li>If snacks are the problem, make a simple snack box.</li>
</ul>
<h2>Step 2: Pick One Protein Anchor</h2>
<p>Protein helps meals feel more satisfying. Choose one option that fits your budget, preferences, and cooking energy.</p>
<ul>
  <li>Beans, lentils, chickpeas, tofu, tempeh, eggs, Greek yogurt, cottage cheese, fish, poultry, lean meats, nuts, seeds, or nut butter.</li>
  <li>Use canned or frozen options when they make prep easier.</li>
  <li>Prepare enough for two to four meals, not the whole week if that feels overwhelming.</li>
</ul>
<h2>Step 3: Add Produce That Is Easy to Use</h2>
<p>Produce does not need to be fancy. Choose options that are easy to wash, chop, roast, or open.</p>
<ul>
  <li>Bagged greens, baby carrots, frozen vegetables, apples, berries, peppers, cucumber, broccoli, tomatoes, or roasted vegetables.</li>
  <li>Use frozen produce if fresh produce keeps going bad.</li>
  <li>Prep one raw option and one cooked option if variety helps.</li>
</ul>
<h2>Step 4: Choose a Fiber-Rich Carbohydrate</h2>
<p>Carbohydrates can support energy and make meals satisfying. Choose options with fiber when possible.</p>
<ul>
  <li>Oats, brown rice, quinoa, potatoes, sweet potatoes, whole-grain bread, whole-grain pasta, beans, lentils, or fruit.</li>
  <li>Cook one batch, or use quick options like microwave grains or canned beans.</li>
  <li>Pair carbohydrates with protein and produce for a fuller plate.</li>
</ul>
<h2>Step 5: Add Flavor So You Actually Eat It</h2>
<p>Meal prep fails when food feels boring. Keep flavor simple but intentional.</p>
<ul>
  <li>Salsa, hummus, yogurt sauce, vinaigrette, tahini, pesto, curry sauce, herbs, spices, lemon, hot sauce, or olive oil.</li>
  <li>Store sauce separately if it keeps food fresher.</li>
  <li>Use one sauce in multiple ways to reduce decisions.</li>
</ul>
<h2>Beginner Meal Prep Formula</h2>
<p>Use this simple formula for a flexible meal:</p>
<ul>
  <li>Protein: beans, tofu, eggs, fish, poultry, yogurt, or another anchor.</li>
  <li>Produce: one colorful fruit or vegetable.</li>
  <li>Carbohydrate: grain, potato, bread, oats, beans, or fruit.</li>
  <li>Flavor: sauce, herbs, spices, or dressing.</li>
</ul>
<h2>Three Easy Meal Prep Examples</h2>
<h3>Lunch Bowl</h3>
<p>Brown rice, black beans, roasted peppers, greens, salsa, and avocado or yogurt sauce.</p>
<h3>Breakfast Box</h3>
<p>Greek yogurt, berries, oats, nuts, and chia seeds.</p>
<h3>Dinner Starter</h3>
<p>Cooked lentils, roasted vegetables, potatoes, and a lemon-tahini sauce. Combine them as a bowl, wrap, or side plate.</p>
<h2>Common Beginner Mistakes</h2>
<p>One mistake is prepping too much food before you know what you like. Another is choosing meals that require too many steps. A third is forgetting flavor. Start small: two proteins, two produce options, one carbohydrate, and one sauce can create several meals.</p>
<h2>How to Keep Meal Prep Flexible</h2>
<p>Instead of making five identical containers, prep components. Components let you build bowls, wraps, plates, soups, and snack plates throughout the week. This reduces boredom and helps you use what you have.</p>
<h2>Food Safety Note</h2>
<p>Store prepared food safely, refrigerate promptly, and use leftovers within a safe timeframe. When in doubt, follow food safety guidance from trusted public health sources.</p>
<h2>Related VitalBloom Guides</h2>
<ul>
  <li><a href="/balanced-plate-printable-guide">Balanced Plate Printable Guide</a></li>
  <li><a href="/balanced-plate-guide">Balanced Plate Guide</a></li>
  <li><a href="/simple-meal-prep-healthy-lunches">Simple Meal Prep Ideas for Healthy Weekday Lunches</a></li>
  <li><a href="/high-protein-vegetarian-meals">High-Protein Vegetarian Meals</a></li>
</ul>
<p>Disclaimer: This article is for general educational purposes only and is not a substitute for professional medical or nutrition advice.</p>
""",
    },
    {
        "title": "Hydration Tracker Printable: A Simple Way to Notice Your Water Habits",
        "slug": "hydration-tracker-printable",
        "category": "Nutrition",
        "keyword": "hydration tracker printable",
        "meta_title": "Hydration Tracker Printable",
        "meta_description": "Use this hydration tracker printable to notice water habits, plan easy hydration cues, and support balanced daily routines.",
        "excerpt": "A simple hydration tracker for noticing water habits without turning hydration into another complicated rule.",
        "content": """
<p>Hydration advice can become confusing fast. Some people hear one-size-fits-all rules, while others forget water until they feel tired, headachy, or distracted. A hydration tracker can help you notice patterns without making water intake feel like a strict performance goal.</p>
<p>This guide is for general education. Fluid needs vary based on body size, activity, climate, health conditions, medications, pregnancy, breastfeeding, and other factors. If you have kidney, heart, or fluid restriction concerns, follow professional guidance.</p>
<h2>Why Use a Hydration Tracker?</h2>
<p>A tracker helps you answer simple questions:</p>
<ul>
  <li>Do I drink mostly in the morning, afternoon, or evening?</li>
  <li>Do I forget water during work or school?</li>
  <li>Do I rely on caffeine when I may need fluids or food?</li>
  <li>Do I drink late because I forgot earlier?</li>
  <li>What cues help me remember?</li>
</ul>
<h2>Simple Daily Hydration Tracker</h2>
<p>Use a simple table with four check-in times: morning, midday, afternoon, and evening. At each check-in, write what you drank and how you feel. Keep it loose. The goal is awareness.</p>
<ul>
  <li>Morning: water near wake-up or breakfast.</li>
  <li>Midday: water with lunch.</li>
  <li>Afternoon: water before another caffeinated drink.</li>
  <li>Evening: enough fluid to feel comfortable without disrupting sleep.</li>
</ul>
<h2>Hydration Cues That Actually Work</h2>
<p>Most people do better with cues than with willpower.</p>
<ul>
  <li>Keep water visible.</li>
  <li>Pair water with meals.</li>
  <li>Refill after bathroom breaks.</li>
  <li>Drink water before opening the next work task.</li>
  <li>Use a bottle you like holding and cleaning.</li>
  <li>Add lemon, cucumber, mint, or fruit if flavor helps.</li>
</ul>
<h2>Hydration and Balanced Meals</h2>
<p>Hydration is easier when meals are balanced and satisfying. If you skip meals or rely on caffeine, you may misread hunger, fatigue, or stress. Pair hydration with protein, produce, fiber-rich carbohydrates, and a comfortable meal rhythm.</p>
<h2>What Counts Toward Hydration?</h2>
<p>Water is a simple choice, but fluids can come from other drinks and water-rich foods too. Fruits, vegetables, soups, milk, and other beverages may contribute. Sugary drinks and high-caffeine drinks may not feel as steady for everyone, so notice your own response.</p>
<h2>Signs You May Need to Pay Attention</h2>
<p>Dry mouth, dark urine, headaches, dizziness, fatigue, or feeling very thirsty can be clues that hydration needs attention. These signs can have other causes too. If symptoms are severe, unusual, or persistent, seek medical advice.</p>
<h2>Hydration Without Obsession</h2>
<p>A tracker should reduce decision fatigue, not create anxiety. If tracking every sip makes you stressed, use fewer check-ins. You can simply ask: did I drink something with meals, and did I keep water available?</p>
<h2>Weekly Review</h2>
<p>At the end of the week, ask which cue helped most. Keep that cue and remove anything unrealistic. Hydration habits work best when they fit your real day.</p>
<h2>Related VitalBloom Guides</h2>
<ul>
  <li><a href="/balanced-plate-printable-guide">Balanced Plate Printable Guide</a></li>
  <li><a href="/remote-worker-wellness-checklist">Remote Worker Wellness Checklist</a></li>
  <li><a href="/beginner-meal-prep-checklist">Beginner Meal Prep Checklist</a></li>
  <li><a href="/healthy-breakfast-ideas">Healthy Breakfast Ideas</a></li>
</ul>
<p>Disclaimer: This article is for general educational purposes only and is not a substitute for professional medical or nutrition advice.</p>
""",
    },
    {
        "title": "How to Add Protein to Every Meal Without Overthinking It",
        "slug": "add-protein-to-every-meal",
        "category": "Nutrition",
        "keyword": "add protein to every meal",
        "meta_title": "How to Add Protein to Every Meal",
        "meta_description": "Learn simple ways to add protein to breakfast, lunch, dinner, and snacks without complicated tracking.",
        "excerpt": "A practical guide to adding protein to meals with simple anchors, vegetarian options, snack ideas, and balanced plate examples.",
        "content": """
<p>Protein can help meals feel satisfying, but adding it does not need to involve complicated tracking or expensive foods. The easiest approach is to choose a protein anchor for each meal, then build the rest of the plate around it.</p>
<p>This guide is for general education and is not a personalized nutrition plan. Protein needs vary based on age, body size, activity, health, pregnancy, and medical conditions.</p>
<h2>Start With the Protein Anchor</h2>
<p>Before deciding everything else, ask: what is the protein anchor? Options include eggs, Greek yogurt, cottage cheese, tofu, tempeh, beans, lentils, chickpeas, fish, poultry, lean meats, nuts, seeds, or nut butter.</p>
<h2>Breakfast Protein Ideas</h2>
<ul>
  <li>Greek yogurt with berries, oats, and nuts.</li>
  <li>Eggs with whole-grain toast and fruit.</li>
  <li>Tofu scramble with vegetables.</li>
  <li>Overnight oats with yogurt, milk, chia, or nut butter.</li>
  <li>Cottage cheese with fruit and whole-grain toast.</li>
</ul>
<h2>Lunch Protein Ideas</h2>
<ul>
  <li>Bean and rice bowl with vegetables and salsa.</li>
  <li>Lentil soup with whole-grain bread.</li>
  <li>Turkey, tuna, tofu, or chickpea salad wrap.</li>
  <li>Leftover chicken, fish, tofu, or beans over greens.</li>
  <li>Hummus plate with vegetables, pita, and fruit.</li>
</ul>
<h2>Dinner Protein Ideas</h2>
<p>Dinner can be simple: one protein, one produce option, one fiber-rich carbohydrate, and one flavor element. You might choose salmon with potatoes and broccoli, tofu stir-fry with brown rice, lentil pasta with vegetables, or beans with roasted vegetables and avocado.</p>
<h2>Snack Protein Ideas</h2>
<ul>
  <li>Yogurt and fruit.</li>
  <li>Apple with peanut butter.</li>
  <li>Hummus and carrots.</li>
  <li>Boiled egg and whole-grain crackers.</li>
  <li>Edamame, nuts, or roasted chickpeas.</li>
</ul>
<h2>Vegetarian Protein Tips</h2>
<p>Vegetarian meals can include plenty of protein, but they may need a little planning. Keep beans, lentils, tofu, tempeh, Greek yogurt, cottage cheese, eggs, nuts, seeds, and whole grains available. Combining protein with fiber-rich carbohydrates can make meals satisfying.</p>
<h2>Make It Easier With Meal Prep</h2>
<p>Prepare one protein at the start of the week. Cook lentils, bake tofu, boil eggs, roast chickpeas, grill chicken, or portion yogurt. When protein is ready, balanced meals come together faster.</p>
<h2>Common Protein Mistakes</h2>
<p>One mistake is saving protein for dinner and eating low-protein meals earlier. Another is choosing protein but forgetting produce or carbohydrates. Balance matters. Protein works best as part of a full plate, not as the only goal.</p>
<h2>Related VitalBloom Guides</h2>
<ul>
  <li><a href="/balanced-plate-printable-guide">Balanced Plate Printable Guide</a></li>
  <li><a href="/high-protein-vegetarian-meals">High-Protein Vegetarian Meals</a></li>
  <li><a href="/beginner-meal-prep-checklist">Beginner Meal Prep Checklist</a></li>
  <li><a href="/balanced-plate-guide">Balanced Plate Guide</a></li>
</ul>
<p>Disclaimer: This article is for general educational purposes only and is not a substitute for professional medical or nutrition advice.</p>
""",
    },
    {
        "title": "Fiber-Rich Carbohydrates: A Beginner Guide for Balanced Plates",
        "slug": "fiber-rich-carbohydrates-guide",
        "category": "Nutrition",
        "keyword": "fiber rich carbohydrates",
        "meta_title": "Fiber-Rich Carbohydrates Guide",
        "meta_description": "Learn how fiber-rich carbohydrates fit into balanced meals, including oats, beans, whole grains, fruit, and potatoes.",
        "excerpt": "A beginner guide to fiber-rich carbohydrates and how to use them in satisfying balanced meals.",
        "content": """
<p>Carbohydrates are often discussed in confusing ways, but they can be part of balanced, satisfying meals. Fiber-rich carbohydrates are especially helpful because they add energy, texture, and fullness.</p>
<p>This guide explains simple options and meal ideas. It is general education, not medical nutrition advice. People with diabetes, kidney disease, digestive conditions, allergies, or other needs should follow professional guidance.</p>
<h2>What Are Fiber-Rich Carbohydrates?</h2>
<p>Fiber-rich carbohydrates include foods such as oats, beans, lentils, fruit, vegetables, potatoes, sweet potatoes, brown rice, quinoa, whole-grain bread, and whole-grain pasta. These foods provide carbohydrates along with fiber and other nutrients.</p>
<h2>Why Fiber Matters</h2>
<p>Fiber can support fullness, digestion, and steadier meal satisfaction. Many fiber-rich foods also pair well with protein and produce, making them useful in balanced plate meals.</p>
<h2>Easy Fiber-Rich Options</h2>
<ul>
  <li>Oats with yogurt, fruit, and nuts.</li>
  <li>Brown rice with beans and vegetables.</li>
  <li>Whole-grain toast with eggs or nut butter.</li>
  <li>Potatoes with Greek yogurt, beans, or fish.</li>
  <li>Lentil soup with vegetables.</li>
  <li>Fruit with cottage cheese or nuts.</li>
</ul>
<h2>How to Add Fiber Gradually</h2>
<p>If you are not used to high-fiber foods, add them gradually and drink enough fluids. Adding too much fiber suddenly may cause discomfort for some people.</p>
<h2>Balanced Plate Examples</h2>
<ul>
  <li>Protein: tofu. Produce: broccoli. Carbohydrate: brown rice. Flavor: sesame ginger sauce.</li>
  <li>Protein: eggs. Produce: fruit. Carbohydrate: whole-grain toast. Flavor: avocado or salsa.</li>
  <li>Protein: lentils. Produce: carrots and greens. Carbohydrate: potato. Flavor: lemon and herbs.</li>
</ul>
<h2>Do You Need to Count Fiber?</h2>
<p>Some people like tracking, but many beginners do better by adding one fiber-rich food to a meal. Start with practical swaps: oats instead of a low-fiber breakfast, beans in a bowl, fruit with a snack, or whole-grain bread for a sandwich.</p>
<h2>When Fiber Needs Extra Care</h2>
<p>Some digestive conditions require specific fiber guidance. If fiber causes persistent pain, significant bloating, or changes in bowel habits, talk with a healthcare professional.</p>
<h2>Related VitalBloom Guides</h2>
<ul>
  <li><a href="/balanced-plate-printable-guide">Balanced Plate Printable Guide</a></li>
  <li><a href="/foods-support-better-digestion">Foods That Support Better Digestion Naturally</a></li>
  <li><a href="/high-fiber-breakfast-ideas">High-Fiber Breakfast Ideas</a></li>
  <li><a href="/balanced-plate-method">Balanced Plate Method</a></li>
</ul>
<p>Disclaimer: This article is for general educational purposes only and is not a substitute for professional medical or nutrition advice.</p>
""",
    },
    {
        "title": "Healthy Snack Plate Ideas for Energy Between Meals",
        "slug": "healthy-snack-plate-ideas",
        "category": "Nutrition",
        "keyword": "healthy snack plate ideas",
        "meta_title": "Healthy Snack Plate Ideas",
        "meta_description": "Build simple snack plates with protein, produce, fiber-rich carbohydrates, and satisfying flavor between meals.",
        "excerpt": "Simple healthy snack plate ideas that combine protein, produce, fiber-rich carbs, and flavor for satisfying breaks.",
        "content": """
<p>Snacks can be more than something grabbed in a rush. A simple snack plate can help bridge the gap between meals, support energy, and reduce the feeling of arriving at the next meal overly hungry.</p>
<p>This guide uses the same balanced plate idea in a smaller format: protein, produce, fiber-rich carbohydrate, and flavor. It is not a medical nutrition plan.</p>
<h2>The Snack Plate Formula</h2>
<ul>
  <li>Protein: yogurt, cheese, hummus, nuts, egg, beans, tofu, or nut butter.</li>
  <li>Produce: fruit or vegetables.</li>
  <li>Fiber-rich carbohydrate: whole-grain crackers, oats, toast, pita, potato, or fruit.</li>
  <li>Flavor: herbs, spices, dip, sauce, cinnamon, or a little sweetness.</li>
</ul>
<h2>Quick Snack Plate Ideas</h2>
<ul>
  <li>Apple slices, peanut butter, and whole-grain crackers.</li>
  <li>Greek yogurt, berries, oats, and nuts.</li>
  <li>Hummus, carrots, cucumber, and pita.</li>
  <li>Boiled egg, fruit, and toast.</li>
  <li>Cottage cheese, tomatoes, crackers, and pepper.</li>
  <li>Roasted chickpeas, grapes, and cheese.</li>
</ul>
<h2>Snack Plates for Work or School</h2>
<p>Pack snacks that can survive your schedule. Use containers, shelf-stable options, or simple pairings. Nuts and fruit, roasted chickpeas, whole-grain crackers, tuna packets, or hummus cups may work depending on storage and preferences.</p>
<h2>Snack Plates for Evening Hunger</h2>
<p>If you often get hungry at night, check whether dinner was satisfying. An evening snack can be fine, but repeated intense hunger may mean earlier meals need more protein, fiber, or overall food.</p>
<h2>Snack Mistakes to Avoid</h2>
<p>One mistake is choosing a snack that is only quick sugar when you need something more satisfying. Another is waiting too long and then feeling out of control. A third is making snacks overly complicated. Keep a few reliable options ready.</p>
<h2>How to Use Snack Plates Without Diet Pressure</h2>
<p>Snack plates are not about perfection. Some snacks will be simple, packaged, or chosen for comfort. The formula is a tool, not a rule. Use it when you want steadier energy and less decision fatigue.</p>
<h2>Related VitalBloom Guides</h2>
<ul>
  <li><a href="/balanced-plate-printable-guide">Balanced Plate Printable Guide</a></li>
  <li><a href="/low-sugar-snack-ideas">Low-Sugar Snack Ideas</a></li>
  <li><a href="/add-protein-to-every-meal">How to Add Protein to Every Meal</a></li>
  <li><a href="/hydration-tracker-printable">Hydration Tracker Printable</a></li>
</ul>
<p>Disclaimer: This article is for general educational purposes only and is not a substitute for professional medical or nutrition advice.</p>
""",
    },
]


def run_wp(*args: str) -> str:
    result = subprocess.run(["wp", *args, "--allow-root"], cwd=WP_PATH, text=True, capture_output=True, check=False)
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


def publish(post: dict[str, object]) -> str:
    slug = str(post["slug"])
    category_id = get_or_create_category(str(post["category"]))
    existing_id = find_post_id(slug)
    args = [
        f"--post_title={post['title']}",
        f"--post_name={slug}",
        f"--post_content={str(post['content']).strip()}",
        f"--post_excerpt={post['excerpt']}",
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

    run_wp("post", "meta", "update", post_id, "_yoast_wpseo_title", str(post["meta_title"]))
    run_wp("post", "meta", "update", post_id, "_yoast_wpseo_metadesc", str(post["meta_description"]))
    run_wp("post", "meta", "update", post_id, "_yoast_wpseo_focuskw", str(post["keyword"]))
    run_wp("post", "meta", "update", post_id, "_vitalbloom_sources", json.dumps(COMMON_SOURCES, ensure_ascii=True))
    run_wp("post", "meta", "update", post_id, "_vitalbloom_fact_checked_by", "VitalBloom Editorial Team")
    run_wp("post", "meta", "update", post_id, "_vitalbloom_fact_checked_at", TODAY)
    return f"{action}: {post_id} {slug}"


def main() -> None:
    for post in POSTS:
        print(publish(post))


if __name__ == "__main__":
    main()
