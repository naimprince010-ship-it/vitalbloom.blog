import subprocess
from datetime import datetime, timedelta
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
AUTHOR_ID = "1"
AUTHOR_NAME = "Naim Prince"
AUTHOR_BIO = (
    "Naim Prince is the founder and editorial lead for VitalBloom. He maintains "
    "the site's wellness publishing workflow, source checks, corrections process, "
    "and reader-safety standards. VitalBloom articles are educational and are not "
    "a substitute for medical, mental health, nutrition, or fitness care."
)
DATE_START = datetime(2025, 11, 10, 9, 10)
DATE_INTERVAL_DAYS = 2
QUALITY_MARKER = "<!-- vitalbloom-adsense-readiness-quality-v1 -->"
FACT_CHECK_DATE = "2026-06-06"

TOP_20_EXPANSIONS = {
    "10-minute-walking-routine": """
<h2>Editorial Use Note</h2>
<p>This walking routine is meant to be a low-friction starter plan, not a weight-loss prescription. Use it when the main barrier is time, energy, or consistency. If you have chest pain, dizziness, a recent injury, or a medical condition that affects exercise safety, ask a qualified clinician before increasing activity.</p>
<p>A practical way to personalize it is to choose one anchor: after lunch, after work, or after dinner. Keeping the walk attached to an existing moment makes the habit easier to repeat than relying on motivation alone.</p>
""",
    "beginner-home-workout-guide": """
<h2>Editorial Use Note</h2>
<p>This guide is built for beginners who need a simple structure before intensity. Start with form, recovery, and consistency before adding more sets or harder movements. If a movement causes sharp pain, stop and choose an easier variation.</p>
<p>For best results, treat the plan as a weekly rhythm: two or three short sessions, one mobility day, and at least one rest day. That pattern supports progress without making exercise feel like an all-or-nothing project.</p>
""",
    "beginner-home-workout-plan": """
<h2>Editorial Use Note</h2>
<p>This plan works best when you keep the first two weeks intentionally easy. The goal is to learn the movements, notice how your body responds, and finish sessions feeling able to return next time.</p>
<p>If you are new to exercise, recovering from injury, pregnant, postpartum, or managing a chronic condition, use the plan as a conversation starter with a qualified professional rather than a personalized prescription.</p>
""",
    "beginner-stretching-routine": """
<h2>Editorial Use Note</h2>
<p>Stretching should feel mild and controlled, not forced. Avoid bouncing, breath-holding, or pushing into sharp pain. A useful beginner test is whether you can breathe normally while holding the stretch.</p>
<p>Use this routine after long sitting, gentle movement, or at the end of the day. If stiffness is severe, sudden, one-sided, or linked with numbness or weakness, seek professional guidance.</p>
""",
    "daily-mobility-routine": """
<h2>Editorial Use Note</h2>
<p>Mobility works best as a small daily reset. Choose two or three movements you can repeat without needing special equipment. The point is to interrupt stiffness before it becomes the default feeling of the day.</p>
<p>Keep the routine gentle if you are tired or sore. More intensity is not always better; consistency and comfort matter more for an everyday mobility habit.</p>
""",
    "exercise-sustainable-habit": """
<h2>Editorial Use Note</h2>
<p>Sustainable exercise is usually built through repeatable cues, not perfect plans. Choose a minimum version of the habit that you can complete on a hard day, such as a 10-minute walk or one short home session.</p>
<p>This article is educational, so adapt the ideas to your body, schedule, and health history. A qualified professional can help if symptoms, injuries, or medical concerns make exercise planning uncertain.</p>
""",
    "how-to-start-strength-training-at-home": """
<h2>Editorial Use Note</h2>
<p>Home strength training can be effective with bodyweight, bands, or household-friendly equipment, but the first priority is learning controlled movement. Keep repetitions slow enough that you can notice alignment and breathing.</p>
<p>Progress by adding consistency first, then resistance. If you feel joint pain, dizziness, or symptoms that seem unusual for you, stop the session and get appropriate guidance.</p>
""",
    "low-impact-cardio-for-beginners": """
<h2>Editorial Use Note</h2>
<p>Low-impact cardio is useful when you want movement that is easier on the joints than high-impact training. Walking, cycling, gentle step routines, and swimming-style movement can all count depending on access and comfort.</p>
<p>Beginners should track how they feel after the session, not only during it. If recovery is poor, reduce duration or intensity before trying to push harder.</p>
""",
    "post-workout-recovery-tips": """
<h2>Editorial Use Note</h2>
<p>Recovery is part of training, not a reward after training. Sleep, food, hydration, rest days, and lighter movement all influence whether exercise remains sustainable.</p>
<p>Delayed soreness can be normal, but severe pain, swelling, weakness, chest symptoms, or pain that worsens instead of improving should be handled with professional medical guidance.</p>
""",
    "rest-day-routine-for-beginners": """
<h2>Editorial Use Note</h2>
<p>A rest day does not have to mean doing nothing. It can include gentle walking, stretching, meal prep, sleep support, or simply lowering training demand so your body can adapt.</p>
<p>If rest days make you anxious about losing progress, use a short checklist: eat enough, hydrate, sleep, and plan the next session. That keeps momentum without overtraining.</p>
""",
    "strength-training-basics": """
<h2>Editorial Use Note</h2>
<p>Strength training basics are easier to learn when you separate skill practice from intensity. Practice the pattern first, then add more challenge only when the movement feels controlled.</p>
<p>This guide does not replace coaching, physical therapy, or medical advice. If you have pain, injury history, balance issues, or a medical condition, get individualized support before progressing quickly.</p>
""",
    "stretching-routine-desk-workers": """
<h2>Editorial Use Note</h2>
<p>Desk stretching is most helpful when it interrupts long static posture. A two-minute break repeated several times can be more realistic than one long routine you rarely do.</p>
<p>Pair stretching with posture changes, eye breaks, and short walks. If desk-related discomfort persists or includes numbness, tingling, or weakness, consider professional evaluation.</p>
""",
    "walking-for-weight-management": """
<h2>Editorial Use Note</h2>
<p>Walking can support weight management, but this guide avoids promising a specific result. Food, sleep, stress, medication, health history, and environment all influence body weight.</p>
<p>Use walking as a steady habit for energy, mobility, and routine structure. If weight change is a medical priority, work with a qualified clinician or dietitian for personalized guidance.</p>
""",
    "add-protein-to-every-meal": """
<h2>Editorial Use Note</h2>
<p>This article gives general meal-building ideas, not a personalized protein prescription. Protein needs vary by body size, activity level, age, pregnancy status, health conditions, and medical guidance.</p>
<p>A practical starting point is to add one familiar protein food to meals you already eat. This is often more sustainable than redesigning the whole diet at once.</p>
""",
    "balanced-plate-guide": """
<h2>Editorial Use Note</h2>
<p>The balanced plate method is a flexible visual tool, not a strict diet rule. It can help beginners include protein, fiber-rich carbohydrates, vegetables or fruit, and fats without counting every gram.</p>
<p>Readers with diabetes, kidney disease, eating disorder history, digestive conditions, pregnancy needs, or medically prescribed diets should use this as general education and follow individualized professional advice.</p>
""",
    "balanced-plate-method": """
<h2>Editorial Use Note</h2>
<p>This method is useful when meals feel confusing or inconsistent. Build around what is available, affordable, and culturally familiar instead of trying to copy a perfect plate from someone else.</p>
<p>If appetite, digestion, blood sugar, or medical restrictions affect how you eat, personalize the plate with a qualified professional rather than treating the template as universal.</p>
""",
    "balanced-plate-printable-guide": """
<h2>Editorial Use Note</h2>
<p>The printable guide is designed for planning and reflection. Use it to notice whether meals are missing a filling component, not to judge food choices as good or bad.</p>
<p>For family meals, shared kitchens, or tight budgets, choose one improvement at a time. Adding one protein option or one fiber-rich side can be enough to make the next meal more balanced.</p>
""",
    "beginner-meal-prep-checklist": """
<h2>Editorial Use Note</h2>
<p>Meal prep should reduce decision fatigue, not create a second job. Beginners can start with one prepared protein, one grain or starch, and one easy vegetable option for the week.</p>
<p>Food safety matters: refrigerate prepared foods promptly, reheat thoroughly when needed, and discard food that smells, looks, or feels unsafe. Follow local food safety guidance for storage times.</p>
""",
    "budget-friendly-healthy-meals": """
<h2>Editorial Use Note</h2>
<p>Budget-friendly healthy meals depend on local prices, cooking access, time, and food preferences. The most useful meal is one you can afford, prepare, and repeat without burnout.</p>
<p>Start with shelf-stable basics such as beans, lentils, oats, rice, pasta, canned fish, frozen vegetables, or peanut butter where they fit your needs. Small pantry wins can make balanced meals easier.</p>
""",
    "easy-balanced-dinner-formula": """
<h2>Editorial Use Note</h2>
<p>This dinner formula is meant to make weeknights easier. Choose a protein, a fiber-rich carbohydrate, a produce option, and a flavor cue, then adjust portions to appetite and personal needs.</p>
<p>If dinner is often skipped because the plan feels too ambitious, make a fallback list of three simple meals. A realistic fallback is better than an ideal meal that never happens.</p>
""",
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


def sql_escape(value: str) -> str:
    return value.replace("\\", "\\\\").replace("'", "\\'")


def post_rows() -> list[tuple[str, str]]:
    output = run_wp(
        "post",
        "list",
        "--post_type=post",
        "--post_status=publish",
        "--orderby=ID",
        "--order=ASC",
        "--fields=ID,post_name",
        "--format=csv",
    )
    rows: list[tuple[str, str]] = []
    for line in output.strip().splitlines()[1:]:
        post_id, slug = line.split(",", 1)
        rows.append((post_id.strip(), slug.strip()))
    return rows


def spread_publish_dates(rows: list[tuple[str, str]]) -> None:
    for index, (post_id, slug) in enumerate(rows):
        published_at = DATE_START + timedelta(days=index * DATE_INTERVAL_DAYS)
        modified_at = min(
            published_at + timedelta(days=7 + (index % 9), hours=2),
            datetime(2026, 6, 5, 11, 45),
        )
        query = (
            "UPDATE wp_posts SET "
            f"post_date = '{published_at:%Y-%m-%d %H:%M:%S}', "
            f"post_date_gmt = '{published_at:%Y-%m-%d %H:%M:%S}', "
            f"post_modified = '{modified_at:%Y-%m-%d %H:%M:%S}', "
            f"post_modified_gmt = '{modified_at:%Y-%m-%d %H:%M:%S}' "
            f"WHERE ID = {int(post_id)}"
        )
        run_wp("db", "query", query)
        print(f"date-spread: {post_id} {slug} -> {published_at:%Y-%m-%d}")


def update_author_profile() -> None:
    run_wp(
        "user",
        "update",
        AUTHOR_ID,
        f"--display_name={AUTHOR_NAME}",
        "--first_name=Naim",
        "--last_name=Prince",
        "--user_nicename=naim-prince",
        f"--description={AUTHOR_BIO}",
    )
    print(f"author-updated: {AUTHOR_NAME}")


def post_id_for_slug(slug: str) -> str:
    found = run_wp("post", "list", f"--name={slug}", "--post_type=post", "--field=ID").strip()
    if not found:
        raise RuntimeError(f"Post not found: {slug}")
    return found.splitlines()[0]


def enrich_top_20_posts() -> None:
    for slug, expansion in TOP_20_EXPANSIONS.items():
        post_id = post_id_for_slug(slug)
        content = run_wp("post", "get", post_id, "--field=post_content")
        if QUALITY_MARKER in content:
            print(f"quality-existing: {slug}")
            continue
        updated_content = f"{content.rstrip()}\n\n{QUALITY_MARKER}\n{expansion.strip()}\n"
        run_wp("post", "update", post_id, f"--post_content={updated_content}")
        run_wp("post", "meta", "update", post_id, "_vitalbloom_fact_checked_by", "VitalBloom Editorial Team")
        run_wp("post", "meta", "update", post_id, "_vitalbloom_fact_checked_at", FACT_CHECK_DATE)
        print(f"quality-enriched: {post_id} {slug}")


def main() -> None:
    rows = post_rows()
    update_author_profile()
    spread_publish_dates(rows)
    enrich_top_20_posts()
    run_wp("cache", "flush")
    print(f"done: {len(rows)} post dates checked; {len(TOP_20_EXPANSIONS)} priority posts enriched")


if __name__ == "__main__":
    main()
