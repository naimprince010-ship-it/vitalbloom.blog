import json
import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
IMAGE_DIR = Path("/tmp/vitalbloom-drafts")
TODAY = "2026-06-02"

COMMON_SOURCES = [
    {
        "title": "Adult Activity: An Overview",
        "url": "https://www.cdc.gov/physical-activity-basics/guidelines/adults.html",
        "publisher": "Centers for Disease Control and Prevention",
        "accessedAt": TODAY,
    },
    {
        "title": "Steps for Getting Started With Physical Activity",
        "url": "https://www.cdc.gov/healthy-weight-growth/physical-activity/getting-started.html",
        "publisher": "Centers for Disease Control and Prevention",
        "accessedAt": TODAY,
    },
    {
        "title": "Move Your Way Activity Planner: Why These Goals?",
        "url": "https://odphp.health.gov/moveyourway/activity-planner/why-these-goals/",
        "publisher": "Office of Disease Prevention and Health Promotion",
        "accessedAt": TODAY,
    },
]


def article(intro: list[str], sections: list[tuple[str, list[str]]], related: list[tuple[str, str]]) -> str:
    html = []
    for paragraph in intro:
        html.append(f"<p>{paragraph}</p>")
    for heading, paragraphs in sections:
        html.append(f"<h2>{heading}</h2>")
        for paragraph in paragraphs:
            html.append(paragraph if paragraph.startswith("<ul>") else f"<p>{paragraph}</p>")
    html.append("<h2>Related VitalBloom Guides</h2>")
    html.append("<ul>")
    for title, url in related:
        html.append(f'  <li><a href="{url}">{title}</a></li>')
    html.append("</ul>")
    html.append("<p>Disclaimer: This article is for general educational purposes only and is not medical advice. If you have pain, injury, a health condition, pregnancy-related concerns, or have been inactive for a long time, talk with a qualified healthcare professional before changing your activity routine.</p>")
    return "\n".join(html)


POSTS = [
    {
        "title": "Beginner Stretching Routine for Everyday Comfort",
        "slug": "beginner-stretching-routine",
        "category": "Fitness",
        "keyword": "beginner stretching routine",
        "meta_title": "Beginner Stretching Routine",
        "meta_description": "Try a beginner stretching routine with gentle full-body stretches, simple timing, comfort cues, and realistic consistency tips.",
        "excerpt": "A gentle beginner stretching routine for everyday comfort, built around simple movements and realistic consistency.",
        "image": "beginner-stretching-routine.png",
        "image_alt": "beginner stretching routine",
        "content": article(
            [
                "A beginner stretching routine should feel calm, simple, and repeatable. You do not need to force deep positions or turn stretching into a long workout. The goal is to spend a few minutes moving through comfortable ranges so your body feels less stiff during ordinary days.",
                "Stretching can be useful after sitting, after light activity, before bed, or during a work break. This guide focuses on gentle general movement, not rehabilitation or treatment. If a stretch causes sharp pain, numbness, dizziness, or worsening symptoms, stop and seek professional guidance.",
            ],
            [
                ("Start With a Comfortable Warm-Up", [
                    "Stretching usually feels better when your body is a little warm. Walk around the room, march in place, roll your shoulders, or do gentle arm swings for two to three minutes before holding stretches.",
                    "A warm-up does not need to be intense. The point is to tell your body that movement is beginning. This can make the routine feel smoother and reduce the urge to force a stretch before you are ready.",
                ]),
                ("Use a Simple Full-Body Order", [
                    "A predictable order makes stretching easier to repeat. Start with the neck and shoulders, move to the chest and upper back, then hips, hamstrings, calves, and ankles. You can finish with a slow breathing pause.",
                    "The order matters less than consistency. If you prefer starting with hips or legs, that is fine. A routine you remember is more useful than a perfect routine you skip.",
                ]),
                ("Try a 10-Minute Beginner Routine", [
                    "<ul><li>Shoulder rolls: 30 seconds each direction.</li><li>Chest opener: hold 30 to 45 seconds.</li><li>Upper back reach: hold 30 seconds each side.</li><li>Hip flexor stretch: hold 30 seconds each side.</li><li>Seated or standing hamstring stretch: hold 30 seconds each side.</li><li>Calf stretch: hold 30 seconds each side.</li><li>Gentle ankle circles: 30 seconds each side.</li></ul>",
                    "Move slowly between stretches. Use a chair, wall, counter, or cushion if support helps. The routine should feel steady, not like a balance test.",
                ]),
                ("How Stretching Should Feel", [
                    "A stretch can feel like mild tension, warmth, or a gentle pull. It should not feel sharp, electric, or painful. If you find yourself holding your breath or bracing, ease out until the stretch feels manageable.",
                    "More intense is not automatically better. Beginners often make better progress by using a comfortable range and repeating it consistently.",
                ]),
                ("Use Breathing as a Cue", [
                    "Breathing can keep stretching calm. Try a slow inhale, then soften slightly on the exhale. Do not push deeper just because you exhaled. Let the breath remind you to relax your jaw, shoulders, and hands.",
                    "If a position makes breathing difficult, change the position. Stretching should not feel like a struggle to stay still.",
                ]),
                ("Stretch After Sitting", [
                    "Long sitting can make the hips, chest, and calves feel tight. A short reset can include standing, reaching overhead, opening the chest, stretching the hip flexors, and moving the ankles.",
                    "This kind of mini-routine can be done during the day instead of saving all movement for the evening. Small resets add up and make stretching easier to remember.",
                ]),
                ("Stretching and Exercise Days", [
                    "On exercise days, stretching can be part of a cool-down. After walking, strength training, or low-impact cardio, use gentle stretches for the areas you used most.",
                    "You do not need a different routine every day. A familiar short routine can support consistency and help you notice how your body feels after activity.",
                ]),
                ("Avoid Common Beginner Mistakes", [
                    "Common mistakes include bouncing, forcing range, holding the breath, stretching through pain, and choosing too many stretches at once. Start with fewer movements and learn how they feel.",
                    "Another mistake is expecting stretching to fix every discomfort. Stiffness can come from sleep, stress, sitting, weakness, injury, or medical issues. Stretching is one tool, not a complete answer for every symptom.",
                ]),
                ("Make the Routine Easy to Repeat", [
                    "Attach stretching to an existing cue: after brushing teeth, after logging off work, after a walk, or before bed. Keep the routine short enough that you can do it even when motivation is low.",
                    "Track completion with a simple check mark. You do not need to measure flexibility every day. The first goal is building a reliable habit.",
                ]),
                ("When to Get Help", [
                    "If stretching causes pain, if one side feels dramatically different, or if stiffness limits daily life, consider professional guidance. A physical therapist or qualified clinician can help identify what kind of movement is appropriate.",
                    "Gentle stretching should support comfort. It should not create fear, pain, or pressure to push past your limits.",
                ]),
                ("A Simple Weekly Plan", [
                    "Start with three days per week. Use the 10-minute routine on two days and a five-minute desk or evening reset on one day. After two weeks, add another day if the routine feels helpful.",
                    "Keeping the plan modest makes it easier to continue. A short routine repeated often is more valuable than a long routine that disappears after one week.",
                ]),
            ],
            [
                ("Stretching Routine for Desk Workers", "/stretching-routine-desk-workers"),
                ("Beginner Home Workout Plan", "/beginner-home-workout-plan"),
                ("Daily Wellness Routine for Beginners", "/daily-wellness-routine-beginners"),
                ("10-Minute Walking Routine", "/10-minute-walking-routine"),
            ],
        ),
    },
    {
        "title": "Low-Impact Cardio for Beginners: Simple Ways to Start",
        "slug": "low-impact-cardio-for-beginners",
        "category": "Fitness",
        "keyword": "low impact cardio for beginners",
        "meta_title": "Low-Impact Cardio for Beginners",
        "meta_description": "Start low-impact cardio with beginner-friendly walking, cycling, step, dance, and home movement ideas that feel realistic.",
        "excerpt": "Beginner-friendly low-impact cardio ideas for building movement without jumping, complicated routines, or gym pressure.",
        "image": "low-impact-cardio-for-beginners.png",
        "image_alt": "low impact cardio for beginners",
        "content": article(
            [
                "Low-impact cardio can be a practical starting point if you want to move more without jumping, sprinting, or doing complicated workouts. It can be done at home, outside, in a gym, or in small breaks across the day.",
                "Low-impact does not mean low value. Walking, cycling, swimming, step-ups, dancing, and gentle circuits can all support cardiovascular activity when they raise your breathing and feel repeatable.",
            ],
            [
                ("What Low-Impact Cardio Means", [
                    "Low-impact cardio usually means at least one foot stays on the ground or the movement reduces pounding on the joints. Examples include walking, cycling, elliptical training, rowing, swimming, water aerobics, low-impact dance, and step-touch routines.",
                    "The right option depends on your body, equipment, space, and preferences. If one activity feels uncomfortable, choose another. There is no single best beginner cardio exercise.",
                ]),
                ("Start With the Talk Test", [
                    "A simple way to judge moderate intensity is the talk test. During moderate activity, you can talk but may not be able to sing comfortably. If you cannot speak in short phrases, slow down.",
                    "Beginners do not need to chase high intensity. Consistency matters first. Build a routine that feels challenging enough to notice but comfortable enough to repeat.",
                ]),
                ("Try a 15-Minute Starter Plan", [
                    "<ul><li>Minutes 1-3: easy warm-up pace.</li><li>Minutes 4-12: steady movement that raises breathing slightly.</li><li>Minutes 13-15: slow down and cool down.</li></ul>",
                    "This can be a walk, cycling session, marching routine, low-impact dance, or gentle step routine. Use the same structure for different activities.",
                ]),
                ("Low-Impact Cardio Options", [
                    "Walking is the simplest option for many people. Stationary cycling can be helpful when you prefer seated movement. Swimming and water exercise can feel gentle for some bodies. Low-impact dance can make movement feel less clinical.",
                    "At home, try marching in place, side steps, heel taps, gentle knee lifts, wall push-ups between movement sets, or slow step-ups if stairs are safe for you.",
                ]),
                ("Build Gradually", [
                    "Start with two or three sessions per week. If 15 minutes feels too long, use five minutes twice. If it feels easy after a few weeks, add time before adding intensity.",
                    "A gradual plan protects momentum. Doing too much too soon can make the routine feel exhausting or discouraging.",
                ]),
                ("Use Movement Snacks", [
                    "Movement snacks are short activity breaks. Three five-minute walks can be easier than one 15-minute session. A few minutes of marching, stairs, or cycling can break up long sitting days.",
                    "This is useful if your schedule is unpredictable. The body does not require every movement session to be perfectly scheduled to count as progress.",
                ]),
                ("Make It Joint-Friendly", [
                    "Use supportive shoes if walking, choose a smooth surface, and keep movements controlled. If step-ups bother your knees, switch to walking or cycling. If cycling bothers your back, adjust the seat or choose another option.",
                    "Low-impact should feel approachable. Pain is not a sign that the workout is working.",
                ]),
                ("Pair Cardio With Strength", [
                    "Public health guidelines encourage adults to include both aerobic and muscle-strengthening activity. Low-impact cardio can cover the aerobic side, while strength training supports muscles and function.",
                    "You do not need to do both in the same session. A simple week might include walking on three days and beginner strength work on two days.",
                ]),
                ("Track the Right Things", [
                    "Instead of tracking only calories or distance, track completion, energy, breathing, mood, or how easy it was to start. These signals can keep the routine meaningful before performance improves.",
                    "A beginner routine is successful when it becomes repeatable. Speed and duration can grow later.",
                ]),
                ("Common Beginner Questions", [
                    "If you feel tired after cardio, reduce the time or intensity. If you feel bored, change music, route, or activity. If you miss a week, restart with the easiest version.",
                    "The goal is not to prove discipline every day. The goal is to create a movement pattern your life can hold.",
                ]),
                ("A Simple Weekly Schedule", [
                    "Try Monday, Wednesday, and Saturday for low-impact cardio. Keep each session 10 to 20 minutes. Add one short walk on another day if you want extra movement.",
                    "After three consistent weeks, decide whether to add five minutes to one session or one additional short movement snack.",
                ]),
            ],
            [
                ("10-Minute Walking Routine", "/10-minute-walking-routine"),
                ("Walking for Weight Management", "/walking-for-weight-management"),
                ("Exercise as a Sustainable Habit", "/exercise-sustainable-habit"),
                ("Beginner Home Workout Plan", "/beginner-home-workout-plan"),
            ],
        ),
    },
    {
        "title": "How to Start Strength Training at Home Without a Gym",
        "slug": "how-to-start-strength-training-at-home",
        "category": "Fitness",
        "keyword": "start strength training at home",
        "meta_title": "How to Start Strength Training at Home",
        "meta_description": "Learn how to start strength training at home with beginner exercises, simple weekly planning, recovery, and safe progression.",
        "excerpt": "A beginner guide to strength training at home with simple exercises, realistic progression, and no gym requirement.",
        "image": "how-to-start-strength-training-at-home.png",
        "image_alt": "how to start strength training at home",
        "content": article(
            [
                "Strength training at home can be simple, effective, and beginner-friendly. You do not need a full gym, heavy weights, or a complicated program to start. You need a few movement patterns, enough recovery, and a plan you can repeat.",
                "Adults are encouraged to include muscle-strengthening activity during the week, and home training can help you build that habit. This guide focuses on general beginner education, not individualized exercise prescription.",
            ],
            [
                ("Start With Movement Patterns", [
                    "Instead of memorizing many exercises, learn basic movement patterns: squat, hinge, push, pull, carry, and core stability. These patterns show up in daily life and can be trained with body weight, bands, dumbbells, or household items.",
                    "A squat might be sitting to a chair. A hinge might be a hip hinge with hands on hips. A push might be a wall push-up. A pull might use a resistance band. A carry might be walking with grocery bags.",
                ]),
                ("Begin With Two Days Per Week", [
                    "Two strength sessions per week is a realistic starting point for many beginners. Space them apart so your body has time to recover. For example, try Tuesday and Friday or Monday and Thursday.",
                    "More days are not automatically better when you are starting. Consistency, form, and recovery matter more than doing a lot immediately.",
                ]),
                ("Try a Beginner Home Routine", [
                    "<ul><li>Chair squat: 2 sets of 8 to 10 reps.</li><li>Wall or counter push-up: 2 sets of 8 to 10 reps.</li><li>Hip hinge: 2 sets of 8 to 10 reps.</li><li>Band row or towel row variation: 2 sets of 8 to 10 reps.</li><li>Dead bug or bird dog: 2 sets of 6 to 8 reps per side.</li><li>Optional carry: 2 short walks with light bags.</li></ul>",
                    "Rest between sets. Move slowly enough that you can control the exercise. Stop if you feel sharp pain or symptoms that concern you.",
                ]),
                ("Use Good Enough Equipment", [
                    "You can start with no equipment. A chair, wall, towel, backpack, water bottles, resistance band, or light dumbbells can be enough. Equipment should make the movement clearer, not more intimidating.",
                    "If you buy one item, a resistance band or adjustable dumbbell can be useful, but neither is required for your first sessions.",
                ]),
                ("Progress Slowly", [
                    "Progress can mean adding a repetition, adding a set, using a slightly harder variation, increasing resistance, or improving control. Choose one kind of progress at a time.",
                    "If you add everything at once, the routine may become too hard to repeat. A simple progression is to add one or two reps per set until the exercise feels easy, then choose a slightly harder version.",
                ]),
                ("Pay Attention to Form Cues", [
                    "Good form does not need to be perfect, but it should feel controlled. Move through a comfortable range, keep breathing, and avoid rushing. If a movement feels confusing, simplify it.",
                    "For squats, use a chair target. For push-ups, start at a wall or counter. For hinges, practice moving hips back while keeping the spine comfortable. For core work, choose a version that lets you breathe.",
                ]),
                ("Balance Strength With Daily Movement", [
                    "Strength training does not replace all movement. Walking, low-impact cardio, mobility, and stretching can support an active week. The exact balance depends on your goals and schedule.",
                    "A beginner week might include two strength sessions, two walks, and a few short mobility breaks. That is enough structure to build momentum without crowding the calendar.",
                ]),
                ("Recovery Is Part of Training", [
                    "Muscles need recovery after strength work. Mild soreness can happen, especially when starting, but soreness should not be the goal. Sleep, hydration, balanced meals, and rest days help the routine continue.",
                    "If soreness is intense or lasts too long, reduce the next session. Starting easier is often smarter than proving you can do a hard workout once.",
                ]),
                ("Common Beginner Mistakes", [
                    "Common mistakes include doing too much on day one, skipping pulling movements, holding the breath, using momentum, and changing the routine before learning it. Repeat the same basic routine for a few weeks.",
                    "Another mistake is waiting until you have perfect equipment. Start with the easiest safe version and build from there.",
                ]),
                ("Make the Habit Visible", [
                    "Put your plan somewhere visible. Write two strength days on the calendar. Keep the band or shoes where you can see them. A visible cue makes it easier to start when motivation is low.",
                    "Track sessions with a check mark and one note: easy, medium, or hard. That is enough feedback for a beginner routine.",
                ]),
                ("When to Seek Coaching", [
                    "If you have pain, past injuries, balance concerns, or feel unsure about form, a qualified trainer, physical therapist, or clinician can help. Support can make the beginning safer and more confident.",
                    "Strength training should feel challenging but learnable. You do not need to master everything before starting, but you should feel able to move safely.",
                ]),
            ],
            [
                ("Strength Training Basics", "/strength-training-basics"),
                ("Beginner Home Workout Plan", "/beginner-home-workout-plan"),
                ("Exercise as a Sustainable Habit", "/exercise-sustainable-habit"),
                ("Post-Workout Recovery Tips", "/post-workout-recovery-tips"),
            ],
        ),
    },
    {
        "title": "Daily Mobility Routine: Small Movement Breaks for Real Life",
        "slug": "daily-mobility-routine",
        "category": "Fitness",
        "keyword": "daily mobility routine",
        "meta_title": "Daily Mobility Routine",
        "meta_description": "Try a daily mobility routine with small movement breaks for hips, shoulders, spine, ankles, and long sitting days.",
        "excerpt": "A daily mobility routine built around small movement breaks for hips, shoulders, spine, ankles, and everyday stiffness.",
        "image": "daily-mobility-routine.png",
        "image_alt": "daily mobility routine",
        "content": article(
            [
                "A daily mobility routine can be short, gentle, and practical. Mobility is about moving joints through comfortable ranges with control. It does not need to look impressive or take a full workout block.",
                "For many people, the best mobility routine is a set of small movement breaks that reduce stiffness from sitting, repetitive tasks, or long periods in one position. This guide is general education, not a treatment plan.",
            ],
            [
                ("Think of Mobility as Movement Practice", [
                    "Mobility is not just stretching. It includes controlled movement, range of motion, balance, coordination, and awareness. A mobility routine might include shoulder circles, hip circles, ankle rocks, gentle spinal rotation, and slow squats to a comfortable depth.",
                    "The goal is to move smoothly and notice how your body feels. You are not trying to force maximum flexibility.",
                ]),
                ("Use a Five-Minute Daily Routine", [
                    "<ul><li>Neck turns: 30 seconds, slow and comfortable.</li><li>Shoulder circles: 30 seconds each direction.</li><li>Cat-cow or standing spine waves: 60 seconds.</li><li>Hip circles or standing hip shifts: 60 seconds.</li><li>Ankle rocks or calf raises: 60 seconds.</li><li>Slow sit-to-stand or supported squat: 60 seconds.</li></ul>",
                    "Use support if needed. The routine can be done near a desk, next to a bed, or before a walk.",
                ]),
                ("Focus on Comfort, Not Range", [
                    "Mobility should feel controlled. If a movement pinches, hurts, or feels unstable, reduce the range or choose a different movement. Bigger range is not automatically better.",
                    "A comfortable small circle can be more useful than a large forced circle. The routine should leave you feeling more aware, not irritated.",
                ]),
                ("Use Mobility During Work Breaks", [
                    "If you sit for long periods, mobility breaks can help interrupt stiffness. Stand, roll the shoulders, rotate gently, move the ankles, and shift the hips. Even two minutes can create a useful reset.",
                    "Pair mobility with things you already do: before coffee, after a meeting, before lunch, or after shutting down the computer.",
                ]),
                ("Choose Movements by Body Area", [
                    "For shoulders, try circles, wall slides, or gentle reaches. For hips, try hip circles, supported lunges, or sit-to-stand practice. For ankles, try rocks, circles, or calf raises. For the spine, try gentle rotation or cat-cow variations.",
                    "You do not need every movement every day. Choose the areas that feel most affected by your routine.",
                ]),
                ("Mobility Before Exercise", [
                    "A short mobility warm-up can prepare you for walking, strength training, or low-impact cardio. Move the joints you plan to use, gradually increase pace, and avoid long forced holds before activity.",
                    "For a walk, move ankles, hips, and shoulders. For strength work, practice the movement pattern lightly before adding resistance.",
                ]),
                ("Mobility After Exercise", [
                    "After exercise, mobility can become slower and calmer. Use it to check in with how your body feels. Gentle hip, shoulder, ankle, and back movements can be part of a cool-down.",
                    "If you feel unusually sore, keep movements easy. Recovery days are not the time to force uncomfortable positions.",
                ]),
                ("Make It a Daily Anchor", [
                    "A mobility anchor is a predictable moment when the routine happens. Morning, lunch, after work, or before bed can all work. The best time is the one you will remember.",
                    "Keep the routine small enough to do on low-motivation days. A five-minute routine repeated often can be more useful than a complex routine that rarely happens.",
                ]),
                ("Common Mistakes", [
                    "Common mistakes include moving too fast, forcing range, ignoring pain, and changing movements constantly. Repeat a few movements long enough to learn what normal feels like for you.",
                    "Another mistake is expecting mobility to replace strength, cardio, sleep, or recovery. Mobility supports movement, but it is one part of a broader wellness routine.",
                ]),
                ("Track What Changes", [
                    "Notice whether mobility breaks make sitting days easier, help you start workouts, reduce stiffness, or improve body awareness. These are practical wins.",
                    "Do not worry about dramatic flexibility changes at first. The routine is working if it helps you move more comfortably and consistently.",
                ]),
                ("When Mobility Needs Professional Help", [
                    "If a joint feels unstable, painful, locked, swollen, or limited in a way that affects daily life, get professional guidance. A clinician or physical therapist can help identify what kind of movement is appropriate.",
                    "Mobility should feel supportive. It should not become a way to push through symptoms that need attention.",
                ]),
            ],
            [
                ("Stretching Routine for Desk Workers", "/stretching-routine-desk-workers"),
                ("Beginner Stretching Routine", "/beginner-stretching-routine"),
                ("Better Breaks for Remote Work", "/better-breaks-remote-work"),
                ("Exercise as a Sustainable Habit", "/exercise-sustainable-habit"),
            ],
        ),
    },
    {
        "title": "Rest Day Routine for Beginners: Recover Without Losing Momentum",
        "slug": "rest-day-routine-for-beginners",
        "category": "Fitness",
        "keyword": "rest day routine for beginners",
        "meta_title": "Rest Day Routine for Beginners",
        "meta_description": "Build a beginner rest day routine with light movement, recovery habits, sleep, hydration, meals, and realistic training momentum.",
        "excerpt": "A beginner rest day routine that supports recovery, light movement, and consistency without treating rest like failure.",
        "image": "rest-day-routine-for-beginners.png",
        "image_alt": "rest day routine for beginners",
        "content": article(
            [
                "Rest days are part of a sustainable fitness routine. They do not mean you are losing momentum. They give your body and mind a chance to recover so movement can continue over time.",
                "For beginners, rest days can feel confusing. Should you do nothing? Should you stretch? Should you walk? The answer depends on how you feel, what you did recently, and what helps you return to activity without burnout.",
            ],
            [
                ("What a Rest Day Is For", [
                    "A rest day gives your body time to recover from training stress. Strength work, cardio, long walks, and new routines can all create fatigue. Recovery helps the next session feel more manageable.",
                    "Rest also supports motivation. If every day feels demanding, the routine may become hard to sustain. Planned rest lowers pressure and keeps fitness from becoming all-or-nothing.",
                ]),
                ("Choose Rest or Active Recovery", [
                    "Some rest days are true rest: gentle daily activities, no workout, and extra recovery. Other days are active recovery: easy walking, light mobility, stretching, or relaxed movement.",
                    "Active recovery should feel easy. It should not secretly become another workout. If you finish more tired than you started, reduce the intensity next time.",
                ]),
                ("Try a Simple Rest Day Routine", [
                    "<ul><li>Sleep: protect a realistic bedtime or wake time.</li><li>Hydration: drink with meals and keep water visible.</li><li>Food: include protein, produce, and carbohydrates.</li><li>Movement: take an easy walk or five-minute mobility break if it feels good.</li><li>Reflection: note what felt hard or helpful in the last workout.</li></ul>",
                    "This routine supports recovery without making rest days complicated.",
                ]),
                ("Use Light Movement Wisely", [
                    "Light movement can help some people feel better on rest days. Walking, gentle cycling, stretching, or mobility can reduce stiffness and keep the habit of showing up.",
                    "However, light movement is optional. If you are very tired, sore, sick, or stressed, a quieter rest day may be more appropriate.",
                ]),
                ("Eat Enough to Recover", [
                    "Some beginners unintentionally under-eat on rest days because they think less exercise means they should restrict food. Recovery still needs energy, protein, fluids, and balanced meals.",
                    "A balanced plate with protein, produce, fiber-rich carbohydrates, and flavor can support rest days just as much as training days.",
                ]),
                ("Sleep Matters", [
                    "Sleep is one of the most important recovery habits. If training feels harder than usual, look at sleep before assuming you need a new program.",
                    "A rest day can be a good time to make the evening calmer, reduce late scrolling, or prepare for the next morning.",
                ]),
                ("Review Your Training Load", [
                    "Use rest days to notice patterns. Are you sore every time? Are workouts too long? Are you skipping warm-ups? Are you recovering well between sessions?",
                    "These observations can help you adjust. A beginner routine should challenge you lightly while still feeling repeatable.",
                ]),
                ("Avoid Rest Day Guilt", [
                    "Rest day guilt is common, especially when motivation is high. Remind yourself that recovery is part of the plan. You are not falling behind by resting; you are creating room to continue.",
                    "If guilt shows up, keep a small rest day habit such as a walk, stretch, or planning tomorrow's workout. This can preserve momentum without overtraining.",
                ]),
                ("Plan the Next Session", [
                    "Before the rest day ends, decide when the next workout will happen and what it will be. Keep it simple: a walk, strength session, mobility routine, or low-impact cardio.",
                    "A clear next step prevents rest from turning into uncertainty. It also reduces the need to make a decision when you are busy.",
                ]),
                ("When to Take Extra Rest", [
                    "Take extra rest if you feel unusually exhausted, sick, injured, or mentally overloaded. Persistent pain, swelling, dizziness, chest pain, or severe symptoms need medical attention.",
                    "Beginners often improve faster by recovering well than by pushing through every warning sign.",
                ]),
                ("Build a Weekly Rhythm", [
                    "A simple beginner rhythm might include two strength days, two cardio or walking days, one mobility day, and two rest or active recovery days. Adjust based on your life.",
                    "The best rhythm is one you can repeat. Fitness grows from cycles of effort and recovery, not constant pressure.",
                ]),
            ],
            [
                ("Post-Workout Recovery Tips", "/post-workout-recovery-tips"),
                ("Exercise as a Sustainable Habit", "/exercise-sustainable-habit"),
                ("Daily Mobility Routine", "/daily-mobility-routine"),
                ("Better Sleep Routine", "/better-sleep-routine"),
            ],
        ),
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


def existing_attachment_id(slug: str) -> str | None:
    attachments_json = run_wp(
        "post",
        "list",
        "--post_type=attachment",
        "--post_mime_type=image",
        "--fields=ID,post_name",
        "--format=json",
    )
    attachments = json.loads(attachments_json or "[]")
    for attachment in attachments:
        post_name = str(attachment.get("post_name", ""))
        if post_name == slug or post_name.startswith(f"{slug}-"):
            return str(attachment["ID"])
    return None


def set_featured_image(post_id: str, post: dict[str, object]) -> None:
    slug = str(post["slug"])
    attachment_id = existing_attachment_id(slug)
    if not attachment_id:
        attachment_id = run_wp(
            "media",
            "import",
            str(IMAGE_DIR / str(post["image"])),
            f"--title={post['title']}",
            f"--alt={post['image_alt']}",
            "--porcelain",
        )
    run_wp("post", "meta", "update", post_id, "_thumbnail_id", attachment_id)


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
    set_featured_image(post_id, post)
    return f"{action}: {post_id} {slug}"


def main() -> None:
    for post in POSTS:
        print(publish(post))


if __name__ == "__main__":
    main()
