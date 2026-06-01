import json
import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
TODAY = "2026-06-01"


ASSETS = [
    {
        "title": "Stress Reset Checklist Printable",
        "slug": "stress-reset-checklist-printable",
        "category": "Stress",
        "keyword": "stress reset checklist printable",
        "meta_title": "Stress Reset Checklist Printable",
        "meta_description": "Use this printable-style stress reset checklist to calm your body, reduce overwhelm, and plan a simple next step.",
        "excerpt": "A practical stress reset checklist for grounding, breathing, body tension, support, and next-step planning.",
        "sources": [
            {
                "title": "Managing Stress",
                "url": "https://www.cdc.gov/mental-health/living-with/index.html",
                "publisher": "Centers for Disease Control and Prevention",
                "accessedAt": TODAY,
            },
            {
                "title": "I'm So Stressed Out! Fact Sheet",
                "url": "https://www.nimh.nih.gov/health/publications/stress/index.shtml",
                "publisher": "National Institute of Mental Health",
                "accessedAt": TODAY,
            },
            {
                "title": "Stress",
                "url": "https://www.nccih.nih.gov/health/stress",
                "publisher": "National Center for Complementary and Integrative Health",
                "accessedAt": TODAY,
            },
        ],
        "content": """
<p>Stress can make your body feel urgent even when the next step is small. Your shoulders tighten, your thoughts speed up, your breathing changes, and ordinary choices can feel harder than they should.</p>
<p>This printable-style stress reset checklist is designed for those moments. It will not remove every source of stress, and it is not a substitute for professional mental health care. But it can help you pause, lower the intensity, and choose one realistic next action.</p>
<h2>Quick Stress Reset Checklist</h2>
<p>Use this short version when you need a reset in five minutes or less.</p>
<ul>
  <li>Name what is happening: "I am feeling stressed right now."</li>
  <li>Unclench your jaw, lower your shoulders, and relax your hands.</li>
  <li>Take three slow breaths with a longer exhale than inhale.</li>
  <li>Notice five things you can see around you.</li>
  <li>Drink water or step away from the screen for one minute.</li>
  <li>Write down the next smallest useful step.</li>
  <li>Decide whether you need support, rest, movement, or information.</li>
</ul>
<h2>Step 1: Check Your Body</h2>
<p>Stress often shows up physically before you can explain it. Start with a body scan so you can respond to the tension instead of arguing with it.</p>
<ul>
  <li>Jaw: unclench and let your tongue rest.</li>
  <li>Shoulders: drop them away from your ears.</li>
  <li>Hands: open your fingers and release your grip.</li>
  <li>Breath: slow the exhale if your breathing feels shallow.</li>
  <li>Feet: feel the floor or press your toes into your shoes.</li>
</ul>
<p>This is not about forcing yourself to relax. It is about giving your nervous system a clear signal that you are paying attention.</p>
<h2>Step 2: Use a Grounding Cue</h2>
<p>Grounding helps when stress pulls your attention into future worries, worst-case stories, or repeated mental loops. Pick one simple cue.</p>
<ul>
  <li>5-4-3-2-1: notice five things you see, four things you feel, three things you hear, two things you smell, and one thing you taste.</li>
  <li>Cold water: rinse your hands or hold a cool glass for a few breaths.</li>
  <li>Room scan: slowly look around and name the objects near you.</li>
  <li>Feet on floor: press both feet down and notice the support under you.</li>
  <li>Anchor phrase: "This is a hard moment. I can take one next step."</li>
</ul>
<h2>Step 3: Reduce the Input</h2>
<p>When stress is high, more information can feel helpful but often adds pressure. Try reducing input before making a decision.</p>
<ul>
  <li>Close extra browser tabs.</li>
  <li>Silence non-urgent notifications for 20 minutes.</li>
  <li>Move away from breaking news or stressful feeds.</li>
  <li>Pause a difficult message before replying.</li>
  <li>Write the problem in one sentence instead of rereading everything.</li>
</ul>
<p>A calmer environment will not solve every problem, but it can make the next action easier to see.</p>
<h2>Step 4: Choose the Right Reset</h2>
<p>Different stress moments need different responses. Choose the reset that matches what is actually happening.</p>
<h3>If your body feels activated</h3>
<ul>
  <li>Walk for two to five minutes.</li>
  <li>Stretch your neck, chest, hips, or hands.</li>
  <li>Take slow breaths with a long exhale.</li>
  <li>Do one small physical task, such as washing a cup or clearing your desk.</li>
</ul>
<h3>If your thoughts are looping</h3>
<ul>
  <li>Write the worry down once.</li>
  <li>Separate facts from predictions.</li>
  <li>Ask, "What do I know for sure?"</li>
  <li>Choose a time to revisit the issue instead of thinking about it all day.</li>
</ul>
<h3>If you feel overloaded</h3>
<ul>
  <li>List every task quickly.</li>
  <li>Circle the one that matters most today.</li>
  <li>Break it into a 10-minute starting step.</li>
  <li>Move the rest to a later list or calendar.</li>
</ul>
<h2>Printable Daily Stress Reset</h2>
<p>Use this as a daily tracker. Keep it simple enough that you can actually repeat it.</p>
<ul>
  <li>Morning check: What is my stress level from 1 to 10?</li>
  <li>Body cue: Where am I holding tension?</li>
  <li>Support cue: Who or what can help today?</li>
  <li>Boundary cue: What can wait?</li>
  <li>Evening check: What helped even a little?</li>
</ul>
<h2>Two-Minute Workday Reset</h2>
<p>This version works between meetings, before a hard email, or after a stressful call.</p>
<ol>
  <li>Put both feet on the floor.</li>
  <li>Relax your jaw and shoulders.</li>
  <li>Take three slow breaths.</li>
  <li>Write the next action in one sentence.</li>
  <li>Open only the tab or tool needed for that action.</li>
</ol>
<h2>Stress Reset for Students</h2>
<p>Students often face stress from deadlines, exams, finances, social pressure, and uncertainty. A reset should make the next study block smaller, not more complicated.</p>
<ul>
  <li>Choose one assignment or topic.</li>
  <li>Set a 20-minute timer.</li>
  <li>Put the phone out of reach if it keeps pulling attention.</li>
  <li>Write one question to ask a teacher, tutor, or classmate.</li>
  <li>Plan a real break after the timer ends.</li>
</ul>
<h2>Stress Reset for Caregivers and Busy Households</h2>
<p>Caregiving stress may not come with a clean break. If you cannot step away for long, use a smaller reset that fits the moment.</p>
<ul>
  <li>Take one slow breath before responding.</li>
  <li>Lower noise or light if possible.</li>
  <li>Use a short phrase: "One thing at a time."</li>
  <li>Ask for a specific kind of help instead of general help.</li>
  <li>Let a non-urgent task wait until later.</li>
</ul>
<h2>What Not to Do During a Stress Spike</h2>
<p>Some common reactions make stress louder. You do not have to judge yourself for them, but it helps to notice the pattern.</p>
<ul>
  <li>Do not make every big decision at the peak of stress if it can wait.</li>
  <li>Do not answer a difficult message while your body is still activated.</li>
  <li>Do not use the checklist as another perfection test.</li>
  <li>Do not ignore repeated stress signals that are affecting your sleep, relationships, work, or health.</li>
</ul>
<h2>When to Get More Support</h2>
<p>Consider reaching out to a healthcare professional, counselor, crisis line, or trusted support person if stress feels unmanageable, lasts for weeks, disrupts daily life, or comes with panic, depression, thoughts of self-harm, substance use concerns, unsafe situations, or symptoms that worry you.</p>
<p>If you or someone else may be in immediate danger, contact local emergency services or a crisis support line right away.</p>
<h2>How to Share This Checklist</h2>
<p>This checklist can be used as a student wellness handout, employee wellness resource, coaching prompt, therapy homework companion, or personal desk reset. It is designed to be practical, printable, and easy to revisit.</p>
<p>For outreach or resource pages, it pairs well with stress management, mental health, work-life balance, sleep, burnout prevention, and student support content.</p>
<h2>Related VitalBloom Guides</h2>
<ul>
  <li><a href="/simple-breathing-exercises">Simple Breathing Exercises for Everyday Stress</a></li>
  <li><a href="/stress-affects-sleep">How Stress Affects Sleep</a></li>
  <li><a href="/mindfulness-for-beginners">Mindfulness for Beginners</a></li>
  <li><a href="/healthy-habits-remote-workers">Healthy Habits for Remote Workers</a></li>
  <li><a href="/sleep-hygiene-checklist-printable">Sleep Hygiene Checklist Printable</a></li>
</ul>
<p>Disclaimer: This resource is for general educational purposes only and is not a substitute for professional medical, mental health, or crisis support.</p>
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
    run_wp("post", "meta", "update", post_id, "_vitalbloom_sources", json.dumps(asset["sources"], ensure_ascii=True))
    run_wp("post", "meta", "update", post_id, "_vitalbloom_fact_checked_by", "VitalBloom Editorial Team")
    run_wp("post", "meta", "update", post_id, "_vitalbloom_fact_checked_at", TODAY)
    return f"{action}: {post_id} {slug}"


def main() -> None:
    for asset in ASSETS:
        print(publish(asset))


if __name__ == "__main__":
    main()
