import json
import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
IMAGE_DIR = Path("/tmp/vitalbloom-journaling-pillar")
TODAY = "2026-05-31"
SLUG = "journaling-for-mental-clarity"
MARKER = "<!-- vitalbloom-journaling-pillar-link-v1 -->"

POST = {
    "title": "Journaling for Mental Clarity: Benefits, Prompts, and How to Start",
    "slug": SLUG,
    "category": "Mindfulness",
    "keyword": "journaling for mental clarity",
    "meta_title": "Journaling for Mental Clarity: Benefits and Prompts",
    "meta_description": "Learn how journaling can support mental clarity with a 5-minute routine, beginner prompts, common mistakes, and evidence-informed tips.",
    "excerpt": "A beginner-friendly guide to journaling for mental clarity, with practical prompts, a 5-minute routine, common mistakes, and credible sources.",
    "image": "journaling-for-mental-clarity.png",
    "image_alt": "journaling for mental clarity benefits prompts and starter routine",
    "sources": [
        {
            "title": "Effects of Expressive Writing on Psychological and Physical Health",
            "url": "https://pubmed.ncbi.nlm.nih.gov/15250814/",
            "publisher": "PubMed",
            "accessedAt": TODAY,
        },
        {
            "title": "Online Positive Affect Journaling in the Improvement of Mental Distress and Well-Being",
            "url": "https://pubmed.ncbi.nlm.nih.gov/30407099/",
            "publisher": "PubMed",
            "accessedAt": TODAY,
        },
        {
            "title": "Emotional Wellness Toolkit",
            "url": "https://www.nih.gov/health-information/emotional-wellness-toolkit",
            "publisher": "National Institutes of Health",
            "accessedAt": TODAY,
        },
        {
            "title": "Relaxation Techniques for Health",
            "url": "https://www.nccih.nih.gov/health/relaxation-techniques-what-you-need-to-know",
            "publisher": "National Center for Complementary and Integrative Health",
            "accessedAt": TODAY,
        },
    ],
    "content": """
<p>Journaling for mental clarity is a simple way to slow down, sort through busy thoughts, and turn vague stress into something you can see more clearly. It does not have to be poetic, long, or perfectly consistent. A useful journal entry can be five messy minutes on paper.</p>
<p>This guide explains how journaling may support reflection, emotional awareness, planning, and daily stress management. It also gives you a 5-minute routine, beginner prompts, and practical mistakes to avoid. It is for general education and is not a replacement for mental health care. If distress feels intense, persistent, or unsafe, contact a qualified professional or local emergency support.</p>
<h2>Start Here: A 5-Minute Journaling Routine</h2>
<p>If you want to try journaling tonight, use this short routine:</p>
<ol>
  <li>Write one sentence that names how you feel right now.</li>
  <li>Write the main thought that keeps repeating in your mind.</li>
  <li>Write one thing you can do next, even if it is small.</li>
  <li>Write one thing you do not need to solve tonight.</li>
  <li>Close with one sentence of support you would say to a friend.</li>
</ol>
<p>The goal is not to fix your whole life in one entry. The goal is to create enough space to think more clearly.</p>
<h2>What Does Journaling for Mental Clarity Mean?</h2>
<p>Mental clarity means being able to notice what is happening inside your mind without being completely pulled around by it. Journaling helps because it moves thoughts from an invisible loop into visible words. Once a thought is written down, it is easier to question, organize, prioritize, or set aside.</p>
<p>For example, the thought "everything is too much" may become a clearer list: one work deadline, one unresolved message, poor sleep, and a messy room. That list still matters, but it is more workable than a cloud of pressure.</p>
<p>Journaling pairs well with other simple mindfulness habits. You can combine it with <a href="/practice-mindfulness-simply">simple mindfulness practice</a>, <a href="/simple-breathing-exercises">breathing exercises</a>, or a quiet <a href="/mindful-morning-routine">mindful morning routine</a>.</p>
<h2>Evidence-Informed Benefits of Journaling</h2>
<p>Research on expressive writing and positive affect journaling suggests that writing about thoughts and experiences may support emotional processing and well-being for some people. The results are not magic, and journaling is not equally helpful for everyone, but it can be a low-cost tool for reflection and self-organization.</p>
<p>Here are practical ways journaling may help:</p>
<ul>
  <li><strong>It names emotions.</strong> Writing helps turn a vague mood into clearer language.</li>
  <li><strong>It reduces mental clutter.</strong> Tasks, worries, and ideas stop competing for attention when they have a place to land.</li>
  <li><strong>It reveals patterns.</strong> Repeated entries may show sleep, stress, relationship, or workload patterns.</li>
  <li><strong>It supports problem solving.</strong> A written problem can be broken into smaller next steps.</li>
  <li><strong>It creates a pause.</strong> Journaling can slow the reaction cycle before a decision or conversation.</li>
</ul>
<p>If stress is affecting sleep, journaling may also help you separate planning time from bedtime. For more context, read <a href="/stress-affects-sleep">How Stress Affects Sleep and What You Can Do</a>.</p>
<h2>Best Journaling Methods for Mental Clarity</h2>
<p>There is no single correct journaling style. Choose the method that fits your mind and your available time.</p>
<table>
  <thead>
    <tr>
      <th>Method</th>
      <th>Best for</th>
      <th>How to do it</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Brain dump</td>
      <td>Overwhelm and racing thoughts</td>
      <td>Write everything on your mind for 5 to 10 minutes without editing.</td>
    </tr>
    <tr>
      <td>Prompt journaling</td>
      <td>Beginners who do not know what to write</td>
      <td>Answer one focused question, such as "What needs my attention today?"</td>
    </tr>
    <tr>
      <td>Reflection journaling</td>
      <td>Learning from the day</td>
      <td>Write what happened, what you felt, and what you learned.</td>
    </tr>
    <tr>
      <td>Decision journal</td>
      <td>Choosing between options</td>
      <td>List the decision, options, assumptions, risks, and next step.</td>
    </tr>
    <tr>
      <td>Gratitude or positive affect journaling</td>
      <td>Noticing supportive moments</td>
      <td>Write a few specific things that felt good, meaningful, or steady.</td>
    </tr>
  </tbody>
</table>
<h2>12 Journaling Prompts for Mental Clarity</h2>
<p>Use one prompt at a time. Short answers are enough.</p>
<ol>
  <li>What thought has been taking up the most space today?</li>
  <li>What am I feeling, and where do I notice it in my body?</li>
  <li>What is one thing I can control right now?</li>
  <li>What is one thing I am trying to control that may not be mine to solve?</li>
  <li>What decision feels unclear, and what information is missing?</li>
  <li>What would make today 10 percent easier?</li>
  <li>What am I avoiding, and what is the smallest next step?</li>
  <li>What helped me feel calmer this week?</li>
  <li>What pattern keeps repeating in my days?</li>
  <li>What boundary would protect my energy?</li>
  <li>What do I need to tell someone honestly and kindly?</li>
  <li>What would I say to a friend who felt this way?</li>
</ol>
<p>For a shorter article on this topic, read <a href="/journaling-mental-clarity">Journaling for Mental Clarity and Reflection</a>.</p>
<h2>How to Build a Journaling Habit</h2>
<p>The easiest journaling habit is attached to something you already do. Try writing after morning coffee, before shutting your laptop, or as part of your evening routine. Keep the notebook or notes app visible so you do not rely on motivation.</p>
<p>Start with a tiny rule: one prompt, five minutes, three times per week. You can always write more, but the minimum should feel easy enough to repeat on a normal day.</p>
<h2>Common Journaling Mistakes</h2>
<ul>
  <li><strong>Trying to sound impressive.</strong> Useful journaling is honest, not polished.</li>
  <li><strong>Only writing when overwhelmed.</strong> Calm entries help you see what supports you.</li>
  <li><strong>Turning journaling into rumination.</strong> If writing makes you spiral, pause and use grounding or professional support.</li>
  <li><strong>Making entries too long.</strong> Short entries are easier to sustain.</li>
  <li><strong>Forgetting next steps.</strong> End with one practical action or one thing to release.</li>
</ul>
<h2>When Journaling May Not Be Enough</h2>
<p>Journaling can support reflection, but it should not carry more weight than it can hold. Consider seeking professional help if you experience persistent anxiety or depression symptoms, panic, trauma symptoms, thoughts of self-harm, major sleep disruption, or distress that interferes with work, school, relationships, or daily functioning.</p>
<p>If journaling brings up difficult memories or makes distress stronger, stop and choose a safer grounding activity. You can return to writing later with support.</p>
<h2>A Simple Weekly Journaling Template</h2>
<p>Use this template once per week to review patterns:</p>
<ul>
  <li>This week felt mostly: ____</li>
  <li>The biggest source of stress was: ____</li>
  <li>One thing that helped was: ____</li>
  <li>One thing I want to simplify is: ____</li>
  <li>One next step for the coming week is: ____</li>
</ul>
<p>You can combine this with <a href="/beginner-meditation-guide">beginner meditation</a> if you want a calmer reflection practice.</p>
<h2>Common Questions</h2>
<h3>Does journaling really help mental clarity?</h3>
<p>It can help many people organize thoughts, name emotions, and notice patterns. It is not a guaranteed treatment, but it is a practical self-reflection tool.</p>
<h3>How long should I journal each day?</h3>
<p>Five minutes is enough to start. Consistency matters more than length.</p>
<h3>Should I journal in the morning or at night?</h3>
<p>Morning journaling can help with planning and focus. Evening journaling can help with reflection and offloading worries. Choose the time you can repeat.</p>
<h3>What should I write when my mind is blank?</h3>
<p>Start with one sentence: "Right now I notice..." or answer one prompt from this guide.</p>
<h3>Can journaling make anxiety worse?</h3>
<p>For some people, certain writing styles can increase rumination. If journaling makes you feel worse, shorten the session, use grounding, or seek professional guidance.</p>
<h3>Is digital journaling okay?</h3>
<p>Yes. Paper can reduce screen distractions, but a notes app is still useful if it helps you write consistently.</p>
""",
}

BACKLINK_POSTS = [
    "journaling-mental-clarity",
    "practice-mindfulness-simply",
    "simple-breathing-exercises",
    "stress-affects-sleep",
    "beginner-meditation-guide",
    "mindful-morning-routine",
]

BACKLINK_HTML = f"""
{MARKER}
<section>
  <h2>Complete Journaling Guide</h2>
  <p>For a deeper step-by-step guide, read <a href="/{SLUG}">Journaling for Mental Clarity: Benefits, Prompts, and How to Start</a>.</p>
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
