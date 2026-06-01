import json
import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
TODAY = "2026-06-01"


ASSETS = [
    {
        "title": "Sleep Hygiene Checklist Printable",
        "slug": "sleep-hygiene-checklist-printable",
        "category": "Sleep",
        "keyword": "sleep hygiene checklist printable",
        "meta_title": "Sleep Hygiene Checklist Printable",
        "meta_description": "Use this printable-style sleep hygiene checklist to build calmer evenings, healthier sleep cues, and a more restful bedroom.",
        "excerpt": "A practical sleep hygiene checklist you can use as a simple evening reset, bedroom audit, and weekly sleep routine tracker.",
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
<p>Sleep hygiene is the set of habits, timing cues, and environment choices that make rest easier. It does not force sleep, and it does not replace medical care for ongoing sleep problems. But it can help you build a calmer routine around the hours before bed.</p>
<p>Use this printable-style checklist as a simple weekly reset. Choose one or two items at first, then add more after they feel realistic. The goal is not to create a perfect night. The goal is to make your sleep routine easier to repeat.</p>
<h2>Daily Sleep Hygiene Checklist</h2>
<ul>
  <li>Wake up at a reasonably consistent time.</li>
  <li>Get morning light when possible.</li>
  <li>Move your body during the day.</li>
  <li>Keep caffeine earlier if it affects your sleep.</li>
  <li>Eat heavier meals with enough time before bed.</li>
  <li>Reduce stressful screen content at night.</li>
  <li>Start a short wind-down routine.</li>
  <li>Keep the bedroom cool, dark, quiet, and comfortable.</li>
  <li>Write down worries or tomorrow's first task before bed.</li>
  <li>Avoid checking the clock repeatedly if it makes you anxious.</li>
</ul>
<h2>Evening Wind-Down Checklist</h2>
<p>A wind-down routine gives your mind and body a familiar signal that the active part of the day is closing. Keep this routine short enough that it works on normal weeknights.</p>
<ul>
  <li>Dim lights or switch to softer lamps.</li>
  <li>Close work tabs and non-urgent messages.</li>
  <li>Prepare one thing for tomorrow.</li>
  <li>Choose one calming habit: reading, stretching, breathing, journaling, or a warm shower.</li>
  <li>Move the phone away from the bed if scrolling delays sleep.</li>
</ul>
<h2>Bedroom Audit</h2>
<p>Your bedroom does not need to be perfect, but it should reduce obvious friction around rest. Ask these questions once per week:</p>
<ul>
  <li>Is the room too warm, bright, or noisy?</li>
  <li>Is the bed mostly used for sleep and rest?</li>
  <li>Are notifications interrupting the night?</li>
  <li>Is clutter making the room feel stressful?</li>
  <li>Would curtains, earplugs, a fan, or a different charging spot help?</li>
</ul>
<h2>Weekly Sleep Reflection</h2>
<p>At the end of the week, use a short reflection instead of judging every night separately.</p>
<ul>
  <li>Which habit helped most?</li>
  <li>Which habit felt unrealistic?</li>
  <li>What pushed bedtime later?</li>
  <li>What can I simplify next week?</li>
  <li>Do sleep problems need professional support?</li>
</ul>
<h2>How to Use This Checklist</h2>
<p>Choose one daytime habit and one evening habit first. For example, get morning light and start a 20-minute wind-down routine. Practice those for a week before adding anything else.</p>
<p>If the checklist feels overwhelming, shrink it. A five-minute routine can still help: dim the lights, write tomorrow's first task, take a few slow breaths, and move the phone away from the bed.</p>
<h2>Printable Weekly Tracker</h2>
<p>If you want to use this as a weekly tracker, choose five habits and mark them once per day. Keep the tracking simple so it supports awareness instead of becoming another source of pressure.</p>
<ul>
  <li>Morning light.</li>
  <li>Movement during the day.</li>
  <li>Caffeine cutoff time.</li>
  <li>Screen wind-down.</li>
  <li>Bedroom reset.</li>
</ul>
<p>At the end of the week, circle the habit that felt most useful. Keep that one for the next week and add only one new habit if your routine feels stable.</p>
<h2>Troubleshooting Common Sleep Hygiene Problems</h2>
<h3>I follow a routine but still feel wired.</h3>
<p>Look earlier in the day. Late caffeine, intense evening work, stressful conversations, bright light, or a packed schedule may be keeping your body alert. Try moving one stimulating habit earlier rather than adding more bedtime tasks.</p>
<h3>I get sleepy, then wake up again.</h3>
<p>Notice alcohol, late fluids, heavy meals, room temperature, and stress. If waking is frequent or paired with breathing concerns, talk with a healthcare professional.</p>
<h3>I cannot keep the same bedtime.</h3>
<p>Keep the same routine order instead. A consistent sequence can still help even when bedtime changes. A stable wake time may also support rhythm when possible.</p>
<h2>Sleep Hygiene for Busy Households</h2>
<p>Parents, caregivers, shift workers, students, and people with shared spaces may not control every part of the evening. Focus on the small parts you can control: a dimmer light, a written plan for tomorrow, a quieter phone setting, or a short breathing cue. Even partial routines can help create a sense of closure.</p>
<p>If your household schedule is unpredictable, use a flexible checklist instead of a strict clock. The same three steps can happen at different times: reduce stimulation, prepare for tomorrow, and choose one calming cue.</p>
<h2>When to Get Help</h2>
<p>Speak with a healthcare professional if sleep problems are persistent, worsening, or affecting daily life. Also seek guidance if you have loud snoring, breathing pauses, restless legs, severe daytime sleepiness, panic at night, or sleep issues connected to depression, anxiety, trauma, pain, medication, or another health concern.</p>
<h2>Related VitalBloom Guides</h2>
<ul>
  <li><a href="/sleep-hygiene-checklist">Sleep Hygiene Checklist for Everyday Life</a></li>
  <li><a href="/evening-habits-better-rest">Evening Habits for Better Rest</a></li>
  <li><a href="/screen-time-and-sleep-quality">Screen Time and Sleep Quality</a></li>
  <li><a href="/stress-affects-sleep">How Stress Affects Sleep</a></li>
</ul>
<p>Disclaimer: This resource is for general educational purposes only and is not a substitute for professional medical advice, diagnosis, or treatment.</p>
""",
    }
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
    run_wp(
        "post",
        "meta",
        "update",
        post_id,
        "_vitalbloom_sources",
        json.dumps(asset["sources"], ensure_ascii=True),
    )
    run_wp("post", "meta", "update", post_id, "_vitalbloom_fact_checked_by", "VitalBloom Editorial Team")
    run_wp("post", "meta", "update", post_id, "_vitalbloom_fact_checked_at", TODAY)
    return f"{action}: {post_id} {slug}"


def main() -> None:
    for asset in ASSETS:
        print(publish(asset))


if __name__ == "__main__":
    main()
