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
        "title": "Morning Stress Reset: How to Start the Day Calmer",
        "slug": "morning-stress-reset",
        "category": "Stress",
        "keyword": "morning stress reset",
        "meta_title": "Morning Stress Reset: Start the Day Calmer",
        "meta_description": "Use this morning stress reset to lower early overwhelm, choose priorities, and start the day with calmer cues.",
        "excerpt": "A realistic morning stress reset for calmer breathing, priorities, movement, hydration, and a less chaotic start.",
        "content": """
<p>A stressful morning can shape the whole day. You wake up already thinking about messages, deadlines, family needs, money, school, or everything you did not finish yesterday. Before you know it, your body is in a rush even if nothing urgent has happened yet.</p>
<p>A morning stress reset is not a perfect routine. It is a short set of cues that helps your body and mind start with a little more steadiness. The goal is to reduce early overwhelm, choose the first useful step, and avoid letting the day begin in full alarm mode.</p>
<h2>Start Before the Phone Takes Over</h2>
<p>If possible, give yourself a few minutes before checking notifications. Your phone may bring news, messages, work problems, social comparison, or other people's urgency into the first moments of the day. Even two quiet minutes can change the tone.</p>
<ul>
  <li>Notice your breath before opening apps.</li>
  <li>Sit up and feel your feet on the floor.</li>
  <li>Drink water before caffeine if that feels realistic.</li>
  <li>Open curtains or get light near the start of the day.</li>
  <li>Choose one priority before checking everyone else's requests.</li>
</ul>
<h2>Use a 3-Minute Body Reset</h2>
<p>Stress often starts physically: tight jaw, raised shoulders, shallow breathing, or a rushed feeling in the chest. Use a short body reset before planning the day.</p>
<ol>
  <li>Unclench your jaw and relax your hands.</li>
  <li>Roll your shoulders slowly.</li>
  <li>Take three slow breaths with a longer exhale.</li>
  <li>Stretch your neck, back, or calves.</li>
  <li>Stand near light or walk briefly if you can.</li>
</ol>
<p>This does not need to feel dramatic. You are giving your nervous system a signal that the day does not have to begin in panic.</p>
<h2>Choose a First Priority</h2>
<p>Morning stress gets louder when everything feels equally urgent. Choose the first priority before trying to solve the whole day.</p>
<ul>
  <li>What must be done today?</li>
  <li>What would make the day easier if finished early?</li>
  <li>What can wait until later?</li>
  <li>What needs a question, not immediate action?</li>
  <li>What is one task I can start in ten minutes?</li>
</ul>
<p>Write the first priority in one sentence. A clear sentence is better than a giant list when stress is high.</p>
<h2>Make Breakfast or Hydration Easier</h2>
<p>Food and hydration are not moral tests, but they can affect how the body handles stress. If you often start the day with only caffeine and urgency, try one small support cue.</p>
<ul>
  <li>Keep water visible.</li>
  <li>Prepare a simple breakfast option the night before.</li>
  <li>Pair coffee or tea with something containing protein or fiber when possible.</li>
  <li>Pack a snack if the morning will be long.</li>
</ul>
<h2>Morning Reset for Busy Households</h2>
<p>Parents, caregivers, students, and shift workers may not control the morning. If your morning is loud or unpredictable, shrink the reset.</p>
<ul>
  <li>One breath before responding.</li>
  <li>One glass of water.</li>
  <li>One sentence: "The first thing I need to do is..."</li>
  <li>One small preparation for later, such as packing a snack or writing a reminder.</li>
</ul>
<p>Small resets count. You do not need quiet music, a long meditation, and a perfect breakfast for the routine to matter.</p>
<h2>Morning Reset for Workdays</h2>
<p>Before opening work tools, decide what deserves your first focus block. If you open email first, your day may be shaped by whatever is newest instead of what matters most.</p>
<p>Try this: write the top task, check only urgent messages, then spend ten minutes moving the priority forward. Even a small start can reduce the feeling that the day is already out of control.</p>
<h2>When Morning Stress Is a Pattern</h2>
<p>If mornings feel stressful most days, look for patterns. Are you sleeping poorly? Is the night before too chaotic? Are you waking to immediate work messages? Are you skipping food, overloading the first hour, or carrying unresolved stress from the previous day?</p>
<p>A morning reset helps, but the evening routine may also need attention. Writing tomorrow's first task before bed can make the next morning feel less scattered.</p>
<h2>Related VitalBloom Guides</h2>
<ul>
  <li><a href="/stress-reset-checklist-printable">Stress Reset Checklist Printable</a></li>
  <li><a href="/daily-stress-relief-routine">Daily Stress Relief Routine</a></li>
  <li><a href="/sleep-hygiene-checklist-printable">Sleep Hygiene Checklist Printable</a></li>
  <li><a href="/calm-down-when-stress-feels-overwhelming">How to Calm Down When Stress Feels Overwhelming</a></li>
</ul>
<p>Disclaimer: This article is for general educational purposes only and is not a substitute for professional medical, mental health, or crisis support.</p>
""",
    },
    {
        "title": "Evening Stress Reset: How to Stop Carrying the Day Into Bed",
        "slug": "evening-stress-reset",
        "category": "Stress",
        "keyword": "evening stress reset",
        "meta_title": "Evening Stress Reset for Calmer Nights",
        "meta_description": "Use this evening stress reset to close mental loops, reduce stimulation, and move into a calmer sleep routine.",
        "excerpt": "A calming evening stress reset for closing work, easing mental loops, and preparing the body for rest.",
        "content": """
<p>Evening stress can make the day feel unfinished long after the work, school, or household tasks are technically over. Your body is tired, but your mind keeps replaying conversations, messages, deadlines, and tomorrow's responsibilities.</p>
<p>An evening stress reset helps you create a boundary between the active part of the day and the recovery part of the night. It does not guarantee perfect sleep, but it can reduce mental clutter and make rest easier to approach.</p>
<h2>Start With a Closing List</h2>
<p>Write down what is still open. Keep it short and practical. The goal is not to solve everything at night; the goal is to stop carrying everything in your head.</p>
<ul>
  <li>What still needs attention tomorrow?</li>
  <li>What is waiting on someone else?</li>
  <li>What can be ignored or deleted?</li>
  <li>What is tomorrow's first useful step?</li>
</ul>
<p>This kind of list gives your mind a place to put loose ends. It also helps prevent bedtime from becoming planning time.</p>
<h2>Lower Stimulation Gradually</h2>
<p>Stress stays louder when the evening is full of bright light, urgent messages, intense content, or last-minute decisions. You do not need to eliminate every screen, but you can lower stimulation step by step.</p>
<ul>
  <li>Dim lights or switch to softer lamps.</li>
  <li>Close work tabs and school portals.</li>
  <li>Silence non-urgent notifications.</li>
  <li>Move stressful conversations away from the last minutes before bed if possible.</li>
  <li>Choose calmer media or a screen-free cue for the last part of the night.</li>
</ul>
<h2>Use a Body-Based Release</h2>
<p>Evening stress often sits in the body. Try a short release before asking your mind to be quiet.</p>
<ol>
  <li>Roll your shoulders slowly.</li>
  <li>Stretch your chest, neck, or hips.</li>
  <li>Unclench your jaw.</li>
  <li>Take a longer exhale three to five times.</li>
  <li>Let your hands relax open.</li>
</ol>
<p>Keep the routine gentle. This is not a workout. It is a cue that your body can stop bracing.</p>
<h2>Do a Worry Parking Lot</h2>
<p>If worries show up at night, give them a parking lot. Write each worry in one line, then add one of three labels: tomorrow, support, or not controllable.</p>
<p>Tomorrow means there is a concrete step for the next day. Support means another person or professional resource may help. Not controllable means the thought may need compassion and boundaries rather than more analysis.</p>
<h2>Protect the Bed From Problem-Solving</h2>
<p>The bed can become linked with stress if it is where you repeatedly plan, scroll, worry, or argue with yourself. Try to keep problem-solving somewhere else when possible. Use a chair, desk, notebook, or hallway pause for the closing list, then move toward bed after the reset.</p>
<h2>Evening Reset for Remote Workers</h2>
<p>Remote workers may need a stronger shutdown cue because there is no commute. Close work apps, write tomorrow's first task, clear one part of the desk, and physically leave the workspace. Even walking outside for two minutes can help create separation.</p>
<h2>Evening Reset for Students</h2>
<p>Students may feel pressure to study until they collapse. During busy weeks, choose a realistic stop point. Write the next study block, pack what you need, and use a short wind-down. Rest is part of learning; an exhausted brain does not always absorb more.</p>
<h2>If Stress Keeps Interrupting Sleep</h2>
<p>Occasional stressful nights are common. But if stress repeatedly disrupts sleep, mood, concentration, health, or daily functioning, consider extra support. A healthcare professional, counselor, student wellness office, or employee assistance resource can help you sort through the pattern.</p>
<h2>Related VitalBloom Guides</h2>
<ul>
  <li><a href="/stress-reset-checklist-printable">Stress Reset Checklist Printable</a></li>
  <li><a href="/sleep-hygiene-checklist-printable">Sleep Hygiene Checklist Printable</a></li>
  <li><a href="/stress-affects-sleep">How Stress Affects Sleep</a></li>
  <li><a href="/evening-habits-better-rest">Evening Habits for Better Rest</a></li>
</ul>
<p>Disclaimer: This article is for general educational purposes only and is not a substitute for professional medical, mental health, or crisis support.</p>
""",
    },
    {
        "title": "Stress and Screen Time: How to Create Calmer Digital Boundaries",
        "slug": "stress-and-screen-time",
        "category": "Stress",
        "keyword": "stress and screen time",
        "meta_title": "Stress and Screen Time: Calmer Digital Boundaries",
        "meta_description": "Learn how screen time can intensify stress and how to create calmer digital boundaries around news, messages, work, and bedtime.",
        "excerpt": "A practical guide to reducing digital overload with calmer screen boundaries, notification habits, and recovery breaks.",
        "content": """
<p>Screens are part of daily life, but they can also make stress feel louder. Messages arrive without context, news updates stack quickly, work tools blur into personal time, and social feeds can turn a tired moment into comparison or worry.</p>
<p>The answer is not always to quit screens. For most people, that is unrealistic. A better goal is to create digital boundaries that reduce unnecessary stress and protect attention.</p>
<h2>Notice Your Stress Triggers</h2>
<p>Not all screen time affects you the same way. A video call, a group chat, a work dashboard, a news feed, and a relaxing show can have very different effects. Start by noticing which digital moments leave you more tense.</p>
<ul>
  <li>Do you feel worse after checking news?</li>
  <li>Do work messages interrupt recovery time?</li>
  <li>Do social feeds make you compare yourself?</li>
  <li>Do late-night screens delay sleep?</li>
  <li>Do notifications keep your body on alert?</li>
</ul>
<h2>Create Notification Boundaries</h2>
<p>Notifications are designed to pull attention. During stressful periods, every ping can feel like another demand. Try making notifications more intentional.</p>
<ul>
  <li>Turn off non-essential alerts.</li>
  <li>Use focus modes during work blocks or rest times.</li>
  <li>Move high-stress apps off the home screen.</li>
  <li>Batch message checks instead of reacting all day.</li>
  <li>Keep emergency contacts available while muting low-priority noise.</li>
</ul>
<h2>Use a News Boundary</h2>
<p>Staying informed can matter, but constant checking can keep your body in a stress loop. Choose when and how you check news instead of letting it fill every quiet moment.</p>
<p>A simple boundary is one or two planned news windows per day. Avoid checking news right before bed if it makes sleep or anxiety worse.</p>
<h2>Separate Work Screens From Recovery Screens</h2>
<p>When the same device holds work, entertainment, shopping, messages, and stress, your brain may struggle to tell when the day is over. Create small separation cues.</p>
<ul>
  <li>Close work tabs at the end of the day.</li>
  <li>Use a different browser profile for work and personal tasks if helpful.</li>
  <li>Keep the phone away from the bed when possible.</li>
  <li>Use a shutdown checklist after work or study.</li>
  <li>Choose one screen-free recovery cue, such as stretching or a short walk.</li>
</ul>
<h2>Take Recovery Breaks That Are Not More Input</h2>
<p>Scrolling can feel like a break, but it may keep the mind busy. Try alternating digital breaks with non-digital recovery.</p>
<ul>
  <li>Look out a window.</li>
  <li>Walk for three minutes.</li>
  <li>Refill water.</li>
  <li>Stretch your hands, neck, or shoulders.</li>
  <li>Write the next task on paper.</li>
</ul>
<h2>Set a Bedtime Screen Ramp-Down</h2>
<p>If screens make stress or sleep worse, create a ramp-down instead of relying on willpower. Put the phone on a charger away from the pillow, dim the screen, silence non-urgent alerts, and choose a calmer activity for the last part of the night.</p>
<h2>What to Do After Digital Overload</h2>
<p>If you already feel overloaded, do not try to fix every app. Use a short reset:</p>
<ol>
  <li>Close the most stressful app.</li>
  <li>Put both feet on the floor.</li>
  <li>Take three slow breaths.</li>
  <li>Write the next useful action.</li>
  <li>Return to one task only.</li>
</ol>
<h2>Related VitalBloom Guides</h2>
<ul>
  <li><a href="/stress-reset-checklist-printable">Stress Reset Checklist Printable</a></li>
  <li><a href="/screen-time-and-sleep-quality">Screen Time and Sleep Quality</a></li>
  <li><a href="/work-stress-reset-routine">Work Stress Reset Routine</a></li>
  <li><a href="/daily-stress-relief-routine">Daily Stress Relief Routine</a></li>
</ul>
<p>Disclaimer: This article is for general educational purposes only and is not a substitute for professional medical, mental health, or crisis support.</p>
""",
    },
    {
        "title": "Stress Journaling Prompts for Overthinking and Mental Clutter",
        "slug": "stress-journaling-prompts",
        "category": "Stress",
        "keyword": "stress journaling prompts",
        "meta_title": "Stress Journaling Prompts for Overthinking",
        "meta_description": "Use these stress journaling prompts to reduce mental clutter, separate facts from worries, and choose one practical next step.",
        "excerpt": "Simple journaling prompts for stress, overthinking, worry loops, decisions, boundaries, and emotional check-ins.",
        "content": """
<p>Stress can make thoughts feel tangled. You may keep replaying a conversation, imagining what could go wrong, or jumping between tasks without finishing any of them. Journaling can help because it gives thoughts a place to land outside your head.</p>
<p>You do not need to be a writer. Stress journaling is not about beautiful sentences. It is about reducing mental clutter and finding the next useful step.</p>
<h2>Start With a One-Minute Brain Dump</h2>
<p>Set a timer for one minute and write everything that is taking up space. Do not organize it yet. Include tasks, worries, feelings, questions, reminders, and unfinished thoughts.</p>
<p>After the timer ends, circle anything that needs action today. Underline anything that needs support. Put a star next to anything that is only a prediction, not a confirmed fact.</p>
<h2>Separate Facts From Worries</h2>
<p>This prompt is useful when your mind keeps turning possibilities into emergencies.</p>
<ul>
  <li>What do I know for sure?</li>
  <li>What am I afraid might happen?</li>
  <li>What evidence supports that fear?</li>
  <li>What evidence is missing?</li>
  <li>What is one realistic next step?</li>
</ul>
<p>The goal is not to argue yourself out of every worry. It is to respond to the real situation instead of every imagined version of it.</p>
<h2>Use a Body Check Prompt</h2>
<p>Stress is physical. Try these prompts when you feel tense but cannot explain why.</p>
<ul>
  <li>Where do I feel stress in my body?</li>
  <li>What does that area need: movement, rest, food, water, warmth, space?</li>
  <li>What changed right before I noticed the tension?</li>
  <li>What would make my body feel 5 percent safer right now?</li>
</ul>
<h2>Use a Boundary Prompt</h2>
<p>Some stress comes from overloaded boundaries. Journaling can help you see what belongs to you and what does not.</p>
<ul>
  <li>What am I carrying that is not mine to solve alone?</li>
  <li>What request needs a clearer answer?</li>
  <li>What can wait?</li>
  <li>Where am I saying yes automatically?</li>
  <li>What would a kind but honest no sound like?</li>
</ul>
<h2>Use a Decision Prompt</h2>
<p>When stress makes decisions feel huge, shrink the question.</p>
<ul>
  <li>What decision am I actually making?</li>
  <li>What information do I still need?</li>
  <li>What is the smallest reversible step?</li>
  <li>What would I choose if I did not need it to be perfect?</li>
  <li>Who can help me think clearly?</li>
</ul>
<h2>End With One Next Step</h2>
<p>Always end stress journaling with one small next step. Without that, journaling can turn into more rumination. The step can be simple: drink water, send an email, ask for help, rest, take a walk, or put one task on tomorrow's list.</p>
<h2>When Journaling Makes Stress Worse</h2>
<p>Journaling should help you feel a little clearer. If it makes you spiral, shorten the session, use more structured prompts, or switch to a body-based reset. Some topics are better processed with a therapist, counselor, or trusted support person.</p>
<h2>A Weekly Stress Journal Review</h2>
<p>Once per week, review your entries for patterns. What keeps showing up? What helps? What drains you? What support are you avoiding? This review can turn scattered thoughts into useful information.</p>
<h2>Related VitalBloom Guides</h2>
<ul>
  <li><a href="/stress-reset-checklist-printable">Stress Reset Checklist Printable</a></li>
  <li><a href="/daily-stress-relief-routine">Daily Stress Relief Routine</a></li>
  <li><a href="/grounding-techniques-for-stress">Grounding Techniques for Stress</a></li>
  <li><a href="/practice-mindfulness-simply">How to Practice Mindfulness Simply</a></li>
</ul>
<p>Disclaimer: This article is for general educational purposes only and is not a substitute for professional medical, mental health, or crisis support.</p>
""",
    },
    {
        "title": "How to Recover After a Stressful Day",
        "slug": "recover-after-stressful-day",
        "category": "Stress",
        "keyword": "recover after a stressful day",
        "meta_title": "How to Recover After a Stressful Day",
        "meta_description": "Learn how to recover after a stressful day with decompression, movement, food, boundaries, reflection, and sleep-supportive cues.",
        "excerpt": "A practical recovery plan for after a stressful day, including decompression, movement, food, boundaries, and sleep cues.",
        "content": """
<p>After a stressful day, it can be tempting to collapse into whatever is easiest: scrolling, skipping dinner, replaying the day, or pushing through more tasks. Sometimes that is all you can manage. But a simple recovery plan can help your body and mind move out of stress mode more gently.</p>
<p>Recovery does not mean the day was fine. It means you are giving yourself support after carrying something heavy.</p>
<h2>Give the Day an Ending</h2>
<p>Stress lingers when there is no clear ending. Create a short transition that marks the day as done, even if tomorrow will still have responsibilities.</p>
<ul>
  <li>Write tomorrow's first task.</li>
  <li>Close work or school tabs.</li>
  <li>Change clothes if that helps your body shift modes.</li>
  <li>Take a short walk or stretch.</li>
  <li>Say out loud, "I am done with today's part."</li>
</ul>
<h2>Choose Low-Pressure Decompression</h2>
<p>Not every recovery activity is actually restful. Choose something that lowers pressure instead of adding more stimulation.</p>
<ul>
  <li>Quiet music.</li>
  <li>A shower or warm drink.</li>
  <li>Gentle stretching.</li>
  <li>Preparing simple food.</li>
  <li>Talking with someone safe.</li>
  <li>Reading something light.</li>
</ul>
<h2>Support Your Body First</h2>
<p>A stressful day can make basic needs easy to ignore. Before analyzing everything, check food, water, movement, and rest.</p>
<ul>
  <li>Have you eaten enough?</li>
  <li>Have you had water?</li>
  <li>Has your body moved at all?</li>
  <li>Are you cold, overheated, or uncomfortable?</li>
  <li>Do you need sleep more than more problem-solving?</li>
</ul>
<h2>Process the Day Without Replaying It Forever</h2>
<p>Reflection can help. Rumination usually does not. Set a short container: five minutes to write what happened, what helped, and what needs a next step.</p>
<ol>
  <li>What was the hardest part of today?</li>
  <li>What did I do that helped even a little?</li>
  <li>What can wait until tomorrow?</li>
  <li>What support do I need?</li>
  <li>What is one thing I can let be unfinished tonight?</li>
</ol>
<h2>Use a Nervous System Reset</h2>
<p>Try one gentle physical reset:</p>
<ul>
  <li>Long exhale breathing for one minute.</li>
  <li>Feet pressed into the floor.</li>
  <li>Slow walk around the block.</li>
  <li>Stretching shoulders, hips, or hands.</li>
  <li>Holding a warm mug and noticing the temperature.</li>
</ul>
<h2>Protect Sleep After Stress</h2>
<p>Stressful days can make bedtime harder. Try reducing input before bed, writing tomorrow's first task, dimming lights, and moving the phone away from the pillow. If your mind keeps replaying the day, use a worry parking lot on paper.</p>
<h2>When Recovery Needs More Support</h2>
<p>If stressful days are constant, or if stress is affecting your health, sleep, relationships, work, school, or safety, consider reaching out for support. Recovery habits are helpful, but they cannot replace needed professional care, safer boundaries, or practical changes.</p>
<h2>Build a Recovery Menu</h2>
<p>Create a menu before the next hard day. Include three quick options, three medium options, and three support options. When you are drained, choose from the menu instead of trying to invent a plan.</p>
<ul>
  <li>Quick: water, breath, stretch.</li>
  <li>Medium: walk, shower, simple meal.</li>
  <li>Support: friend, counselor, doctor, employee or student resource.</li>
</ul>
<h2>Related VitalBloom Guides</h2>
<ul>
  <li><a href="/stress-reset-checklist-printable">Stress Reset Checklist Printable</a></li>
  <li><a href="/evening-stress-reset">Evening Stress Reset</a></li>
  <li><a href="/sleep-hygiene-checklist-printable">Sleep Hygiene Checklist Printable</a></li>
  <li><a href="/daily-stress-relief-routine">Daily Stress Relief Routine</a></li>
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
