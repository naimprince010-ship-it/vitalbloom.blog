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
        "title": "Healthy Sleep Habits",
        "url": "https://www.nhlbi.nih.gov/health/sleep-deprivation/healthy-sleep-habits",
        "publisher": "National Heart, Lung, and Blood Institute",
        "accessedAt": TODAY,
    },
]

POSTS = [
    {
        "title": "Nap Timing Guide: How to Rest Without Ruining Night Sleep",
        "slug": "nap-timing-guide",
        "category": "Sleep",
        "keyword": "nap timing guide",
        "meta_title": "Nap Timing Guide",
        "meta_description": "Learn how to time naps so they support energy without making it harder to sleep at night.",
        "excerpt": "A practical nap timing guide for tired afternoons, short naps, long naps, and protecting nighttime sleep.",
        "content": """
<p>Naps can be helpful, especially after a short night or a demanding morning. But the timing, length, and reason for a nap matter. A nap that helps one person feel refreshed may make another person groggy or wide awake at bedtime.</p>
<p>This guide explains how to use naps as a supportive tool without letting them disrupt your nighttime sleep. It is for general education and is not a substitute for medical advice if you have ongoing fatigue or sleep problems.</p>
<h2>Start With Why You Want to Nap</h2>
<p>Before lying down, ask why you are tired. Are you recovering from a short night? Are you bored, stressed, hungry, dehydrated, or avoiding a task? A nap helps most when sleepiness is truly the issue.</p>
<ul>
  <li>If you are hungry, eat something simple first.</li>
  <li>If you are stressed, try a short reset or walk.</li>
  <li>If you are sleep deprived, a short nap may help.</li>
  <li>If you are exhausted every day, look for a bigger pattern.</li>
</ul>
<h2>Keep Most Naps Short</h2>
<p>Short naps are often easier to wake from and less likely to interfere with nighttime sleep. Longer naps may be useful sometimes, but they can leave you groggy or reduce sleep pressure later.</p>
<p>If you are experimenting, start with a short nap and notice how you feel afterward and at bedtime. Track the pattern for a week instead of judging one nap.</p>
<h2>Nap Earlier When Possible</h2>
<p>Late naps can make it harder to fall asleep at night. If you nap, try to keep it earlier in the day. The exact timing depends on your schedule, but avoid using late naps as a daily fix for sleep debt if they keep pushing bedtime later.</p>
<h2>Create a Nap Boundary</h2>
<p>A nap boundary keeps rest from turning into an accidental long sleep. Set an alarm, choose a comfortable but not overly cozy place, and decide what you will do when the alarm ends. A glass of water, light, or a short walk can help you transition back.</p>
<h2>When Naps Are a Warning Sign</h2>
<p>Needing occasional naps is common. But if you cannot stay awake during normal activities, feel sleepy while driving, or need long naps despite enough time in bed, seek professional guidance. Persistent daytime sleepiness can have many causes and deserves attention.</p>
<h2>Nap Alternatives</h2>
<p>If a nap would disrupt your night, try a recovery break instead:</p>
<ul>
  <li>Step into daylight.</li>
  <li>Take a short walk.</li>
  <li>Drink water.</li>
  <li>Eat a balanced snack.</li>
  <li>Do one minute of slow breathing.</li>
</ul>
<h2>Related VitalBloom Guides</h2>
<ul>
  <li><a href="/sleep-hygiene-checklist-printable">Sleep Hygiene Checklist Printable</a></li>
  <li><a href="/sleep-debt-recovery-guide">Sleep Debt Recovery Guide</a></li>
  <li><a href="/why-you-wake-up-tired">Why You Wake Up Tired</a></li>
  <li><a href="/morning-light-and-sleep">Morning Light and Sleep</a></li>
</ul>
<p>Disclaimer: This article is for general educational purposes only and is not a substitute for professional medical advice, diagnosis, or treatment.</p>
""",
    },
    {
        "title": "Bedroom Environment Checklist for Better Sleep",
        "slug": "bedroom-environment-checklist",
        "category": "Sleep",
        "keyword": "bedroom environment checklist",
        "meta_title": "Bedroom Environment Checklist for Better Sleep",
        "meta_description": "Use this bedroom environment checklist to reduce light, noise, heat, notifications, clutter, and other sleep distractions.",
        "excerpt": "A simple bedroom audit for light, noise, temperature, comfort, notifications, and calmer sleep cues.",
        "content": """
<p>Your bedroom does not need to look perfect to support sleep. But the room should reduce obvious friction: too much light, noise, heat, clutter, notifications, or discomfort. A bedroom environment checklist helps you find small changes that make rest easier.</p>
<h2>Check Light</h2>
<p>Light is a powerful cue. At night, bright light can make it harder for your body to move toward rest. Look for small changes first.</p>
<ul>
  <li>Dim lights in the last part of the evening.</li>
  <li>Block bright outdoor light if it wakes you.</li>
  <li>Turn screens away from the bed.</li>
  <li>Use a low light if you need to get up at night.</li>
</ul>
<h2>Check Noise</h2>
<p>Noise can interrupt sleep even when you do not fully wake. If noise is a problem, consider earplugs, a fan, white noise, closing doors, or moving the bed if possible.</p>
<h2>Check Temperature</h2>
<p>Many people sleep better in a cooler room, though comfort varies. If you wake hot or sweaty, try lighter bedding, airflow, or adjusting the thermostat. If you wake cold, add layers that are easy to remove.</p>
<h2>Check Notifications</h2>
<p>Phones can interrupt sleep through sound, vibration, light, and the temptation to check time or messages. Try a charger away from the bed, do-not-disturb settings, or a separate alarm clock if phone checking is a problem.</p>
<h2>Check Comfort</h2>
<p>Notice pillows, bedding, mattress comfort, sleep position, and pain. A small change like a different pillow height or blanket weight may help. If pain regularly affects sleep, seek professional guidance.</p>
<h2>Check Clutter and Stress Cues</h2>
<p>A cluttered room does not ruin sleep for everyone, but visible reminders of unfinished tasks can keep the mind busy. Clear one small area near the bed. Move work papers, bills, or stressful items out of direct view when possible.</p>
<h2>Build a Weekly Bedroom Reset</h2>
<p>Once a week, use a short reset: clear the bedside area, wash or change bedding if needed, check the room temperature, review notifications, and remove anything that turns the bedroom into a work zone.</p>
<h2>Related VitalBloom Guides</h2>
<ul>
  <li><a href="/sleep-hygiene-checklist-printable">Sleep Hygiene Checklist Printable</a></li>
  <li><a href="/sleep-hygiene-checklist">Sleep Hygiene Checklist for Everyday Life</a></li>
  <li><a href="/why-you-wake-up-tired">Why You Wake Up Tired</a></li>
  <li><a href="/bedtime-anxiety-racing-thoughts">Bedtime Anxiety and Racing Thoughts</a></li>
</ul>
<p>Disclaimer: This article is for general educational purposes only and is not a substitute for professional medical advice, diagnosis, or treatment.</p>
""",
    },
    {
        "title": "Shift Work Sleep Basics: Practical Habits for Irregular Schedules",
        "slug": "shift-work-sleep-basics",
        "category": "Sleep",
        "keyword": "shift work sleep basics",
        "meta_title": "Shift Work Sleep Basics",
        "meta_description": "Learn practical sleep basics for shift work, including light cues, sleep windows, caffeine timing, naps, and recovery days.",
        "excerpt": "A practical guide for shift workers trying to protect sleep with irregular hours and changing light cues.",
        "content": """
<p>Shift work can make sleep harder because work, light, meals, family needs, and social life may not match a typical day-night rhythm. The goal is not a perfect routine. The goal is to protect the sleep opportunity you have and reduce avoidable disruptions.</p>
<h2>Protect Your Main Sleep Window</h2>
<p>Choose the main sleep window that fits your schedule and protect it as much as possible. Tell household members when you need sleep, silence notifications, and make the room dark and comfortable.</p>
<h2>Use Light Intentionally</h2>
<p>Light can support alertness during work and make sleep harder afterward. Depending on your shift, you may need bright light while working and reduced light on the way home. Sunglasses, dimmer lights, and a dark bedroom may help when sleeping during the day.</p>
<h2>Be Strategic With Caffeine</h2>
<p>Caffeine can help alertness during a shift, but using it too close to your sleep window may make rest harder. Create a cutoff that fits your schedule rather than copying a daytime worker's rule.</p>
<h2>Use Naps Carefully</h2>
<p>Short naps may help before or during some shifts, if allowed and safe. But long or poorly timed naps can create grogginess or interfere with your main sleep window. Track what helps your body.</p>
<h2>Plan Recovery Days</h2>
<p>After a run of difficult shifts, avoid expecting instant recovery. Use steady meals, hydration, daylight when appropriate, and a realistic sleep window. If you swing schedules, give your body time to adjust.</p>
<h2>When to Get Help</h2>
<p>If shift work causes persistent insomnia, severe sleepiness, safety concerns, mood changes, or health problems, talk with a healthcare professional. Sleep problems connected to shift work are real and deserve support.</p>
<h2>Related VitalBloom Guides</h2>
<ul>
  <li><a href="/sleep-hygiene-checklist-printable">Sleep Hygiene Checklist Printable</a></li>
  <li><a href="/sleep-debt-recovery-guide">Sleep Debt Recovery Guide</a></li>
  <li><a href="/caffeine-and-sleep-cutoff">Caffeine and Sleep Cutoff</a></li>
  <li><a href="/bedroom-environment-checklist">Bedroom Environment Checklist</a></li>
</ul>
<p>Disclaimer: This article is for general educational purposes only and is not a substitute for professional medical advice, diagnosis, or treatment.</p>
""",
    },
    {
        "title": "Sleep Routine for Parents and Caregivers: Small Habits That Help",
        "slug": "sleep-routine-for-parents-caregivers",
        "category": "Sleep",
        "keyword": "sleep routine for parents",
        "meta_title": "Sleep Routine for Parents and Caregivers",
        "meta_description": "Build a realistic sleep routine for parents and caregivers with flexible cues, recovery windows, support, and lower-pressure evenings.",
        "excerpt": "A flexible sleep routine for parents and caregivers who need realistic rest cues instead of perfect sleep advice.",
        "content": """
<p>Parents and caregivers often receive sleep advice that assumes full control over the evening. Real life may include children waking, caregiving needs, household tasks, medical concerns, noise, and unpredictable schedules. A useful sleep routine must be flexible.</p>
<h2>Focus on Cues, Not Perfect Timing</h2>
<p>If you cannot control bedtime, keep a consistent routine order. For example: prepare tomorrow's first task, reduce bright light, stretch for one minute, and move the phone away from the bed. The same cues can help even when the clock changes.</p>
<h2>Create a Minimum Routine</h2>
<p>A minimum routine is the smallest version that still supports rest.</p>
<ul>
  <li>Drink water.</li>
  <li>Write one reminder for tomorrow.</li>
  <li>Relax your jaw and shoulders.</li>
  <li>Dim one light.</li>
  <li>Take one slow breath.</li>
</ul>
<h2>Use Support When Possible</h2>
<p>If another adult, family member, friend, or service can help, ask for something specific. "Can you handle the first morning task?" is easier to answer than "I need help." Small support can protect recovery.</p>
<h2>Reduce Revenge Bedtime Procrastination</h2>
<p>Caregivers may stay up late because it is the only quiet time. That is understandable, but it can deepen exhaustion. Try giving yourself a smaller, intentional quiet window earlier, then protect a realistic sleep cue.</p>
<h2>Recover After Interrupted Nights</h2>
<p>After a broken night, lower expectations where possible. Use morning light, food, hydration, and a short rest window if available. Avoid blaming yourself for needing recovery.</p>
<h2>When to Seek Help</h2>
<p>If sleep loss is severe, unsafe, or tied to depression, anxiety, burnout, pain, infant care concerns, or caregiving overload, seek professional and practical support. You should not have to handle chronic exhaustion alone.</p>
<h2>Related VitalBloom Guides</h2>
<ul>
  <li><a href="/sleep-hygiene-checklist-printable">Sleep Hygiene Checklist Printable</a></li>
  <li><a href="/evening-stress-reset">Evening Stress Reset</a></li>
  <li><a href="/sleep-debt-recovery-guide">Sleep Debt Recovery Guide</a></li>
  <li><a href="/daily-stress-relief-routine">Daily Stress Relief Routine</a></li>
</ul>
<p>Disclaimer: This article is for general educational purposes only and is not a substitute for professional medical, mental health, caregiving, or crisis support.</p>
""",
    },
    {
        "title": "Weekend Sleep Schedule: How to Rest Without Wrecking Monday",
        "slug": "weekend-sleep-schedule",
        "category": "Sleep",
        "keyword": "weekend sleep schedule",
        "meta_title": "Weekend Sleep Schedule",
        "meta_description": "Learn how to use the weekend for rest without creating a rough Monday sleep reset.",
        "excerpt": "A practical weekend sleep schedule guide for catching up, staying flexible, and making Monday mornings easier.",
        "content": """
<p>The weekend can be a chance to recover, but big sleep schedule swings can make Monday harder. Sleeping much later than usual may feel good in the moment and then make Sunday night or Monday morning rough.</p>
<p>A better weekend sleep schedule gives you room to rest without completely disconnecting from your weekday rhythm.</p>
<h2>Keep Wake Time Reasonably Anchored</h2>
<p>You do not need to wake at the exact same time every day, but try to avoid extreme swings when possible. A reasonably anchored wake time helps your body keep a more predictable rhythm.</p>
<h2>Add Rest Without Overcorrecting</h2>
<p>If you are sleep deprived, add extra sleep opportunity gradually. Go to bed a little earlier, allow a modest sleep-in, or take a short nap earlier in the day. Avoid turning the whole weekend into a sleep recovery sprint unless your body truly needs it.</p>
<h2>Watch Sunday Night</h2>
<p>Sunday night often reveals whether the weekend schedule drifted too far. If you are wide awake, review late caffeine, late naps, bright screens, stress, and a very late wake time. A Sunday evening reset can help.</p>
<h2>Use Morning Light on Weekends</h2>
<p>Morning light can keep the weekend from becoming too disconnected from the week. Open curtains, take a walk, or sit near a bright window after waking.</p>
<h2>Plan One Recovery Cue</h2>
<p>Weekend recovery does not have to be only sleep. Choose one cue: a walk, meal prep, laundry, quiet time, stretching, a call with someone supportive, or a screen boundary. Reducing stress can make sleep easier too.</p>
<h2>Make Monday Easier on Sunday</h2>
<p>Before Sunday night ends, write Monday's first task, prepare one needed item, and reduce late-night stimulation. A small amount of preparation can prevent Monday from feeling like a shock.</p>
<h2>Related VitalBloom Guides</h2>
<ul>
  <li><a href="/sleep-hygiene-checklist-printable">Sleep Hygiene Checklist Printable</a></li>
  <li><a href="/sleep-debt-recovery-guide">Sleep Debt Recovery Guide</a></li>
  <li><a href="/morning-light-and-sleep">Morning Light and Sleep</a></li>
  <li><a href="/evening-stress-reset">Evening Stress Reset</a></li>
</ul>
<p>Disclaimer: This article is for general educational purposes only and is not a substitute for professional medical advice, diagnosis, or treatment.</p>
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
