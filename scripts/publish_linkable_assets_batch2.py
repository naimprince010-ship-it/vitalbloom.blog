import json
import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
TODAY = "2026-06-01"


ASSETS = [
    {
        "title": "Balanced Plate Printable Guide",
        "slug": "balanced-plate-printable-guide",
        "category": "Nutrition",
        "keyword": "balanced plate printable",
        "meta_title": "Balanced Plate Printable Guide",
        "meta_description": "Use this balanced plate printable guide to build simple meals with protein, produce, fiber-rich carbohydrates, and healthy fats.",
        "excerpt": "A practical balanced plate worksheet for planning simple meals without calorie counting or complicated rules.",
        "sources": [
            {
                "title": "MyPlate Plan",
                "url": "https://www.myplate.gov/myplate-plan",
                "publisher": "U.S. Department of Agriculture",
                "accessedAt": TODAY,
            },
            {
                "title": "Healthy Eating Plate",
                "url": "https://www.health.harvard.edu/plate/healthy-eating-plate",
                "publisher": "Harvard Health Publishing",
                "accessedAt": TODAY,
            },
        ],
        "content": """
<p>The balanced plate method is a visual way to build meals that feel satisfying and realistic. It can help you include protein, produce, fiber-rich carbohydrates, and healthy fats without needing to count every calorie.</p>
<p>Use this printable-style guide as a meal planning worksheet. It is not a medical nutrition plan, and people with medical conditions or special dietary needs should follow professional guidance.</p>
<h2>Balanced Plate Formula</h2>
<ul>
  <li>Half the plate: vegetables or fruit.</li>
  <li>One quarter: protein.</li>
  <li>One quarter: fiber-rich carbohydrates.</li>
  <li>Add a small amount of healthy fat or flavorful sauce.</li>
  <li>Include water or another unsweetened drink when possible.</li>
</ul>
<h2>Protein Ideas</h2>
<p>Choose one protein anchor first. Options include eggs, Greek yogurt, cottage cheese, beans, lentils, tofu, tempeh, fish, poultry, lean meats, nuts, seeds, or nut butter.</p>
<h2>Produce Ideas</h2>
<p>Add color and fiber with salad greens, broccoli, carrots, peppers, tomatoes, berries, apples, citrus fruits, or roasted vegetables.</p>
<h2>Fiber-Rich Carbohydrate Ideas</h2>
<p>Useful options include oats, brown rice, quinoa, potatoes, sweet potatoes, whole-grain bread, beans, lentils, whole-grain pasta, and fruit.</p>
<h2>Meal Planning Worksheet</h2>
<ul>
  <li>Protein:</li>
  <li>Produce:</li>
  <li>Carbohydrate:</li>
  <li>Fat or sauce:</li>
  <li>Optional side:</li>
</ul>
<p>Example: lentils, roasted vegetables, brown rice, and tahini-lemon dressing.</p>
<h2>Three-Day Practice Plan</h2>
<p>Day one: use the formula for one meal only. Pick the easiest meal of the day and make one small adjustment, such as adding fruit to breakfast or vegetables to lunch.</p>
<p>Day two: build one full plate from the worksheet. Choose protein first, then add produce, carbohydrate, and flavor.</p>
<p>Day three: review what felt easiest. Keep the meal that worked and simplify anything that felt too complicated.</p>
<h2>Balanced Plate Examples</h2>
<h3>Breakfast</h3>
<ul>
  <li>Greek yogurt with berries, oats, chia seeds, and nuts.</li>
  <li>Eggs with whole-grain toast, avocado, and fruit.</li>
  <li>Tofu scramble with vegetables and potatoes.</li>
</ul>
<h3>Lunch</h3>
<ul>
  <li>Chickpea wrap with greens, cucumber, yogurt sauce, and fruit.</li>
  <li>Rice bowl with beans, roasted vegetables, salsa, and avocado.</li>
  <li>Lentil soup with whole-grain bread and salad.</li>
</ul>
<h3>Dinner</h3>
<ul>
  <li>Salmon or tofu with sweet potato, broccoli, and olive oil dressing.</li>
  <li>Pasta with vegetables, beans, and a side salad.</li>
  <li>Stir-fry with tempeh, vegetables, brown rice, and sesame sauce.</li>
</ul>
<h2>Quick Fixes for Common Meals</h2>
<ul>
  <li>Pasta: add vegetables and protein.</li>
  <li>Sandwich: add fruit, soup, salad, or yogurt on the side.</li>
  <li>Breakfast: pair toast or oats with protein.</li>
  <li>Snack plate: include fruit or vegetables plus protein.</li>
  <li>Rice bowl: add beans, tofu, eggs, fish, or chicken plus vegetables.</li>
</ul>
<h2>How to Use the Guide Without Diet Pressure</h2>
<p>This guide is meant to reduce decision fatigue, not create food rules. Some meals will not match the plate perfectly, and that is normal. Look at your meals across the day or week instead of grading every plate.</p>
<p>If one meal is low in protein, choose a protein-rich snack later. If lunch has few vegetables, add fruit or cooked vegetables at dinner. Flexible adjustments are easier to sustain than strict rules.</p>
<h2>Grocery List Template</h2>
<p>Choose two from each group: protein, produce, carbohydrate, and flavor. Keeping the list short makes meal planning easier and helps reduce food waste.</p>
<h2>Common Balanced Plate Problems</h2>
<h3>The meal does not keep me full.</h3>
<p>Check protein, fiber, and fat. A plate with mostly refined carbohydrates may taste good but leave you hungry quickly. Add Greek yogurt, eggs, beans, lentils, tofu, fish, poultry, nuts, seeds, avocado, olive oil, or another satisfying option that fits your eating pattern.</p>
<h3>I do not like many vegetables.</h3>
<p>Start with familiar options and change the preparation. Roasted carrots, cooked spinach, soup vegetables, salsa, salad greens, or fruit may feel easier than a large raw salad. The goal is more variety over time, not forcing foods you dislike.</p>
<h3>I eat mixed dishes instead of separate plates.</h3>
<p>The method still works. For soup, pasta, wraps, casseroles, or bowls, ask whether the meal includes protein, produce, fiber-rich carbohydrate, and flavor. You do not need the foods to sit in separate sections.</p>
<h2>Weekly Meal Planning Prompts</h2>
<ul>
  <li>What protein can I prepare once and use twice?</li>
  <li>What produce is easy to add to meals this week?</li>
  <li>What carbohydrate will make meals satisfying?</li>
  <li>What sauce or seasoning will make the meal enjoyable?</li>
  <li>What backup meal can I use on a busy day?</li>
</ul>
<p>Planning with prompts keeps the guide practical. You are not trying to create perfect meals; you are making the next meal easier to assemble.</p>
<h2>How to Share This Guide</h2>
<p>This guide works well as a simple handout for meal planning, workplace wellness, beginner nutrition education, or family meal prep. The worksheet format gives readers a practical next step instead of a long list of rules.</p>
<h2>Related VitalBloom Guides</h2>
<ul>
  <li><a href="/balanced-plate-guide">Balanced Plate Guide</a></li>
  <li><a href="/balanced-plate-method">How to Build a Balanced Plate Without Counting Calories</a></li>
  <li><a href="/high-protein-vegetarian-meals">High-Protein Vegetarian Meals</a></li>
  <li><a href="/low-sugar-snack-ideas">Low-Sugar Snack Ideas</a></li>
</ul>
<p>Disclaimer: This resource is for general educational purposes only and is not a substitute for professional medical advice, diagnosis, or treatment.</p>
""",
    },
    {
        "title": "Remote Worker Wellness Checklist",
        "slug": "remote-worker-wellness-checklist",
        "category": "Wellness",
        "keyword": "remote worker wellness checklist",
        "meta_title": "Remote Worker Wellness Checklist",
        "meta_description": "Use this remote worker wellness checklist to plan movement breaks, eye rest, meals, hydration, posture, and work shutdown cues.",
        "excerpt": "A practical checklist for healthier remote workdays with better breaks, movement, hydration, posture, and boundaries.",
        "sources": [
            {
                "title": "Office Environments and Your Safety",
                "url": "https://www.cdc.gov/niosh/office-environment/about/index.html",
                "publisher": "Centers for Disease Control and Prevention",
                "accessedAt": TODAY,
            },
            {
                "title": "Office Ergonomics: Your How-to Guide",
                "url": "https://www.mayoclinic.org/health/office-ergonomics/MY01460",
                "publisher": "Mayo Clinic",
                "accessedAt": TODAY,
            },
        ],
        "content": """
<p>Remote work can make healthy routines harder to notice. Without a commute or office rhythm, it is easy to sit too long, skip breaks, eat at the desk, and let work spill into the evening.</p>
<p>Use this checklist as a simple reset for your workday. It is not a medical or ergonomic assessment, but it can help you build more supportive daily cues.</p>
<h2>Start-of-Day Checklist</h2>
<ul>
  <li>Drink water before opening work apps.</li>
  <li>Get light near the start of the day.</li>
  <li>Choose the top one to three priorities.</li>
  <li>Set a lunch window.</li>
  <li>Decide when the workday should end.</li>
</ul>
<h2>Desk and Posture Checklist</h2>
<ul>
  <li>Screen is near eye level.</li>
  <li>Feet are supported.</li>
  <li>Shoulders are relaxed.</li>
  <li>Keyboard and mouse are easy to reach.</li>
  <li>Lighting does not create strong glare.</li>
  <li>Frequently used items are within comfortable reach.</li>
</ul>
<h2>Break Checklist</h2>
<ul>
  <li>Stand or move at least once each hour when possible.</li>
  <li>Look away from the screen during short pauses.</li>
  <li>Refill water away from the desk.</li>
  <li>Stretch neck, shoulders, wrists, hips, or calves.</li>
  <li>Use one real recovery break that is not more scrolling.</li>
</ul>
<h2>Micro-Break Menu</h2>
<ul>
  <li>Shoulder rolls and chest opener after a video call.</li>
  <li>Wrist and forearm stretch after a long typing block.</li>
  <li>Water refill between tasks.</li>
  <li>One minute of slow breathing before a difficult message.</li>
  <li>Looking out a window or across the room to rest your eyes.</li>
  <li>Ten bodyweight squats or a short hallway walk.</li>
</ul>
<p>Micro-breaks are not a replacement for lunch or real rest, but they can interrupt long sitting blocks before stiffness builds.</p>
<h2>Lunch and Hydration Checklist</h2>
<ul>
  <li>Eat away from the keyboard when possible.</li>
  <li>Include protein and fiber for a more satisfying meal.</li>
  <li>Keep water visible.</li>
  <li>Prepare one simple snack before hunger gets intense.</li>
  <li>Avoid letting back-to-back meetings erase lunch every day.</li>
</ul>
<h2>Shutdown Checklist</h2>
<ul>
  <li>Write tomorrow's first task.</li>
  <li>Close work tabs.</li>
  <li>Turn off non-urgent notifications.</li>
  <li>Clear one small part of the desk.</li>
  <li>Step away with a walk, stretch, or household transition.</li>
</ul>
<h2>Weekly Remote Work Reset</h2>
<ul>
  <li>Which meeting block made breaks hardest?</li>
  <li>Did lunch happen away from the keyboard?</li>
  <li>Which part of the desk caused discomfort?</li>
  <li>Did work end at a clear time?</li>
  <li>What is one boundary to protect next week?</li>
</ul>
<h2>Better Break Examples</h2>
<p>Morning reset: refill water, stand near daylight, and choose the next priority.</p>
<p>Midday reset: eat lunch away from the desk, walk for five minutes, and return with one clear task.</p>
<p>Afternoon reset: stretch shoulders and wrists, look away from the screen, and close unused tabs.</p>
<p>End-of-day reset: write tomorrow's first task, close work apps, and step away from the workspace.</p>
<h2>When to Get Extra Support</h2>
<p>If you have persistent pain, numbness, tingling, vision problems, severe stress, or symptoms that affect daily functioning, consider professional support. Remote work habits can help, but they do not replace medical, ergonomic, or mental health guidance when it is needed.</p>
<h2>Common Remote Work Problems</h2>
<h3>I forget breaks when I am focused.</h3>
<p>Use visible cues instead of memory. Put water across the room, set meetings to end a few minutes early when possible, or place a sticky note near your screen. Break reminders work best when they are hard to miss.</p>
<h3>I eat lunch at my desk every day.</h3>
<p>Start with one screen-free lunch per week or a ten-minute desk-free reset. If a full lunch break is unrealistic, protect the first few minutes of the meal so it feels different from another work block.</p>
<h3>I keep working after hours.</h3>
<p>Use a shutdown ritual: write tomorrow's first task, close work tabs, silence non-urgent notifications, and physically step away. A clear ending cue helps remote work feel less endless.</p>
<h2>Team Wellness Ideas</h2>
<p>This checklist can also be used by managers, HR teams, or small groups. Try a shared five-minute meeting buffer, a no-lunch-meeting block, or a weekly reminder to review desk comfort. Small team norms can make healthy breaks easier for everyone.</p>
<h2>How to Share This Checklist</h2>
<p>This checklist can be shared as a remote work resource, onboarding handout, team wellness prompt, or personal weekly reset. It is designed to be practical enough for a busy workday.</p>
<h2>Personalize the Checklist</h2>
<p>Not every remote worker needs the same routine. If your main issue is stiffness, focus on movement and desk setup. If your main issue is feeling scattered, focus on start-of-day planning and shutdown cues. If your main issue is isolation, add one intentional connection point during the day.</p>
<p>The checklist works best when it solves the most repeated friction point in your workday. Start there, then add more habits only when the first one feels steady.</p>
<h2>Related VitalBloom Guides</h2>
<ul>
  <li><a href="/healthy-habits-remote-workers">Healthy Habits for Remote Workers</a></li>
  <li><a href="/better-breaks-remote-work">How to Take Better Breaks During Remote Work</a></li>
  <li><a href="/stretching-routine-desk-workers">Stretching Routine for Desk Workers</a></li>
  <li><a href="/simple-breathing-exercises">Simple Breathing Exercises for Everyday Stress</a></li>
</ul>
<p>Disclaimer: This resource is for general educational purposes only and is not a substitute for professional medical, ergonomic, or mental health advice.</p>
""",
    },
]


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


def publish(asset: dict[str, object]) -> str:
    slug = str(asset["slug"])
    category_id = get_or_create_category(str(asset["category"]))
    existing_id = find_post_id(slug)
    args = [
        f"--post_title={asset['title']}",
        f"--post_name={slug}",
        f"--post_content={str(asset['content']).strip()}",
        f"--post_excerpt={asset['excerpt']}",
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

    run_wp("post", "meta", "update", post_id, "_yoast_wpseo_title", str(asset["meta_title"]))
    run_wp("post", "meta", "update", post_id, "_yoast_wpseo_metadesc", str(asset["meta_description"]))
    run_wp("post", "meta", "update", post_id, "_yoast_wpseo_focuskw", str(asset["keyword"]))
    run_wp("post", "meta", "update", post_id, "_vitalbloom_sources", json.dumps(asset["sources"], ensure_ascii=True))
    run_wp("post", "meta", "update", post_id, "_vitalbloom_fact_checked_by", "VitalBloom Editorial Team")
    run_wp("post", "meta", "update", post_id, "_vitalbloom_fact_checked_at", TODAY)
    return f"{action}: {post_id} {slug}"


def main() -> None:
    for asset in ASSETS:
        print(publish(asset))


if __name__ == "__main__":
    main()
