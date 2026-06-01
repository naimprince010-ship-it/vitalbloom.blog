import json
import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
TODAY = "2026-06-01"

COMMON_SOURCES = [
    {
        "title": "About Sleep",
        "url": "https://www.cdc.gov/sleep/about/index.html",
        "publisher": "Centers for Disease Control and Prevention",
        "accessedAt": TODAY,
    },
    {
        "title": "Sleep Deprivation and Deficiency",
        "url": "https://www.nhlbi.nih.gov/health/sleep-deprivation",
        "publisher": "National Heart, Lung, and Blood Institute",
        "accessedAt": TODAY,
    },
    {
        "title": "Office Ergonomics and Sleep Health: Healthy Sleep Habits",
        "url": "https://www.nhlbi.nih.gov/health/sleep-deprivation/healthy-sleep-habits",
        "publisher": "National Heart, Lung, and Blood Institute",
        "accessedAt": TODAY,
    },
]


POSTS = [
    {
        "title": "Sleep Debt Recovery Guide: How to Reset After Short Nights",
        "slug": "sleep-debt-recovery-guide",
        "category": "Sleep",
        "keyword": "sleep debt recovery",
        "meta_title": "Sleep Debt Recovery Guide",
        "meta_description": "Learn how to recover from sleep debt with realistic sleep timing, naps, morning light, caffeine boundaries, and calmer evenings.",
        "excerpt": "A practical guide to recovering after short nights without trying to fix everything in one weekend.",
        "content": """
<p>Sleep debt builds when you regularly get less sleep than your body needs. One short night may leave you tired, but repeated short nights can affect mood, attention, energy, and daily functioning. Recovery usually takes patience, not one dramatic catch-up sleep.</p>
<p>This guide explains practical ways to reset after a run of short nights. It is for general education and does not replace medical care for ongoing sleep problems, severe daytime sleepiness, or symptoms that concern you.</p>
<h2>Start With a Realistic Recovery Window</h2>
<p>After several short nights, it is tempting to sleep extremely late on the weekend. Extra sleep can help, but a huge schedule swing may make the next night harder. A steadier recovery plan often works better.</p>
<ul>
  <li>Add 30 to 60 minutes of sleep opportunity for several nights.</li>
  <li>Keep wake time reasonably consistent when possible.</li>
  <li>Use a short nap only if it does not interfere with nighttime sleep.</li>
  <li>Reduce late caffeine and late intense work.</li>
  <li>Protect a calmer wind-down routine.</li>
</ul>
<h2>Use Morning Light as a Reset Cue</h2>
<p>Morning light helps signal daytime to your body. If your schedule has drifted after late nights, getting light near the start of the day can support a more stable rhythm.</p>
<p>You do not need a perfect morning routine. Open curtains, step outside briefly, or sit near a bright window. Pair the light cue with water, movement, or a simple breakfast if that fits your morning.</p>
<h2>Be Careful With Long Naps</h2>
<p>Naps can help when you are very tired, but long or late naps may reduce sleep pressure at night. If you nap, keep it earlier and shorter when possible. Notice how your body responds; some people feel refreshed, while others feel groggy or sleep worse later.</p>
<h2>Lower the Evening Load</h2>
<p>Sleep debt recovery is harder when evenings stay overstimulating. A calmer evening gives your body a better chance to use the sleep opportunity you create.</p>
<ul>
  <li>Write tomorrow's first task before bed.</li>
  <li>Close work or school tabs.</li>
  <li>Dim lights or reduce bright screens.</li>
  <li>Choose a repeatable wind-down cue.</li>
  <li>Keep the bedroom cool, dark, quiet, and comfortable.</li>
</ul>
<h2>Do Not Chase Perfect Sleep</h2>
<p>Trying too hard to sleep can make bedtime feel like a performance. Focus on the conditions you can influence: timing, light, caffeine, stress, routine, and environment. The body often needs a few nights of consistency before you feel the difference.</p>
<h2>When Sleep Debt Needs Professional Support</h2>
<p>Talk with a healthcare professional if sleep problems are persistent, worsening, or affecting daily life. Also seek help if you have loud snoring, breathing pauses, severe daytime sleepiness, restless legs, panic at night, or sleep issues linked to pain, mood, medication, trauma, or another health concern.</p>
<h2>Related VitalBloom Guides</h2>
<ul>
  <li><a href="/sleep-hygiene-checklist-printable">Sleep Hygiene Checklist Printable</a></li>
  <li><a href="/better-sleep-routine-guide">Better Sleep Routine Guide</a></li>
  <li><a href="/evening-habits-better-rest">Evening Habits for Better Rest</a></li>
  <li><a href="/stress-affects-sleep">How Stress Affects Sleep</a></li>
</ul>
<p>Disclaimer: This article is for general educational purposes only and is not a substitute for professional medical advice, diagnosis, or treatment.</p>
""",
    },
    {
        "title": "Why You Wake Up Tired: Common Causes and Simple Fixes",
        "slug": "why-you-wake-up-tired",
        "category": "Sleep",
        "keyword": "why you wake up tired",
        "meta_title": "Why You Wake Up Tired",
        "meta_description": "Learn common reasons you wake up tired, including sleep timing, stress, caffeine, screens, sleep environment, and when to get help.",
        "excerpt": "A practical guide to common reasons for waking up tired and small changes that may support better rest.",
        "content": """
<p>Waking up tired can be frustrating, especially if you went to bed at a reasonable time. Sometimes the issue is not one obvious mistake. It may be a combination of sleep timing, sleep quality, stress, caffeine, light, environment, and health factors.</p>
<p>This guide helps you look for patterns. It is not a diagnosis, and ongoing fatigue deserves professional guidance when it affects daily life.</p>
<h2>Your Sleep Opportunity May Be Too Short</h2>
<p>Time in bed is not always the same as time asleep. If you go to bed at midnight and wake at six, you may not be getting six full hours of sleep. Build in a realistic sleep opportunity that includes time to fall asleep and normal brief awakenings.</p>
<h2>Your Schedule May Be Inconsistent</h2>
<p>Large swings between weekday and weekend sleep can make mornings harder. A consistent wake time, when possible, helps your body predict the rhythm of the day. You do not need perfection, but reducing extreme swings can help.</p>
<h2>Stress May Be Fragmenting Your Sleep</h2>
<p>Stress can make sleep lighter, delay sleep onset, or cause middle-of-the-night waking. If your mind feels active at bedtime, try writing tomorrow's first task, using a short wind-down routine, or practicing a simple grounding cue.</p>
<h2>Caffeine May Be Lasting Longer Than You Think</h2>
<p>Caffeine affects people differently. If you wake tired, experiment with moving caffeine earlier for one to two weeks. Notice whether falling asleep, staying asleep, or morning energy changes.</p>
<h2>Your Bedroom May Be Working Against You</h2>
<p>Light, noise, heat, notifications, and uncomfortable bedding can all affect sleep quality. Do a simple bedroom audit:</p>
<ul>
  <li>Is the room too warm?</li>
  <li>Are notifications interrupting the night?</li>
  <li>Is light leaking into the room?</li>
  <li>Is noise waking you?</li>
  <li>Is the bed mostly used for sleep and rest?</li>
</ul>
<h2>Alcohol or Heavy Meals May Affect Sleep Quality</h2>
<p>Some evening habits make it easier to feel sleepy but harder to sleep well. Notice whether late alcohol, heavy meals, or late fluids are connected with waking tired or waking during the night.</p>
<h2>When Waking Tired Needs Medical Attention</h2>
<p>Seek professional guidance if tiredness is persistent, severe, or paired with loud snoring, breathing pauses, morning headaches, restless legs, depression, anxiety, pain, medication changes, or daytime sleepiness that affects driving, work, or school.</p>
<h2>Related VitalBloom Guides</h2>
<ul>
  <li><a href="/sleep-hygiene-checklist-printable">Sleep Hygiene Checklist Printable</a></li>
  <li><a href="/foods-drinks-affect-sleep">Foods and Drinks That Can Affect Sleep Quality</a></li>
  <li><a href="/screen-time-and-sleep-quality">Screen Time and Sleep Quality</a></li>
  <li><a href="/sleep-debt-recovery-guide">Sleep Debt Recovery Guide</a></li>
</ul>
<p>Disclaimer: This article is for general educational purposes only and is not a substitute for professional medical advice, diagnosis, or treatment.</p>
""",
    },
    {
        "title": "Morning Light and Sleep: A Simple Habit for Better Rhythm",
        "slug": "morning-light-and-sleep",
        "category": "Sleep",
        "keyword": "morning light and sleep",
        "meta_title": "Morning Light and Sleep",
        "meta_description": "Learn how morning light can support sleep rhythm and how to build a simple light cue into your morning routine.",
        "excerpt": "A simple guide to using morning light as a daily cue for steadier sleep and wake rhythm.",
        "content": """
<p>Morning light is one of the simplest cues your body uses to understand daytime. It can support a steadier sleep-wake rhythm, especially when paired with a reasonably consistent wake time and calmer evenings.</p>
<p>You do not need an elaborate routine. The goal is to give your body a clear morning signal that the day has started.</p>
<h2>Why Morning Light Matters</h2>
<p>Your sleep rhythm is influenced by light and darkness. Bright light near the start of the day can help reinforce wakefulness, while dimmer evenings can support the transition toward sleep. Modern schedules, indoor work, and late screens can blur those cues.</p>
<h2>How to Get Morning Light</h2>
<ul>
  <li>Open curtains soon after waking.</li>
  <li>Step outside for a few minutes when possible.</li>
  <li>Sit near a bright window during breakfast.</li>
  <li>Take a short morning walk.</li>
  <li>Pair light with water, movement, or planning your first task.</li>
</ul>
<p>Outdoor light is usually stronger than indoor light, but any realistic improvement is a useful start.</p>
<h2>What If Mornings Are Dark?</h2>
<p>In winter, during early shifts, or in some climates, natural morning light may be limited. Use the brightest safe indoor light available, keep a consistent wake cue, and consider professional guidance before using light therapy devices, especially if you have eye conditions, bipolar disorder, or other health concerns.</p>
<h2>Pair Morning Light With Evening Darkness</h2>
<p>Morning light works best when evenings also support sleep. Reduce bright light and stressful screens near bedtime when possible. A simple evening routine can include dimming lights, closing work tabs, and writing tomorrow's first task.</p>
<h2>A One-Week Morning Light Experiment</h2>
<p>For one week, get light within the first hour after waking. Keep the rest of your routine mostly the same so you can notice any changes. Track bedtime, wake time, energy, and how hard it feels to fall asleep.</p>
<h2>Common Barriers</h2>
<p>If you forget, place a visual cue near your phone, kettle, toothbrush, or coffee. If you work from home, start the day near a window instead of in a dim room. If you commute, notice whether part of the commute can become your light cue.</p>
<h2>Related VitalBloom Guides</h2>
<ul>
  <li><a href="/sleep-hygiene-checklist-printable">Sleep Hygiene Checklist Printable</a></li>
  <li><a href="/mindful-morning-routine">Mindful Morning Routine</a></li>
  <li><a href="/better-sleep-routine-guide">Better Sleep Routine Guide</a></li>
  <li><a href="/morning-stress-reset">Morning Stress Reset</a></li>
</ul>
<p>Disclaimer: This article is for general educational purposes only and is not a substitute for professional medical advice, diagnosis, or treatment.</p>
""",
    },
    {
        "title": "Caffeine and Sleep: How to Find Your Cutoff Time",
        "slug": "caffeine-and-sleep-cutoff",
        "category": "Sleep",
        "keyword": "caffeine and sleep cutoff",
        "meta_title": "Caffeine and Sleep: Find Your Cutoff Time",
        "meta_description": "Learn how caffeine may affect sleep and how to test a realistic caffeine cutoff time without overhauling your whole routine.",
        "excerpt": "A practical guide to finding a caffeine cutoff time that supports better sleep without making mornings miserable.",
        "content": """
<p>Caffeine can be useful. It can help with alertness, focus, and morning energy. But for some people, caffeine too late in the day can make it harder to fall asleep, stay asleep, or wake feeling rested.</p>
<p>There is no perfect cutoff time for everyone. The best approach is to run a simple experiment and notice your own sleep pattern.</p>
<h2>Why Caffeine Timing Matters</h2>
<p>Caffeine can stay active in the body for hours. Some people metabolize it quickly, while others feel the effects much longer. Stress, sleep debt, medications, and sensitivity can also change how caffeine feels.</p>
<h2>Signs Your Cutoff May Be Too Late</h2>
<ul>
  <li>You feel tired but wired at bedtime.</li>
  <li>You fall asleep later than intended.</li>
  <li>You wake during the night after late caffeine.</li>
  <li>You rely on more caffeine the next morning because sleep felt poor.</li>
  <li>Your energy pattern feels like spikes and crashes.</li>
</ul>
<h2>Run a Two-Week Cutoff Experiment</h2>
<p>Choose a cutoff time that feels realistic, such as early afternoon. Keep it for two weeks and track bedtime, wake time, nighttime waking, and morning energy. If sleep improves, keep the cutoff or adjust gradually.</p>
<p>If nothing changes, caffeine may not be the main issue. Look at stress, light, screens, schedule consistency, alcohol, meals, and sleep environment.</p>
<h2>Make the Cutoff Easier</h2>
<ul>
  <li>Move the last caffeinated drink earlier by 30 minutes every few days.</li>
  <li>Switch to a smaller serving instead of quitting suddenly.</li>
  <li>Use decaf, herbal tea, water, or a short walk as an afternoon cue.</li>
  <li>Eat enough earlier in the day so caffeine is not replacing food.</li>
</ul>
<h2>Be Careful With Hidden Caffeine</h2>
<p>Caffeine may appear in coffee, tea, energy drinks, cola, chocolate, supplements, and some medications. Check labels if you are trying to understand your sleep pattern.</p>
<h2>When to Ask for Guidance</h2>
<p>Talk with a healthcare professional if you have ongoing insomnia, anxiety, heart symptoms, pregnancy-related questions, medication concerns, or severe daytime sleepiness. Caffeine changes can help some people, but they are not a full sleep treatment.</p>
<h2>Related VitalBloom Guides</h2>
<ul>
  <li><a href="/sleep-hygiene-checklist-printable">Sleep Hygiene Checklist Printable</a></li>
  <li><a href="/foods-drinks-affect-sleep">Foods and Drinks That Can Affect Sleep Quality</a></li>
  <li><a href="/why-you-wake-up-tired">Why You Wake Up Tired</a></li>
  <li><a href="/better-sleep-routine-guide">Better Sleep Routine Guide</a></li>
</ul>
<p>Disclaimer: This article is for general educational purposes only and is not a substitute for professional medical advice, diagnosis, or treatment.</p>
""",
    },
    {
        "title": "Bedtime Anxiety: How to Quiet Racing Thoughts at Night",
        "slug": "bedtime-anxiety-racing-thoughts",
        "category": "Sleep",
        "keyword": "bedtime anxiety racing thoughts",
        "meta_title": "Bedtime Anxiety and Racing Thoughts",
        "meta_description": "Learn practical ways to handle bedtime anxiety and racing thoughts, including worry lists, wind-down cues, grounding, and support.",
        "excerpt": "A practical guide for bedtime anxiety, racing thoughts, worry lists, grounding, and calmer sleep routines.",
        "content": """
<p>Bedtime anxiety can feel unfair. The day is finally quiet, but your mind gets louder. You may replay conversations, plan tomorrow, worry about health, money, school, work, family, or the fact that you are not asleep yet.</p>
<p>The goal is not to force your mind blank. The goal is to give thoughts a place to go and help your body move toward rest.</p>
<h2>Write a Worry Parking Lot</h2>
<p>Keep a notebook or note nearby before bed. Write each worry in one sentence. Then add one next step or a time to revisit it.</p>
<ul>
  <li>Worry: I might forget the appointment.</li>
  <li>Next step: set a reminder for 9 a.m.</li>
  <li>Worry: I do not know how to start the project.</li>
  <li>Next step: write three questions tomorrow morning.</li>
</ul>
<p>This helps your brain trust that the issue is not being ignored, but it does not need to be solved in bed.</p>
<h2>Use a Body Cue</h2>
<p>Anxiety is not only mental. Try relaxing the jaw, lowering the shoulders, opening the hands, or taking a slow exhale. A body cue can give your nervous system a signal that it is safe to reduce alertness.</p>
<h2>Move Problem-Solving Earlier</h2>
<p>If bedtime is your first quiet moment, your brain may use it for planning. Create a short planning window earlier in the evening. Write tomorrow's first task, check your calendar, and close the list before the final wind-down.</p>
<h2>Reduce Clock Checking</h2>
<p>Checking the time repeatedly can add pressure. If clock watching makes you anxious, turn the clock away or move the phone out of reach. Focus on resting your body rather than monitoring every minute.</p>
<h2>Try a Gentle Grounding Cue</h2>
<p>Name five things you can feel: the pillow, blanket, mattress, air, or your feet. Or silently repeat: "This is a thought, not a task for tonight." Keep the cue simple and repeatable.</p>
<h2>When Bedtime Anxiety Needs Support</h2>
<p>Seek support if anxiety regularly disrupts sleep, affects daily functioning, or comes with panic, depression, trauma symptoms, substance use concerns, or thoughts of self-harm. A healthcare professional or mental health provider can help you find a plan that fits your situation.</p>
<h2>Related VitalBloom Guides</h2>
<ul>
  <li><a href="/sleep-hygiene-checklist-printable">Sleep Hygiene Checklist Printable</a></li>
  <li><a href="/evening-stress-reset">Evening Stress Reset</a></li>
  <li><a href="/stress-journaling-prompts">Stress Journaling Prompts</a></li>
  <li><a href="/grounding-techniques-for-stress">Grounding Techniques for Stress</a></li>
</ul>
<p>Disclaimer: This article is for general educational purposes only and is not a substitute for professional medical, mental health, or crisis support.</p>
""",
    },
]


def run_wp(*args: str) -> str:
    result = subprocess.run(["wp", *args, "--allow-root"], cwd=WP_PATH, text=True, capture_output=True, check=False)
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
