import json
import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
IMAGE_DIR = Path("/tmp/vitalbloom-sleep-pillar")
TODAY = "2026-05-31"
SLUG = "better-sleep-routine-guide"
MARKER = "<!-- vitalbloom-sleep-pillar-link-v1 -->"

POST = {
    "title": "How to Build a Better Sleep Routine: A Complete Beginner Guide",
    "slug": SLUG,
    "category": "Sleep",
    "keyword": "better sleep routine",
    "meta_title": "Better Sleep Routine: Complete Beginner Guide",
    "meta_description": "Build a better sleep routine with a simple evening plan, 7-day starter steps, troubleshooting tips, and evidence-informed sleep habits.",
    "excerpt": "A complete beginner guide to building a better sleep routine with realistic evening habits, a 7-day starter plan, troubleshooting tips, and credible sources.",
    "image": "better-sleep-routine-guide.png",
    "image_alt": "better sleep routine complete beginner guide",
    "sources": [
        {
            "title": "About Sleep",
            "url": "https://www.cdc.gov/sleep/about/index.html",
            "publisher": "Centers for Disease Control and Prevention",
            "accessedAt": TODAY,
        },
        {
            "title": "Sleep Deprivation and Deficiency - Healthy Sleep Habits",
            "url": "https://www.nhlbi.nih.gov/health/sleep-deprivation/healthy-sleep-habits",
            "publisher": "National Heart, Lung, and Blood Institute",
            "accessedAt": TODAY,
        },
        {
            "title": "How Sleep Affects Your Health",
            "url": "https://www.nhlbi.nih.gov/health/sleep-deprivation/health-effects",
            "publisher": "National Heart, Lung, and Blood Institute",
            "accessedAt": TODAY,
        },
        {
            "title": "Sleep Tips: 6 Steps to Better Sleep",
            "url": "https://www.mayoclinic.org/healthy-lifestyle/adult-health/in-depth/sleep/art-20048379",
            "publisher": "Mayo Clinic",
            "accessedAt": TODAY,
        },
    ],
    "content": """
<p>A better sleep routine is not about creating a perfect night. It is about building a repeatable set of cues that help your body and mind move from daytime activity into rest. For many adults, the most helpful routine is simple, realistic, and easy to restart after a busy day.</p>
<p>This guide gives you a beginner-friendly evening routine, a 7-day starter plan, and troubleshooting ideas for common sleep routine problems. It is for general education and does not replace medical care. If sleep problems are persistent, worsening, or affecting daily life, talk with a qualified healthcare professional.</p>
<h2>Start Here Tonight</h2>
<p>If you only want the short version, start with these five steps tonight:</p>
<ul>
  <li>Pick a consistent wind-down time.</li>
  <li>Dim lights and reduce screen stimulation.</li>
  <li>Prepare tomorrow's essentials before bed.</li>
  <li>Choose one calming activity, such as reading, stretching, breathing, or journaling.</li>
  <li>Keep your wake time consistent as often as possible.</li>
</ul>
<p>You do not have to change everything at once. The goal is to create a routine that feels steady enough to repeat.</p>
<h2>What Makes a Sleep Routine Work?</h2>
<p>A sleep routine works because it reduces friction at the end of the day. Instead of asking your brain to switch instantly from work, screens, chores, or stress into sleep, the routine creates a transition. That transition may support more consistent sleep timing and a calmer bedtime environment.</p>
<p>Several factors can influence sleep: light exposure, caffeine, alcohol, stress, activity, meal timing, bedroom temperature, and wake time. A routine does not control all of those perfectly, but it gives you a practical way to improve the parts you can influence.</p>
<p>For a shorter checklist version, read <a href="/sleep-hygiene-checklist">Sleep Hygiene Checklist for Everyday Life</a>.</p>
<h2>The Simple Better Sleep Routine</h2>
<p>Use this as a flexible template. Adjust the timing to fit your schedule.</p>
<table>
  <thead>
    <tr>
      <th>Time</th>
      <th>Habit</th>
      <th>Why it helps</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>60 minutes before bed</td>
      <td>Finish heavy work and decisions</td>
      <td>Reduces mental activation before sleep</td>
    </tr>
    <tr>
      <td>45 minutes before bed</td>
      <td>Lower light and screen intensity</td>
      <td>Creates a calmer evening environment</td>
    </tr>
    <tr>
      <td>30 minutes before bed</td>
      <td>Prepare tomorrow</td>
      <td>Reduces bedtime worry and planning loops</td>
    </tr>
    <tr>
      <td>15 minutes before bed</td>
      <td>Read, stretch, breathe, or journal</td>
      <td>Gives your body a repeatable rest cue</td>
    </tr>
    <tr>
      <td>Bedtime</td>
      <td>Keep the room cool, dark, and quiet</td>
      <td>Supports a sleep-friendly environment</td>
    </tr>
  </tbody>
</table>
<p>If screen habits are your biggest challenge, see <a href="/screen-time-and-sleep-quality">Screen Time and Sleep Quality: What to Know</a>. For more evening ideas, see <a href="/evening-habits-better-rest">Evening Habits for Better Rest</a>.</p>
<h2>A 7-Day Starter Plan</h2>
<p>A new sleep routine is easier when you build it in layers. Try this 7-day plan instead of changing everything at once.</p>
<h3>Day 1: Choose a wake time</h3>
<p>Pick a wake time you can keep most days. A consistent wake time helps anchor the rest of the routine.</p>
<h3>Day 2: Set a wind-down reminder</h3>
<p>Use an alarm or calendar reminder that tells you when to begin closing the day.</p>
<h3>Day 3: Reduce one screen habit</h3>
<p>Choose one specific change: no work email in bed, lower brightness, or stop short-form videos before bedtime.</p>
<h3>Day 4: Prepare tomorrow before bed</h3>
<p>Write down one priority, set out clothes, fill a water bottle, or prepare breakfast basics.</p>
<h3>Day 5: Add one calming activity</h3>
<p>Choose reading, breathing, stretching, journaling, or another quiet activity that feels realistic.</p>
<h3>Day 6: Adjust caffeine timing</h3>
<p>Notice whether afternoon or evening caffeine affects your sleep. If it does, move it earlier gradually.</p>
<h3>Day 7: Review and simplify</h3>
<p>Keep the habits that helped most. Remove anything that made the routine feel too complicated.</p>
<h2>What to Do If Stress Keeps You Awake</h2>
<p>Stress can make bedtime feel like the first quiet moment of the day, which is exactly when worries may get louder. A better routine gives those thoughts a place to go before your head hits the pillow.</p>
<ul>
  <li>Write worries or tasks on paper.</li>
  <li>Separate problem-solving time from bedtime.</li>
  <li>Use a short breathing exercise or light stretch.</li>
  <li>Avoid doing work from bed when possible.</li>
</ul>
<p>For more support, read <a href="/stress-affects-sleep">How Stress Affects Sleep and What You Can Do</a>, <a href="/simple-breathing-exercises">Simple Breathing Exercises for Everyday Stress</a>, and <a href="/journaling-mental-clarity">Journaling for Mental Clarity and Reflection</a>.</p>
<h2>Foods, Drinks, and Timing That Can Affect Sleep</h2>
<p>Food and drink choices do not affect everyone the same way, but some patterns are worth noticing. Caffeine later in the day, heavy late meals, alcohol, and going to bed uncomfortably hungry may all influence sleep for some people.</p>
<p>Try tracking one pattern at a time. For example, move caffeine earlier for a week and see whether falling asleep feels easier. Or choose a lighter evening meal if heavy meals leave you uncomfortable at bedtime.</p>
<p>For a deeper guide, read <a href="/foods-drinks-affect-sleep">Foods and Drinks That Can Affect Sleep Quality</a>.</p>
<h2>What to Do After a Poor Night of Sleep</h2>
<p>A bad night can make you want to overhaul everything the next day. Usually, a calmer approach works better. Try to keep your wake time reasonably consistent, get daylight, avoid overdoing caffeine, and return to the routine the next night.</p>
<p>If you nap, keep it short and avoid napping too late in the day. The goal is to recover without making the next night harder.</p>
<h2>Common Sleep Routine Mistakes</h2>
<ul>
  <li>Trying to change every habit at once.</li>
  <li>Making the routine so long that it becomes stressful.</li>
  <li>Using the bed as a work, scrolling, or planning zone.</li>
  <li>Sleeping much later on weekends and disrupting the weekly rhythm.</li>
  <li>Ignoring persistent symptoms that deserve professional attention.</li>
</ul>
<h2>When to Talk to a Professional</h2>
<p>A routine can support healthy habits, but it is not a substitute for care. Consider speaking with a qualified healthcare professional if you have persistent insomnia symptoms, loud snoring or gasping, excessive daytime sleepiness, sleep problems that affect driving or work, or sleep issues connected to a health condition.</p>
<h2>Better Sleep Routine Checklist</h2>
<ul>
  <li>Keep a consistent wake time as often as possible.</li>
  <li>Set a wind-down reminder.</li>
  <li>Lower evening stimulation.</li>
  <li>Prepare tomorrow before bed.</li>
  <li>Choose one calming activity.</li>
  <li>Make the bedroom cool, dark, and quiet when possible.</li>
  <li>Watch caffeine timing.</li>
  <li>Review your routine weekly and simplify it when needed.</li>
</ul>
<h2>Common Questions</h2>
<h3>How long does it take to build a better sleep routine?</h3>
<p>Many people need a few weeks of consistency before a routine feels natural. Start with one or two habits and build gradually.</p>
<h3>What is the best bedtime routine for adults?</h3>
<p>The best routine is realistic and repeatable. A strong starting point is lowering stimulation, preparing tomorrow, and doing one calming activity before bed.</p>
<h3>Should I stop using my phone before bed?</h3>
<p>You do not have to be perfect, but reducing stimulating phone use near bedtime may help many people wind down more easily.</p>
<h3>Is it better to wake up at the same time every day?</h3>
<p>A consistent wake time can help anchor your sleep schedule. Exact consistency is not always possible, but it is a useful goal.</p>
<h3>What should I do if I cannot fall asleep?</h3>
<p>Keep the environment calm and avoid turning the bed into a place for planning or scrolling. If the problem is frequent, seek professional guidance.</p>
<h3>Can food or caffeine affect sleep?</h3>
<p>Yes, for some people. Caffeine timing, alcohol, heavy late meals, and hunger can all influence sleep quality or timing.</p>
<p>For a shorter routine, read <a href="/better-sleep-routine">How to Build a Better Sleep Routine</a>.</p>
""",
}

BACKLINK_POSTS = [
    "better-sleep-routine",
    "sleep-hygiene-checklist",
    "evening-habits-better-rest",
    "screen-time-and-sleep-quality",
    "stress-affects-sleep",
    "foods-drinks-affect-sleep",
]

BACKLINK_HTML = f"""
{MARKER}
<section>
  <h2>Complete Sleep Routine Guide</h2>
  <p>For a deeper step-by-step plan, read <a href="/{SLUG}">How to Build a Better Sleep Routine: A Complete Beginner Guide</a>.</p>
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
