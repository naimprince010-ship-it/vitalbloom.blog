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
    <li>Use plain labels like "thinking," "planning," or "worrying" when your mind wanders.</li>
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
  <p>Screen time can affect sleep in more than one way. Bright light may delay sleepiness, but stimulating content, late messages, and "one more video" loops can also keep the brain alert. A better approach is to design a clear digital wind-down period.</p>
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
    "post-workout-recovery-tips": """
<section>
  <h2>How to Recover Without Overcomplicating It</h2>
  <p>Recovery is not just what happens after a hard workout. It is the combination of sleep, hydration, food, rest days, and smart progression. When those basics are consistent, your body has a better chance to adapt to training.</p>
  <p>Beginners often recover better by doing slightly less than they think they can handle. Leave some energy in reserve, especially during the first few weeks of a new routine.</p>
</section>
<section>
  <h2>Post-Workout Recovery Checklist</h2>
  <ul>
    <li>Cool down with gentle movement instead of stopping suddenly.</li>
    <li>Drink water and replace fluids after sweaty sessions.</li>
    <li>Eat a balanced meal or snack with protein and carbohydrates.</li>
    <li>Sleep enough before increasing workout intensity.</li>
  </ul>
</section>
<section>
  <h2>Common Questions</h2>
  <h3>Should soreness guide every workout?</h3>
  <p>Soreness is one signal, but energy, performance, sleep, and joint comfort also matter.</p>
  <h3>Do I need expensive recovery tools?</h3>
  <p>No. Sleep, gradual training, hydration, and balanced meals usually matter more than gadgets.</p>
</section>
""",
    "seasonal-wellness-tips": """
<section>
  <h2>How to Adjust Your Routine by Season</h2>
  <p>Seasonal wellness is about planning for predictable changes. Shorter daylight, hotter weather, cold and flu season, travel, and holiday schedules can all disrupt routines if you wait until the last minute.</p>
  <p>Use the start of each season as a checkpoint. Review your sleep schedule, movement plan, hydration, food choices, and preventive health habits so your routine matches the environment you are actually in.</p>
</section>
<section>
  <h2>Seasonal Reset Checklist</h2>
  <ul>
    <li>Prepare weather-appropriate walking or workout options.</li>
    <li>Keep hydration visible during hot or dry months.</li>
    <li>Make sleep routines stronger during busy holiday periods.</li>
    <li>Follow common illness-prevention habits during cold and flu season.</li>
  </ul>
</section>
<section>
  <h2>Common Questions</h2>
  <h3>Should my routine change every season?</h3>
  <p>The core habits can stay the same, but the details may need to change with weather, daylight, and schedule demands.</p>
  <h3>What is the easiest seasonal habit to start?</h3>
  <p>Plan one backup movement option for days when weather or daylight interrupts your normal routine.</p>
</section>
""",
    "strength-training-basics": """
<section>
  <h2>How Beginners Should Think About Strength</h2>
  <p>Strength training is not only for athletes. It supports daily movement, balance, bone health, and long-term independence. Beginners can start with simple movements such as squats, hinges, pushes, pulls, and carries.</p>
  <p>The first goal is learning control. Use a range of motion that feels safe, keep the pace steady, and increase resistance gradually after your technique feels consistent.</p>
</section>
<section>
  <h2>Beginner Strength Checklist</h2>
  <ul>
    <li>Start with two sessions per week if you are new to training.</li>
    <li>Practice movement quality before chasing heavy weight.</li>
    <li>Include both upper-body and lower-body exercises.</li>
    <li>Rest at least a day between challenging strength sessions at first.</li>
  </ul>
</section>
<section>
  <h2>Common Questions</h2>
  <h3>Can I strength train at home?</h3>
  <p>Yes. Bodyweight exercises, resistance bands, and household weights can be enough for a beginner routine.</p>
  <h3>When should I increase weight?</h3>
  <p>Increase gradually when you can finish the planned reps with good form and no unusual pain.</p>
</section>
""",
    "simple-hydration-guide": """
<section>
  <h2>How to Make Hydration Easier</h2>
  <p>Hydration habits work best when water is easy to reach. Many people do not need a complicated tracking system; they need a visible bottle, regular meal-time fluids, and extra attention during heat, illness, or sweaty activity.</p>
  <p>Thirst, urine color, activity level, climate, and medical conditions can all affect fluid needs. People with specific health concerns should follow advice from their healthcare professional.</p>
</section>
<section>
  <h2>Daily Hydration Checklist</h2>
  <ul>
    <li>Drink water with meals and snacks.</li>
    <li>Carry water during errands, commuting, or workouts.</li>
    <li>Increase fluids during hot weather or heavier sweating.</li>
    <li>Choose water more often than sugary drinks.</li>
  </ul>
</section>
<section>
  <h2>Common Questions</h2>
  <h3>Does coffee count toward hydration?</h3>
  <p>Many beverages contribute fluid, but water is still a simple default choice for everyday hydration.</p>
  <h3>Can I drink too much water?</h3>
  <p>Yes, although it is uncommon for most healthy adults. Follow medical guidance if you have kidney, heart, or electrolyte concerns.</p>
</section>
""",
    "how-to-avoid-burnout": """
<section>
  <h2>How to Notice Burnout Risk Earlier</h2>
  <p>Burnout risk often builds gradually. You may notice constant fatigue, cynicism, lower motivation, difficulty focusing, or feeling detached from work that used to feel manageable. The earlier you notice those signals, the easier it is to adjust.</p>
  <p>Prevention starts with boundaries that are specific enough to protect. Decide when work ends, which notifications can wait, and what recovery habits are non-negotiable during demanding weeks.</p>
</section>
<section>
  <h2>Burnout Boundary Checklist</h2>
  <ul>
    <li>Define a daily shutdown cue for work.</li>
    <li>Schedule short breaks before exhaustion hits.</li>
    <li>Protect sleep and meals during high-pressure periods.</li>
    <li>Talk with a manager, clinician, or trusted support person if symptoms persist.</li>
  </ul>
</section>
<section>
  <h2>Common Questions</h2>
  <h3>Is burnout the same as normal tiredness?</h3>
  <p>No. Burnout is more persistent and is often tied to chronic work-related stress.</p>
  <h3>Can a weekend fix burnout?</h3>
  <p>A weekend can help with rest, but deeper burnout usually requires ongoing changes to workload, boundaries, and support.</p>
</section>
""",
    "beginner-meditation-guide": """
<section>
  <h2>How to Start Meditation Gently</h2>
  <p>Meditation can be simple: sit comfortably, choose a focus, notice when your mind wanders, and return without judging yourself. Wandering is not a mistake. It is part of the practice.</p>
  <p>For beginners, short sessions are enough. Try two to five minutes at the same time each day, then slowly add time only if the habit feels steady.</p>
</section>
<section>
  <h2>Beginner Meditation Checklist</h2>
  <ul>
    <li>Choose a quiet enough place, not a perfect place.</li>
    <li>Use your breath, a phrase, or body sensations as an anchor.</li>
    <li>Restart gently whenever attention drifts.</li>
    <li>End by noticing how your body feels before moving on.</li>
  </ul>
</section>
<section>
  <h2>Common Questions</h2>
  <h3>Do I have to sit cross-legged?</h3>
  <p>No. A chair, cushion, or supported position can work as long as you are comfortable and alert.</p>
  <h3>What if meditation feels uncomfortable?</h3>
  <p>Keep it short, try grounding techniques, and seek professional support if intense distress comes up.</p>
</section>
""",
    "evening-habits-better-rest": """
<section>
  <h2>How to Create a Realistic Evening Wind-Down</h2>
  <p>Better rest often starts before you get into bed. A consistent wind-down routine gives your body cues that the active part of the day is ending. The routine can be simple: dim lights, finish heavy tasks, prepare tomorrow's essentials, and choose one calming activity.</p>
  <p>Try to repeat the same order most nights. Predictability can make the routine easier, even when the exact bedtime shifts slightly.</p>
</section>
<section>
  <h2>Evening Routine Checklist</h2>
  <ul>
    <li>Set a reminder to begin winding down.</li>
    <li>Move stimulating work or conversations earlier when possible.</li>
    <li>Lower light and reduce screen intensity.</li>
    <li>Prepare your bedroom for cool, dark, quiet sleep.</li>
  </ul>
</section>
<section>
  <h2>Common Questions</h2>
  <h3>How long should a wind-down routine be?</h3>
  <p>Even 15 to 30 minutes can help if it is consistent and calming.</p>
  <h3>What if I cannot keep the same bedtime?</h3>
  <p>Keep the same routine order and wake time as often as possible, even when bedtime varies.</p>
</section>
""",
    "simple-breathing-exercises": """
<section>
  <h2>How to Use Breathing Exercises Safely</h2>
  <p>Breathing exercises can be a quick way to slow down during everyday stress. The goal is not to force huge breaths. It is to breathe in a steady, comfortable rhythm that helps your body feel less rushed.</p>
  <p>If a technique makes you dizzy or uncomfortable, stop and return to normal breathing. People with respiratory, cardiac, panic, or trauma-related concerns may want guidance from a qualified professional.</p>
</section>
<section>
  <h2>Simple Breathing Checklist</h2>
  <ul>
    <li>Start with one or two minutes instead of long sessions.</li>
    <li>Keep the shoulders relaxed and the jaw unclenched.</li>
    <li>Use a slow exhale when you want to settle down.</li>
    <li>Practice when calm so the skill is easier during stress.</li>
  </ul>
</section>
<section>
  <h2>Common Questions</h2>
  <h3>Can breathing exercises stop all anxiety?</h3>
  <p>No. They can help some people manage stress in the moment, but they are not a complete treatment for anxiety disorders.</p>
  <h3>When is the best time to practice?</h3>
  <p>Practice during low-stress moments first, then use the same technique during harder moments.</p>
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
