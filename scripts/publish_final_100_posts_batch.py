import json
import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
IMAGE_DIR = Path("/tmp/vitalbloom-drafts")
TODAY = "2026-06-02"

COMMON_SOURCES = [
    {
        "title": "Stress",
        "url": "https://www.nimh.nih.gov/health/publications/stress/index.shtml",
        "publisher": "National Institute of Mental Health",
        "accessedAt": TODAY,
    },
    {
        "title": "Physical Activity Basics and Your Health",
        "url": "https://www.cdc.gov/physicalactivity/basics/index.htm",
        "publisher": "Centers for Disease Control and Prevention",
        "accessedAt": TODAY,
    },
    {
        "title": "About Sleep",
        "url": "https://www.cdc.gov/sleep/about/index.html",
        "publisher": "Centers for Disease Control and Prevention",
        "accessedAt": TODAY,
    },
    {
        "title": "MyPlate Nutrition Information for Adults",
        "url": "https://www.myplate.gov/browse-by-audience/view-all-audiences/adults",
        "publisher": "U.S. Department of Agriculture",
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
    html.append("<p>Disclaimer: This article is for general educational purposes only and is not medical, nutrition, fitness, or mental health advice. For persistent symptoms, medical conditions, injury, pregnancy-related needs, or major lifestyle changes, consult a qualified professional.</p>")
    return "\n".join(html)


POSTS = [
    {
        "title": "How to Build a Simple Wellness Plan That Fits Real Life",
        "slug": "how-to-build-a-simple-wellness-plan",
        "category": "Wellness",
        "keyword": "simple wellness plan",
        "meta_title": "How to Build a Simple Wellness Plan",
        "meta_description": "Build a simple wellness plan with realistic steps for sleep, meals, movement, stress, hydration, and weekly review.",
        "excerpt": "A realistic simple wellness plan for sleep, meals, movement, stress, hydration, and weekly habit review.",
        "image": "how-to-build-a-simple-wellness-plan.png",
        "image_alt": "simple wellness plan",
        "content": article(
            [
                "A simple wellness plan helps you turn vague goals into daily choices. Instead of trying to improve everything at once, a useful plan focuses on a few basics: sleep, meals, movement, stress recovery, hydration, and connection.",
                "The best wellness plan is not the most ambitious one. It is the one you can repeat during normal weeks, adjust during busy weeks, and restart without shame after a difficult week.",
            ],
            [
                ("Choose Your Main Support Area", [
                    "Start by choosing the area that would make the biggest difference right now. It might be sleep, food, movement, stress, screen boundaries, or recovery. Choosing one focus gives the plan direction.",
                    "If everything feels important, choose the area that affects the others most. For many people, sleep or meal rhythm is a strong starting point because low energy makes every other habit harder.",
                ]),
                ("Use the Four-Part Wellness Map", [
                    "A simple map includes body basics, movement, recovery, and environment. Body basics include meals, fluids, and sleep. Movement includes walking, stretching, mobility, or strength. Recovery includes rest, stress resets, and connection. Environment includes cues that make habits easier.",
                    "This map keeps the plan balanced. It prevents wellness from becoming only exercise, only food, or only productivity.",
                ]),
                ("Write Small Actions", [
                    "Turn each area into one small action. For sleep, the action might be charging your phone away from the bed. For meals, it might be keeping one easy breakfast ready. For movement, it might be a 10-minute walk three times per week.",
                    "Small actions work because they are specific. A goal like be healthier is hard to act on. A step like walk after lunch on Monday, Wednesday, and Friday is easier to follow.",
                ]),
                ("Make a Busy-Week Version", [
                    "Every plan needs a busy-week version. If your normal movement goal is 30 minutes, the busy version may be five minutes. If your normal dinner plan involves cooking, the busy version may be a pantry meal.",
                    "This protects consistency. You do not have to abandon the plan just because life becomes full. You adjust the size of the habit.",
                ]),
                ("Use Cues Instead of Motivation", [
                    "Motivation changes. Cues are more reliable. Put shoes by the door, keep water visible, set a bedtime reminder, place breakfast ingredients together, or block a walking time on your calendar.",
                    "A cue makes the next action obvious. When the environment supports the plan, you need less willpower.",
                ]),
                ("Plan for Recovery", [
                    "Recovery belongs in the plan, not as an afterthought. Include a wind-down routine, rest day, stress reset, phone boundary, quiet break, or weekly check-in. Without recovery, healthy habits can start to feel like another demand.",
                    "Recovery helps the plan stay humane. It gives your body and mind a way to return to baseline.",
                ]),
                ("Track Lightly", [
                    "Track only what helps. A check mark, one sentence, or a weekly review can be enough. Avoid tracking so much that the plan becomes a burden.",
                    "Useful tracking answers simple questions: Did I do the habit? Did it help? What made it easier or harder? What should change next week?",
                ]),
                ("Review Weekly", [
                    "Once a week, review the plan. Keep what worked, shrink what felt too big, and remove habits that do not fit. A wellness plan should evolve as your schedule, energy, and needs change.",
                    "The review is not about judging yourself. It is about making the next week easier.",
                ]),
                ("Avoid Common Planning Mistakes", [
                    "Common mistakes include adding too many habits, choosing actions that depend on perfect conditions, copying someone else's routine, and forgetting recovery. Another mistake is making the plan so strict that one missed day feels like failure.",
                    "A resilient plan expects interruptions. It includes a restart path.",
                ]),
                ("A Simple Starter Plan", [
                    "<ul><li>Sleep: dim lights and charge phone away from bed three nights per week.</li><li>Meals: prepare one easy breakfast and one backup dinner.</li><li>Movement: walk 10 minutes three times per week.</li><li>Stress: use one two-minute breathing or grounding reset daily.</li><li>Review: check what worked every Sunday or Monday.</li></ul>",
                    "This plan is modest on purpose. Once it feels steady, you can add more.",
                ]),
            ],
            [
                ("Daily Wellness Routine for Beginners", "/daily-wellness-routine-beginners"),
                ("Healthy Habits When Life Feels Busy", "/healthy-habits-when-life-feels-busy"),
                ("Simple Self-Care Checklist", "/simple-self-care-checklist"),
                ("Beginner Guide to Balanced Living", "/beginner-guide-to-balanced-living"),
            ],
        ),
    },
    {
        "title": "Healthy Routine After Travel: Reset Gently Without Overcorrecting",
        "slug": "healthy-routine-after-travel",
        "category": "Wellness",
        "keyword": "healthy routine after travel",
        "meta_title": "Healthy Routine After Travel",
        "meta_description": "Reset a healthy routine after travel with sleep, hydration, simple meals, light movement, unpacking, and realistic planning.",
        "excerpt": "A gentle post-travel reset routine for sleep, meals, hydration, movement, unpacking, and returning to normal habits.",
        "image": "healthy-routine-after-travel.png",
        "image_alt": "healthy routine after travel",
        "content": article(
            [
                "Travel can disrupt sleep, meals, movement, hydration, digestion, and work rhythms. A healthy routine after travel should help you return gently, not punish yourself for being out of routine.",
                "The goal is to reestablish basics in the first 24 to 48 hours: light, fluids, simple meals, movement, unpacking, and a realistic bedtime. You do not need a dramatic reset.",
            ],
            [
                ("Start With Light and Wake Time", [
                    "After travel, your body may feel shifted. Morning light and a reasonable wake time can help signal that normal rhythm is returning. Open curtains, step outside, or sit near a bright window.",
                    "If you crossed time zones, be patient. Keep the first day simple and avoid stacking too many demands on a tired body.",
                ]),
                ("Hydrate Before You Optimize", [
                    "Travel often changes fluid intake. Before planning a perfect diet or workout, drink water or another appropriate fluid and eat something steady. Hydration and food basics can make the rest of the day feel less chaotic.",
                    "Pair fluids with meals so you do not have to think about it constantly. If you drank more caffeine or alcohol than usual while traveling, return gradually to your normal rhythm.",
                ]),
                ("Choose Simple Post-Travel Meals", [
                    "Use meals that are easy to assemble: yogurt and fruit, eggs and toast, rice with beans and vegetables, soup and bread, or a snack plate with protein and produce.",
                    "Post-travel meals should reduce friction. They do not need to compensate for travel food. They simply help your body feel steady again.",
                ]),
                ("Move Gently", [
                    "Long sitting, flights, drives, and schedule changes can leave the body stiff. Try a walk, mobility routine, stretching, or gentle low-impact cardio. Keep it easy unless you feel truly ready for more.",
                    "Movement can help you reconnect with your normal routine without demanding a hard workout immediately.",
                ]),
                ("Unpack Enough to Reduce Stress", [
                    "Unpacking can become a background stressor. You do not need to unpack everything at once. Start with essentials: laundry, toiletries, chargers, medications, and anything needed for the next day.",
                    "Set a timer for 15 minutes. A partial unpack can make home feel calmer and prevent travel clutter from stretching through the week.",
                ]),
                ("Protect the First Bedtime", [
                    "The first bedtime after travel matters. Start winding down earlier than usual if possible. Lower lights, reduce screens, prepare tomorrow, and choose one calming cue.",
                    "Avoid staying up late to catch up on everything. A calmer night can make the next day easier.",
                ]),
                ("Plan the Next Day Lightly", [
                    "Write down the next day's top three priorities. Keep the list realistic. Travel recovery often takes more energy than expected, so avoid overloading the first normal day.",
                    "If work resumes immediately, choose one food support, one movement support, and one rest support before the day begins.",
                ]),
                ("Avoid Overcorrection", [
                    "A common mistake is trying to fix travel by forcing a strict diet, hard workout, or packed productivity day. Overcorrection can create more fatigue and make the routine harder to restart.",
                    "Return to basics instead. Basics are powerful because they are repeatable: sleep, meals, fluids, movement, and planning.",
                ]),
                ("Use a 48-Hour Travel Reset", [
                    "<ul><li>Day 1: light, fluids, simple meals, unpack essentials, gentle movement.</li><li>Night 1: screen boundary and earlier wind-down.</li><li>Day 2: grocery basics, laundry, normal movement, top priorities.</li><li>Night 2: return to usual sleep cue.</li></ul>",
                    "This gives you structure without making travel recovery another high-pressure routine.",
                ]),
                ("When Recovery Takes Longer", [
                    "If travel involved illness, intense stress, jet lag, grief, or major disruption, recovery may take longer. Adjust expectations and seek care if symptoms are concerning or persistent.",
                    "A healthy routine after travel should support your return, not rush it.",
                ]),
            ],
            [
                ("Sleep Debt Recovery Guide", "/sleep-debt-recovery-guide"),
                ("Simple Grocery List for Healthy Eating", "/simple-grocery-list-for-healthy-eating"),
                ("Daily Mobility Routine", "/daily-mobility-routine"),
                ("How to Build a Weekly Reset Routine", "/how-to-build-a-weekly-reset-routine"),
            ],
        ),
    },
    {
        "title": "How to Stay Consistent With Healthy Habits Without Perfection",
        "slug": "how-to-stay-consistent-with-healthy-habits",
        "category": "Wellness",
        "keyword": "stay consistent with healthy habits",
        "meta_title": "How to Stay Consistent With Healthy Habits",
        "meta_description": "Stay consistent with healthy habits using small actions, cues, flexible routines, recovery, tracking, and realistic restart plans.",
        "excerpt": "A realistic guide to staying consistent with healthy habits without perfection, shame, or all-or-nothing routines.",
        "image": "how-to-stay-consistent-with-healthy-habits.png",
        "image_alt": "stay consistent with healthy habits",
        "content": article(
            [
                "Consistency with healthy habits does not mean doing everything perfectly every day. It means returning to supportive actions often enough that they become part of your life.",
                "Most people lose consistency when habits are too big, too vague, or too dependent on perfect conditions. A better approach uses small actions, clear cues, flexible versions, and quick restarts.",
            ],
            [
                ("Make the Habit Specific", [
                    "A vague habit is hard to repeat. Instead of saying exercise more, choose walk 10 minutes after lunch on Monday, Wednesday, and Friday. Instead of eat better, choose add protein to breakfast.",
                    "Specific habits are easier to start because the next action is clear. Clarity lowers friction.",
                ]),
                ("Shrink the Habit", [
                    "If consistency is hard, make the habit smaller. Two minutes of stretching, one glass of water, one prepared snack, or a five-minute walk can keep the routine alive.",
                    "Small habits may seem too easy, but they build identity and momentum. You can grow them later.",
                ]),
                ("Use Habit Cues", [
                    "Attach the habit to something that already happens. Stretch after brushing teeth, walk after lunch, prepare breakfast while making coffee, or write tomorrow's first task after closing work.",
                    "A cue makes the habit easier to remember. Repetition links the old routine to the new action.",
                ]),
                ("Plan for Obstacles", [
                    "Consistency improves when you expect obstacles. If it rains, what is the indoor movement option? If work runs late, what is the quick dinner? If sleep is poor, what is the low-energy version?",
                    "Planning obstacles is not pessimistic. It is practical. A habit that has backup options survives longer.",
                ]),
                ("Use the Never Twice Idea Carefully", [
                    "Missing one day is normal. The useful question is how to restart quickly. Try not to let one missed habit become a week-long pause. Return with the smallest version.",
                    "Do not use this as a harsh rule. Use it as a gentle reminder that the next action matters more than the missed one.",
                ]),
                ("Track Without Pressure", [
                    "Tracking can help if it stays simple. Use check marks, a habit calendar, or one sentence per week. Avoid tracking in a way that creates shame or obsession.",
                    "The purpose of tracking is to learn what supports consistency: time of day, environment, energy level, and habit size.",
                ]),
                ("Make Habits Enjoyable Enough", [
                    "You are more likely to repeat habits that feel at least somewhat rewarding. Choose movement you do not dread, meals you enjoy, and routines that create relief.",
                    "Healthy habits do not need to be entertainment, but they should not feel like constant punishment.",
                ]),
                ("Build Recovery Into Consistency", [
                    "Consistency includes rest. If you never recover, the routine becomes unsustainable. Schedule rest days, quiet evenings, lower-effort meals, and screen breaks.",
                    "Recovery keeps the habit system from burning out. It also helps you return with more energy.",
                ]),
                ("Use Identity Gently", [
                    "Instead of saying I failed, try I am someone who restarts. This identity supports consistency without demanding perfection.",
                    "The strongest habit identity is flexible. It leaves room for travel, illness, stress, and real life.",
                ]),
                ("Review Monthly", [
                    "Once a month, review your habits. Which ones feel natural? Which ones still require too much effort? Which ones no longer matter? Adjust the plan.",
                    "Consistency is easier when the habit stays relevant to your current life.",
                ]),
            ],
            [
                ("Small Healthy Habits", "/small-healthy-habits"),
                ("Sustainable Wellness Routine", "/sustainable-wellness-routine"),
                ("Exercise as a Sustainable Habit", "/exercise-sustainable-habit"),
                ("Healthy Habits When Life Feels Busy", "/healthy-habits-when-life-feels-busy"),
            ],
        ),
    },
    {
        "title": "Weekend Reset for Better Sleep Without Wrecking Monday",
        "slug": "weekend-reset-for-better-sleep",
        "category": "Sleep",
        "keyword": "weekend reset for better sleep",
        "meta_title": "Weekend Reset for Better Sleep",
        "meta_description": "Use a weekend reset for better sleep with wake time, light, naps, caffeine, wind-down cues, and Monday-friendly routines.",
        "excerpt": "A weekend sleep reset that helps you rest without drifting so far that Monday feels harder.",
        "image": "weekend-reset-for-better-sleep.png",
        "image_alt": "weekend reset for better sleep",
        "content": article(
            [
                "Weekends can help you recover, but they can also disrupt sleep if bedtime and wake time drift far from your weekday rhythm. A weekend reset for better sleep gives you rest without making Monday harder.",
                "The goal is not to make weekends rigid. It is to use a few sleep-friendly cues: morning light, reasonable wake time, careful naps, caffeine timing, and a calmer Sunday evening.",
            ],
            [
                ("Keep Wake Time Within Reach", [
                    "Sleeping in a little may feel good, but sleeping much later than usual can shift your rhythm. Try keeping wake time close enough that Sunday night and Monday morning are not a shock.",
                    "If you are very sleep-deprived, rest matters. Just notice whether long sleep-ins make the next night harder.",
                ]),
                ("Get Morning Light", [
                    "Morning light helps signal daytime. Open curtains, step outside, or take a short walk. This can be especially useful on weekends when the day starts slowly.",
                    "Pair light with a simple morning cue such as water, breakfast, or stretching. This gives the day structure without pressure.",
                ]),
                ("Use Naps Strategically", [
                    "A nap can help if you are tired, but long or late naps may interfere with bedtime. If you nap, keep it earlier and consider a shorter rest.",
                    "If naps leave you groggy, try quiet rest instead: lying down, reading, breathing, or taking a screen-free break.",
                ]),
                ("Watch Caffeine Timing", [
                    "Weekend caffeine can drift later because the schedule feels looser. If caffeine affects your sleep, keep a cutoff time even on weekends.",
                    "A consistent caffeine boundary can protect Sunday night and reduce the Monday morning tired cycle.",
                ]),
                ("Plan a Sunday Wind-Down", [
                    "Sunday evening is a useful reset point. Prepare Monday's first task, choose breakfast, set clothes, reduce screens, and dim lights. Keep the routine short so it does not feel like another chore.",
                    "A Sunday wind-down reduces bedtime worry because the next day has a plan.",
                ]),
                ("Avoid Revenge Bedtime", [
                    "If the weekend felt too full or not restful enough, you may want to stay up late to reclaim time. This is understandable, but it can make Monday harder.",
                    "Choose one enjoyable activity earlier in the evening, then protect a realistic bedtime. Rest and enjoyment can both fit with a boundary.",
                ]),
                ("Use Weekend Movement", [
                    "Gentle movement can support energy and sleep. A walk, stretching, mobility, low-impact cardio, or outdoor activity can help the weekend feel better without becoming intense.",
                    "Avoid using exercise as punishment for weekday choices. Use it as a rhythm cue and stress release.",
                ]),
                ("Do a Light Meal Reset", [
                    "Weekend meals may look different. A light reset can mean grocery basics, one simple breakfast, and one easy dinner for Monday. You do not need a strict food plan.",
                    "Balanced meals with protein, produce, fiber-rich carbohydrates, and fluids can support energy after a loose weekend.",
                ]),
                ("Create a Monday Buffer", [
                    "If possible, reduce Monday morning friction. Pack a bag, set out clothes, prepare coffee or breakfast, and write the first task. This can make Monday feel less abrupt.",
                    "A sleep reset works better when the morning after it is not chaotic.",
                ]),
                ("Keep Weekends Human", [
                    "Weekends are for rest, connection, errands, fun, and recovery. The goal is not to control every hour. Choose a few anchors that protect sleep while leaving room for life.",
                    "A flexible weekend rhythm can make both Sunday night and Monday morning easier.",
                ]),
            ],
            [
                ("Weekend Sleep Schedule", "/weekend-sleep-schedule"),
                ("Sleep-Friendly Evening Routine", "/sleep-friendly-evening-routine"),
                ("Sleep Debt Recovery Guide", "/sleep-debt-recovery-guide"),
                ("How to Reset After a Bad Night's Sleep", "/how-to-reset-after-a-bad-night-sleep"),
            ],
        ),
    },
    {
        "title": "Simple Energy-Boosting Habits for Steadier Days",
        "slug": "simple-energy-boosting-habits",
        "category": "Wellness",
        "keyword": "simple energy boosting habits",
        "meta_title": "Simple Energy-Boosting Habits",
        "meta_description": "Try simple energy-boosting habits with sleep, hydration, balanced meals, light, movement, breaks, and realistic stress recovery.",
        "excerpt": "Simple energy-boosting habits for steadier days, built around sleep, hydration, meals, light, movement, and breaks.",
        "image": "simple-energy-boosting-habits.png",
        "image_alt": "simple energy boosting habits",
        "content": article(
            [
                "Energy is not only about motivation. It is affected by sleep, meals, hydration, movement, light, stress, breaks, health, and workload. Simple energy-boosting habits work best when they support the basics instead of relying on quick fixes.",
                "If tiredness is severe, persistent, or unusual, it is worth getting professional guidance. For everyday low energy, a few practical habits can make the day feel steadier.",
            ],
            [
                ("Start With Sleep Opportunity", [
                    "Energy often begins the night before. Protect one sleep cue: a consistent wake time, a screen boundary, a caffeine cutoff, or a calmer wind-down. You do not need to fix every sleep habit at once.",
                    "Better sleep habits can make daytime energy more reliable over time. Start with the cue that feels most realistic.",
                ]),
                ("Use Morning Light", [
                    "Morning light can help signal wakefulness. Open curtains, step outside, or sit near a bright window. Pair light with water or breakfast so the habit is easy to remember.",
                    "This is especially helpful after a poor night or a slow morning.",
                ]),
                ("Eat for Steady Energy", [
                    "Balanced meals can reduce energy swings. Aim for protein, produce, fiber-rich carbohydrates, and flavor. For snacks, pair protein with fiber, such as yogurt with fruit or hummus with crackers and vegetables.",
                    "Skipping meals or relying only on caffeine can make energy feel more unstable for some people.",
                ]),
                ("Hydrate With Cues", [
                    "Hydration does not need to be complicated. Drink with meals, keep water visible, and refill during transitions. If plain water is hard to remember, use flavor, tea, or another suitable option.",
                    "Fluid needs vary, but visible cues help many people notice hydration before they feel depleted.",
                ]),
                ("Move Before You Crash", [
                    "Short movement can support alertness. Walk for five to 10 minutes, stretch, do mobility, or stand during a break. Movement does not need to be intense to be useful.",
                    "If you wait until you are completely drained, starting may be harder. Use movement earlier as a preventive reset.",
                ]),
                ("Take Real Breaks", [
                    "A real break changes your state. Looking at a different screen may not be enough. Try standing, looking outside, breathing, drinking water, or stepping away from the desk.",
                    "Short breaks can make long work blocks feel more manageable and reduce the sense of mental drag.",
                ]),
                ("Watch the Caffeine Loop", [
                    "Caffeine can help, but it can also become a loop if it replaces sleep, food, water, and breaks. Use caffeine intentionally and notice whether late caffeine affects your sleep.",
                    "Before another caffeine dose, ask whether you need a meal, water, light, or movement.",
                ]),
                ("Reduce Energy Drains", [
                    "Energy habits are not only about adding things. Remove one drain: unnecessary notifications, late work, cluttered mornings, skipped meals, or overcommitted evenings.",
                    "Reducing a drain can be more effective than adding another wellness task.",
                ]),
                ("Use an Afternoon Reset", [
                    "<ul><li>Drink water.</li><li>Eat a balanced snack if hungry.</li><li>Step into light or look outside.</li><li>Move for three to five minutes.</li><li>Choose the next single task.</li></ul>",
                    "This reset can help when the day starts to blur.",
                ]),
                ("Know When Energy Needs Care", [
                    "If fatigue is new, severe, persistent, or paired with symptoms like shortness of breath, pain, dizziness, mood changes, or sleep disruption, seek medical guidance.",
                    "Habits can support energy, but they should not replace care when something deeper may be happening.",
                ]),
            ],
            [
                ("Morning Routine for Low-Energy Days", "/morning-routine-for-low-energy-days"),
                ("Hydration Tracker Printable", "/hydration-tracker-printable"),
                ("Healthy Snacks for Work", "/healthy-snacks-for-work"),
                ("Better Breaks for Remote Work", "/better-breaks-remote-work"),
            ],
        ),
    },
    {
        "title": "Beginner Guide to Balanced Living: A Practical Wellness Framework",
        "slug": "beginner-guide-to-balanced-living",
        "category": "Wellness",
        "keyword": "beginner guide to balanced living",
        "meta_title": "Beginner Guide to Balanced Living",
        "meta_description": "Use this beginner guide to balanced living with practical habits for sleep, food, movement, stress, screens, and weekly recovery.",
        "excerpt": "A beginner guide to balanced living with practical habits for sleep, food, movement, stress, screens, and recovery.",
        "image": "beginner-guide-to-balanced-living.png",
        "image_alt": "beginner guide to balanced living",
        "content": article(
            [
                "Balanced living is not about perfectly dividing your time or doing every healthy habit every day. It is about building enough support into your routine that your body, mind, work, relationships, and recovery all have some room.",
                "For beginners, balanced living starts with basics: sleep, nourishing meals, regular movement, stress recovery, digital boundaries, and weekly reflection. The goal is a sustainable rhythm, not a flawless lifestyle.",
            ],
            [
                ("Redefine Balance", [
                    "Balance does not mean every day looks equal. Some days focus on work, some on rest, some on family, some on errands, and some on recovery. A balanced life is built across a week or season, not a single perfect day.",
                    "This perspective reduces pressure. If one day is demanding, the question becomes how to recover and rebalance, not how to make every day ideal.",
                ]),
                ("Start With Body Foundations", [
                    "Sleep, food, hydration, and movement are foundations. They influence focus, mood, stress tolerance, and energy. Choose one small habit in each area or start with the area that needs the most support.",
                    "For example, protect a bedtime cue, keep an easy breakfast ready, walk three times per week, and drink water with meals.",
                ]),
                ("Build Emotional Recovery", [
                    "Balanced living includes emotional recovery. Stress needs a place to go. Use journaling, breathing, connection, boundaries, therapy, prayer, time outside, or quiet breaks depending on what fits your life.",
                    "Recovery does not have to be dramatic. A two-minute pause can be the difference between reacting automatically and choosing the next step.",
                ]),
                ("Create Digital Boundaries", [
                    "Screens can support life, but they can also crowd out rest and attention. Choose one digital boundary: no phone in bed, fewer notifications, a focus block, or a screen-free meal.",
                    "Digital balance is not about rejecting technology. It is about making sure technology does not decide every transition for you.",
                ]),
                ("Use Simple Planning", [
                    "A weekly reset can help balanced living become practical. Review the calendar, plan a few meals, schedule movement, choose a sleep cue, and protect one recovery window.",
                    "Planning should reduce stress, not create a rigid script. Leave room for life to change.",
                ]),
                ("Practice Flexible Consistency", [
                    "Flexible consistency means keeping habits in some form even when conditions change. If you cannot do the full workout, walk five minutes. If you cannot cook, assemble a balanced snack plate. If bedtime is late, return to the routine the next night.",
                    "This approach keeps you from restarting from zero every time life gets busy.",
                ]),
                ("Include Relationships and Support", [
                    "Balanced living is not only personal habits. Connection matters. Make room for supportive relationships, honest conversations, shared meals, or asking for help.",
                    "If you are carrying too much alone, no checklist will fully solve that. Support is part of wellness.",
                ]),
                ("Watch for Over-Optimization", [
                    "Wellness can become stressful if every choice is optimized. If your routine makes you anxious, guilty, or rigid, simplify it. Healthy habits should support your life, not shrink it.",
                    "Choose a few practices that create real benefit and let the rest be optional.",
                ]),
                ("Use a Balanced Living Checklist", [
                    "<ul><li>Did I protect one sleep cue?</li><li>Did I eat something steady?</li><li>Did I move in a way that fits today?</li><li>Did I take one real break?</li><li>Did I connect with someone or ask for support?</li><li>Did I reduce one unnecessary drain?</li></ul>",
                    "Use the checklist as a reflection tool, not a test.",
                ]),
                ("Let Balance Change With Seasons", [
                    "Your balance will change during busy work seasons, travel, caregiving, illness, school, or major life transitions. Adjust habit size instead of forcing the same routine forever.",
                    "Balanced living is a practice of returning, adjusting, and caring for the basics over time.",
                ]),
            ],
            [
                ("How to Build a Simple Wellness Plan", "/how-to-build-a-simple-wellness-plan"),
                ("Healthy Habits When Life Feels Busy", "/healthy-habits-when-life-feels-busy"),
                ("Digital Wellness Routine", "/digital-wellness-routine"),
                ("Sustainable Wellness Routine", "/sustainable-wellness-routine"),
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
