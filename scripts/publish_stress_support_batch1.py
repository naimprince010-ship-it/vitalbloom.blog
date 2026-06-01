import json
import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
TODAY = "2026-06-01"

COMMON_SOURCES = [
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
]


POSTS = [
    {
        "title": "How to Calm Down When Stress Feels Overwhelming",
        "slug": "calm-down-when-stress-feels-overwhelming",
        "category": "Stress",
        "keyword": "how to calm down when stressed",
        "meta_title": "How to Calm Down When Stress Feels Overwhelming",
        "meta_description": "Learn simple steps to calm down when stress feels overwhelming, including grounding, breathing, reducing input, and choosing a next step.",
        "excerpt": "A practical guide for calming your body and choosing one realistic next step when stress feels too loud.",
        "content": """
<p>Stress can feel overwhelming when your body and thoughts both speed up at the same time. You may know that you need to respond calmly, but the moment feels too loud to sort through. The goal is not to force instant peace. The goal is to lower the intensity enough to choose one safe, useful next step.</p>
<p>This guide gives you a simple sequence you can use when stress feels bigger than the task in front of you. It is for general education, not a substitute for professional care, crisis support, or medical advice.</p>
<h2>Start by Naming the Moment</h2>
<p>A short label can reduce the sense that everything is happening at once. Try saying, "This is stress," or "My body is activated right now." Naming the state does not solve the problem, but it gives you a little distance from it.</p>
<p>Avoid turning the label into judgment. "I am stressed" is more useful than "I am failing." Stress is a body and mind response, not a character flaw.</p>
<h2>Lower the Physical Volume</h2>
<p>When stress spikes, your body may prepare for action. You might notice shallow breathing, tight shoulders, a clenched jaw, a fast heart rate, or restless energy. Start with the body because it is often easier than trying to reason with racing thoughts.</p>
<ul>
  <li>Drop your shoulders away from your ears.</li>
  <li>Unclench your jaw and soften your tongue.</li>
  <li>Open your hands and relax your fingers.</li>
  <li>Put both feet on the floor.</li>
  <li>Take three slow breaths, making the exhale a little longer.</li>
</ul>
<p>These are not magic switches. They are small signals of safety. Repeat the one that feels most doable.</p>
<h2>Reduce Extra Input</h2>
<p>Overwhelm often grows when too many signals compete for attention. Before you solve anything, reduce the input around you.</p>
<ul>
  <li>Close unused tabs.</li>
  <li>Silence non-urgent notifications for 20 minutes.</li>
  <li>Step away from social media or news for a short block.</li>
  <li>Move to a quieter spot if possible.</li>
  <li>Write the problem in one sentence.</li>
</ul>
<p>Writing one sentence helps because it turns a cloud of stress into something you can look at. For example: "I need to answer this email," or "I am worried about tomorrow's appointment."</p>
<h2>Use a Grounding Cue</h2>
<p>Grounding brings attention back to the present moment. Choose one cue instead of trying every technique at once.</p>
<ul>
  <li>Name five things you can see.</li>
  <li>Press your feet into the floor for ten seconds.</li>
  <li>Hold a cool glass of water and notice the temperature.</li>
  <li>Look around the room slowly from left to right.</li>
  <li>Say, "I am here. This is now. One step at a time."</li>
</ul>
<p>If one technique makes you feel more frustrated, choose a simpler one. The best grounding cue is the one you can repeat when life is messy.</p>
<h2>Separate Facts From Predictions</h2>
<p>Stress often mixes facts with predictions. Facts are what you know. Predictions are what your mind thinks might happen. Both can matter, but they should not be treated the same.</p>
<p>Write two columns:</p>
<ul>
  <li>Facts: what is confirmed?</li>
  <li>Predictions: what am I afraid might happen?</li>
</ul>
<p>This helps you respond to the real situation without letting every possible outcome become today's emergency.</p>
<h2>Choose One Next Step</h2>
<p>When stress is high, do not plan the entire month. Choose the next smallest useful step. It should be specific enough that you can start within a few minutes.</p>
<ul>
  <li>Send one clarifying message.</li>
  <li>Make one appointment.</li>
  <li>Drink water and eat something simple.</li>
  <li>Open the document and write the first sentence.</li>
  <li>Ask one person for help.</li>
</ul>
<p>The next step does not need to fix everything. It only needs to move you out of frozen overwhelm.</p>
<h2>When Calming Down Is Not Enough</h2>
<p>If stress is persistent, worsening, or affecting sleep, work, school, relationships, or safety, consider extra support. A healthcare professional, counselor, trusted support person, employee assistance program, student wellness office, or crisis line may be appropriate depending on the situation.</p>
<p>If you or someone else may be in immediate danger, contact local emergency services or a crisis support line right away.</p>
<h2>Related VitalBloom Guides</h2>
<ul>
  <li><a href="/stress-reset-checklist-printable">Stress Reset Checklist Printable</a></li>
  <li><a href="/simple-breathing-exercises">Simple Breathing Exercises for Everyday Stress</a></li>
  <li><a href="/stress-management-guide">Stress Management Guide</a></li>
  <li><a href="/practice-mindfulness-simply">How to Practice Mindfulness Simply</a></li>
</ul>
<p>Disclaimer: This article is for general educational purposes only and is not a substitute for professional medical, mental health, or crisis support.</p>
""",
    },
    {
        "title": "Grounding Techniques for Stress: Simple Ways to Feel Present Again",
        "slug": "grounding-techniques-for-stress",
        "category": "Stress",
        "keyword": "grounding techniques for stress",
        "meta_title": "Grounding Techniques for Stress",
        "meta_description": "Try simple grounding techniques for stress, including sensory cues, breathing anchors, body awareness, and quick workday resets.",
        "excerpt": "Simple grounding techniques that can help you feel more present when stress pulls your attention into worry loops.",
        "content": """
<p>Grounding techniques are small practices that bring attention back to the present moment. They can be helpful when stress pulls your mind into worry, replaying, planning, or imagining worst-case outcomes.</p>
<p>Grounding does not erase real problems, and it does not replace mental health care. Its job is more modest: helping your body and attention settle enough to choose what to do next.</p>
<h2>What Grounding Is For</h2>
<p>Grounding is useful when you feel scattered, tense, frozen, restless, or pulled away from what is happening now. It works best when it is simple and repeatable. You do not need a perfect setting, special equipment, or a long routine.</p>
<h2>The 5-4-3-2-1 Technique</h2>
<p>This is one of the easiest sensory grounding practices to remember.</p>
<ul>
  <li>Name five things you can see.</li>
  <li>Name four things you can feel.</li>
  <li>Name three things you can hear.</li>
  <li>Name two things you can smell.</li>
  <li>Name one thing you can taste.</li>
</ul>
<p>You can say the answers out loud or silently. The point is to gently redirect attention to your environment.</p>
<h2>Feet-on-Floor Grounding</h2>
<p>Put both feet on the floor. Press down lightly for five seconds, then release. Notice the surface under your shoes or feet. Repeat three times.</p>
<p>This works well at a desk, in a classroom, before a meeting, or while waiting for a difficult conversation. It is discreet and does not require closing your eyes.</p>
<h2>Object Grounding</h2>
<p>Choose one object nearby: a pen, mug, key, notebook, or phone case. Notice its weight, texture, edges, temperature, and color. Describe it like you are explaining it to someone who cannot see it.</p>
<p>Object grounding can interrupt spiraling thoughts because it gives the mind a concrete task.</p>
<h2>Breath as an Anchor</h2>
<p>If breathing exercises feel comfortable, use the breath as a short anchor. Try inhaling for a comfortable count, then exhaling a little longer. Do not force deep breathing if it makes you uncomfortable.</p>
<p>A simple version is: inhale gently, exhale slowly, relax your jaw, and repeat three times.</p>
<h2>Movement Grounding</h2>
<p>Some people ground better through movement than stillness. Try one of these:</p>
<ul>
  <li>Walk slowly across the room and notice each step.</li>
  <li>Stretch your hands and wrists.</li>
  <li>Roll your shoulders backward five times.</li>
  <li>Stand up, sit down, and notice the transition.</li>
  <li>Carry a glass of water to another room and return.</li>
</ul>
<p>Movement can help when stress feels restless or trapped in the body.</p>
<h2>Grounding at Work or School</h2>
<p>Grounding does not need to be obvious. Before a meeting, class, exam, or hard message, try this short reset:</p>
<ol>
  <li>Put both feet down.</li>
  <li>Relax your shoulders.</li>
  <li>Look at one fixed point.</li>
  <li>Take one slow exhale.</li>
  <li>Write the next action in one sentence.</li>
</ol>
<h2>When Grounding Does Not Work Right Away</h2>
<p>If grounding does not immediately calm you, that does not mean you failed. Stress may be high, the situation may be serious, or your body may need more time. Repeat one simple cue, change your environment if possible, and consider support if symptoms continue.</p>
<p>Grounding is one tool. Rest, food, hydration, movement, social support, therapy, medical care, and safer boundaries may also matter.</p>
<h2>Build a Personal Grounding Menu</h2>
<p>Write down three grounding cues that feel realistic. Keep one for work or school, one for home, and one for bedtime. A small menu prevents you from having to invent a coping strategy during a stressful moment.</p>
<h2>Related VitalBloom Guides</h2>
<ul>
  <li><a href="/stress-reset-checklist-printable">Stress Reset Checklist Printable</a></li>
  <li><a href="/simple-breathing-exercises">Simple Breathing Exercises for Everyday Stress</a></li>
  <li><a href="/practice-mindfulness-simply">How to Practice Mindfulness Without Overcomplicating It</a></li>
  <li><a href="/calm-down-when-stress-feels-overwhelming">How to Calm Down When Stress Feels Overwhelming</a></li>
</ul>
<p>Disclaimer: This article is for general educational purposes only and is not a substitute for professional medical, mental health, or crisis support.</p>
""",
    },
    {
        "title": "Work Stress Reset: A Practical Routine for Busy Days",
        "slug": "work-stress-reset-routine",
        "category": "Stress",
        "keyword": "work stress reset",
        "meta_title": "Work Stress Reset Routine",
        "meta_description": "Use this work stress reset routine to reduce overload, recover between tasks, set boundaries, and end the day with less mental clutter.",
        "excerpt": "A realistic work stress reset routine for meetings, messages, deadlines, and the end of the workday.",
        "content": """
<p>Work stress often builds through small moments: back-to-back meetings, unclear priorities, difficult messages, skipped lunch, and the feeling that every task is urgent. A work stress reset helps you interrupt that build-up before it turns into a full-day spiral.</p>
<p>This routine is not about pretending work is easy. It is about creating small recovery points so your body and attention are not stuck in alert mode all day.</p>
<h2>Start With a Priority Reset</h2>
<p>When everything feels important, write down the top three tasks. Then choose the one that matters most today. This does not mean the others are unimportant. It means your attention needs a starting point.</p>
<ul>
  <li>What must be done today?</li>
  <li>What can wait until tomorrow?</li>
  <li>What needs clarification before I can act?</li>
  <li>What can be shortened, delegated, or simplified?</li>
</ul>
<h2>Use a Two-Minute Meeting Reset</h2>
<p>After a stressful meeting, do not immediately jump into the next demand if you can avoid it. Take two minutes.</p>
<ol>
  <li>Stand up or shift posture.</li>
  <li>Take three slow breaths.</li>
  <li>Write the next action from the meeting.</li>
  <li>Close tabs or notes you no longer need.</li>
  <li>Drink water before opening the next task.</li>
</ol>
<p>This small pause helps your brain mark one task as complete before another begins.</p>
<h2>Reset Before Sending a Difficult Message</h2>
<p>Stress can make messages sharper than you intend. Before replying to a difficult email or chat, use this sequence:</p>
<ul>
  <li>Read the message once.</li>
  <li>Step away for one minute if your body feels activated.</li>
  <li>Write the goal of your reply in one sentence.</li>
  <li>Remove extra emotion or over-explaining.</li>
  <li>Ask for the next concrete step if the issue is unclear.</li>
</ul>
<h2>Protect a Real Lunch Cue</h2>
<p>Lunch does not need to be perfect, but it should not disappear every day. If you cannot take a full break, protect a smaller cue.</p>
<ul>
  <li>Eat away from the keyboard for the first five minutes.</li>
  <li>Refill water before returning to work.</li>
  <li>Step outside or near daylight briefly.</li>
  <li>Avoid using lunch only for more scrolling.</li>
</ul>
<h2>Reduce Digital Clutter</h2>
<p>Digital clutter can keep the nervous system alert. Try a short reset when your screen feels chaotic.</p>
<ul>
  <li>Close completed tabs.</li>
  <li>Move non-urgent messages out of view.</li>
  <li>Use one document for the current task.</li>
  <li>Turn off notifications during deep work blocks.</li>
  <li>Keep a simple parking lot list for later ideas.</li>
</ul>
<h2>End the Day With a Shutdown Routine</h2>
<p>Work stress often follows you home when there is no clear ending. A shutdown routine gives your mind a stopping point.</p>
<ol>
  <li>Write tomorrow's first task.</li>
  <li>List anything waiting on someone else.</li>
  <li>Close work tabs and apps.</li>
  <li>Clear one small part of your desk.</li>
  <li>Use a transition cue: walk, stretch, music, or changing clothes.</li>
</ol>
<p>If you work from home, the transition cue matters even more. Without a commute, your body may need another signal that work has ended.</p>
<h2>When Work Stress Needs More Than a Reset</h2>
<p>A reset can help with daily overload, but it cannot fix unsafe work conditions, chronic understaffing, harassment, unmanageable workloads, or health symptoms that need care. If stress is affecting your health or safety, consider professional support, HR options, employee assistance resources, or medical guidance.</p>
<h2>Related VitalBloom Guides</h2>
<ul>
  <li><a href="/stress-reset-checklist-printable">Stress Reset Checklist Printable</a></li>
  <li><a href="/remote-worker-wellness-checklist">Remote Worker Wellness Checklist</a></li>
  <li><a href="/healthy-habits-remote-workers">Healthy Habits for Remote Workers</a></li>
  <li><a href="/how-to-avoid-burnout">How to Avoid Burnout With Better Daily Boundaries</a></li>
</ul>
<p>Disclaimer: This article is for general educational purposes only and is not a substitute for professional medical, mental health, legal, or workplace advice.</p>
""",
    },
    {
        "title": "Student Stress Management Checklist for Busy Weeks",
        "slug": "student-stress-management-checklist",
        "category": "Stress",
        "keyword": "student stress management checklist",
        "meta_title": "Student Stress Management Checklist",
        "meta_description": "Use this student stress management checklist to plan study blocks, reduce overwhelm, protect sleep, and ask for support during busy weeks.",
        "excerpt": "A student-friendly stress management checklist for deadlines, exams, assignments, sleep, and support.",
        "content": """
<p>Student stress can build quickly because school pressure rarely comes from one place. Deadlines, exams, money, relationships, work, family expectations, and uncertainty can all stack together. A checklist helps you sort the stack instead of carrying it all at once.</p>
<p>This guide is designed for busy academic weeks. It is practical, flexible, and meant to help you choose the next useful step. It is not a replacement for counseling, medical care, academic advising, or crisis support.</p>
<h2>Step 1: Make a Stress Inventory</h2>
<p>Write down everything that is taking up space in your mind. Do not organize it yet. Include assignments, exams, emails, forms, errands, social stress, health concerns, and anything you keep remembering at inconvenient times.</p>
<p>Then mark each item:</p>
<ul>
  <li>Due soon.</li>
  <li>Important but not urgent.</li>
  <li>Needs information.</li>
  <li>Needs support.</li>
  <li>Can wait.</li>
</ul>
<h2>Step 2: Choose the First Academic Move</h2>
<p>When stress is high, "study" is too vague. Choose a concrete starting action.</p>
<ul>
  <li>Open the assignment instructions.</li>
  <li>Make a rough outline.</li>
  <li>Review one lecture section.</li>
  <li>Write three questions for office hours.</li>
  <li>Set a 25-minute timer and start the smallest task.</li>
</ul>
<p>Starting small is not lazy. It is often how you get unstuck.</p>
<h2>Step 3: Protect Sleep Basics</h2>
<p>Academic stress and sleep problems can feed each other. You may not be able to create a perfect routine during a busy week, but you can protect a few basics.</p>
<ul>
  <li>Choose a realistic stopping point for studying.</li>
  <li>Write tomorrow's first task before bed.</li>
  <li>Move stressful messages away from the last minutes of the night.</li>
  <li>Keep caffeine earlier if it affects your sleep.</li>
  <li>Use a short wind-down cue, even if it is only five minutes.</li>
</ul>
<h2>Step 4: Use Support Earlier</h2>
<p>Students often wait until stress becomes severe before asking for help. Try asking earlier and more specifically.</p>
<ul>
  <li>Email a professor or teaching assistant with one clear question.</li>
  <li>Use tutoring, writing center, advising, or study group options.</li>
  <li>Contact student wellness or counseling resources if stress is affecting daily life.</li>
  <li>Tell a trusted person what kind of support would help.</li>
</ul>
<p>"Can you help me figure out the next step?" is easier to answer than "I am overwhelmed."</p>
<h2>Step 5: Reset Between Study Blocks</h2>
<p>Breaks should help your brain recover. If every break turns into scrolling, you may return more scattered.</p>
<ul>
  <li>Stand up and stretch.</li>
  <li>Refill water.</li>
  <li>Walk for five minutes.</li>
  <li>Eat a simple snack with protein or fiber.</li>
  <li>Look away from screens.</li>
</ul>
<h2>Step 6: Plan for the Next 24 Hours</h2>
<p>During stressful weeks, long-range planning can feel impossible. Plan the next 24 hours instead.</p>
<ol>
  <li>What is the most important deadline?</li>
  <li>What is the first 25-minute task?</li>
  <li>When will I eat?</li>
  <li>When will I stop working tonight?</li>
  <li>Who can I contact if I get stuck?</li>
</ol>
<h2>When Student Stress Needs More Support</h2>
<p>Reach out for support if stress is affecting sleep, eating, concentration, safety, relationships, attendance, or your ability to function. If you have thoughts of self-harm or feel unsafe, contact emergency services or a crisis support line immediately.</p>
<h2>Related VitalBloom Guides</h2>
<ul>
  <li><a href="/stress-reset-checklist-printable">Stress Reset Checklist Printable</a></li>
  <li><a href="/sleep-hygiene-checklist-printable">Sleep Hygiene Checklist Printable</a></li>
  <li><a href="/calm-down-when-stress-feels-overwhelming">How to Calm Down When Stress Feels Overwhelming</a></li>
  <li><a href="/stress-management-guide">Stress Management Guide</a></li>
</ul>
<p>Disclaimer: This article is for general educational purposes only and is not a substitute for professional medical, mental health, academic, or crisis support.</p>
""",
    },
    {
        "title": "How to Build a Daily Stress Relief Routine That Actually Fits",
        "slug": "daily-stress-relief-routine",
        "category": "Stress",
        "keyword": "daily stress relief routine",
        "meta_title": "Daily Stress Relief Routine That Actually Fits",
        "meta_description": "Build a realistic daily stress relief routine with morning check-ins, workday resets, movement, boundaries, and evening recovery cues.",
        "excerpt": "A realistic daily stress relief routine for people who need small repeatable habits instead of complicated wellness plans.",
        "content": """
<p>A daily stress relief routine does not need to be long, expensive, or impressive. In fact, the best routine is usually the one you can repeat on ordinary days. It should help you notice stress earlier, recover in small moments, and end the day with less mental clutter.</p>
<p>This guide focuses on simple habits that fit into real life. It is not medical or mental health advice, and it is not a replacement for professional support when stress is persistent or severe.</p>
<h2>Start With a Morning Check-In</h2>
<p>Before the day speeds up, ask two questions:</p>
<ul>
  <li>What is my stress level from 1 to 10?</li>
  <li>What is one thing that would make today easier?</li>
</ul>
<p>The answer might be a shorter to-do list, a real lunch, a message you need to send, or an earlier bedtime. Keep the check-in short so you will actually do it.</p>
<h2>Choose One Body-Based Habit</h2>
<p>Stress lives in the body as well as the mind. Add one body-based habit to your day.</p>
<ul>
  <li>Morning light near a window or outside.</li>
  <li>A short walk.</li>
  <li>Shoulder and neck stretches.</li>
  <li>Slow breathing for one minute.</li>
  <li>Drinking water before caffeine.</li>
</ul>
<p>Choose the easiest option first. A routine that starts too big is harder to keep.</p>
<h2>Build a Midday Reset</h2>
<p>Midday is where stress routines often fall apart. Instead of waiting until evening, build one small reset into the middle of the day.</p>
<ol>
  <li>Step away from the screen.</li>
  <li>Drink water.</li>
  <li>Move your body for two minutes.</li>
  <li>Ask what still matters today.</li>
  <li>Return to one task, not five.</li>
</ol>
<h2>Use a Boundary Cue</h2>
<p>Stress relief is not only about calming down. Sometimes it is about reducing unnecessary load. A boundary cue helps you notice where the day is becoming too crowded.</p>
<ul>
  <li>What can wait?</li>
  <li>What is not mine to solve?</li>
  <li>What needs a clearer request?</li>
  <li>What can be done at a simpler level?</li>
  <li>What would I tell a friend in this situation?</li>
</ul>
<h2>Create an Evening Recovery Cue</h2>
<p>Evening routines do not have to be perfect. Choose one cue that tells your body the active part of the day is closing.</p>
<ul>
  <li>Write tomorrow's first task.</li>
  <li>Close work tabs.</li>
  <li>Dim bright lights.</li>
  <li>Stretch for five minutes.</li>
  <li>Put your phone away from the bed.</li>
</ul>
<p>If your schedule changes often, keep the order consistent even when the timing changes.</p>
<h2>Make the Routine Smaller When Life Gets Hard</h2>
<p>A useful routine should shrink during difficult weeks. Create a minimum version:</p>
<ul>
  <li>One breath.</li>
  <li>One glass of water.</li>
  <li>One sentence about the next step.</li>
  <li>One message asking for support if needed.</li>
</ul>
<p>This keeps the routine from becoming another source of pressure.</p>
<h2>Track What Helps</h2>
<p>At the end of the week, ask:</p>
<ul>
  <li>Which habit helped most?</li>
  <li>Which habit felt unrealistic?</li>
  <li>When did stress build fastest?</li>
  <li>What should I simplify next week?</li>
</ul>
<p>Tracking should support awareness, not perfection. If you miss a day, restart with the smallest version.</p>
<h2>When to Add More Support</h2>
<p>If stress is persistent, intense, or affecting your health, sleep, work, school, relationships, or safety, consider professional support. Daily habits can help, but they are not meant to carry everything alone.</p>
<h2>Related VitalBloom Guides</h2>
<ul>
  <li><a href="/stress-reset-checklist-printable">Stress Reset Checklist Printable</a></li>
  <li><a href="/grounding-techniques-for-stress">Grounding Techniques for Stress</a></li>
  <li><a href="/simple-breathing-exercises">Simple Breathing Exercises for Everyday Stress</a></li>
  <li><a href="/how-to-avoid-burnout">How to Avoid Burnout With Better Daily Boundaries</a></li>
</ul>
<p>Disclaimer: This article is for general educational purposes only and is not a substitute for professional medical, mental health, or crisis support.</p>
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


def publish(post: dict[str, object]) -> str:
    slug = str(post["slug"])
    category_id = get_or_create_category(str(post["category"]))
    existing_id = find_post_id(slug)
    args = [
        f"--post_title={post['title']}",
        f"--post_name={slug}",
        f"--post_content={str(post['content']).strip()}",
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

    run_wp("post", "meta", "update", post_id, "_yoast_wpseo_title", str(post["meta_title"]))
    run_wp("post", "meta", "update", post_id, "_yoast_wpseo_metadesc", str(post["meta_description"]))
    run_wp("post", "meta", "update", post_id, "_yoast_wpseo_focuskw", str(post["keyword"]))
    run_wp("post", "meta", "update", post_id, "_vitalbloom_sources", json.dumps(COMMON_SOURCES, ensure_ascii=True))
    run_wp("post", "meta", "update", post_id, "_vitalbloom_fact_checked_by", "VitalBloom Editorial Team")
    run_wp("post", "meta", "update", post_id, "_vitalbloom_fact_checked_at", TODAY)
    return f"{action}: {post_id} {slug}"


def main() -> None:
    for post in POSTS:
        print(publish(post))


if __name__ == "__main__":
    main()
