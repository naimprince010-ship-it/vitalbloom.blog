import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
MARKER = "<!-- vitalbloom-polish-v1 -->"

POLISH_SECTIONS: dict[str, str] = {
    "daily-wellness-routine-beginners": """
<section>
  <h2>How to Build a Routine That Actually Fits</h2>
  <p>A beginner wellness routine should support your day instead of becoming another source of pressure. Start with a few repeatable anchors: hydration after waking, a balanced meal, some movement, a short mental reset, and a consistent wind-down time.</p>
  <p>Keep the routine flexible. A busy day might only include a five-minute walk and a simple dinner, while a calmer day may allow more time for exercise, meal prep, or reflection. Consistency comes from having a fallback version, not from doing everything perfectly.</p>
</section>
<section>
  <h2>Beginner Routine Checklist</h2>
  <ul>
    <li>Choose one morning habit that takes less than five minutes.</li>
    <li>Add movement in a way that matches your current fitness level.</li>
    <li>Plan one simple meal or snack that helps you avoid last-minute choices.</li>
    <li>Use a short evening cue to prepare for sleep.</li>
  </ul>
</section>
<section>
  <h2>Common Questions</h2>
  <h3>How long does a wellness routine need to be?</h3>
  <p>It can be very short. A realistic 15-minute routine is often more useful than an ideal routine that is too hard to repeat.</p>
  <h3>What should I track first?</h3>
  <p>Track completion of one or two habits, such as daily movement or bedtime consistency, before adding more details.</p>
</section>
""",
    "practice-mindfulness-simply": """
<section>
  <h2>A Simple Way to Start This Week</h2>
  <p>Mindfulness works best when it is easy to repeat. Instead of trying to clear your mind completely, choose one small anchor: your breath, the feeling of your feet on the floor, or the sound around you. Set a timer for two to five minutes and gently return to that anchor whenever your attention wanders.</p>
  <p>If you miss a day, restart without treating it as failure. The goal is not perfection. The goal is to build a familiar pause that helps you notice stress earlier and respond with more intention.</p>
</section>
<section>
  <h2>Beginner Mindfulness Checklist</h2>
  <ul>
    <li>Choose one daily cue, such as after brushing your teeth or before opening email.</li>
    <li>Keep the first sessions short enough that they feel almost too easy.</li>
    <li>Use plain labels like “thinking,” “planning,” or “worrying” when your mind wanders.</li>
    <li>End by noticing one practical next step for the rest of your day.</li>
  </ul>
</section>
<section>
  <h2>Common Questions</h2>
  <h3>Do I need a meditation app?</h3>
  <p>No. Apps can help with guidance, but a quiet timer and a repeatable routine are enough to begin.</p>
  <h3>What if mindfulness makes me more aware of stress?</h3>
  <p>That can happen at first. Keep sessions short, stay grounded in the present moment, and seek professional support if difficult emotions feel overwhelming.</p>
</section>
""",
    "exercise-sustainable-habit": """
<section>
  <h2>How to Make Exercise Easier to Repeat</h2>
  <p>A sustainable exercise habit usually starts smaller than people expect. A ten-minute walk, two sets of bodyweight movements, or a short mobility session can build the identity and consistency needed for longer workouts later.</p>
  <p>Use a weekly rhythm instead of relying on motivation. For example, plan two strength sessions, two walks, and one flexible recovery day. This gives structure while leaving room for real life.</p>
</section>
<section>
  <h2>Weekly Habit Checklist</h2>
  <ul>
    <li>Pick a realistic time of day and protect it on your calendar.</li>
    <li>Prepare shoes, clothes, or equipment before the workout window starts.</li>
    <li>Track completion, not perfection, for the first month.</li>
    <li>Increase volume slowly when the routine feels stable.</li>
  </ul>
</section>
<section>
  <h2>Common Questions</h2>
  <h3>How many days should beginners exercise?</h3>
  <p>Many beginners do well with three to five light or moderate sessions per week, depending on current fitness, recovery, and medical considerations.</p>
  <h3>What should I do when I miss a workout?</h3>
  <p>Return to the next planned session. Avoid doubling up aggressively, especially if soreness or fatigue is already high.</p>
</section>
""",
    "screen-time-and-sleep-quality": """
<section>
  <h2>How to Reduce Evening Screen Disruption</h2>
  <p>Screen time can affect sleep in more than one way. Bright light may delay sleepiness, but stimulating content, late messages, and “one more video” loops can also keep the brain alert. A better approach is to design a clear digital wind-down period.</p>
  <p>Start with the final 30 minutes before bed. Put the phone on charge away from the bed, lower room lighting, and switch to a calm offline activity such as reading, stretching, or preparing for the next morning.</p>
</section>
<section>
  <h2>Evening Screen Checklist</h2>
  <ul>
    <li>Set a device curfew that is realistic for your schedule.</li>
    <li>Turn on night settings and reduce brightness after sunset.</li>
    <li>Move work notifications out of the bedroom.</li>
    <li>Keep one non-screen wind-down option ready.</li>
  </ul>
</section>
<section>
  <h2>Common Questions</h2>
  <h3>Is blue light the only issue?</h3>
  <p>No. Emotional stimulation, work stress, and inconsistent bedtimes can matter too.</p>
  <h3>Do I have to stop all screens at night?</h3>
  <p>Not always. The practical goal is to reduce the screen habits that delay sleep or make it harder to relax.</p>
</section>
""",
    "balanced-plate-method": """
<section>
  <h2>How to Use the Balanced Plate Method in Real Meals</h2>
  <p>The balanced plate method is useful because it gives structure without requiring calorie tracking. A practical plate often includes colorful vegetables or fruit, a protein source, a fiber-rich carbohydrate, and a small amount of healthy fat.</p>
  <p>This approach can work with many cuisines. A rice bowl, pasta dish, sandwich, or breakfast plate can all be adjusted by adding produce, choosing a satisfying protein, and watching portions of energy-dense extras.</p>
</section>
<section>
  <h2>Balanced Plate Checklist</h2>
  <ul>
    <li>Fill part of the plate with vegetables or fruit when possible.</li>
    <li>Add protein such as eggs, fish, poultry, beans, lentils, tofu, yogurt, or nuts.</li>
    <li>Choose higher-fiber carbohydrates more often.</li>
    <li>Use sauces, oils, and toppings intentionally rather than automatically.</li>
  </ul>
</section>
<section>
  <h2>Common Questions</h2>
  <h3>Do I need to count calories?</h3>
  <p>Not necessarily. Many people can improve meal quality by using plate balance, hunger cues, and consistent meal timing.</p>
  <h3>Can this work for vegetarian meals?</h3>
  <p>Yes. Beans, lentils, tofu, tempeh, Greek yogurt, eggs, nuts, and seeds can help build satisfying vegetarian plates.</p>
</section>
""",
    "stress-affects-sleep": """
<section>
  <h2>What to Do When Stress Shows Up at Bedtime</h2>
  <p>Stress often becomes louder at night because there are fewer distractions. Thoughts about work, family, money, or tomorrow's responsibilities can make the body feel alert even when you are tired. A short transition routine can help signal that the day is closing.</p>
  <p>Try writing down tomorrow's top priorities before bed, then choose one calming activity for ten minutes. Gentle breathing, light stretching, or a warm shower can help separate problem-solving time from sleep time.</p>
</section>
<section>
  <h2>Sleep-Stress Reset Checklist</h2>
  <ul>
    <li>Keep a consistent wake time as often as possible.</li>
    <li>Write worries or tasks on paper instead of rehearsing them in bed.</li>
    <li>Limit late caffeine and heavy evening work sessions.</li>
    <li>Use the bed mainly for sleep, rest, and intimacy.</li>
  </ul>
</section>
<section>
  <h2>Common Questions</h2>
  <h3>Can stress cause poor sleep even if I feel tired?</h3>
  <p>Yes. Stress can increase alertness and make it harder to fall asleep or return to sleep after waking.</p>
  <h3>When should I get help?</h3>
  <p>If sleep problems are persistent, worsening, or affecting daily life, it is wise to speak with a qualified healthcare professional.</p>
</section>
""",
    "small-healthy-habits": """
<section>
  <h2>Why Small Habits Work</h2>
  <p>Small habits reduce friction. When a habit feels easy to start, you are more likely to repeat it on stressful or busy days. Over time, these repeated actions can become the foundation for larger health changes.</p>
  <p>Instead of changing everything at once, choose one habit from each area of daily life: movement, meals, hydration, sleep, and mental reset. Give each one a clear cue so it happens at the same point in your day.</p>
</section>
<section>
  <h2>Five Low-Friction Habits to Try</h2>
  <ul>
    <li>Drink water with your first meal.</li>
    <li>Take a short walk after lunch or dinner.</li>
    <li>Add one fruit or vegetable to a meal you already eat.</li>
    <li>Pause for three slow breaths before checking messages.</li>
    <li>Set a consistent time to begin winding down at night.</li>
  </ul>
</section>
<section>
  <h2>Common Questions</h2>
  <h3>Should I start many habits at once?</h3>
  <p>It is usually better to start with one or two habits, then add more after they feel automatic.</p>
  <h3>How do I know if a habit is too hard?</h3>
  <p>If you skip it repeatedly, shrink it. A smaller version keeps momentum alive while your schedule changes.</p>
</section>
""",
    "mindful-morning-routine": """
<section>
  <h2>A Calmer Morning Without a Complicated Routine</h2>
  <p>A mindful morning routine does not need to include a long meditation session. It can begin with a pause before the first screen, a glass of water, a few breaths, and one clear intention for the day.</p>
  <p>The key is to create a buffer between waking up and reacting to the outside world. Even five quiet minutes can make the morning feel less rushed and more deliberate.</p>
</section>
<section>
  <h2>Morning Mindfulness Checklist</h2>
  <ul>
    <li>Keep your phone away for the first few minutes after waking.</li>
    <li>Notice your breathing before starting tasks.</li>
    <li>Choose one priority instead of opening every app or inbox.</li>
    <li>Pair mindfulness with an existing habit, such as making tea or coffee.</li>
  </ul>
</section>
<section>
  <h2>Common Questions</h2>
  <h3>What if my mornings are rushed?</h3>
  <p>Use a smaller routine. One minute of breathing or a screen-free first sip of coffee can still be useful.</p>
  <h3>Can a mindful morning improve the whole day?</h3>
  <p>It can help set a calmer tone, especially when paired with realistic planning and enough sleep.</p>
</section>
""",
    "journaling-mental-clarity": """
<section>
  <h2>How Journaling Can Support Clearer Thinking</h2>
  <p>Journaling gives thoughts a place to land. When worries, plans, or decisions stay only in your head, they can feel larger and harder to organize. Writing them down can help you separate facts, feelings, and next steps.</p>
  <p>Keep the format simple. A few sentences at the same time each day may be more sustainable than a long entry that feels like homework.</p>
</section>
<section>
  <h2>Simple Journaling Prompts</h2>
  <ul>
    <li>What is taking up the most mental space today?</li>
    <li>What is one thing I can control in this situation?</li>
    <li>What helped me feel steady yesterday?</li>
    <li>What is one realistic next step?</li>
  </ul>
</section>
<section>
  <h2>Common Questions</h2>
  <h3>Do I need to journal every day?</h3>
  <p>No. A few times per week can still help, especially during stressful seasons.</p>
  <h3>Should journaling replace therapy?</h3>
  <p>No. Journaling can support reflection, but it does not replace professional mental health care when support is needed.</p>
</section>
""",
    "foods-drinks-affect-sleep": """
<section>
  <h2>How Food and Drink Choices Can Shape Sleep</h2>
  <p>Sleep quality is affected by the full day, not only the final hour before bed. Caffeine timing, alcohol, large late meals, hydration, and blood sugar swings can all influence how easily you fall asleep and how rested you feel.</p>
  <p>You do not need a perfect evening diet. The practical goal is to notice which choices repeatedly make sleep worse for you and adjust them gradually.</p>
</section>
<section>
  <h2>Evening Nutrition Checklist</h2>
  <ul>
    <li>Watch caffeine timing, especially in the afternoon and evening.</li>
    <li>Avoid making heavy late meals your default routine.</li>
    <li>Limit alcohol if it makes your sleep lighter or more interrupted.</li>
    <li>Choose a simple snack if hunger keeps you awake.</li>
  </ul>
</section>
<section>
  <h2>Common Questions</h2>
  <h3>Is one food guaranteed to improve sleep?</h3>
  <p>No single food works for everyone. Overall routine, sleep schedule, stress, and caffeine timing usually matter more.</p>
  <h3>Should I stop drinking water before bed?</h3>
  <p>Stay hydrated during the day. If nighttime bathroom trips disrupt sleep, consider shifting more fluids earlier.</p>
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
    for slug, section in POLISH_SECTIONS.items():
        pid = post_id(slug)
        content = run_wp("post", "get", pid, "--field=post_content")
        if MARKER in content:
            print(f"already-polished: {slug}")
            continue

        updated = content.rstrip() + "\n\n" + MARKER + "\n" + section.strip() + "\n"
        run_wp("post", "update", pid, f"--post_content={updated}")
        print(f"polished: {slug}")


if __name__ == "__main__":
    main()
