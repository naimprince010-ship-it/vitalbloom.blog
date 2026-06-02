import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
MARKER = "<!-- vitalbloom-sleep-stress-support-batch3-expanded-v1 -->"

EXPANSIONS = {
    "how-to-wind-down-after-work": """
<h2>Use a Work Bag or Digital Closing Ritual</h2>
<p>If you work outside the home, the act of putting items into a work bag can become a closing ritual. If you work digitally, create a similar ritual: close the project, save notes, shut down work chat, and move the device out of sight. The ritual gives the day a clear edge.</p>
<p>When work has no edge, the mind keeps checking for unfinished business. A closing ritual does not solve every workload problem, but it reduces the constant feeling that you might need to jump back in.</p>
<h2>Choose a Decompression Activity Before Chores</h2>
<p>Many people leave work and immediately enter another list: dishes, errands, messages, dinner, or family logistics. If possible, place a decompression activity before chores. This might be a short walk, music, stretching, breathing, or sitting quietly for five minutes.</p>
<p>This small pause can improve the tone of the evening. You are not avoiding responsibilities; you are creating a steadier state before entering them.</p>
""",
    "sleep-friendly-evening-routine": """
<h2>Keep the Routine Flexible for Real Life</h2>
<p>A sleep-friendly routine should have a full version and a short version. The full version might take 30 minutes. The short version might be three steps: dim lights, put the phone away, and write tomorrow's first task. Both versions count.</p>
<p>This matters because evenings are unpredictable. If the routine only works on perfect nights, it will not survive normal life. A flexible routine lets you restart quickly after late work, family needs, travel, or stress.</p>
<h2>Notice Evening Energy Traps</h2>
<p>Some habits make evenings stretch later than planned. Common traps include opening work again, watching one more episode, scrolling in bed, starting chores too late, or drinking caffeine late in the day. Choose one trap to adjust first.</p>
<p>Small boundaries are easier than total overhauls. For example, stop work email before the wind-down routine or charge the phone before getting into bed.</p>
""",
    "phone-free-bedtime-routine": """
<h2>Make the Phone Less Interesting at Night</h2>
<p>Distance helps, but you can also make the phone less tempting. Move distracting apps off the home screen, turn the display grayscale, disable nonessential notifications, or set app limits for the evening. These changes reduce friction before bedtime.</p>
<p>The goal is not to hate your phone. The goal is to make the restful choice easier when you are tired and more vulnerable to automatic habits.</p>
<h2>Prepare for the First Phone-Free Week</h2>
<p>The first week may feel awkward. You may reach toward the old charging spot or feel restless without scrolling. Prepare for that by choosing one replacement activity and keeping it visible: a book, notebook, stretching mat, or calming playlist.</p>
<p>Track phone-free nights with a simple mark. Seeing progress can make the routine feel real without turning it into another pressure-filled goal.</p>
""",
    "simple-relaxation-techniques": """
<h2>Match the Technique to the Stress</h2>
<p>Different stress states need different tools. If your thoughts are racing, grounding or writing may help. If your body is tense, progressive muscle relaxation or stretching may help. If you feel rushed, slow breathing or a one-minute pause may be enough to create space.</p>
<p>Matching the technique to the stress makes relaxation more practical. You are not trying random tools; you are choosing the tool that fits the moment.</p>
<h2>Practice Before You Need It</h2>
<p>Relaxation techniques are easier to use during high stress if you practice them during low stress. Try one minute after lunch, before bed, or after closing work. This builds familiarity.</p>
<p>When stress is high, the brain often prefers familiar habits. Practicing a calm reset when life is ordinary makes it more available when life feels difficult.</p>
""",
    "how-to-reset-after-a-bad-night-sleep": """
<h2>Use a Minimum Viable Day</h2>
<p>After a bad night, lower the bar without abandoning the day. Choose the minimum viable version of your routines: a simple breakfast, a short walk, essential work tasks, and an early wind-down. This keeps you functioning without pretending you are fully rested.</p>
<p>A minimum viable day can prevent overcorrection. You do not need to fix everything by noon. You need enough support to get through the day and protect the next night.</p>
<h2>Avoid Revenge Bedtime After a Rough Day</h2>
<p>Poor sleep can make the day feel unproductive, which can lead to staying up late to reclaim personal time. This is understandable, but it can repeat the cycle. Choose a small enjoyable evening activity earlier instead of pushing bedtime later.</p>
<p>For example, take a short walk, read for ten minutes, call someone, or watch one planned episode before the wind-down routine. Enjoyment and recovery can both fit if the evening has a boundary.</p>
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
