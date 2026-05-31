import json
import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
IMAGE_DIR = Path("/tmp/vitalbloom-next-batch1")
TODAY = "2026-05-31"


POSTS = [
    {
        "title": "How to Build a 10-Minute Walking Routine for Busy Days",
        "slug": "10-minute-walking-routine",
        "category": "Fitness",
        "keyword": "10 minute walking routine",
        "meta_title": "10-Minute Walking Routine for Busy Days",
        "meta_description": "Build a simple 10-minute walking routine for busy days with realistic steps, weekly planning tips, and beginner-friendly movement guidance.",
        "excerpt": "A practical walking routine for busy days, built around short sessions, realistic goals, and simple ways to stay consistent.",
        "image": "10-minute-walking-routine.png",
        "image_alt": "10 minute walking routine guide",
        "sources": [
            {
                "title": "Adult Activity: An Overview",
                "url": "https://www.cdc.gov/physical-activity-basics/guidelines/adults.html",
                "publisher": "Centers for Disease Control and Prevention",
                "accessedAt": TODAY,
            },
            {
                "title": "Steps for Getting Started With Physical Activity",
                "url": "https://www.cdc.gov/healthy-weight-growth/physical-activity/getting-started.html",
                "publisher": "Centers for Disease Control and Prevention",
                "accessedAt": TODAY,
            },
        ],
        "content": """
<p>A 10-minute walking routine can be a realistic way to build movement into a busy day. It does not require a gym, special equipment, or a perfect schedule. The main goal is to make walking easy enough to repeat, even on days when your calendar is full.</p>
<p>Walking also gives you a flexible starting point. You can walk outside, around your building, on a treadmill, or through a quiet hallway. For general education, this guide focuses on habit design rather than medical advice. If you have a health condition or have been inactive for a long time, speak with a qualified healthcare professional before changing your activity routine.</p>
<h2>Why 10 Minutes Can Be Enough to Start</h2>
<p>Many people delay exercise because they imagine it has to be long or intense. A short walk lowers the barrier. Ten minutes can help you practice showing up, notice how your body feels, and create a repeatable cue in your day.</p>
<p>The CDC notes that adults benefit from regular moderate-intensity physical activity, and brisk walking is one example of moderate activity. A short routine can become the first piece of a larger weekly movement plan.</p>
<h2>Pick a Walking Window</h2>
<p>Choose one daily time when a short walk is most likely to happen. Good options include after breakfast, during a lunch break, after work, or after dinner. Pairing walking with an existing habit makes the routine easier to remember.</p>
<p>If your schedule changes often, create two options: a preferred time and a backup time. For example, you might walk after lunch on normal days and after dinner on busy days.</p>
<h2>Use a Simple 10-Minute Plan</h2>
<ul>
  <li>Minute 1: Start slowly and check posture.</li>
  <li>Minutes 2-8: Walk at a comfortable pace that feels steady but not forced.</li>
  <li>Minute 9: Slow down slightly.</li>
  <li>Minute 10: Finish with a relaxed pace and notice how you feel.</li>
</ul>
<p>You can repeat this plan once per day or use it as a short break between longer sitting periods.</p>
<h2>Make It Easier to Repeat</h2>
<p>Keep shoes, a jacket, headphones, or a water bottle where you can see them. If you work from home, block the walk on your calendar. If you commute, consider getting off transit one stop earlier or walking around the block before going inside.</p>
<p>Track completion with a check mark. Do not worry about speed, distance, or calories at first. A reliable habit is more valuable than a complicated plan you do only once.</p>
<h2>When to Add More Time</h2>
<p>After two or three consistent weeks, you can add a second 10-minute walk, extend one walk to 15 minutes, or include gentle hills. Increase gradually so the routine continues to feel manageable.</p>
<h2>10-Minute Walking Checklist</h2>
<ul>
  <li>Choose one preferred walking time.</li>
  <li>Keep a backup time for busy days.</li>
  <li>Start at a comfortable pace.</li>
  <li>Track completion, not perfection.</li>
  <li>Build slowly after consistency feels stable.</li>
</ul>
<h2>Common Questions</h2>
<h3>Is 10 minutes of walking worth it?</h3>
<p>Yes, it can be worth it as a starting point. Short walks can help you build consistency and may make longer movement sessions feel more approachable later.</p>
<h3>Should I walk fast?</h3>
<p>Start with a comfortable pace. If you want moderate intensity, aim for a pace where you can talk but not sing easily.</p>
<h3>Can I split walking into multiple short sessions?</h3>
<p>Yes. Several short walks can be a practical way to add movement across the day, especially if your schedule is unpredictable.</p>
<p>Related reading: <a href="/walking-for-weight-management">Walking for Weight Management and Better Energy</a>, <a href="/daily-wellness-routine-beginners">Daily Wellness Routine for Beginners</a>, and <a href="/exercise-sustainable-habit">How to Make Exercise a Sustainable Habit</a>.</p>
""",
    },
    {
        "title": "Simple Meal Prep Ideas for Healthy Weekday Lunches",
        "slug": "simple-meal-prep-healthy-lunches",
        "category": "Nutrition",
        "keyword": "simple healthy lunch meal prep",
        "meta_title": "Simple Healthy Lunch Meal Prep Ideas",
        "meta_description": "Try simple healthy lunch meal prep ideas built around balanced plates, flexible ingredients, and realistic weekday routines.",
        "excerpt": "Easy lunch meal prep ideas that use balanced plate basics, flexible ingredients, and realistic planning for busy weekdays.",
        "image": "simple-meal-prep-healthy-lunches.png",
        "image_alt": "simple healthy lunch meal prep ideas",
        "sources": [
            {
                "title": "Meal Planning",
                "url": "https://www.myplate.gov/sites/default/files/2024-06/TipSheet-24-Meal-Planning.pdf",
                "publisher": "MyPlate, U.S. Department of Agriculture",
                "accessedAt": TODAY,
            },
            {
                "title": "Healthy Eating Tips",
                "url": "https://www.cdc.gov/nutrition/features/healthy-eating-tips.html",
                "publisher": "Centers for Disease Control and Prevention",
                "accessedAt": TODAY,
            },
        ],
        "content": """
<p>Healthy weekday lunches are easier when you do not have to make every decision at the last minute. Simple meal prep can help you keep balanced options ready without spending an entire weekend in the kitchen.</p>
<p>The best meal prep system is one you can repeat. Instead of trying to prepare five perfect lunches, start with a few flexible building blocks: a protein, a fiber-rich carbohydrate, vegetables or fruit, and a sauce or seasoning that makes the meal enjoyable.</p>
<h2>Start With One Lunch Formula</h2>
<p>A simple lunch formula reduces decision fatigue. Try protein plus produce plus fiber-rich carbohydrate plus flavor. For example, beans, roasted vegetables, brown rice, and salsa can become a bowl. Turkey, greens, whole-grain bread, and fruit can become a quick lunch plate.</p>
<p>This approach connects well with the balanced plate method because it focuses on food groups and meal quality rather than strict rules.</p>
<h2>Choose Ingredients That Hold Up</h2>
<p>Good meal prep ingredients stay appealing for several days. Roasted vegetables, cooked grains, beans, lentils, grilled chicken, boiled eggs, tofu, Greek yogurt, nuts, and sturdy greens can all be useful depending on your eating pattern.</p>
<p>Keep sauces separate when possible. This helps salads, wraps, bowls, and leftovers taste fresher.</p>
<h2>Prep Components, Not Every Meal</h2>
<p>Component prep gives you variety without extra work. Cook a grain, wash or chop produce, prepare one protein, and keep two sauces ready. During the week, combine them in different ways.</p>
<ul>
  <li>Monday: grain bowl with vegetables and beans.</li>
  <li>Tuesday: wrap with protein, greens, and yogurt sauce.</li>
  <li>Wednesday: leftovers with fruit and a simple side.</li>
  <li>Thursday: salad bowl with nuts or seeds.</li>
  <li>Friday: snack plate with protein, produce, and whole grains.</li>
</ul>
<h2>Keep Food Safety in Mind</h2>
<p>Use clean containers, refrigerate prepared foods promptly, and avoid leaving perishable lunches at room temperature for long periods. If you commute, an insulated lunch bag and ice pack can help.</p>
<h2>Meal Prep Checklist</h2>
<ul>
  <li>Pick one lunch formula for the week.</li>
  <li>Prep two or three components instead of five complete meals.</li>
  <li>Include a protein source and fiber-rich foods.</li>
  <li>Keep sauces or dressings separate.</li>
  <li>Plan one backup lunch for unusually busy days.</li>
</ul>
<h2>Common Questions</h2>
<h3>Do I need to prep all lunches at once?</h3>
<p>No. Many people do better prepping two or three days at a time so meals stay fresher and the process feels lighter.</p>
<h3>What if I get bored with the same lunch?</h3>
<p>Change the sauce, seasoning, or side rather than rebuilding the entire meal. This keeps prep simple while adding variety.</p>
<h3>Can meal prep work for vegetarian lunches?</h3>
<p>Yes. Beans, lentils, tofu, tempeh, eggs, Greek yogurt, nuts, and seeds can support satisfying vegetarian lunch options.</p>
<p>Related reading: <a href="/balanced-plate-method">How to Build a Balanced Plate Without Counting Calories</a>, <a href="/healthy-breakfast-ideas">Healthy Breakfast Ideas for Busy Mornings</a>, and <a href="/low-sugar-snack-ideas">Low-Sugar Snack Ideas That Still Feel Satisfying</a>.</p>
""",
    },
    {
        "title": "A Beginner-Friendly Evening Routine for Better Sleep",
        "slug": "beginner-evening-routine-better-sleep",
        "category": "Sleep",
        "keyword": "evening routine for better sleep",
        "meta_title": "Beginner Evening Routine for Better Sleep",
        "meta_description": "Create a beginner-friendly evening routine for better sleep with realistic wind-down habits, screen boundaries, and calming bedtime cues.",
        "excerpt": "A realistic evening routine for better sleep, built around simple wind-down habits, screen boundaries, and consistent cues.",
        "image": "beginner-evening-routine-better-sleep.png",
        "image_alt": "beginner evening routine for better sleep",
        "sources": [
            {
                "title": "Sleep Deprivation and Deficiency - Healthy Sleep Habits",
                "url": "https://www.nhlbi.nih.gov/health/sleep-deprivation/healthy-sleep-habits",
                "publisher": "National Heart, Lung, and Blood Institute",
                "accessedAt": TODAY,
            },
            {
                "title": "About Sleep",
                "url": "https://www.cdc.gov/sleep/about/index.html",
                "publisher": "Centers for Disease Control and Prevention",
                "accessedAt": TODAY,
            },
        ],
        "content": """
<p>A beginner-friendly evening routine should help your body and mind transition from the demands of the day into rest. It does not need to be long, expensive, or perfect. A few repeated cues can make bedtime feel less abrupt.</p>
<p>Sleep is influenced by timing, light, stress, caffeine, activity, and consistency. This routine focuses on practical habits that may support better rest while avoiding unrealistic rules.</p>
<h2>Start With a Wind-Down Time</h2>
<p>Choose a time when the active part of your day begins to close. This may be 30 minutes before bed or closer to an hour if your evenings are busy. The goal is to stop asking your brain to switch instantly from work, chores, or screens to sleep.</p>
<p>If your bedtime changes, keep the order of your routine consistent. Predictability matters even when the exact time is not perfect.</p>
<h2>Lower Stimulation Gradually</h2>
<p>Bright lights, stressful messages, late work, and fast-moving content can make it harder to feel sleepy. A gentle routine might include dimmer lights, quieter tasks, and a screen boundary for the final part of the evening.</p>
<h2>Prepare Tomorrow Before Bed</h2>
<p>A small amount of planning can reduce bedtime worry. Write down tomorrow's top priority, set out clothes, pack a bag, or prepare breakfast basics. This tells your mind that the next day has a plan.</p>
<h2>Choose One Calming Habit</h2>
<p>Pick one activity that feels calming and repeatable. Options include light stretching, breathing, reading, journaling, or a warm shower. Avoid turning the routine into a long checklist that becomes stressful.</p>
<h2>Beginner Evening Checklist</h2>
<ul>
  <li>Set a wind-down reminder.</li>
  <li>Dim lights or reduce screen brightness.</li>
  <li>Write down tomorrow's top task.</li>
  <li>Choose one calming activity.</li>
  <li>Keep the bedroom cool, dark, and quiet when possible.</li>
</ul>
<h2>Common Questions</h2>
<h3>How long should an evening routine be?</h3>
<p>Start with 15 to 30 minutes. A short routine is easier to repeat than a long routine that feels like another obligation.</p>
<h3>Do I have to stop screens completely?</h3>
<p>Not always. The practical goal is to reduce the screen habits that delay sleep or increase stress.</p>
<h3>What if I wake up during the night?</h3>
<p>Keep the environment calm and avoid turning the wake-up into a long problem-solving session. If sleep problems persist, consider professional guidance.</p>
<p>Related reading: <a href="/better-sleep-routine">How to Build a Better Sleep Routine</a>, <a href="/evening-habits-better-rest">Evening Habits for Better Rest</a>, and <a href="/sleep-hygiene-checklist">Sleep Hygiene Checklist for Everyday Life</a>.</p>
""",
    },
    {
        "title": "How to Take Better Breaks During Remote Work",
        "slug": "better-breaks-remote-work",
        "category": "Lifestyle",
        "keyword": "remote work breaks",
        "meta_title": "Better Breaks During Remote Work",
        "meta_description": "Learn how to take better breaks during remote work with movement, eye rest, boundaries, and simple routines that support energy.",
        "excerpt": "Simple ways to take better breaks during remote work so long sitting days feel more manageable and less draining.",
        "image": "better-breaks-remote-work.png",
        "image_alt": "better breaks during remote work",
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
<p>Remote work can make breaks harder to notice. Without a commute, hallway conversations, or natural transitions between meetings, it is easy to sit for hours and feel drained by the end of the day.</p>
<p>Better breaks do not need to be long. A good break gives your eyes, body, and attention a real change of state. The goal is to return to work with a little more comfort and clarity.</p>
<h2>Schedule Breaks Before You Need Them</h2>
<p>If you wait until you are stiff or exhausted, you may already be past the point where a short break helps. Add small breaks to your calendar or use a timer that reminds you to stand, move, or look away from the screen.</p>
<h2>Use Different Types of Breaks</h2>
<p>Not every break has to be a walk. Rotate between movement breaks, eye breaks, hydration breaks, breathing breaks, and quick reset tasks. Variety helps you respond to what your body actually needs.</p>
<ul>
  <li>Movement break: stand, stretch, or walk for two to five minutes.</li>
  <li>Eye break: look away from the screen and focus on something farther away.</li>
  <li>Hydration break: refill water and step away from the desk.</li>
  <li>Boundary break: close work tabs before lunch or after the day ends.</li>
</ul>
<h2>Build a Desk Reset</h2>
<p>A better break can also include adjusting your workspace. Check monitor height, chair position, keyboard reach, and lighting. Small ergonomic improvements can reduce avoidable discomfort.</p>
<h2>Protect Lunch From Becoming Another Meeting</h2>
<p>Remote workers often eat at the desk. When possible, take lunch away from the screen. Even 10 minutes of separation can make the day feel less compressed.</p>
<h2>Remote Break Checklist</h2>
<ul>
  <li>Stand or move at least once each hour when possible.</li>
  <li>Look away from the screen during short pauses.</li>
  <li>Keep water close but refill it away from the desk.</li>
  <li>Use a real lunch break, not just a muted meeting.</li>
  <li>Create a shutdown cue at the end of the workday.</li>
</ul>
<h2>Common Questions</h2>
<h3>How often should I take breaks?</h3>
<p>There is no perfect number for everyone. Start with a brief break every hour and adjust based on your schedule and comfort.</p>
<h3>Do short breaks hurt productivity?</h3>
<p>Short breaks can support focus for many people because they reduce fatigue and make long work blocks feel more manageable.</p>
<h3>What if my meetings are back-to-back?</h3>
<p>Use micro-breaks. Stand for one minute, stretch your hands, or look away from the screen before the next call.</p>
<p>Related reading: <a href="/healthy-habits-remote-workers">Healthy Habits for Remote Workers</a>, <a href="/stretching-routine-desk-workers">Stretching Routine for Desk Workers</a>, and <a href="/simple-breathing-exercises">Simple Breathing Exercises for Everyday Stress</a>.</p>
""",
    },
    {
        "title": "High-Fiber Breakfast Ideas That Keep Mornings Simple",
        "slug": "high-fiber-breakfast-ideas",
        "category": "Nutrition",
        "keyword": "high fiber breakfast ideas",
        "meta_title": "High-Fiber Breakfast Ideas for Simple Mornings",
        "meta_description": "Try high-fiber breakfast ideas that keep mornings simple with oats, fruit, whole grains, beans, seeds, and balanced add-ins.",
        "excerpt": "Simple high-fiber breakfast ideas built around oats, fruit, whole grains, seeds, and balanced add-ins for busy mornings.",
        "image": "high-fiber-breakfast-ideas.png",
        "image_alt": "high fiber breakfast ideas",
        "sources": [
            {
                "title": "Dietary Fiber",
                "url": "https://medlineplus.gov/dietaryfiber.html",
                "publisher": "MedlinePlus",
                "accessedAt": TODAY,
            },
            {
                "title": "Fiber",
                "url": "https://nutritionsource.hsph.harvard.edu/carbohydrates/fiber/",
                "publisher": "The Nutrition Source, Harvard T.H. Chan School of Public Health",
                "accessedAt": TODAY,
            },
        ],
        "content": """
<p>A high-fiber breakfast does not have to be complicated. Many simple foods, including oats, fruit, whole-grain toast, beans, seeds, and vegetables, can help make breakfast more satisfying and support digestive wellness.</p>
<p>Fiber needs vary, and some people need to increase fiber slowly to avoid discomfort. Drink fluids and consider personal health needs, especially if you have digestive conditions or follow a medically guided diet.</p>
<h2>Start With a Fiber Base</h2>
<p>Choose one fiber-rich base for the meal. Oats, whole-grain cereal, whole-grain toast, beans, lentils, fruit, or vegetables can all work. The base makes breakfast easier to build because the rest of the meal can be simple.</p>
<h2>Add Protein for Staying Power</h2>
<p>Fiber and protein together can make breakfast feel more complete. Options include Greek yogurt, eggs, cottage cheese, tofu, nut butter, seeds, beans, or a protein-rich milk option.</p>
<h2>Use Fruit and Seeds Strategically</h2>
<p>Berries, pears, apples, bananas, chia seeds, ground flaxseed, and nuts can raise fiber without making breakfast complicated. Add them to yogurt, oats, toast, smoothies, or breakfast bowls.</p>
<h2>Simple High-Fiber Breakfast Ideas</h2>
<ul>
  <li>Overnight oats with berries and chia seeds.</li>
  <li>Greek yogurt with fruit, nuts, and high-fiber cereal.</li>
  <li>Whole-grain toast with nut butter and sliced banana.</li>
  <li>Bean and egg breakfast wrap with vegetables.</li>
  <li>Warm oatmeal with apples, cinnamon, and ground flaxseed.</li>
</ul>
<h2>Make It Easier on Busy Mornings</h2>
<p>Prepare one ingredient the night before. Portion oats, wash fruit, boil eggs, or place yogurt and toppings together in the refrigerator. A small amount of preparation can make the healthier choice easier when you are rushed.</p>
<h2>High-Fiber Breakfast Checklist</h2>
<ul>
  <li>Choose one fiber-rich base.</li>
  <li>Add a protein source.</li>
  <li>Include fruit or vegetables when possible.</li>
  <li>Increase fiber gradually if your body needs time to adjust.</li>
  <li>Drink fluids during the morning.</li>
</ul>
<h2>Common Questions</h2>
<h3>Can I eat a high-fiber breakfast every day?</h3>
<p>Many people can, but it is best to increase fiber gradually and choose a variety of foods.</p>
<h3>What if high-fiber foods upset my stomach?</h3>
<p>Try smaller portions, drink water, and add fiber slowly. If symptoms continue, talk with a healthcare professional.</p>
<h3>Are smoothies a good high-fiber breakfast?</h3>
<p>They can be if they include whole fruits, vegetables, seeds, oats, or other fiber-rich ingredients rather than mostly juice.</p>
<p>Related reading: <a href="/healthy-breakfast-ideas">Healthy Breakfast Ideas for Busy Mornings</a>, <a href="/foods-support-better-digestion">Foods That Support Better Digestion Naturally</a>, and <a href="/balanced-plate-method">How to Build a Balanced Plate Without Counting Calories</a>.</p>
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


def set_featured_image(post_id: str, post: dict) -> None:
    attachment_id = existing_attachment_id(post["slug"])
    if not attachment_id:
        attachment_id = run_wp(
            "media",
            "import",
            str(IMAGE_DIR / post["image"]),
            f"--title={post['title']}",
            f"--alt={post['image_alt']}",
            "--porcelain",
        )
    run_wp("post", "meta", "update", post_id, "_thumbnail_id", attachment_id)


def publish(post: dict) -> str:
    category_id = get_or_create_category(post["category"])
    existing_id = find_post_id(post["slug"])
    args = [
        f"--post_title={post['title']}",
        f"--post_name={post['slug']}",
        f"--post_content={post['content'].strip()}",
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

    run_wp("post", "meta", "update", post_id, "_yoast_wpseo_title", post["meta_title"])
    run_wp("post", "meta", "update", post_id, "_yoast_wpseo_metadesc", post["meta_description"])
    run_wp("post", "meta", "update", post_id, "_yoast_wpseo_focuskw", post["keyword"])
    run_wp("post", "meta", "update", post_id, "_vitalbloom_sources", json.dumps(post["sources"], ensure_ascii=True))
    run_wp("post", "meta", "update", post_id, "_vitalbloom_fact_checked_by", "VitalBloom Editorial Team")
    run_wp("post", "meta", "update", post_id, "_vitalbloom_fact_checked_at", TODAY)
    set_featured_image(post_id, post)
    return f"{action}: {post_id} {post['slug']}"


def main() -> None:
    for post in POSTS:
        print(publish(post))


if __name__ == "__main__":
    main()
