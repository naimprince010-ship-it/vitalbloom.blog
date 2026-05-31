import json
import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
IMAGE_DIR = Path("/tmp/vitalbloom-fitness-pillar")
TODAY = "2026-05-31"
SLUG = "beginner-home-workout-guide"
MARKER = "<!-- vitalbloom-fitness-pillar-link-v1 -->"

POST = {
    "title": "Beginner Home Workout Guide: A Simple Plan to Build Strength and Consistency",
    "slug": SLUG,
    "category": "Fitness",
    "keyword": "beginner home workout guide",
    "meta_title": "Beginner Home Workout Guide: Simple Starter Plan",
    "meta_description": "Start a beginner home workout routine with simple strength moves, a weekly plan, recovery tips, and safe progression rules.",
    "excerpt": "A beginner-friendly home workout guide with simple strength moves, a weekly starter plan, recovery tips, and safe progression rules.",
    "image": "beginner-home-workout-guide.png",
    "image_alt": "beginner home workout guide with simple strength exercises",
    "sources": [
        {
            "title": "Physical Activity Basics",
            "url": "https://www.cdc.gov/physical-activity-basics/index.html",
            "publisher": "Centers for Disease Control and Prevention",
            "accessedAt": TODAY,
        },
        {
            "title": "Physical Activity Guidelines for Americans",
            "url": "https://health.gov/our-work/nutrition-physical-activity/physical-activity-guidelines",
            "publisher": "U.S. Department of Health and Human Services",
            "accessedAt": TODAY,
        },
        {
            "title": "Strength Training: Get Stronger, Leaner, Healthier",
            "url": "https://www.mayoclinic.org/healthy-lifestyle/fitness/in-depth/strength-training/art-20046670",
            "publisher": "Mayo Clinic",
            "accessedAt": TODAY,
        },
        {
            "title": "Exercise and Physical Fitness",
            "url": "https://medlineplus.gov/exerciseandphysicalfitness.html",
            "publisher": "MedlinePlus",
            "accessedAt": TODAY,
        },
    ],
    "content": """
<p>A beginner home workout does not need a gym, a complicated program, or expensive equipment. The best starting plan is simple enough to repeat: a few strength movements, some walking or easy cardio, gentle mobility, and enough recovery to come back again.</p>
<p>This guide gives you a safe beginner-friendly structure, a weekly starter plan, a 20-minute no-equipment workout, and practical ways to progress. It is for general education. If you have chest pain, dizziness, recent injury, pregnancy-related concerns, a heart condition, uncontrolled blood pressure, or any medical condition that affects exercise, check with a qualified healthcare professional before starting.</p>
<h2>Start Here: The Simple Beginner Formula</h2>
<p>For the first month, aim for consistency instead of intensity:</p>
<ul>
  <li>Strength training: 2 to 3 days per week.</li>
  <li>Walking or easy cardio: 2 to 5 days per week.</li>
  <li>Mobility or stretching: 5 to 10 minutes after workouts or on rest days.</li>
  <li>Recovery: at least one easier day between harder strength sessions.</li>
</ul>
<p>This is enough to build the habit without making exercise feel like a second job.</p>
<h2>What Should a Beginner Home Workout Include?</h2>
<p>A good beginner routine trains basic movement patterns. These patterns help you build general strength for daily life, not just for workouts.</p>
<table>
  <thead>
    <tr>
      <th>Pattern</th>
      <th>Beginner example</th>
      <th>Everyday carryover</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Squat</td>
      <td>Chair squat</td>
      <td>Sitting down and standing up</td>
    </tr>
    <tr>
      <td>Hinge</td>
      <td>Hip hinge or glute bridge</td>
      <td>Picking things up safely</td>
    </tr>
    <tr>
      <td>Push</td>
      <td>Wall push-up or incline push-up</td>
      <td>Pushing doors or objects</td>
    </tr>
    <tr>
      <td>Pull</td>
      <td>Towel row or band row</td>
      <td>Posture and upper-back strength</td>
    </tr>
    <tr>
      <td>Core</td>
      <td>Dead bug or plank variation</td>
      <td>Trunk stability and control</td>
    </tr>
  </tbody>
</table>
<p>For more detail, read <a href="/strength-training-basics">Strength Training Basics for Beginners</a>.</p>
<h2>A 20-Minute Beginner Home Workout</h2>
<p>Use this workout two or three times per week. Move slowly, breathe steadily, and stop if anything feels sharp, painful, or unsafe.</p>
<ol>
  <li><strong>Warm up:</strong> 3 minutes of marching in place, shoulder rolls, and easy bodyweight squats.</li>
  <li><strong>Chair squat:</strong> 2 sets of 8 to 12 reps.</li>
  <li><strong>Wall push-up:</strong> 2 sets of 8 to 12 reps.</li>
  <li><strong>Glute bridge:</strong> 2 sets of 10 to 15 reps.</li>
  <li><strong>Bird dog:</strong> 2 sets of 6 to 10 reps per side.</li>
  <li><strong>Step-back lunge or supported split squat:</strong> 1 to 2 sets of 6 to 10 reps per side.</li>
  <li><strong>Cool down:</strong> 3 minutes of easy walking and light stretching.</li>
</ol>
<p>If this feels too hard, do one set of each exercise. If it feels too easy, slow the movement down before adding more reps.</p>
<h2>Weekly Starter Plan</h2>
<p>This plan balances strength, walking, and recovery:</p>
<ul>
  <li><strong>Monday:</strong> 20-minute home strength workout.</li>
  <li><strong>Tuesday:</strong> 10 to 20 minute walk.</li>
  <li><strong>Wednesday:</strong> Rest or gentle stretching.</li>
  <li><strong>Thursday:</strong> 20-minute home strength workout.</li>
  <li><strong>Friday:</strong> 10 to 20 minute walk.</li>
  <li><strong>Saturday:</strong> Optional easy movement, walk, or mobility.</li>
  <li><strong>Sunday:</strong> Rest and plan the next week.</li>
</ul>
<p>For a walking-focused option, see <a href="/10-minute-walking-routine">10-Minute Walking Routine for Busy Days</a> and <a href="/walking-for-weight-management">Walking for Weight Management</a>.</p>
<h2>How to Progress Safely</h2>
<p>Progress should feel steady, not dramatic. Pick one change at a time:</p>
<ul>
  <li>Add 1 to 2 reps per exercise.</li>
  <li>Add one extra set to one exercise.</li>
  <li>Choose a slightly harder variation.</li>
  <li>Slow down the lowering phase.</li>
  <li>Add light dumbbells or a resistance band if available.</li>
</ul>
<p>A simple rule: finish most workouts feeling like you could have done a little more. That keeps the habit alive.</p>
<h2>Common Beginner Workout Mistakes</h2>
<ul>
  <li><strong>Starting too hard.</strong> Soreness and exhaustion can make consistency harder.</li>
  <li><strong>Skipping warm-ups.</strong> A few minutes of easy movement helps you feel ready.</li>
  <li><strong>Doing random workouts every day.</strong> Repeating simple movements helps you learn and progress.</li>
  <li><strong>Ignoring pain.</strong> Muscle effort is normal; sharp or worsening pain is a signal to stop.</li>
  <li><strong>Forgetting recovery.</strong> Strength improves between workouts, not only during them.</li>
</ul>
<p>For habit-building support, read <a href="/exercise-sustainable-habit">How to Make Exercise a Sustainable Habit</a>.</p>
<h2>Recovery Basics</h2>
<p>Recovery does not need to be complicated. Sleep, food, hydration, and easier days all matter. Beginners often do better with moderate workouts they can repeat than intense workouts that require several days to recover from.</p>
<p>After workouts, eat a balanced meal when it fits your schedule, drink enough fluid, and notice how your body responds. For more, see <a href="/post-workout-recovery-tips">Post-Workout Recovery Tips</a>.</p>
<h2>Mobility and Desk-Worker Adjustments</h2>
<p>If you sit for long hours, your workout can include gentle mobility: shoulder circles, hip flexor stretches, chest openers, and short walking breaks. These do not replace strength training, but they can make your body feel less stiff between sessions.</p>
<p>Try <a href="/stretching-routine-desk-workers">Stretching Routine for Desk Workers</a> if stiffness is your main barrier.</p>
<h2>When to Get Professional Guidance</h2>
<p>Get professional guidance if you have a medical condition, are returning after surgery or injury, feel pain during basic movements, or feel unsure about exercise safety. A physical therapist, qualified trainer, or clinician can adapt exercises to your body and goals.</p>
<h2>Beginner Home Workout Checklist</h2>
<ul>
  <li>Choose two strength days this week.</li>
  <li>Start with one short full-body routine.</li>
  <li>Use easier variations when needed.</li>
  <li>Walk or do easy cardio on separate days.</li>
  <li>Track reps, sets, or how the workout felt.</li>
  <li>Progress only one variable at a time.</li>
  <li>Stop if pain feels sharp, unusual, or worsening.</li>
</ul>
<h2>Common Questions</h2>
<h3>How many days a week should a beginner work out?</h3>
<p>Two to three strength sessions per week is a realistic start for many beginners. You can add walking or easy cardio on other days.</p>
<h3>Can I build strength at home without equipment?</h3>
<p>Yes. Bodyweight exercises can build a foundation. Over time, adding bands, dumbbells, or harder variations can help you keep progressing.</p>
<h3>How long should a beginner workout be?</h3>
<p>Start with 15 to 25 minutes. A shorter workout you repeat is better than a long workout you avoid.</p>
<h3>Should I work out if I am sore?</h3>
<p>Mild soreness can be normal, especially at first. Choose easier movement or rest if soreness changes your form or feels intense.</p>
<h3>Do I need cardio and strength training?</h3>
<p>Both can support health and fitness. Beginners can start with simple strength workouts and walking, then build from there.</p>
<h3>What is the easiest first workout?</h3>
<p>Try chair squats, wall push-ups, glute bridges, bird dogs, and a short walk. Keep the first session easy enough to repeat.</p>
<p>For a shorter plan, read <a href="/beginner-home-workout-plan">Beginner Home Workout Plan</a>.</p>
""",
}

BACKLINK_POSTS = [
    "beginner-home-workout-plan",
    "strength-training-basics",
    "exercise-sustainable-habit",
    "walking-for-weight-management",
    "stretching-routine-desk-workers",
    "post-workout-recovery-tips",
    "10-minute-walking-routine",
]

BACKLINK_HTML = f"""
{MARKER}
<section>
  <h2>Complete Beginner Home Workout Guide</h2>
  <p>For a deeper step-by-step plan, read <a href="/{SLUG}">Beginner Home Workout Guide: A Simple Plan to Build Strength and Consistency</a>.</p>
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
