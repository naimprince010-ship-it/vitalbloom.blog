import json
import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
IMAGE_DIR = Path("/tmp/vitalbloom-drafts")
TODAY = "2026-06-02"

COMMON_SOURCES = [
    {
        "title": "About Sleep",
        "url": "https://www.cdc.gov/sleep/about/index.html",
        "publisher": "Centers for Disease Control and Prevention",
        "accessedAt": TODAY,
    },
    {
        "title": "Sleep Deprivation and Deficiency: Healthy Sleep Habits",
        "url": "https://www.nhlbi.nih.gov/health/sleep-deprivation/healthy-sleep-habits",
        "publisher": "National Heart, Lung, and Blood Institute",
        "accessedAt": TODAY,
    },
    {
        "title": "Relaxation Techniques: What You Need To Know",
        "url": "https://www.nccih.nih.gov/health/relaxation-techniques-what-you-need-to-know",
        "publisher": "National Center for Complementary and Integrative Health",
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
    html.append("<p>Disclaimer: This article is for general educational purposes only and is not medical or mental health advice. If sleep problems, anxiety, panic, trauma symptoms, or severe stress persist, consider support from a qualified healthcare professional.</p>")
    return "\n".join(html)


POSTS = [
    {
        "title": "How to Wind Down After Work Without Carrying the Day Home",
        "slug": "how-to-wind-down-after-work",
        "category": "Mindfulness",
        "keyword": "how to wind down after work",
        "meta_title": "How to Wind Down After Work",
        "meta_description": "Learn how to wind down after work with transition cues, stress resets, boundaries, light movement, and calmer evening routines.",
        "excerpt": "A practical wind-down routine for leaving work stress behind and creating a calmer transition into the evening.",
        "image": "how-to-wind-down-after-work.png",
        "image_alt": "how to wind down after work",
        "content": article(
            [
                "Winding down after work can be hard when your mind keeps replaying tasks, messages, and unfinished decisions. Even when the workday technically ends, your body may still feel alert and your thoughts may stay in problem-solving mode.",
                "A useful wind-down routine creates a transition. It does not erase stress, but it gives your nervous system and attention a clear signal that the work block is over and the evening can begin.",
            ],
            [
                ("Create a Shutdown Cue", [
                    "A shutdown cue is one small action that marks the end of work. It might be closing work tabs, writing tomorrow's first task, clearing your desk, changing clothes, or taking a short walk. The cue works because it gives your brain a repeatable ending.",
                    "If you work from home, this cue matters even more. Without a commute, work can leak into dinner, family time, and sleep. A visible shutdown ritual helps rebuild that boundary.",
                ]),
                ("Write Down the Loose Ends", [
                    "Unfinished tasks often keep the mind active. Before ending work, write a short list: what is done, what is pending, and the first next step for tomorrow. Keep it brief. The goal is not to finish everything; it is to give your thoughts somewhere to land.",
                    "This can reduce the urge to keep checking messages because you know there is a plan. If a task appears in your mind later, add it to the list instead of reopening work.",
                ]),
                ("Use a Physical Transition", [
                    "Stress often stays in the body. A physical transition can help: walk outside, stretch, shower, change clothes, wash your face, or make tea. Choose something that feels different from work posture and work lighting.",
                    "The action does not need to be dramatic. Even five minutes away from the desk can tell your body that the day has shifted.",
                ]),
                ("Avoid the Instant Scroll", [
                    "It is tempting to leave work and immediately open social media, news, or another screen. Sometimes that feels like rest, but it can keep your attention stimulated. Try a short screen gap before switching to personal content.",
                    "Use the gap for water, a snack, breathing, light movement, or silence. After that, choose screen time more intentionally instead of falling into it automatically.",
                ]),
                ("Try a 15-Minute Wind-Down", [
                    "<ul><li>Minutes 1-3: close work and write tomorrow's first task.</li><li>Minutes 4-7: stand, stretch, or walk slowly.</li><li>Minutes 8-10: drink water or prepare a simple snack.</li><li>Minutes 11-15: breathe, shower, change clothes, or sit quietly.</li></ul>",
                    "This routine is short enough for busy evenings but structured enough to create a real transition.",
                ]),
                ("Name the Stress State", [
                    "Sometimes the body is still running on urgency. Name what you notice: tense shoulders, fast thoughts, irritability, fatigue, or pressure in the chest. Naming is not the same as fixing, but it can reduce the sense that stress is simply taking over.",
                    "After naming the state, choose one response. If your body feels tense, move. If your thoughts feel cluttered, write. If you feel depleted, choose food, water, or quiet.",
                ]),
                ("Protect the First Hour After Work", [
                    "The first hour after work often shapes the rest of the evening. If possible, avoid scheduling another demanding task immediately. Give yourself a short buffer before chores, errands, or family logistics.",
                    "If life does not allow a full hour, protect ten minutes. A small buffer is still a boundary.",
                ]),
                ("Build a Work-to-Home Boundary", [
                    "For remote workers, create a boundary that your space can support. Put the laptop away, turn the chair, close a door, cover the monitor, or move to another room. A physical boundary can reduce the feeling that work is always available.",
                    "For commuters, use the trip home as a transition. Listen to calming audio, sit quietly, or take a few breaths before entering the next environment.",
                ]),
                ("When Work Stress Follows You", [
                    "If work stress regularly follows you into sleep, relationships, or weekends, look beyond the wind-down routine. Boundaries, workload, support, and recovery time may need attention.",
                    "A wind-down routine helps with daily transition, but it cannot solve an unsustainable work pattern by itself. Use it as one support while also noticing bigger patterns.",
                ]),
                ("Make Tomorrow Easier", [
                    "Before the evening ends, set up one thing that makes tomorrow smoother: clothes, lunch, a water bottle, or the first work task. This can lower morning stress and make the workday feel less abrupt.",
                    "A good wind-down routine is not only about tonight. It also creates a calmer handoff into tomorrow.",
                ]),
            ],
            [
                ("Evening Stress Reset", "/evening-stress-reset"),
                ("Stress Reset Checklist Printable", "/stress-reset-checklist-printable"),
                ("Better Breaks for Remote Work", "/better-breaks-remote-work"),
                ("How to Recover After a Stressful Day", "/recover-after-stressful-day"),
            ],
        ),
    },
    {
        "title": "Sleep-Friendly Evening Routine: Simple Cues for Better Rest",
        "slug": "sleep-friendly-evening-routine",
        "category": "Sleep",
        "keyword": "sleep friendly evening routine",
        "meta_title": "Sleep-Friendly Evening Routine",
        "meta_description": "Build a sleep-friendly evening routine with light, timing, screens, calming cues, and realistic habits for better rest.",
        "excerpt": "A realistic sleep-friendly evening routine with simple cues for light, timing, screens, and calmer bedtime transitions.",
        "image": "sleep-friendly-evening-routine.png",
        "image_alt": "sleep friendly evening routine",
        "content": article(
            [
                "A sleep-friendly evening routine does not need to be long or perfect. It should help your body and mind move from daytime activity into rest through repeated cues: lower stimulation, calmer light, less urgency, and a more predictable bedtime path.",
                "Healthy sleep habits can support better rest, but sleep is also affected by stress, health conditions, medications, environment, and schedule. Use this routine as general guidance and adjust it to your life.",
            ],
            [
                ("Start With a Consistent Anchor", [
                    "Choose one evening anchor that happens most nights. It might be dimming lights, making tea, closing the kitchen, taking a shower, setting tomorrow's clothes, or reading. The anchor tells your brain the evening is shifting.",
                    "Consistency matters more than the exact activity. A small cue repeated often can become more powerful than an elaborate routine done once.",
                ]),
                ("Lower Light Gradually", [
                    "Bright light and stimulating screens can make the evening feel more alert. You do not need a perfect blackout ritual. Start by lowering lights, using warmer lamps, and avoiding unnecessary bright screens in the final part of the night.",
                    "If you need screens, reduce intensity and choose calmer content. The goal is a gradual signal that nighttime is approaching.",
                ]),
                ("Move Planning Earlier", [
                    "Bedtime is not the best time to solve tomorrow. Move planning earlier in the evening. Write the next day's first task, check the calendar, and prepare any essentials before you are already in bed.",
                    "This can reduce racing thoughts because your mind knows there is a plan. Keep the list short so planning does not become another work session.",
                ]),
                ("Create a Screen Boundary", [
                    "A screen boundary can be flexible. You might stop work email one hour before bed, charge the phone outside the bed, use an app limit, or switch to audio instead of scrolling.",
                    "The boundary should target the screen habit that most often delays sleep. For many people, that is not all screen use; it is open-ended scrolling, stressful messages, or work content.",
                ]),
                ("Use a 30-Minute Routine", [
                    "<ul><li>Minutes 1-10: finish practical tasks and write tomorrow's first step.</li><li>Minutes 11-20: dim lights, hygiene, and reduce screens.</li><li>Minutes 21-30: read, stretch gently, breathe, or sit quietly.</li></ul>",
                    "If 30 minutes is too long, cut it to 10. A short routine is better than a perfect routine you avoid.",
                ]),
                ("Keep the Bedroom Simple", [
                    "A sleep-friendly bedroom is usually cool, dark, quiet, and comfortable when possible. Small changes help: reduce notifications, move clutter away from the bed, close curtains, or use a fan or white noise if appropriate.",
                    "You do not need a magazine-perfect room. Remove the friction that most often interrupts your sleep.",
                ]),
                ("Choose Calming Instead of Productive", [
                    "Evening routines can accidentally become productivity routines. If every step is about optimizing tomorrow, the mind may stay activated. Include at least one cue that is simply calming, not useful.",
                    "That might be reading, breathing, stretching, music, prayer, journaling, or a warm shower. The point is to let the evening soften.",
                ]),
                ("Handle Off Nights Gently", [
                    "Some nights will not follow the plan. Travel, family needs, illness, stress, and late work can interrupt sleep habits. Do not turn one off night into proof that the routine failed.",
                    "Return to the easiest version the next night: dim light, close open loops, reduce stimulation, and use one calming cue.",
                ]),
                ("Notice What Actually Helps", [
                    "Track one signal for a week. Choose bedtime consistency, screen cutoff, caffeine timing, or how rested you feel. One signal is easier to learn from than trying to measure everything.",
                    "Keep the habits that noticeably help and remove steps that make the routine feel crowded.",
                ]),
                ("When Sleep Needs More Support", [
                    "If sleep problems persist, if you are very sleepy during the day, or if snoring, breathing pauses, restless legs, anxiety, or pain interfere with sleep, consider medical guidance.",
                    "Sleep hygiene is useful, but it is not the only answer for every sleep problem. Professional support can matter.",
                ]),
            ],
            [
                ("Better Sleep Routine", "/better-sleep-routine"),
                ("Beginner Evening Routine for Better Sleep", "/beginner-evening-routine-better-sleep"),
                ("Sleep Hygiene Checklist Printable", "/sleep-hygiene-checklist-printable"),
                ("Bedroom Environment Checklist", "/bedroom-environment-checklist"),
            ],
        ),
    },
    {
        "title": "Phone-Free Bedtime Routine: How to Make Nights Feel Calmer",
        "slug": "phone-free-bedtime-routine",
        "category": "Sleep",
        "keyword": "phone free bedtime routine",
        "meta_title": "Phone-Free Bedtime Routine",
        "meta_description": "Create a phone-free bedtime routine with realistic charging spots, replacement habits, screen boundaries, and calmer sleep cues.",
        "excerpt": "A realistic phone-free bedtime routine that replaces scrolling with calmer cues and clearer sleep boundaries.",
        "image": "phone-free-bedtime-routine.png",
        "image_alt": "phone free bedtime routine",
        "content": article(
            [
                "A phone-free bedtime routine can help if scrolling, messages, or work notifications keep pulling your attention when you are trying to rest. The goal is not to become perfect with technology. The goal is to make bedtime less open-ended.",
                "Phones are useful tools, but they can also bring light, stimulation, comparison, news, and unfinished conversations into bed. A better routine creates distance without relying only on willpower.",
            ],
            [
                ("Choose a Phone Parking Spot", [
                    "Pick a place where the phone goes before bed: a charger across the room, a hallway table, a kitchen counter, or a desk. The spot should be close enough to feel practical but far enough that you cannot scroll from bed.",
                    "If you use your phone as an alarm, try a basic alarm clock or place the phone across the room. Distance changes the habit because reaching for the phone becomes less automatic.",
                ]),
                ("Set a Realistic Cutoff", [
                    "A phone-free routine does not need to start two hours before bed. Begin with the final 15 minutes if that is realistic. Once that feels normal, expand to 30 minutes.",
                    "The cutoff should be specific. For example: after brushing teeth, the phone charges in the kitchen. Specific cues work better than vague goals like use the phone less.",
                ]),
                ("Replace the Phone With Something Concrete", [
                    "Removing the phone creates empty space. Fill that space with a replacement: book, magazine, stretching, breathing, music, prayer, journaling, or preparing tomorrow's clothes.",
                    "The replacement should be easy. If the replacement takes too much effort, the phone will win because it is simpler.",
                ]),
                ("Handle Important Contacts", [
                    "If you worry about missing urgent calls, use do-not-disturb settings with emergency exceptions. Tell close contacts how to reach you if needed. This reduces the anxiety that keeps the phone nearby.",
                    "A phone-free routine should support safety and peace of mind. Adjust settings to fit your real responsibilities.",
                ]),
                ("Use a Wind-Down List", [
                    "<ul><li>Put the phone on its charger.</li><li>Write tomorrow's first task.</li><li>Dim lights.</li><li>Brush teeth and wash face.</li><li>Read, breathe, stretch, or listen to calming audio.</li></ul>",
                    "Keep the list short. The routine should make bedtime easier, not feel like homework.",
                ]),
                ("Reduce Work Creep", [
                    "Work messages are one of the biggest reasons phones disrupt bedtime. If possible, remove work apps from the home screen, turn off notifications, or set a work cutoff time.",
                    "If your job requires availability, create the clearest boundary possible. Even a smaller boundary can reduce repeated checking.",
                ]),
                ("Expect the Urge to Check", [
                    "The urge to check the phone may show up strongly at first. That does not mean the routine is failing. It means the habit is familiar. Notice the urge, wait one minute, and choose the replacement activity.",
                    "You can also keep a notepad nearby. If you remember something important, write it down instead of picking up the phone.",
                ]),
                ("Make Mornings Phone-Lighter Too", [
                    "Bedtime routines are easier when mornings are not phone-heavy. If you wake and immediately scroll, the phone stays linked to bed. Try delaying the first check until after water, light, stretching, or breakfast.",
                    "This reinforces the idea that bed is for rest, not endless input.",
                ]),
                ("Do Not Aim for Perfect", [
                    "Some nights you will use the phone. Travel, family, work, and stress happen. Instead of giving up, return to the routine the next night.",
                    "Progress might mean three phone-free nights per week at first. That can still improve your relationship with bedtime.",
                ]),
                ("When the Phone Masks Stress", [
                    "Sometimes bedtime scrolling is not about the phone; it is about avoiding stress, loneliness, or racing thoughts. If removing the phone makes those feelings louder, add a calming support such as journaling, breathing, or talking with someone safe.",
                    "If distress is intense or persistent, professional support may help. A phone boundary is useful, but it does not have to carry everything alone.",
                ]),
            ],
            [
                ("Screen Time and Sleep Quality", "/screen-time-and-sleep-quality"),
                ("Stress and Screen Time", "/stress-and-screen-time"),
                ("Sleep-Friendly Evening Routine", "/sleep-friendly-evening-routine"),
                ("Bedtime Anxiety and Racing Thoughts", "/bedtime-anxiety-racing-thoughts"),
            ],
        ),
    },
    {
        "title": "Simple Relaxation Techniques for Stress Relief",
        "slug": "simple-relaxation-techniques",
        "category": "Mindfulness",
        "keyword": "simple relaxation techniques",
        "meta_title": "Simple Relaxation Techniques",
        "meta_description": "Try simple relaxation techniques for stress relief, including breathing, progressive muscle relaxation, grounding, and guided imagery.",
        "excerpt": "Simple relaxation techniques for stress relief, including breathing, muscle release, grounding, and calming attention.",
        "image": "simple-relaxation-techniques.png",
        "image_alt": "simple relaxation techniques",
        "content": article(
            [
                "Simple relaxation techniques can help create a pause when stress feels high. They do not remove every problem, but they can help your body shift away from constant urgency and give your mind a clearer next step.",
                "Relaxation practices often involve breathing, focused attention, muscle release, or calming imagery. Start small and choose the method that feels safest and easiest for your body.",
            ],
            [
                ("Start With Slow Breathing", [
                    "Slow breathing is one of the simplest relaxation tools. Sit or stand comfortably, relax your shoulders, and breathe in through the nose if comfortable. Exhale slowly. Repeat for one to three minutes.",
                    "Do not force deep breaths. If deep breathing makes you uncomfortable, keep the breath gentle and natural. The point is to slow the pace, not to perform a perfect technique.",
                ]),
                ("Try Progressive Muscle Relaxation", [
                    "Progressive muscle relaxation involves gently tensing and releasing muscle groups. For example, tense the hands for a few seconds, then release. Move through shoulders, face, legs, and feet if it feels comfortable.",
                    "This can help you notice where tension is stored. Use gentle tension, not maximum effort. Skip any area that hurts.",
                ]),
                ("Use Grounding for Overwhelm", [
                    "Grounding brings attention back to the present moment. Try naming five things you see, four things you feel, three things you hear, two things you smell, and one thing you taste.",
                    "This technique can be useful when thoughts feel scattered. It gives attention a simple task and reconnects you with the environment.",
                ]),
                ("Practice Guided Imagery", [
                    "Guided imagery uses imagination to picture a calming place or scene. It might be a beach, forest, quiet room, or memory that feels steady. Notice colors, sounds, textures, and temperature.",
                    "If imagery is hard, use a real photo, calming music, or a simple phrase instead. Not every relaxation technique works for every person.",
                ]),
                ("Use a One-Minute Reset", [
                    "<ul><li>Pause and put both feet on the floor.</li><li>Relax the jaw and shoulders.</li><li>Take three slow breaths.</li><li>Name one thing you can do next.</li></ul>",
                    "This reset is useful during work, after an argument, before sleep, or when a task feels too big.",
                ]),
                ("Make Relaxation Easier to Remember", [
                    "Attach relaxation to an existing cue: after closing the laptop, before lunch, after getting in the car, or before bed. The cue helps the practice become automatic.",
                    "Short, frequent practice is often easier than waiting for a crisis. Practicing when stress is mild can make the technique more available when stress is high.",
                ]),
                ("Notice Safety and Comfort", [
                    "Some relaxation practices can feel uncomfortable for people with trauma histories, panic, certain medical conditions, or distressing body sensations. Keep your eyes open if that feels safer. Choose grounding instead of body-focused techniques if needed.",
                    "Relaxation should be adaptable. You are allowed to modify or stop any technique.",
                ]),
                ("Use Relaxation With Problem Solving", [
                    "Relaxation is not the same as ignoring problems. It can help you calm enough to choose the next practical step. After a short technique, ask: what is one thing I can do, delay, delegate, or write down?",
                    "This keeps relaxation connected to real life rather than turning it into pressure to feel calm instantly.",
                ]),
                ("Build a Small Menu", [
                    "Choose three techniques: one breathing tool, one body tool, and one attention tool. For example, slow breathing, shoulder release, and grounding. Keep the list visible.",
                    "Having a menu prevents decision fatigue. When stress rises, you can choose from the list instead of searching for a new method.",
                ]),
                ("When Stress Needs More Support", [
                    "If stress feels constant, affects sleep, causes panic, interferes with work or relationships, or leads to thoughts of self-harm, reach out for professional support promptly.",
                    "Relaxation techniques can be helpful, but they are not a substitute for care when symptoms are severe or persistent.",
                ]),
            ],
            [
                ("Simple Breathing Exercises", "/simple-breathing-exercises"),
                ("Grounding Techniques for Stress", "/grounding-techniques-for-stress"),
                ("Stress Reset Checklist Printable", "/stress-reset-checklist-printable"),
                ("Practice Mindfulness Simply", "/practice-mindfulness-simply"),
            ],
        ),
    },
    {
        "title": "How to Reset After a Bad Night's Sleep",
        "slug": "how-to-reset-after-a-bad-night-sleep",
        "category": "Sleep",
        "keyword": "reset after a bad night sleep",
        "meta_title": "How to Reset After a Bad Night's Sleep",
        "meta_description": "Reset after a bad night's sleep with morning light, gentle movement, caffeine timing, realistic naps, and a calmer next bedtime.",
        "excerpt": "A realistic reset plan for the day after poor sleep, with morning light, caffeine timing, naps, and evening recovery.",
        "image": "how-to-reset-after-a-bad-night-sleep.png",
        "image_alt": "how to reset after a bad night sleep",
        "content": article(
            [
                "A bad night's sleep can make the next day feel harder before it even starts. You may feel foggy, irritable, hungry, wired, or tempted to overcorrect. The goal is not to force a perfect day. The goal is to recover gently without making the next night harder.",
                "One rough night happens to many people. If poor sleep becomes frequent, severe, or affects daily functioning, professional guidance may be useful. For an occasional bad night, a simple reset plan can help.",
            ],
            [
                ("Get Morning Light", [
                    "Morning light can help reinforce your daily rhythm. Open curtains, step outside, or sit near bright natural light when possible. Even a short exposure can signal that the day has started.",
                    "If you wake tired, it may be tempting to stay in dim light for hours. Gentle light plus a normal morning routine can help the body reset.",
                ]),
                ("Keep Wake Time Reasonable", [
                    "Sleeping much later than usual can make the next night harder for some people. If you can, keep your wake time close to normal or avoid an extreme sleep-in.",
                    "This does not mean punishing yourself. If you need extra rest, take it carefully. The goal is to avoid shifting the whole schedule so far that bedtime becomes difficult again.",
                ]),
                ("Use Caffeine Strategically", [
                    "Caffeine can help after poor sleep, but timing matters. Use it earlier in the day and avoid leaning on it late if it tends to disrupt your sleep. Notice how your body responds.",
                    "Before a second or third caffeine dose, check whether you need food, water, light, or a short movement break instead.",
                ]),
                ("Try Gentle Movement", [
                    "A walk, mobility routine, or light stretching can help you feel more awake without demanding too much from a tired body. Keep intensity moderate or easy, especially if coordination or energy feels off.",
                    "This is not the day to prove toughness. Choose movement that supports the day instead of draining it.",
                ]),
                ("Use Naps Carefully", [
                    "A short nap can help some people, but long or late naps may interfere with bedtime. If you nap, consider keeping it brief and earlier in the day.",
                    "If naps leave you groggy or make nights worse, choose quiet rest instead: lying down, closing your eyes, breathing, or taking a screen-free break.",
                ]),
                ("Simplify Decisions", [
                    "Poor sleep can make decisions feel harder. Simplify the day where possible. Choose easy meals, reduce unnecessary tasks, and focus on the most important priorities.",
                    "If you can delay complex work or emotional conversations, consider doing so. If you cannot, add more breaks and write down key steps.",
                ]),
                ("Eat Steady Meals", [
                    "Poor sleep can affect appetite and cravings. Aim for steady meals with protein, produce, fiber-rich carbohydrates, and fluids. This can help energy feel less chaotic.",
                    "Do not turn the day into a strict correction plan. Nourishment and hydration are recovery tools.",
                ]),
                ("Protect the Next Bedtime", [
                    "The most important reset may happen in the evening. Avoid making bedtime later because the day felt unproductive. Start winding down earlier, lower stimulation, and prepare tomorrow so your mind has fewer loose ends.",
                    "Use a simple routine: dim lights, reduce screens, write tomorrow's first task, and choose one calming cue.",
                ]),
                ("Avoid Sleep Math Anxiety", [
                    "After a bad night, it is easy to calculate how little sleep you got and worry about the consequences. That worry can make the next night harder. Notice the thought, then return to practical steps.",
                    "One bad night is uncomfortable, but it does not mean the whole week is ruined. Focus on the next helpful cue.",
                ]),
                ("When Bad Nights Repeat", [
                    "If poor sleep happens often, look for patterns: caffeine timing, stress, screen use, pain, snoring, breathing issues, restless legs, shift work, anxiety, or medications. A sleep diary can help you explain the pattern to a professional.",
                    "Repeated sleep problems deserve support. Healthy habits can help, but they are not the only tool.",
                ]),
            ],
            [
                ("Sleep Debt Recovery Guide", "/sleep-debt-recovery-guide"),
                ("Why You Wake Up Tired", "/why-you-wake-up-tired"),
                ("Morning Light and Sleep", "/morning-light-and-sleep"),
                ("Caffeine and Sleep Cutoff", "/caffeine-and-sleep-cutoff"),
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
