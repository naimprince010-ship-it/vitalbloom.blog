import json
import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
IMAGE_DIR = Path("/tmp/vitalbloom-stress-pillar")
TODAY = "2026-05-31"
SLUG = "stress-management-guide"
MARKER = "<!-- vitalbloom-stress-pillar-link-v1 -->"

POST = {
    "title": "Stress Management Guide: Practical Ways to Reduce Everyday Stress",
    "slug": SLUG,
    "category": "Mindfulness",
    "keyword": "stress management guide",
    "meta_title": "Stress Management Guide: Practical Ways to Cope",
    "meta_description": "Use this stress management guide to calm everyday overwhelm with breathing, movement, journaling, sleep habits, and burnout prevention.",
    "excerpt": "A practical stress management guide with quick calming steps, breathing, journaling, movement, sleep support, burnout prevention, and credible sources.",
    "image": "stress-management-guide.png",
    "image_alt": "stress management guide with calming habits for everyday overwhelm",
    "sources": [
        {
            "title": "I'm So Stressed Out! Fact Sheet",
            "url": "https://www.nimh.nih.gov/health/publications/so-stressed-out-fact-sheet",
            "publisher": "National Institute of Mental Health",
            "accessedAt": TODAY,
        },
        {
            "title": "Coping with Stress",
            "url": "https://www.cdc.gov/mental-health/living-with/index.html",
            "publisher": "Centers for Disease Control and Prevention",
            "accessedAt": TODAY,
        },
        {
            "title": "Stress Effects on the Body",
            "url": "https://www.apa.org/topics/stress/body",
            "publisher": "American Psychological Association",
            "accessedAt": TODAY,
        },
        {
            "title": "Stress Management",
            "url": "https://www.mayoclinic.org/healthy-lifestyle/stress-management/basics/stress-basics/hlv-20049495",
            "publisher": "Mayo Clinic",
            "accessedAt": TODAY,
        },
    ],
    "content": """
<p>Stress management is not about removing every source of pressure from life. It is about noticing stress earlier, lowering the intensity when you can, and building daily habits that help your body and mind recover. A practical stress plan should be simple enough to use on a normal busy day.</p>
<p>This guide covers quick calming steps, breathing, journaling, movement, sleep support, work stress, and burnout prevention. It is for general education and does not replace mental health care. If stress feels overwhelming, persistent, unsafe, or connected to thoughts of self-harm, contact a qualified professional or local emergency support right away.</p>
<h2>Start Here: A 5-Minute Stress Reset</h2>
<p>If you feel overwhelmed right now, try this short reset:</p>
<ol>
  <li>Pause and name what is happening: "I am stressed, and I need a reset."</li>
  <li>Take five slow breaths, making the exhale slightly longer than the inhale.</li>
  <li>Relax your shoulders, jaw, and hands.</li>
  <li>Write down the one next action that matters most.</li>
  <li>Write down one thing you can set aside for later.</li>
</ol>
<p>This will not solve every problem, but it can reduce the mental noise enough to choose the next step more clearly.</p>
<h2>What Is Stress?</h2>
<p>Stress is the body's response to a demand, threat, pressure, or change. Some stress can be useful in short bursts because it helps you focus and respond. But when stress stays high for too long, it can affect mood, sleep, attention, appetite, energy, relationships, and physical tension.</p>
<p>Stress can show up as racing thoughts, irritability, headaches, muscle tightness, stomach discomfort, trouble sleeping, difficulty concentrating, or feeling emotionally drained. The signs vary from person to person, which is why self-awareness matters.</p>
<h2>Stress Management Methods That Actually Fit Real Life</h2>
<table>
  <thead>
    <tr>
      <th>Method</th>
      <th>Best for</th>
      <th>How to start</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Breathing</td>
      <td>Immediate tension and racing thoughts</td>
      <td>Try 2 to 5 minutes of slow breathing.</td>
    </tr>
    <tr>
      <td>Movement</td>
      <td>Restless energy and low mood</td>
      <td>Walk for 10 minutes or do gentle mobility.</td>
    </tr>
    <tr>
      <td>Journaling</td>
      <td>Mental clutter and decision stress</td>
      <td>Write the problem, options, and one next step.</td>
    </tr>
    <tr>
      <td>Sleep routine</td>
      <td>Stress that worsens at night</td>
      <td>Build a predictable wind-down routine.</td>
    </tr>
    <tr>
      <td>Boundaries</td>
      <td>Work overload and burnout risk</td>
      <td>Choose one small limit around time or availability.</td>
    </tr>
  </tbody>
</table>
<p>For direct practice, see <a href="/simple-breathing-exercises">Simple Breathing Exercises for Everyday Stress</a> and <a href="/practice-mindfulness-simply">How to Practice Mindfulness Without Overcomplicating It</a>.</p>
<h2>Use Breathing to Calm the Body First</h2>
<p>When stress is high, it is often easier to calm the body before trying to solve the whole situation. Slow breathing gives you a small anchor. You do not need a perfect technique; just slow down and make the exhale gentle and complete.</p>
<p>Try this pattern: inhale for four counts, exhale for six counts, and repeat for two minutes. If counting feels stressful, simply breathe a little slower than usual.</p>
<h2>Use Journaling to Organize Stress</h2>
<p>Stress often feels bigger when everything stays in your head. Journaling can turn a vague cloud into a clearer list. Write what is bothering you, what is in your control, what is not in your control, and the next realistic step.</p>
<p>For a complete routine, read <a href="/journaling-for-mental-clarity">Journaling for Mental Clarity: Benefits, Prompts, and How to Start</a>.</p>
<h2>Move Your Body Without Turning It Into Pressure</h2>
<p>Movement can help release tension and support mood, but it should not become another source of guilt. A short walk, light stretching, or beginner strength session is enough to start.</p>
<p>Try <a href="/beginner-home-workout-guide">Beginner Home Workout Guide</a> or <a href="/better-breaks-remote-work">Better Breaks for Remote Work</a> if your stress is tied to long sitting or screen-heavy workdays.</p>
<h2>Protect Sleep From Stress Spillover</h2>
<p>Stress often follows people into bed. If your mind gets loud at night, create a short transition between the day and sleep: write down tomorrow's top priority, lower screen stimulation, and choose one calming activity.</p>
<p>For more detail, read <a href="/stress-affects-sleep">How Stress Affects Sleep and What You Can Do</a>.</p>
<h2>Work Stress and Burnout Prevention</h2>
<p>Burnout risk rises when stress is chronic and recovery is too limited. You may notice emotional exhaustion, cynicism, reduced motivation, trouble focusing, or feeling like you cannot fully recover between workdays.</p>
<p>Start with small boundaries. Examples include closing work apps after a certain time, taking a real lunch break, batching messages, writing a shutdown list, or talking with a manager about priorities if workload is not realistic.</p>
<p>For a deeper guide, read <a href="/how-to-avoid-burnout">How to Avoid Burnout</a>.</p>
<h2>Common Stress Management Mistakes</h2>
<ul>
  <li><strong>Waiting until stress is extreme.</strong> Small resets work better when used early.</li>
  <li><strong>Trying to fix everything at once.</strong> Choose one next step.</li>
  <li><strong>Using avoidance as the only strategy.</strong> Rest matters, but unresolved stress may still need action.</li>
  <li><strong>Ignoring sleep.</strong> Poor sleep can make stress feel harder to manage.</li>
  <li><strong>Blaming yourself for needing help.</strong> Support is a strength, not a failure.</li>
</ul>
<h2>When to Seek Professional Help</h2>
<p>Consider professional support if stress is persistent, affects work or relationships, disrupts sleep for weeks, triggers panic symptoms, leads to substance misuse, or comes with symptoms of anxiety, depression, trauma, or thoughts of self-harm. A therapist, clinician, or crisis support service can help you build a safer plan.</p>
<h2>Daily Stress Management Checklist</h2>
<ul>
  <li>Name your stress signal early.</li>
  <li>Use one calming body-based tool.</li>
  <li>Write down the next realistic step.</li>
  <li>Move for a few minutes.</li>
  <li>Protect one part of your evening wind-down.</li>
  <li>Set one small boundary around work or screen time.</li>
  <li>Ask for support when stress is too much to carry alone.</li>
</ul>
<h2>Common Questions</h2>
<h3>What is the fastest way to reduce stress?</h3>
<p>A short pause, slow breathing, and naming one next step can help reduce immediate overwhelm. Long-term stress usually needs repeated habits and support.</p>
<h3>Can stress affect sleep?</h3>
<p>Yes. Stress can make it harder to fall asleep or stay asleep. A predictable wind-down routine and writing down worries before bed may help.</p>
<h3>Is journaling good for stress?</h3>
<p>Journaling can help organize thoughts and identify next steps. If journaling makes you spiral, stop and use grounding or professional support.</p>
<h3>How do I manage work stress?</h3>
<p>Clarify priorities, take real breaks, reduce unnecessary context switching, and set one small boundary around availability or workload.</p>
<h3>What is the difference between stress and burnout?</h3>
<p>Stress can be temporary pressure. Burnout is often linked to chronic workplace stress and may include exhaustion, cynicism, and reduced effectiveness.</p>
<h3>When is stress serious?</h3>
<p>Stress is serious when it feels unmanageable, persists for weeks, affects daily life, or comes with panic, depression symptoms, substance misuse, or thoughts of self-harm.</p>
""",
}

BACKLINK_POSTS = [
    "how-to-avoid-burnout",
    "stress-affects-sleep",
    "simple-breathing-exercises",
    "practice-mindfulness-simply",
    "journaling-for-mental-clarity",
    "better-breaks-remote-work",
    "beginner-home-workout-guide",
]

BACKLINK_HTML = f"""
{MARKER}
<section>
  <h2>Complete Stress Management Guide</h2>
  <p>For a deeper step-by-step plan, read <a href="/{SLUG}">Stress Management Guide: Practical Ways to Reduce Everyday Stress</a>.</p>
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
