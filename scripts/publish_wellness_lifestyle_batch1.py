import json
import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
IMAGE_DIR = Path("/tmp/vitalbloom-drafts")
TODAY = "2026-06-02"

COMMON_SOURCES = [
    {
        "title": "Stress",
        "url": "https://www.nimh.nih.gov/health/publications/stress",
        "publisher": "National Institute of Mental Health",
        "accessedAt": TODAY,
    },
    {
        "title": "Adult Activity: An Overview",
        "url": "https://www.cdc.gov/physical-activity-basics/guidelines/adults.html",
        "publisher": "Centers for Disease Control and Prevention",
        "accessedAt": TODAY,
    },
    {
        "title": "Sleep Deprivation and Deficiency: Healthy Sleep Habits",
        "url": "https://www.nhlbi.nih.gov/health/sleep-deprivation/healthy-sleep-habits",
        "publisher": "National Heart, Lung, and Blood Institute",
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
    html.append("<p>Disclaimer: This article is for general educational purposes only and is not medical or mental health advice. If symptoms, stress, low mood, sleep problems, or exhaustion persist, consider support from a qualified healthcare professional.</p>")
    return "\n".join(html)


POSTS = [
    {
        "title": "Morning Routine for Low-Energy Days: Gentle First Steps",
        "slug": "morning-routine-for-low-energy-days",
        "category": "Wellness",
        "keyword": "morning routine for low energy days",
        "meta_title": "Morning Routine for Low-Energy Days",
        "meta_description": "Use a gentle morning routine for low-energy days with light, hydration, easy movement, simple breakfast, and realistic priorities.",
        "excerpt": "A gentle morning routine for low-energy days, built around light, hydration, simple movement, food, and lower-pressure planning.",
        "image": "morning-routine-for-low-energy-days.png",
        "image_alt": "morning routine for low energy days",
        "content": article(
            [
                "Low-energy mornings happen. Poor sleep, stress, busy weeks, long workdays, illness recovery, or emotional overload can make it hard to start the day with momentum. A morning routine for low-energy days should not demand peak motivation. It should help you begin gently.",
                "The goal is to support the day without pretending you feel fully charged. A useful routine gives you light, fluids, food, movement, and one clear priority while keeping the pressure low enough to actually follow.",
            ],
            [
                ("Start With the Smallest Wake-Up Cue", [
                    "Choose one cue that tells your body the day has started. Open curtains, sit up, put both feet on the floor, drink water, or step into natural light. The cue can be tiny. On low-energy days, tiny is often exactly right.",
                    "Avoid judging the morning too early. Feeling slow at wake-up does not mean the entire day is lost. A small cue gives your system a chance to shift gradually.",
                ]),
                ("Use Light Before Productivity", [
                    "Morning light can help anchor your daily rhythm and make the morning feel less foggy. If possible, open curtains or step outside for a few minutes. If the weather is poor, sit near a bright window.",
                    "Do this before checking stressful messages when you can. Light is a body cue. Email, news, and social feeds are attention demands. Starting with the body cue can make the next step easier.",
                ]),
                ("Hydrate and Eat Something Simple", [
                    "Low energy can feel worse when you are under-fueled or dehydrated. Drink water or another fluid that fits your needs, then choose a simple breakfast or snack if you can tolerate it.",
                    "Keep options easy: yogurt and fruit, toast with nut butter, oats, eggs, a smoothie, or leftovers. The meal does not need to be perfect. It just needs to support your body enough to move into the day.",
                ]),
                ("Try a Two-Minute Movement Reset", [
                    "<ul><li>Roll shoulders slowly.</li><li>Turn the neck gently.</li><li>Reach overhead once or twice.</li><li>March in place or walk around the room.</li><li>Take three slow breaths.</li></ul>",
                    "Movement should feel supportive, not punishing. If a full workout is unrealistic, a two-minute reset still counts as caring for your energy.",
                ]),
                ("Pick One Priority", [
                    "Low-energy days become harder when every task feels equally urgent. Write down one priority that would make the day feel steadier. It might be a work task, a household task, a call, a meal, or rest.",
                    "After choosing one priority, choose a first step. Make it small enough that you can begin even if motivation is low.",
                ]),
                ("Use a Lower-Pressure Version of Your Routine", [
                    "If your normal routine includes journaling, exercise, meal prep, and a full planning session, create a low-energy version. Journal one sentence. Walk five minutes. Prepare one meal component. Choose three tasks instead of ten.",
                    "This keeps the routine alive without turning it into a performance test. The low-energy version is not a failure. It is the version designed for real life.",
                ]),
                ("Avoid the Shame Loop", [
                    "Low energy can trigger self-criticism: I should be doing more, I am behind, everyone else is moving faster. That shame often drains more energy. Try naming the day neutrally: this is a low-energy morning, so I am using a low-energy plan.",
                    "Neutral language helps you respond instead of spiral. It turns the morning into a practical adjustment rather than a personal flaw.",
                ]),
                ("Protect Your Attention Early", [
                    "If possible, delay the most chaotic inputs. Do not start with ten tabs, a crowded inbox, or social feeds if those make you feel scattered. Give yourself a short buffer for light, water, food, and the first task.",
                    "If you must check messages early, set a timer and write down only what needs action. Then return to the routine.",
                ]),
                ("When Low Energy Repeats", [
                    "Occasional low-energy mornings are normal. Repeated exhaustion deserves attention. Look at sleep, workload, stress, food, hydration, movement, health conditions, medications, and mood.",
                    "If fatigue is persistent, severe, unexplained, or affecting daily life, professional guidance can help. A routine can support you, but it should not replace care.",
                ]),
                ("A 15-Minute Low-Energy Morning Plan", [
                    "Use this simple plan: five minutes for light and water, five minutes for food or preparing food, three minutes for gentle movement, and two minutes to choose one priority. If 15 minutes is too much, cut it in half.",
                    "The point is to create enough structure to begin. Once the day is moving, you can decide what else is realistic.",
                ]),
            ],
            [
                ("Daily Wellness Routine for Beginners", "/daily-wellness-routine-beginners"),
                ("Why You Wake Up Tired", "/why-you-wake-up-tired"),
                ("Morning Light and Sleep", "/morning-light-and-sleep"),
                ("Mindful Morning Routine", "/mindful-morning-routine"),
            ],
        ),
    },
    {
        "title": "Healthy Habits When Life Feels Busy: A Realistic Guide",
        "slug": "healthy-habits-when-life-feels-busy",
        "category": "Wellness",
        "keyword": "healthy habits when life feels busy",
        "meta_title": "Healthy Habits When Life Feels Busy",
        "meta_description": "Build healthy habits when life feels busy with small routines for sleep, meals, movement, stress, hydration, and recovery.",
        "excerpt": "A realistic guide to healthy habits when life feels busy, focused on small routines that fit tight schedules.",
        "image": "healthy-habits-when-life-feels-busy.png",
        "image_alt": "healthy habits when life feels busy",
        "content": article(
            [
                "When life feels busy, healthy habits can start to feel like one more thing you are failing to do. The answer is not always a stricter routine. Often, the answer is smaller habits that protect the basics: sleep, food, movement, hydration, stress recovery, and connection.",
                "Busy seasons need flexible wellness habits. A realistic routine should help you stay steady without requiring a perfect schedule or unlimited energy.",
            ],
            [
                ("Choose Baseline Habits", [
                    "Baseline habits are the smallest actions that keep you from sliding too far from your needs. They are not the ideal version. They are the minimum useful version.",
                    "Examples include drinking water with meals, taking a 10-minute walk, preparing one simple breakfast, turning off work at a set time, or doing three minutes of breathing before bed.",
                ]),
                ("Protect Sleep First", [
                    "Sleep affects energy, focus, mood, hunger, and stress tolerance. During busy seasons, protect one sleep cue: a consistent wake time, a screen boundary, a caffeine cutoff, or a simple wind-down routine.",
                    "You may not control every night, but one cue can keep sleep from becoming completely unpredictable.",
                ]),
                ("Simplify Food Decisions", [
                    "Busy weeks are easier when meals have defaults. Choose two breakfasts, two lunches, and two easy dinners you can repeat. Use the balanced plate method: protein, produce, fiber-rich carbohydrates, and flavor.",
                    "You do not need elaborate meal prep. Cook one protein, wash fruit, stock yogurt, keep frozen vegetables, or prepare a backup meal. Small food systems reduce daily decision fatigue.",
                ]),
                ("Use Movement Snacks", [
                    "If full workouts are unrealistic, use movement snacks: five-minute walks, stairs, stretching, mobility, or a short strength set. Short movement can interrupt long sitting and keep the habit alive.",
                    "The CDC encourages adults to include regular physical activity, but your routine can build gradually. Busy weeks may require smaller pieces.",
                ]),
                ("Lower the Bar Without Quitting", [
                    "A common mistake is treating busy weeks as all-or-nothing. If you cannot do the full routine, do the smallest version. If you cannot exercise 30 minutes, walk five. If you cannot cook dinner, assemble a snack plate.",
                    "Lowering the bar is not giving up. It is how habits survive real life.",
                ]),
                ("Build Recovery Into Transitions", [
                    "Transitions are natural habit points: after waking, after work, before lunch, before bed, or after a commute. Add one tiny recovery action to a transition.",
                    "Examples include three breaths before opening email, water after a meeting, stretching after logging off, or writing tomorrow's first task before bed.",
                ]),
                ("Use a Busy-Week Checklist", [
                    "<ul><li>Did I drink fluids with meals?</li><li>Did I eat at least one steady meal?</li><li>Did I move for a few minutes?</li><li>Did I protect one sleep cue?</li><li>Did I pause once before reacting to stress?</li></ul>",
                    "This checklist is not a scorecard. It is a quick reminder of the basics that keep you supported.",
                ]),
                ("Reduce Digital Friction", [
                    "Busy life often comes with more messages and more screen switching. Set one boundary: silence nonessential notifications, close work tabs after hours, or keep the phone away from the bed.",
                    "A digital boundary can reduce background stress and make it easier to rest during small pockets of time.",
                ]),
                ("Ask What Can Be Made Easier", [
                    "Instead of asking how to become more disciplined, ask what can be made easier. Put shoes by the door, keep snacks visible, prepare tomorrow's task list, move the phone charger, or use grocery staples that create fast meals.",
                    "Environment often beats willpower. Make the healthy action the obvious action.",
                ]),
                ("Review at the End of the Week", [
                    "At the end of a busy week, ask what helped most. Keep the habits that worked and remove the ones that felt unrealistic. This review helps your routine adapt instead of becoming another rigid plan.",
                    "Busy seasons change. Your habits can change with them while still protecting your health.",
                ]),
            ],
            [
                ("Sustainable Wellness Routine", "/sustainable-wellness-routine"),
                ("Small Healthy Habits", "/small-healthy-habits"),
                ("Meal Planning for Busy Weeks", "/meal-planning-for-busy-weeks"),
                ("Exercise as a Sustainable Habit", "/exercise-sustainable-habit"),
            ],
        ),
    },
    {
        "title": "How to Build a Weekly Reset Routine That Actually Helps",
        "slug": "how-to-build-a-weekly-reset-routine",
        "category": "Wellness",
        "keyword": "weekly reset routine",
        "meta_title": "How to Build a Weekly Reset Routine",
        "meta_description": "Build a weekly reset routine with planning, meals, movement, digital cleanup, rest, and realistic habit reflection.",
        "excerpt": "A practical weekly reset routine for planning, meals, movement, digital cleanup, rest, and calmer habit reflection.",
        "image": "how-to-build-a-weekly-reset-routine.png",
        "image_alt": "weekly reset routine",
        "content": article(
            [
                "A weekly reset routine can help you begin the next week with fewer loose ends. It does not have to be a long Sunday ritual or a perfect home reset. The best version is practical, short enough to repeat, and focused on what makes the coming week easier.",
                "Think of the reset as a way to reduce friction. You are not trying to fix your whole life in one afternoon. You are choosing a few actions that support meals, sleep, movement, planning, and recovery.",
            ],
            [
                ("Choose the Right Reset Time", [
                    "Sunday works for some people, but it is not the only option. Your weekly reset can happen Friday afternoon, Saturday morning, Monday morning, or any time before the next busy stretch begins.",
                    "Choose a time when you usually have enough energy to think clearly. A reset done while exhausted may become overwhelming.",
                ]),
                ("Start With a Calendar Scan", [
                    "Look at the week ahead. Notice late workdays, appointments, travel, deadlines, social plans, and recovery windows. This scan helps you plan habits around real constraints.",
                    "Do not plan a complicated dinner on your busiest night or a long workout after a demanding day. The calendar should shape the routine.",
                ]),
                ("Pick Three Support Areas", [
                    "A reset can include many things, but three areas are usually enough. Choose from meals, movement, sleep, digital cleanup, home basics, finances, errands, or emotional recovery.",
                    "For example, you might plan two meals, schedule two walks, and clear your inbox. Another week might focus on laundry, bedtime, and grocery shopping.",
                ]),
                ("Use a 30-Minute Reset", [
                    "<ul><li>10 minutes: calendar scan and top priorities.</li><li>10 minutes: meals, groceries, or snacks.</li><li>5 minutes: movement or sleep plan.</li><li>5 minutes: clear one small space or digital pile.</li></ul>",
                    "If 30 minutes is too long, do 10. A short reset still creates direction.",
                ]),
                ("Plan Food Without Overplanning", [
                    "Choose a few defaults: one breakfast, one lunch, one dinner, and one backup meal. You do not need to map every bite. A flexible food plan prevents decision fatigue while leaving room for real life.",
                    "Check what you already have before shopping. Build meals around pantry staples, leftovers, and foods that need to be used soon.",
                ]),
                ("Schedule Movement Realistically", [
                    "Add movement to the calendar based on the week ahead. If the week is full, schedule short walks, mobility breaks, or low-impact cardio. If the week has more space, add strength training or longer sessions.",
                    "A movement plan should feel believable. It is better to schedule two sessions you complete than five sessions that create guilt.",
                ]),
                ("Create a Sleep Anchor", [
                    "Choose one sleep-supporting action for the week. That might be a caffeine cutoff, phone boundary, evening routine, or consistent wake time.",
                    "Sleep habits often improve through repeated cues. A weekly reset can remind you which cue you are practicing.",
                ]),
                ("Do a Digital Reset", [
                    "Digital clutter can make the week feel noisy. Clear old tabs, archive nonessential emails, silence notifications, or move distracting apps away from the home screen.",
                    "Keep the digital reset small. The point is to reduce one source of friction, not reorganize your entire online life.",
                ]),
                ("Include Recovery, Not Just Productivity", [
                    "A weekly reset should not become another productivity contest. Include one recovery action: rest, reading, calling someone, stretching, going outside, or protecting a quiet evening.",
                    "Recovery is part of a sustainable week. Without it, the reset can become a list that drains you before the week starts.",
                ]),
                ("Review What Worked", [
                    "At the end of the week, ask what made life easier and what was unrealistic. Keep the helpful parts and adjust the rest.",
                    "A weekly reset becomes better over time. Each week teaches you where your routine needs more support and where it can stay simple.",
                ]),
            ],
            [
                ("Daily Wellness Checklist", "/daily-wellness-checklist"),
                ("Meal Planning for Busy Weeks", "/meal-planning-for-busy-weeks"),
                ("Simple Grocery List for Healthy Eating", "/simple-grocery-list-for-healthy-eating"),
                ("Sleep-Friendly Evening Routine", "/sleep-friendly-evening-routine"),
            ],
        ),
    },
    {
        "title": "Simple Self-Care Checklist for Real-Life Stress",
        "slug": "simple-self-care-checklist",
        "category": "Mindfulness",
        "keyword": "simple self care checklist",
        "meta_title": "Simple Self-Care Checklist",
        "meta_description": "Use a simple self-care checklist for real-life stress with sleep, meals, movement, boundaries, connection, and calming resets.",
        "excerpt": "A practical self-care checklist for real-life stress, focused on basics, boundaries, connection, and small recovery cues.",
        "image": "simple-self-care-checklist.png",
        "image_alt": "simple self care checklist",
        "content": article(
            [
                "Self-care is often presented as something extra, expensive, or aesthetic. In real life, self-care is often much simpler: eating, sleeping, moving, asking for help, setting boundaries, and giving your nervous system a chance to recover.",
                "A simple self-care checklist can help when stress makes it hard to know what you need. Use it as a gentle guide, not a rigid scorecard.",
            ],
            [
                ("Start With Body Basics", [
                    "Before looking for complicated solutions, check the basics. Have you eaten recently? Have you had water? Did you sleep enough? Have you moved your body at all? Is there pain, illness, or exhaustion that needs attention?",
                    "Body basics do not solve every stressor, but they can reduce the intensity of stress. Many hard moments feel harder when you are hungry, dehydrated, sedentary, or sleep-deprived.",
                ]),
                ("Use a Five-Part Self-Care Check", [
                    "<ul><li>Fuel: a meal or snack with protein and fiber.</li><li>Fluid: water or another appropriate drink.</li><li>Movement: a walk, stretch, or mobility break.</li><li>Rest: a quiet pause, earlier bedtime, or lower stimulation.</li><li>Support: a message, conversation, boundary, or request for help.</li></ul>",
                    "Choose the part that feels most neglected today. You do not need to do all five at once.",
                ]),
                ("Add Emotional Naming", [
                    "Stress can feel like a blur. Name what is present: overwhelmed, sad, angry, lonely, tired, pressured, scattered, or numb. Naming does not fix the feeling, but it gives you a clearer starting point.",
                    "After naming the feeling, ask what kind of care fits. Anger may need a boundary. Sadness may need connection. Pressure may need a smaller task list.",
                ]),
                ("Set One Boundary", [
                    "Self-care sometimes means saying no, delaying a task, closing work, turning off notifications, or asking for more time. Boundaries protect energy and attention.",
                    "Start with one small boundary. For example, no work email after dinner, a 10-minute break before chores, or one evening without extra commitments.",
                ]),
                ("Use Connection as Care", [
                    "Self-care is not only solo. Connection can be care too. Text someone safe, ask for help, sit near family, talk with a friend, or join a supportive community.",
                    "If stress makes you withdraw, choose a small connection step. You do not have to explain everything. Even a simple check-in can help.",
                ]),
                ("Make the Checklist Practical", [
                    "Keep the checklist somewhere visible: notes app, journal, refrigerator, or desk. When stress spikes, read it and choose one action.",
                    "Avoid making the checklist too long. A long self-care list can become another burden. Five to seven options are enough.",
                ]),
                ("Self-Care for Busy Days", [
                    "On busy days, self-care may look like eating a real lunch, taking a two-minute breathing break, stretching between meetings, or going to bed instead of finishing one more task.",
                    "Small care still counts. The point is to stay connected to your needs when the day is demanding.",
                ]),
                ("Self-Care for Low Mood", [
                    "When mood is low, self-care may need to be very simple. Open curtains, shower, eat something, change clothes, step outside, or message someone. These actions are not magic, but they can create a small shift.",
                    "If low mood persists, feels severe, or includes thoughts of self-harm, seek professional or emergency support promptly.",
                ]),
                ("Review What Actually Helps", [
                    "After trying a self-care action, ask whether it helped a little, a lot, or not at all. Keep the actions that reliably help and let go of ones that feel performative.",
                    "Your checklist should become personal. Real self-care fits your body, schedule, culture, responsibilities, and support system.",
                ]),
                ("A Simple Daily Version", [
                    "A daily version can be brief: drink water with one meal, step outside once, move for five minutes, name one feeling, and protect one boundary. This is enough to keep care visible.",
                    "Self-care is not about doing everything. It is about not abandoning yourself when life gets loud.",
                ]),
            ],
            [
                ("Stress Reset Checklist Printable", "/stress-reset-checklist-printable"),
                ("Simple Relaxation Techniques", "/simple-relaxation-techniques"),
                ("Daily Wellness Checklist", "/daily-wellness-checklist"),
                ("How to Avoid Burnout", "/how-to-avoid-burnout"),
            ],
        ),
    },
    {
        "title": "Digital Wellness Routine: Healthier Screen Boundaries for Everyday Life",
        "slug": "digital-wellness-routine",
        "category": "Wellness",
        "keyword": "digital wellness routine",
        "meta_title": "Digital Wellness Routine",
        "meta_description": "Build a digital wellness routine with screen boundaries, notification cleanup, bedtime phone habits, focus blocks, and calmer breaks.",
        "excerpt": "A practical digital wellness routine for healthier screen boundaries, focus, sleep, breaks, and calmer everyday technology use.",
        "image": "digital-wellness-routine.png",
        "image_alt": "digital wellness routine",
        "content": article(
            [
                "A digital wellness routine helps you use technology with more intention. It is not about rejecting screens or becoming perfectly productive. It is about reducing the habits that drain attention, disrupt sleep, or keep stress constantly available.",
                "Most people need screens for work, connection, learning, and daily life. The goal is to create boundaries that make screen use feel less automatic and more supportive.",
            ],
            [
                ("Start With One Digital Friction Point", [
                    "Choose the screen habit that causes the most trouble. It might be bedtime scrolling, checking work messages after hours, opening social media during breaks, or constant notifications.",
                    "Start there instead of trying to overhaul every device. One clear boundary is easier to maintain than ten vague rules.",
                ]),
                ("Clean Up Notifications", [
                    "Notifications train attention to jump. Turn off nonessential alerts, group notifications, or set quiet hours. Keep alerts that are truly important and remove the ones that repeatedly interrupt focus or rest.",
                    "This one change can make the phone feel less demanding. You can still check apps intentionally without letting every app decide when you look.",
                ]),
                ("Create Screen-Free Transitions", [
                    "Transitions are powerful: waking up, meals, after work, before bed, and breaks. Choose one transition to make screen-free or screen-light.",
                    "For example, no phone for the first 10 minutes after waking, no phone during lunch, or phone parked outside the bed. Small transitions can change the feel of the whole day.",
                ]),
                ("Use Focus Blocks", [
                    "A focus block is a period when one task gets your attention and distractions are reduced. Close extra tabs, silence alerts, and choose a clear stopping point.",
                    "Start with 25 minutes if that feels manageable. After the block, take a real break: stand, stretch, look away from the screen, drink water, or step outside.",
                ]),
                ("Make Breaks Actually Restful", [
                    "Many digital breaks are just a different screen. That may be fine sometimes, but if you return more tired, try a different break. Move, breathe, stretch, look out a window, or do a small physical task.",
                    "A restful break changes your state. It gives your eyes, posture, and attention a chance to reset.",
                ]),
                ("Protect Bedtime From Screens", [
                    "Evening screen boundaries can support sleep. Try charging the phone away from the bed, stopping work messages before the wind-down routine, or replacing scrolling with reading, stretching, breathing, or audio.",
                    "You do not need a perfect phone-free night. Start with the final 15 minutes and build from there.",
                ]),
                ("Use App Limits With Replacement Habits", [
                    "App limits work better when there is something else to do. If you reduce social media at night, prepare a replacement: book, notebook, music, shower, or short walk.",
                    "Without a replacement, the brain returns to the easiest familiar habit. Make the alternative visible and simple.",
                ]),
                ("Separate Work and Personal Tech", [
                    "If possible, create boundaries between work and personal screens. Close work tabs, remove work apps from the home screen, or use separate browser profiles. If your job requires availability, create the clearest boundary you can.",
                    "The goal is to reduce the feeling that work is always open in the background.",
                ]),
                ("Review Your Digital Week", [
                    "Once a week, ask which screen habits helped and which drained you. Did notifications interrupt rest? Did bedtime scrolling delay sleep? Did focus blocks help? Did online time support connection or avoidance?",
                    "Use the answers to adjust one boundary. Digital wellness improves through small edits, not one dramatic reset.",
                ]),
                ("Keep Digital Wellness Flexible", [
                    "Some days require more screen time. Travel, work, family needs, and social connection can all change your routine. Flexibility prevents all-or-nothing thinking.",
                    "Return to the simplest version when needed: fewer notifications, one screen-free transition, one real break, and a bedtime boundary.",
                ]),
            ],
            [
                ("Phone-Free Bedtime Routine", "/phone-free-bedtime-routine"),
                ("Stress and Screen Time", "/stress-and-screen-time"),
                ("Screen Time and Sleep Quality", "/screen-time-and-sleep-quality"),
                ("Better Breaks for Remote Work", "/better-breaks-remote-work"),
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
