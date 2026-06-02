import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
MARKER = "<!-- vitalbloom-wellness-lifestyle-batch1-expanded-v1 -->"

EXPANSIONS = {
    "morning-routine-for-low-energy-days": """
<h2>Create a No-Decision Morning Menu</h2>
<p>Low-energy mornings become easier when you do not have to invent the first steps. Write a short menu with three options: one food option, one movement option, and one planning option. For example, yogurt and fruit, a five-minute walk, and writing one priority. Keep the menu visible so the morning has a path even when your mind feels slow.</p>
<p>This kind of menu reduces decision fatigue. You are not asking yourself what a perfect morning should look like. You are choosing from a few supportive actions that already fit your life.</p>
<h2>Prepare the Night Before</h2>
<p>A low-energy morning often improves with a small evening setup. Put a glass near the sink, set out clothes, prepare breakfast ingredients, write tomorrow's first task, or place shoes by the door. These small cues make the morning less dependent on motivation.</p>
<p>Do not prepare everything. Choose the one thing that usually slows you down most. Removing one friction point can make the whole morning feel more possible.</p>
""",
    "healthy-habits-when-life-feels-busy": """
<h2>Use Habit Pairing</h2>
<p>Habit pairing means attaching a healthy action to something that already happens. Drink water after brushing teeth, stretch after closing the laptop, walk after lunch, or prepare breakfast while making coffee. Pairing reduces the need to remember a habit from scratch.</p>
<p>This is especially useful during busy seasons because attention is already full. A paired habit becomes part of an existing rhythm instead of another item floating on the task list.</p>
<h2>Make Recovery Non-Negotiable but Small</h2>
<p>Recovery does not have to mean a full day off. It can be a ten-minute quiet break, a phone-free meal, an earlier bedtime, or a walk without multitasking. The important part is giving your system a real pause.</p>
<p>When life is busy, recovery is often the first thing removed. Keeping even a small recovery habit can protect your energy and reduce the chance that stress becomes the normal setting.</p>
""",
    "how-to-build-a-weekly-reset-routine": """
<h2>Keep a Reset Basket or List</h2>
<p>A reset basket or list can make the weekly routine easier to start. The basket might include a notebook, grocery list, planner, charger, water bottle, and any papers that need attention. A digital version might be one note with calendar, meals, errands, and recovery sections.</p>
<p>The purpose is to reduce setup time. When the reset tools are easy to find, you are less likely to delay the routine because it feels scattered.</p>
<h2>Do Not Turn the Reset Into a Marathon</h2>
<p>A weekly reset should leave you clearer, not depleted. If the list grows too long, choose the three actions that will make the biggest difference. For many weeks, that means food basics, calendar clarity, and one recovery window.</p>
<p>Stopping before exhaustion matters. A routine that drains you will be hard to repeat. A routine that creates relief is more likely to become sustainable.</p>
""",
    "simple-self-care-checklist": """
<h2>Use Self-Care Before You Hit Empty</h2>
<p>Self-care is often used only after stress becomes overwhelming. Try using the checklist earlier, when you notice the first signs: irritability, headache, scattered thoughts, tension, skipping meals, or wanting to withdraw. Early care is usually easier than crisis care.</p>
<p>Choose one action before the day fully unravels. Drink water, eat something steady, step outside, stretch, or send one honest message. Small care used early can change the direction of the day.</p>
<h2>Separate Comfort From Avoidance</h2>
<p>Comfort is not bad. Rest, entertainment, snacks, and quiet can all be part of self-care. The question is whether the action helps you feel supported or keeps you stuck in a loop that makes the problem bigger.</p>
<p>If a comfort habit is not helping, add a support habit beside it. For example, watch a show after eating dinner, scroll after writing tomorrow's task, or rest after sending the message you were avoiding.</p>
""",
    "digital-wellness-routine": """
<h2>Create a Screen Start and Stop Ritual</h2>
<p>Many people struggle because screen time has no clear beginning or ending. Create a start ritual for focused use: choose the task, close extra tabs, and set a stopping point. Create a stop ritual: save progress, close the device, stretch, and look away from the screen.</p>
<p>These rituals help your brain understand when technology is a tool and when the tool has taken over the room. Clear edges are a major part of digital wellness.</p>
<h2>Use One Offline Replacement</h2>
<p>Digital boundaries work better when there is an offline replacement. Keep a book, notebook, puzzle, walking shoes, stretching mat, or music option ready. When the urge to scroll appears, the replacement should be visible and easy.</p>
<p>You do not need to replace every screen habit. Start with one time of day, such as after work or before bed. A single reliable offline option can make the boundary feel less empty.</p>
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
