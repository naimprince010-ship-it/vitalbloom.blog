import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
MARKER = "<!-- vitalbloom-final-100-posts-expanded-v1 -->"

EXPANSIONS = {
    "how-to-build-a-simple-wellness-plan": """
<h2>Decide What You Will Not Track</h2>
<p>A simple wellness plan works better when it does not measure everything. Decide what does not need tracking. You may choose not to track calories, step counts, sleep scores, or every glass of water. Instead, focus on the few signals that actually guide behavior.</p>
<p>For example, you might track bedtime consistency, completed walks, and whether breakfast was ready. This keeps the plan light enough to use. Too much tracking can turn wellness into another source of stress.</p>
<h2>Create a Restart Rule</h2>
<p>Every wellness plan needs a restart rule because interruptions are guaranteed. Your rule might be: restart with the smallest version the next morning, restart with one meal, or restart with a five-minute walk. The rule should be simple enough that you can use it after travel, illness, stress, or a busy week.</p>
<p>A restart rule protects the plan from all-or-nothing thinking. Missing a habit does not erase progress. The next supportive action is what brings the routine back.</p>
""",
    "healthy-routine-after-travel": """
<h2>Rebuild Your Grocery Basics</h2>
<p>After travel, the kitchen may be empty or full of foods that no longer fit the week. Buy a few basics before planning anything complicated: one protein, one fruit, one vegetable, one fiber-rich carbohydrate, and one easy flavor item. This could be eggs, apples, frozen vegetables, oats, and salsa.</p>
<p>These basics make the first normal meals easier. You do not need a full grocery trip immediately. You need enough food to avoid relying on convenience choices because nothing else is available.</p>
<h2>Reset Your Digital and Work Boundaries</h2>
<p>Travel can blur phone, email, and schedule boundaries. After returning, close travel tabs, clear urgent messages, and decide when work will start again. If possible, avoid catching up late into the night. That can delay sleep and make the next day harder.</p>
<p>Choose one digital reset: clear notifications, charge the phone away from bed, or write tomorrow's work plan before opening messages. This helps the post-travel routine feel contained.</p>
""",
    "how-to-stay-consistent-with-healthy-habits": """
<h2>Use Friction for Habits You Want Less Of</h2>
<p>Consistency is not only about making healthy habits easier. It can also help to make draining habits a little harder. Move the phone charger away from the bed, keep distracting apps off the home screen, or put work materials away after hours.</p>
<p>Small friction creates a pause. The pause gives you a chance to choose a different action instead of moving automatically into the old habit.</p>
<h2>Celebrate Evidence, Not Perfection</h2>
<p>Look for evidence that you are becoming consistent: you restarted after missing a day, chose the short version, prepared breakfast twice, walked when you could, or protected bedtime once. These examples matter.</p>
<p>Perfection is fragile. Evidence is motivating. When you notice small proof of progress, it becomes easier to keep going.</p>
""",
    "weekend-reset-for-better-sleep": """
<h2>Use Saturday Without Sacrificing Sunday</h2>
<p>If you want a later night, Saturday may be easier to recover from than Sunday. Even then, keep a small morning anchor the next day: light, water, breakfast, or a short walk. This helps the weekend stay enjoyable without completely removing rhythm.</p>
<p>Think of the weekend as flexible, not structure-free. A few anchors can make the difference between feeling rested and feeling thrown off.</p>
<h2>Plan a Monday-Friendly Breakfast</h2>
<p>Monday sleepiness often feels worse when breakfast is chaotic. Prepare one easy option on Sunday: oats, yogurt, eggs, toast, fruit, or a smoothie plan. This gives Monday morning a lower-friction start.</p>
<p>A weekend sleep reset is not only about bedtime. It is also about making the next morning easier to enter.</p>
""",
    "simple-energy-boosting-habits": """
<h2>Use Task Switching Carefully</h2>
<p>Constant task switching can drain energy. If your day involves many messages, tabs, and interruptions, group similar tasks when possible. Answer messages in a block, then do focused work, then take a real break.</p>
<p>This reduces the feeling that your attention is being pulled in every direction. Mental energy often improves when the day has clearer edges.</p>
<h2>Check Your Environment</h2>
<p>Environment can affect energy more than you may notice. Dim light, clutter, poor posture, noise, and constant notifications can all add background fatigue. Choose one environmental reset: open curtains, clear the desk, adjust your chair, silence alerts, or step outside.</p>
<p>Energy habits do not have to live only inside your body. Sometimes changing the room changes the day.</p>
""",
    "beginner-guide-to-balanced-living": """
<h2>Choose Enough, Not Everything</h2>
<p>Balanced living becomes stressful when it turns into a demand to do everything. Choose enough support for the season you are in. During a busy season, enough may be sleep cues, simple meals, and short walks. During a calmer season, you may add strength training, meal planning, or deeper reflection.</p>
<p>The amount of wellness you can hold will change. That is normal. The goal is to keep a few foundations steady while letting the details flex.</p>
<h2>Use Balance as Feedback</h2>
<p>When life feels out of balance, treat that feeling as feedback instead of failure. Ask what is missing: rest, movement, food, focus, connection, boundaries, or fun. Then choose one small correction.</p>
<p>Balance is not a fixed state you finally achieve. It is a repeated practice of noticing, adjusting, and returning to what supports you.</p>
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
