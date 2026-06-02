import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
MARKER = "<!-- vitalbloom-final-100-posts-expanded-v2 -->"

EXPANSIONS = {
    "how-to-build-a-simple-wellness-plan": """
<h2>Make the Plan Visible</h2>
<p>A wellness plan is easier to follow when you can see it. Keep the plan on one page, not buried in a notebook you rarely open. Put it on the refrigerator, inside a planner, on a desk, or in a phone note that is easy to access. The visible version should include only the habits you are actively practicing this week.</p>
<p>Visibility matters because daily life gets noisy. A simple reminder can bring you back to the plan before the day disappears into messages, errands, and decisions. If the plan is too long to glance at, rewrite it in shorter form.</p>
<h2>Include Support People</h2>
<p>Some parts of a wellness plan work better when other people know what you are trying to protect. You might tell a partner that you are working on an earlier wind-down, ask a friend to walk with you, or let family know that one evening is a recovery night. Support can make habits feel less isolated.</p>
<p>You do not need everyone to understand every detail. Choose the person or environment where a small amount of support would reduce friction.</p>
""",
    "healthy-routine-after-travel": """
<h2>Return to Movement Gradually</h2>
<p>After travel, it can be tempting to jump directly back into the hardest workout or full schedule. A gradual return is often more sustainable. Start with walking, mobility, stretching, or a lighter version of your normal routine. Notice how your body feels before adding intensity.</p>
<p>This is especially helpful after long flights, poor sleep, different meals, or busy travel days. The first movement session after travel should help you reconnect with the routine, not punish you for being away.</p>
<h2>Protect One Recovery Window</h2>
<p>Travel can be fun and still tiring. Protect one recovery window after returning, even if it is short. It might be an early bedtime, a quiet morning, an unpacking block, or a screen-light evening. Put it on the calendar if needed.</p>
<p>Without a recovery window, the first week back can feel like a sprint. A small pause helps your normal habits return with less resistance.</p>
""",
    "how-to-stay-consistent-with-healthy-habits": """
<h2>Build Around Your Normal Week</h2>
<p>Healthy habits need to fit the week you actually live. Look at your usual schedule and place habits where they naturally belong. If mornings are rushed, do not depend on a long morning routine. If evenings are unpredictable, use lunch breaks or short movement snacks.</p>
<p>Consistency grows when habits match your real energy patterns. A routine that looks good on paper but fights your schedule every day will be hard to maintain.</p>
<h2>Use a Recovery Plan After Disruption</h2>
<p>Disruption is normal: travel, illness, deadlines, family needs, or poor sleep. Write a recovery plan before you need it. It might include one easy meal, one short walk, one sleep cue, and one planning reset.</p>
<p>This helps you restart without spending extra energy deciding what to do. The recovery plan is the bridge between an interrupted week and your normal rhythm.</p>
""",
    "weekend-reset-for-better-sleep": """
<h2>Keep Sunday Evening Low-Stimulation</h2>
<p>Sunday evening often carries planning, worry, chores, and the feeling that the weekend is ending. A low-stimulation Sunday routine can help. Lower lights, reduce open-ended scrolling, prepare the next morning, and choose a calming activity before bed.</p>
<p>This does not mean Sunday has to be boring. It means the final part of the evening should help your body recognize that sleep is coming. A calmer Sunday night can make Monday feel less abrupt.</p>
<h2>Do Not Use the Weekend to Ignore Sleep Debt</h2>
<p>If you are regularly exhausted by Friday, the weekend can help but may not solve the root issue. Look at weekday bedtime, caffeine, workload, screens, and stress. A weekend reset is most helpful when it supports a better weekly rhythm, not when it becomes the only recovery you get.</p>
<p>Use the weekend to notice what your body is asking for. Then choose one weekday sleep cue to protect next week.</p>
""",
    "simple-energy-boosting-habits": """
<h2>Use Energy Anchors Across the Day</h2>
<p>Energy anchors are small habits placed at predictable times. Morning anchors might be light, water, and breakfast. Midday anchors might be a walk, lunch, and a screen break. Evening anchors might be a wind-down cue and preparing tomorrow's first step.</p>
<p>Anchors help because energy is not one decision. It is supported by repeated cues across the day. Choose one anchor for each part of the day rather than trying to overhaul everything at once.</p>
<h2>Respect Low-Energy Signals</h2>
<p>Sometimes low energy is information. It may point to poor sleep, skipped meals, dehydration, stress, overtraining, illness, or emotional overload. Instead of always pushing harder, ask what the signal may be telling you.</p>
<p>A useful energy habit responds to the signal. If you need food, eat. If you need movement, move gently. If you need rest, protect rest. If low energy persists, seek professional guidance.</p>
""",
    "beginner-guide-to-balanced-living": """
<h2>Build a Personal Definition of Balance</h2>
<p>Your version of balanced living may look different from someone else's. For one person, balance means protecting sleep and family time. For another, it means having energy for work, meals, walking, and quiet evenings. Write your own definition in plain language.</p>
<p>A personal definition helps you avoid chasing every wellness trend. When a new habit appears, ask whether it supports your definition or simply adds more noise.</p>
<h2>Practice the Weekly Rebalance</h2>
<p>At the end of each week, ask what needs rebalancing. Maybe movement was low, screens were high, meals were rushed, or rest disappeared. Choose one correction for the next week. Keep it small enough to do.</p>
<p>This turns balance into a rhythm of adjustment. You do not have to get everything right. You only need to keep noticing and returning to the basics that support your life.</p>
""",
}


def run_wp(*args: str) -> str:
    result = subprocess.run(["wp", *args, "--allow-root"], cwd=WP_PATH, text=True, capture_output=True, check=False)
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip())
    return result.stdout


def post_id(slug: str) -> str:
    found = run_wp("post", "list", f"--name={slug}", "--post_type=post", "--field=ID").strip()
    if not found:
        raise RuntimeError(f"Post not found: {slug}")
    return found.splitlines()[0]


def main() -> None:
    for slug, expansion in EXPANSIONS.items():
        pid = post_id(slug)
        content = run_wp("post", "get", pid, "--field=post_content")
        if MARKER in content:
            print(f"already-expanded: {slug}")
            continue
        run_wp("post", "update", pid, f"--post_content={content.rstrip()}\n\n{MARKER}\n{expansion.strip()}\n")
        print(f"expanded: {pid} {slug}")


if __name__ == "__main__":
    main()
