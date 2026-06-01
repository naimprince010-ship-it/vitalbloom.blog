import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
MARKER = "<!-- vitalbloom-authority-expansion-v3 -->"

AUTHORITY_SECTIONS: dict[str, str] = {
    "balanced-plate-method": """
<section>
  <h2>How to Adjust the Plate for Different Goals</h2>
  <p>The balanced plate method is flexible because it can be adjusted without turning meals into a math problem. If you want more steady energy, focus on protein, fiber-rich carbohydrates, and colorful produce. If you want a lighter meal, keep the same structure but use smaller portions or more non-starchy vegetables.</p>
  <p>For active days, you may need more carbohydrates. For a smaller evening meal, you may prefer extra vegetables with protein and a modest portion of starch. The method is a guide for balance, not a fixed rule that every person must follow exactly.</p>
  <p>People with diabetes, kidney disease, digestive conditions, eating disorder history, pregnancy needs, or other medical concerns should follow personalized guidance from a qualified professional.</p>
</section>
<section>
  <h2>Balanced Plate Fixes for Common Meals</h2>
  <ul>
    <li>Pasta: add vegetables and protein instead of eating noodles alone.</li>
    <li>Sandwich: add fruit, salad, yogurt, or soup on the side.</li>
    <li>Rice bowl: include beans, tofu, eggs, fish, or chicken plus vegetables.</li>
    <li>Breakfast: pair toast or oats with protein and fruit.</li>
  </ul>
  <p>Small adjustments can turn an ordinary meal into a more satisfying one.</p>
</section>
""",
    "strength-training-basics": """
<section>
  <h2>A Simple Beginner Strength Workout</h2>
  <p>If you are not sure how to combine the movement patterns, start with a short full-body routine. Warm up with easy walking or marching in place, then choose one squat movement, one push movement, one pull movement, one hinge movement, and one core exercise.</p>
  <p>A beginner session might include chair squats, wall push-ups, resistance band rows, hip hinges, and bird dogs. Do one or two sets of each exercise and stop while your form still feels controlled. The first few sessions should build confidence, not exhaustion.</p>
  <p>After two or three weeks of consistency, you can add a set, add repetitions, or use a slightly harder version. Progress works best when it is gradual.</p>
</section>
<section>
  <h2>Beginner Safety Reminders</h2>
  <ul>
    <li>Warm up before harder sets.</li>
    <li>Use a pain-free range of motion.</li>
    <li>Rest long enough to keep technique steady.</li>
    <li>Stop if you feel sharp pain, dizziness, or unusual symptoms.</li>
    <li>Ask for professional guidance if you have injuries or medical concerns.</li>
  </ul>
</section>
""",
    "foods-drinks-affect-sleep": """
<section>
  <h2>How to Notice Your Own Food-Sleep Patterns</h2>
  <p>Food and sleep patterns are personal. Instead of changing everything at once, keep a simple note for one week. Write down caffeine timing, alcohol, dinner time, heavy meals, late snacks, and how rested you feel in the morning.</p>
  <p>Look for repeated patterns. Maybe late coffee affects you strongly, or maybe heavy meals are the bigger issue. Some people sleep worse after alcohol, while others notice discomfort after spicy or acidic foods. Your notes can help you make targeted changes.</p>
  <p>Keep the experiment gentle. The goal is not food fear. The goal is to understand which evening choices support better rest for your body.</p>
</section>
<section>
  <h2>A Gentle Evening Food Routine</h2>
  <ul>
    <li>Keep caffeine earlier in the day if sleep is sensitive.</li>
    <li>Eat heavier meals with enough time before lying down.</li>
    <li>Choose a small balanced snack if hunger wakes you up.</li>
    <li>Shift more fluids earlier if bathroom trips interrupt sleep.</li>
    <li>Notice alcohol's effect on waking and sleep quality.</li>
  </ul>
</section>
""",
    "practice-mindfulness-simply": """
<section>
  <h2>Use Mindfulness During Stressful Moments</h2>
  <p>Mindfulness becomes useful when it helps you pause before reacting. During a stressful moment, try naming what is happening in plain language: "I feel rushed," "I am worrying," or "My shoulders are tense." This simple label can create a little space between the feeling and your next action.</p>
  <p>Then choose one anchor. Feel your feet on the floor, notice your breathing, or look around the room and name three things you can see. The anchor does not erase the problem, but it can help your nervous system settle enough to respond more clearly.</p>
  <p>Keep the practice brief. In real life, one mindful minute is often more realistic than a long session.</p>
</section>
<section>
  <h2>Mindfulness Mini-Practices</h2>
  <ul>
    <li>Before replying to a tense message, take one slow breath.</li>
    <li>Before eating, pause and notice hunger level.</li>
    <li>During a walk, feel each step for one minute.</li>
    <li>When distracted, name the distraction and return to one task.</li>
    <li>Before bed, notice three points of contact with the mattress.</li>
  </ul>
</section>
""",
    "stretching-routine-desk-workers": """
<section>
  <h2>Make Desk Stretching Easier to Remember</h2>
  <p>The hardest part of stretching is often remembering to do it before stiffness builds. Attach stretches to events that already happen during the workday: after a meeting, after sending a report, before lunch, or when you refill water.</p>
  <p>You can also use a two-level routine. On busy days, do one minute of shoulder rolls, chest opening, and wrist stretches. On calmer days, do the full five-to-seven-minute routine. The shorter version keeps the habit alive.</p>
  <p>Stretching should feel gentle. If a movement causes sharp pain, numbness, tingling, or symptoms that travel down the arm or leg, stop and seek professional guidance.</p>
</section>
<section>
  <h2>Desk Break Pairings</h2>
  <ul>
    <li>After a video call: shoulder rolls and chest opener.</li>
    <li>After typing for a long block: wrist and forearm stretch.</li>
    <li>Before lunch: hip flexor stretch and short walk.</li>
    <li>Mid-afternoon: neck stretch, seated twist, and water refill.</li>
  </ul>
  <p>Pairing stretches with existing cues makes consistency much easier.</p>
</section>
""",
    "post-workout-recovery-tips": """
<section>
  <h2>How to Tell If Recovery Is Working</h2>
  <p>Good recovery usually shows up as steady energy, normal appetite, improving performance, and soreness that fades within a reasonable time. You do not need to feel perfect after every workout, but you should feel able to return to training without constantly dragging yourself through it.</p>
  <p>If you feel unusually sore, irritable, tired, or weaker for several sessions in a row, your body may need more rest, food, hydration, or sleep. Recovery is feedback, not a sign that you are failing.</p>
  <p>Beginners often make faster progress by doing slightly less and repeating it consistently than by pushing too hard and needing long breaks.</p>
</section>
<section>
  <h2>Recovery Mistakes to Avoid</h2>
  <ul>
    <li>Increasing workout volume too quickly.</li>
    <li>Ignoring sleep while adding harder training.</li>
    <li>Skipping meals after demanding sessions.</li>
    <li>Training through sharp pain.</li>
    <li>Expecting soreness to prove that a workout worked.</li>
  </ul>
</section>
""",
    "stress-affects-sleep": """
<section>
  <h2>Create a Daytime Plan for Nighttime Stress</h2>
  <p>Nighttime stress is often easier to manage when you address some of it earlier in the day. Set aside a short planning window in the afternoon or early evening. Use that time to list concerns, choose next actions, and decide what can wait.</p>
  <p>This gives your mind evidence that the issues have been acknowledged. Then, when worries return at bedtime, you can remind yourself that there is already a plan for tomorrow. The goal is not to force thoughts away, but to reduce the need to solve everything in bed.</p>
  <p>If stress is persistent, intense, or connected to anxiety, trauma, depression, or major life strain, professional support can be important. Sleep habits help, but they do not replace care.</p>
</section>
<section>
  <h2>Bedtime Reset Steps</h2>
  <ul>
    <li>Write down the worry in one sentence.</li>
    <li>Choose whether it needs action tomorrow or can wait.</li>
    <li>Use a slow exhale for one to three minutes.</li>
    <li>Return to a calm cue, such as reading or soft music.</li>
    <li>Avoid checking the clock repeatedly if it increases pressure.</li>
  </ul>
</section>
""",
}


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
    return result.stdout


def post_id(slug: str) -> str:
    found = run_wp("post", "list", f"--name={slug}", "--post_type=post", "--field=ID").strip()
    if not found:
        raise RuntimeError(f"Post not found: {slug}")
    return found.splitlines()[0]


def main() -> None:
    for slug, section in AUTHORITY_SECTIONS.items():
        pid = post_id(slug)
        content = run_wp("post", "get", pid, "--field=post_content")
        if MARKER in content:
            print(f"already-expanded: {slug}")
            continue

        updated = content.rstrip() + "\n\n" + MARKER + "\n" + section.strip() + "\n"
        run_wp("post", "update", pid, f"--post_content={updated}")
        print(f"expanded: {pid} {slug}")


if __name__ == "__main__":
    main()
