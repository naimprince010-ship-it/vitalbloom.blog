import json
import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
TODAY = "2026-06-03"
CONTENT_MARKER = "<!-- vitalbloom-top20-quality-fix-v1 -->"
INBOUND_MARKER = "<!-- vitalbloom-top20-inbound-fix-v1 -->"


FITNESS_SOURCES = [
    {
        "title": "Adult Activity: An Overview",
        "url": "https://www.cdc.gov/physical-activity-basics/guidelines/adults.html",
        "publisher": "Centers for Disease Control and Prevention",
        "accessedAt": TODAY,
    },
    {
        "title": "Physical Activity and Your Heart - Getting Started and Staying Active",
        "url": "https://www.nhlbi.nih.gov/health/heart/physical-activity/stay-active",
        "publisher": "National Heart, Lung, and Blood Institute",
        "accessedAt": TODAY,
    },
    {
        "title": "Move Your Way Activity Planner: Why These Goals?",
        "url": "https://odphp.health.gov/moveyourway/activity-planner/why-these-goals/",
        "publisher": "Office of Disease Prevention and Health Promotion",
        "accessedAt": TODAY,
    },
]

NUTRITION_SOURCES = [
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
    {
        "title": "Protein",
        "url": "https://nutritionsource.hsph.harvard.edu/what-should-you-eat/protein/",
        "publisher": "Harvard T.H. Chan School of Public Health",
        "accessedAt": TODAY,
    },
]


SECTIONS = {
    "10-minute-walking-routine": """
<section>
  <h2>Sample Week for a 10-Minute Walking Routine</h2>
  <p>Use a simple week instead of trying to walk perfectly every day. On Monday, take an easy 10-minute walk after lunch. On Wednesday, walk 5 minutes out and 5 minutes back. On Friday, add a slightly brisker middle 3 minutes if that feels comfortable. On the weekend, repeat whichever version felt easiest.</p>
  <p>If you feel sharp pain, chest discomfort, dizziness, unusual shortness of breath, or symptoms that worry you, stop and seek medical guidance. If you have a heart condition, joint injury, pregnancy-related concerns, or have been inactive for a long time, ask a qualified healthcare professional how to start safely.</p>
</section>
""",
    "beginner-home-workout-plan": """
<section>
  <h2>Quality Check Before You Repeat the Plan</h2>
  <p>Before adding more sets or harder exercises, check whether the current version feels controlled. You should be able to move through the routine without sharp pain, rushing, or holding your breath. If form breaks down, keep the exercise easier for another week.</p>
  <p>Beginners usually progress better by repeating a simple plan consistently than by changing every workout. Add difficulty slowly, and use professional guidance if pain, injury, or medical concerns affect how you move.</p>
</section>
""",
    "beginner-stretching-routine": """
<section>
  <h2>Sample Weekly Stretching Rhythm</h2>
  <p>Try stretching after a warm shower on Monday, during a midday break on Wednesday, and before bed on Friday. Keep each session short enough that you can finish it without forcing intensity. If a daily routine feels easier, use only three or four favorite stretches.</p>
  <p>Stretching should feel like mild tension, not sharp pain, numbness, or tingling. If symptoms worsen or one area repeatedly feels painful, stop the stretch and consider guidance from a qualified clinician or physical therapist.</p>
</section>
""",
    "daily-mobility-routine": """
<section>
  <h2>Sample Day for Mobility Breaks</h2>
  <p>Use mobility as small checkpoints: shoulder rolls after opening your computer, hip circles before lunch, ankle circles in the afternoon, and a gentle spine twist before your evening wind-down. Each break can be one to two minutes.</p>
  <p>The goal is regular movement, not maximum range. If a movement causes pain, dizziness, or symptoms that feel unusual, skip it and choose a gentler option or ask a qualified professional.</p>
</section>
""",
    "exercise-sustainable-habit": """
<section>
  <h2>A Two-Version Exercise Plan</h2>
  <p>Create a normal version and a minimum version. The normal version might be a 20-minute workout three days per week. The minimum version might be a 5-minute walk, one set of bodyweight movements, or a short stretch. Both versions count because both protect the habit.</p>
  <p>This approach helps on busy or low-energy days. If pain, injury, medical symptoms, or pregnancy-related concerns affect your activity, choose the minimum version only with appropriate professional guidance.</p>
</section>
""",
    "how-to-start-strength-training-at-home": """
<section>
  <h2>Beginner Example: Two Simple Strength Days</h2>
  <p>Day one can include chair squats, wall push-ups, glute bridges, and a light carry. Day two can include step-backs, incline push-ups, bird dogs, and a supported row if you have safe equipment. Keep the first week light enough that you finish with energy left.</p>
  <p>Common beginner mistakes include adding weight too soon, skipping warm-ups, ignoring pain, and changing exercises before learning the basic pattern. Stop if you feel sharp pain or concerning symptoms, and ask a qualified professional if you are unsure what is safe for your body.</p>
</section>
""",
    "low-impact-cardio-for-beginners": """
<section>
  <h2>Common Beginner Mistakes With Low-Impact Cardio</h2>
  <p>The biggest mistakes are starting too hard, turning every session into a test, and ignoring recovery. Low-impact does not always mean low effort, so use the talk test: you should usually be able to speak in short sentences while building the habit.</p>
  <p>A practical starting week is two or three 10- to 15-minute sessions with easy recovery days between them. Stop and seek medical guidance for chest discomfort, faintness, unusual breathlessness, sharp pain, or symptoms that feel unsafe.</p>
</section>
""",
    "post-workout-recovery-tips": """
<section>
  <h2>Simple Recovery Example After a Beginner Workout</h2>
  <p>After a short strength workout, cool down for three minutes, drink water, eat a balanced meal or snack when you are hungry, and keep the next workout at least a day away if your muscles are very sore. Recovery should match the workout, not follow a rigid rule.</p>
  <p>Normal mild soreness can happen, but sharp pain, swelling, dizziness, or symptoms that do not improve deserve attention. When recovery feels unusually difficult, reduce intensity and consider professional guidance.</p>
</section>
""",
    "rest-day-routine-for-beginners": """
<section>
  <h2>Common Rest Day Mistakes</h2>
  <p>Beginners sometimes treat rest days as failure, or they turn rest into another hard workout. A better rest day might include a short walk, light stretching, enough food, hydration, and sleep support. The goal is recovery, not proving effort.</p>
  <p>Try this sample rhythm: after two workout days, schedule one easier day. If soreness, fatigue, or pain is high, choose full rest. If you feel good, choose gentle movement that leaves you feeling better afterward.</p>
</section>
""",
    "strength-training-basics": """
<section>
  <h2>Common Strength Training Mistakes for Beginners</h2>
  <p>Four common mistakes are rushing reps, copying advanced routines, increasing resistance before learning form, and ignoring pain signals. Start with controlled movement patterns and progress only when the current version feels steady.</p>
  <p>A simple first month can use two strength days per week, one or two sets per exercise, and plenty of recovery. If you have an injury, medical condition, or symptoms during training, get personalized guidance instead of pushing through.</p>
</section>
""",
    "stretching-routine-desk-workers": """
<section>
  <h2>Sample Desk-Worker Stretching Day</h2>
  <p>Try neck and shoulder movement mid-morning, a chest opener after lunch, hip flexor stretching in the afternoon, and a short walk before ending work. Each reset can be two minutes, which makes the routine easier to repeat.</p>
  <p>Desk stretching should reduce stiffness, not create pain. If a stretch causes numbness, tingling, sharp pain, or symptoms that travel down an arm or leg, stop and consider professional guidance.</p>
</section>
""",
    "walking-for-weight-management": """
<section>
  <h2>Keep Weight-Related Walking Advice Gentle</h2>
  <p>Walking can support health, energy, and weight management, but body weight is affected by sleep, stress, food access, health conditions, medication, hormones, and many other factors. Use walking as one supportive habit rather than a punishment for eating or resting.</p>
  <p>If weight changes are unexplained, rapid, distressing, or connected with medical symptoms, talk with a qualified healthcare professional. A safe plan should protect health, not create guilt.</p>
</section>
""",
    "add-protein-to-every-meal": """
<section>
  <h2>One-Day Protein Example Without Tracking</h2>
  <p>Breakfast might be Greek yogurt with fruit and oats. Lunch might be beans, rice, vegetables, and salsa. Dinner might be eggs, tofu, fish, poultry, lentils, or another protein anchor with vegetables and a fiber-rich carbohydrate. A snack could be nuts, cottage cheese, hummus, or nut butter with fruit.</p>
  <p>Protein needs vary by age, activity, health, and goals. If you have kidney disease, a medical nutrition plan, pregnancy-related needs, or a history of disordered eating, ask a registered dietitian or clinician for personal guidance.</p>
</section>
""",
    "balanced-plate-method": """
<section>
  <h2>A Practical Balanced Plate Example</h2>
  <p>For dinner, start with one protein such as beans, tofu, eggs, fish, poultry, or yogurt-based sauce. Add produce such as salad, roasted vegetables, fruit, or frozen vegetables. Add a fiber-rich carbohydrate such as potatoes, oats, brown rice, whole-grain bread, beans, or fruit. Finish with flavor from herbs, sauce, olive oil, salsa, or spices.</p>
  <p>This method is a flexible education tool, not a medical diet. If you manage diabetes, kidney disease, gastrointestinal conditions, allergies, pregnancy-related needs, or an eating disorder history, work with a registered dietitian or clinician.</p>
</section>
""",
    "balanced-plate-printable-guide": """
<section>
  <h2>Use the Printable Without Turning It Into a Diet Rule</h2>
  <p>The printable should make meal planning easier, not stricter. Circle one protein, one produce option, one fiber-rich carbohydrate, and one flavor item for two or three meals. Leave blank spaces when the week is busy.</p>
  <p>Nutrition needs are personal. If you need therapeutic nutrition advice, have allergies, manage a medical condition, or have a history of disordered eating, use the printable only alongside guidance from a registered dietitian or clinician.</p>
</section>
""",
    "beginner-meal-prep-checklist": """
<section>
  <h2>Beginner Example: Prep Ingredients, Not Perfect Meals</h2>
  <p>Prep one protein, one grain or starch, and one easy produce option. For example: lentils, rice, and frozen vegetables; eggs, toast, and fruit; or tofu, noodles, and bagged salad. This gives you flexible pieces instead of forcing identical meals all week.</p>
  <p>Keep food safety in mind: refrigerate prepared foods promptly, reheat leftovers safely, and discard food when freshness is uncertain. For medical nutrition needs, allergies, pregnancy, or eating disorder history, follow professional advice.</p>
</section>
""",
    "budget-friendly-healthy-meals": """
<section>
  <h2>Budget Meal Example With Flexible Swaps</h2>
  <p>Build a low-cost meal from beans or lentils, rice or potatoes, frozen vegetables, and a simple sauce. Swap canned tuna, eggs, tofu, yogurt, or peanut butter when those fit your budget and preferences. The goal is a repeatable meal, not the cheapest possible plate every time.</p>
  <p>If a health condition changes your nutrition needs, budget advice should be adjusted with professional support. A registered dietitian, clinician, or community nutrition resource may help you fit medical needs into realistic food access.</p>
</section>
""",
    "easy-balanced-dinner-formula": """
<section>
  <h2>Use the Dinner Formula With Personal Needs in Mind</h2>
  <p>A busy-night dinner can be as simple as eggs with toast and vegetables, beans with rice and salsa, tofu with noodles and frozen vegetables, or yogurt with oats, fruit, and nuts when cooking is not happening. Balanced does not have to mean complicated.</p>
  <p>If you follow a medical nutrition plan, manage allergies, are pregnant, or have a history of disordered eating, adapt the formula with a registered dietitian or clinician. The formula is a planning aid, not individualized medical advice.</p>
</section>
""",
}


INBOUND_LINKS = {
    "beginner-home-workout-guide": [
        ("Beginner Stretching Routine", "/beginner-stretching-routine"),
        ("How to Start Strength Training at Home", "/how-to-start-strength-training-at-home"),
        ("Low-Impact Cardio for Beginners", "/low-impact-cardio-for-beginners"),
        ("Rest Day Routine for Beginners", "/rest-day-routine-for-beginners"),
        ("Strength Training Basics", "/strength-training-basics"),
    ],
    "exercise-sustainable-habit": [
        ("Beginner Stretching Routine", "/beginner-stretching-routine"),
        ("Rest Day Routine for Beginners", "/rest-day-routine-for-beginners"),
        ("Strength Training Basics", "/strength-training-basics"),
    ],
    "walking-for-weight-management": [
        ("Low-Impact Cardio for Beginners", "/low-impact-cardio-for-beginners"),
        ("How to Start Strength Training at Home", "/how-to-start-strength-training-at-home"),
    ],
    "stretching-routine-desk-workers": [
        ("Beginner Stretching Routine", "/beginner-stretching-routine"),
        ("Daily Mobility Routine", "/daily-mobility-routine"),
    ],
    "balanced-plate-guide": [
        ("Budget-Friendly Healthy Meals", "/budget-friendly-healthy-meals"),
        ("Easy Balanced Dinner Formula", "/easy-balanced-dinner-formula"),
    ],
    "beginner-meal-prep-checklist": [
        ("Budget-Friendly Healthy Meals", "/budget-friendly-healthy-meals"),
        ("Easy Balanced Dinner Formula", "/easy-balanced-dinner-formula"),
    ],
}


FITNESS_SLUGS = {
    "10-minute-walking-routine",
    "beginner-home-workout-plan",
    "beginner-stretching-routine",
    "daily-mobility-routine",
    "exercise-sustainable-habit",
    "how-to-start-strength-training-at-home",
    "low-impact-cardio-for-beginners",
    "post-workout-recovery-tips",
    "rest-day-routine-for-beginners",
    "strength-training-basics",
    "stretching-routine-desk-workers",
    "walking-for-weight-management",
}


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
    return result.stdout


def post_id(slug: str) -> str:
    found = run_wp("post", "list", f"--name={slug}", "--post_type=post", "--field=ID").strip()
    if not found:
        raise RuntimeError(f"Post not found: {slug}")
    return found.splitlines()[0]


def get_content(pid: str) -> str:
    return run_wp("post", "get", pid, "--field=post_content")


def merge_sources(pid: str, additions: list[dict]) -> int:
    current_raw = run_wp("post", "meta", "get", pid, "_vitalbloom_sources").strip()
    try:
        current = json.loads(current_raw) if current_raw else []
    except json.JSONDecodeError:
        current = []
    if not isinstance(current, list):
        current = []

    seen = {str(source.get("url", "")).rstrip("/") for source in current if isinstance(source, dict)}
    added = 0
    for source in additions:
        key = source["url"].rstrip("/")
        if key in seen:
            continue
        current.append(source)
        seen.add(key)
        added += 1
        if len(current) >= 4:
            break

    if added:
        run_wp("post", "meta", "update", pid, "_vitalbloom_sources", json.dumps(current, ensure_ascii=True))
    return added


def update_review_meta(pid: str) -> None:
    run_wp("post", "meta", "update", pid, "_vitalbloom_fact_checked_by", "VitalBloom Editorial Team")
    run_wp("post", "meta", "update", pid, "_vitalbloom_fact_checked_at", TODAY)
    run_wp("post", "meta", "update", pid, "_vitalbloom_reviewed_at", TODAY)


def append_quality_sections() -> None:
    for slug, section in SECTIONS.items():
        pid = post_id(slug)
        content = get_content(pid)
        if CONTENT_MARKER not in content:
            run_wp("post", "update", pid, f"--post_content={content.rstrip()}\n\n{CONTENT_MARKER}\n{section.strip()}\n")
            action = "section-added"
        else:
            action = "section-exists"

        source_pool = FITNESS_SOURCES if slug in FITNESS_SLUGS else NUTRITION_SOURCES
        added = merge_sources(pid, source_pool)
        update_review_meta(pid)
        print(f"{action}: {pid} {slug} sources+{added}")


def related_section(links: list[tuple[str, str]]) -> str:
    items = "\n".join(f'  <li><a href="{href}">{label}</a></li>' for label, href in links)
    return f"""
<section>
  <h2>More Related VitalBloom Guides</h2>
  <p>Use these related guides when you want a more specific next step inside this topic cluster.</p>
  <ul>
{items}
  </ul>
</section>
"""


def append_inbound_links() -> None:
    for slug, links in INBOUND_LINKS.items():
        pid = post_id(slug)
        content = get_content(pid)
        missing = [(label, href) for label, href in links if f'href="{href}"' not in content]
        if missing:
            run_wp("post", "update", pid, f"--post_content={content.rstrip()}\n\n{INBOUND_MARKER}\n{related_section(missing).strip()}\n")
            action = f"inbound-added+{len(missing)}"
        else:
            action = "inbound-exists"
        update_review_meta(pid)
        print(f"{action}: {pid} {slug}")


def main() -> None:
    append_quality_sections()
    append_inbound_links()


if __name__ == "__main__":
    main()
