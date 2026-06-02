import json
import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
IMAGE_DIR = Path("/tmp/vitalbloom-drafts")
TODAY = "2026-06-02"

COMMON_SOURCES = [
    {
        "title": "Healthy Eating Tips",
        "url": "https://www.cdc.gov/nutrition/features/healthy-eating-tips.html",
        "publisher": "Centers for Disease Control and Prevention",
        "accessedAt": TODAY,
    },
    {
        "title": "MyPlate Plan",
        "url": "https://www.myplate.gov/myplate-plan",
        "publisher": "U.S. Department of Agriculture",
        "accessedAt": TODAY,
    },
    {
        "title": "Healthy Eating Plate",
        "url": "https://www.health.harvard.edu/plate/healthy-eating-plate",
        "publisher": "Harvard Health Publishing",
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
            if paragraph.startswith("<ul>"):
                html.append(paragraph)
            else:
                html.append(f"<p>{paragraph}</p>")
    html.append("<h2>Related VitalBloom Guides</h2>")
    html.append("<ul>")
    for title, url in related:
        html.append(f'  <li><a href="{url}">{title}</a></li>')
    html.append("</ul>")
    html.append("<p>Disclaimer: This article is for general educational purposes only and is not a substitute for professional medical or nutrition advice.</p>")
    return "\n".join(html)


POSTS = [
    {
        "title": "Simple Grocery List for Healthy Eating Without Overbuying",
        "slug": "simple-grocery-list-for-healthy-eating",
        "category": "Nutrition",
        "keyword": "simple grocery list for healthy eating",
        "meta_title": "Simple Grocery List for Healthy Eating",
        "meta_description": "Build a simple grocery list for healthy eating with proteins, produce, fiber-rich carbs, flavor staples, and budget-friendly planning tips.",
        "excerpt": "A simple grocery list framework for balanced meals without overbuying, wasting food, or starting from scratch every week.",
        "image": "simple-grocery-list-for-healthy-eating.png",
        "image_alt": "simple grocery list for healthy eating",
        "content": article(
            [
                "A simple grocery list can make healthy eating feel less like a daily puzzle. When you keep a few reliable foods at home, balanced meals become easier to assemble, even on busy days.",
                "The goal is not to buy every healthy food at once. A useful list gives you enough protein, produce, fiber-rich carbohydrates, and flavor to build several meals without crowding your refrigerator or wasting money.",
            ],
            [
                (
                    "Start With Meals You Actually Eat",
                    [
                        "Before writing a list, think about the meals that happen in your real week. If breakfast is rushed, buy breakfast foods that take two minutes. If lunch is the problem, choose ingredients that pack well. If dinner is the stressful meal, stock quick proteins and vegetables.",
                        "This keeps the list practical. A grocery list should support your schedule, cooking energy, budget, and food preferences. It should not be a fantasy version of a perfect week.",
                    ],
                ),
                (
                    "Use Four Grocery Categories",
                    [
                        "The easiest structure is protein, produce, fiber-rich carbohydrates, and flavor. Protein helps meals feel satisfying. Produce adds color, fiber, and volume. Fiber-rich carbohydrates support energy. Flavor makes the meal something you want to eat.",
                        "<ul><li>Protein: eggs, beans, lentils, tofu, yogurt, fish, poultry, nuts, seeds, or cottage cheese.</li><li>Produce: fresh, frozen, or canned fruits and vegetables.</li><li>Fiber-rich carbohydrates: oats, potatoes, brown rice, quinoa, whole-grain bread, beans, or fruit.</li><li>Flavor: salsa, hummus, herbs, spices, vinaigrette, pesto, lemon, or yogurt sauce.</li></ul>",
                    ],
                ),
                (
                    "Choose Two Proteins for the Week",
                    [
                        "Two protein anchors are enough for many beginners. You might choose eggs and beans, Greek yogurt and lentils, tofu and fish, or chicken and cottage cheese. Keeping the choice small makes shopping and cooking easier.",
                        "If you are vegetarian, beans, lentils, tofu, tempeh, Greek yogurt, cottage cheese, eggs, nuts, and seeds can all work. If you are short on time, choose at least one protein that requires no cooking.",
                    ],
                ),
                (
                    "Pick Produce That Matches Your Week",
                    [
                        "Fresh produce is great when you know you will use it. Frozen and canned options are useful when your week is unpredictable. Frozen vegetables, berries, canned tomatoes, canned beans, apples, carrots, and greens can reduce waste.",
                        "Aim for color, but keep it simple. One fruit, one raw vegetable, and one cooked vegetable can create several meal combinations. If fresh produce often spoils, buy less fresh and more frozen until the routine feels stable.",
                    ],
                ),
                (
                    "Add Fiber-Rich Carbohydrate Staples",
                    [
                        "Carbohydrates are often what turn ingredients into a meal. Oats can become breakfast. Potatoes can become dinner. Brown rice can become bowls. Whole-grain bread can become sandwiches or toast.",
                        "Choose one or two staples you enjoy. You do not need every grain in the pantry. A small, repeatable list is easier to maintain than a crowded pantry full of foods you rarely cook.",
                    ],
                ),
                (
                    "Keep Flavor Staples Ready",
                    [
                        "Flavor is the reason you will use the groceries you buy. Salsa can turn beans and rice into a bowl. Hummus can make vegetables and crackers feel like a snack plate. Lemon, herbs, and vinaigrette can refresh leftovers.",
                        "Choose one creamy flavor, one bright flavor, and one spicy or savory flavor if that fits your taste. This gives variety without requiring complicated recipes.",
                    ],
                ),
                (
                    "Build a One-Week Starter List",
                    [
                        "A starter list might include eggs, Greek yogurt, canned beans, oats, brown rice, whole-grain bread, frozen vegetables, apples, carrots, spinach, hummus, salsa, olive oil, and a few herbs or spices.",
                        "From that list, you can make oatmeal, yogurt bowls, egg toast, bean bowls, vegetable rice plates, snack plates, and quick lunches. The foods overlap, which helps reduce waste.",
                    ],
                ),
                (
                    "Shop Your Kitchen First",
                    [
                        "Before going to the store, check your refrigerator, freezer, and pantry. Look for proteins that need to be used, produce close to spoiling, grains already opened, and sauces you forgot about.",
                        "Then build the grocery list around what is missing. This saves money and helps you finish food before buying more. It also makes the list shorter and calmer.",
                    ],
                ),
                (
                    "Avoid Overbuying Healthy Foods",
                    [
                        "Overbuying can happen with healthy foods too. A cart full of vegetables is not helpful if half of them spoil. Start with what you can realistically cook or assemble in three to four days.",
                        "If you want more variety, rotate weekly instead of buying everything at once. Choose berries one week, apples the next, broccoli one week, peppers the next. Variety over time is easier than variety in one cart.",
                    ],
                ),
                (
                    "Turn the List Into Meals",
                    [
                        "Once you have the groceries, plan three simple meals before the week starts. For example: yogurt bowls for breakfast, bean and rice bowls for lunch, and eggs or tofu with vegetables and toast for dinner.",
                        "You can change the exact meals later, but having a default plan reduces decision fatigue. The best grocery list is one that becomes real food on your plate.",
                    ],
                ),
            ],
            [
                ("Balanced Plate Printable Guide", "/balanced-plate-printable-guide"),
                ("Beginner Meal Prep Checklist", "/beginner-meal-prep-checklist"),
                ("Fiber-Rich Carbohydrates Guide", "/fiber-rich-carbohydrates-guide"),
                ("How to Add Protein to Every Meal", "/add-protein-to-every-meal"),
            ],
        ),
    },
    {
        "title": "Meal Planning for Busy Weeks: A Flexible Beginner System",
        "slug": "meal-planning-for-busy-weeks",
        "category": "Nutrition",
        "keyword": "meal planning for busy weeks",
        "meta_title": "Meal Planning for Busy Weeks",
        "meta_description": "Use this flexible meal planning system for busy weeks with default meals, backup options, grocery anchors, and balanced plate basics.",
        "excerpt": "A flexible meal planning system for busy weeks when you need balanced meals without a strict schedule.",
        "image": "meal-planning-for-busy-weeks.png",
        "image_alt": "meal planning for busy weeks",
        "content": article(
            [
                "Meal planning for busy weeks should make life easier, not create another long chore. The most useful plan is flexible enough to survive schedule changes, low-energy evenings, and unexpected leftovers.",
                "Instead of planning seven perfect dinners, build a small system: a few default meals, one backup option, a short grocery list, and enough structure to avoid starting from zero each day.",
            ],
            [
                (
                    "Plan for Your Actual Calendar",
                    [
                        "Start by looking at the week. Notice late workdays, appointments, family plans, travel, or evenings when cooking will be unrealistic. These are the days that need the simplest meals.",
                        "A busy week plan should include low-cook and no-cook options. If you know Wednesday will be packed, do not assign a complicated recipe to Wednesday. Put the easiest meal on the hardest day.",
                    ],
                ),
                (
                    "Choose Three Default Meals",
                    [
                        "Default meals are reliable meals you can repeat without much thought. They might be a breakfast, a lunch, and a dinner. Examples include overnight oats, a bean bowl, and a sheet-pan dinner.",
                        "Repeating default meals is not boring if they work. You can change sauces, vegetables, or sides while keeping the structure the same. Familiar meals reduce decisions when your attention is already full.",
                    ],
                ),
                (
                    "Use the Balanced Plate Method",
                    [
                        "A balanced plate gives you a quick check without counting or tracking. Ask whether the meal has a protein, produce, fiber-rich carbohydrate, and flavor. If one part is missing, add the easiest option.",
                        "For example, pasta can become more balanced with lentils, vegetables, and a simple sauce. Toast can become breakfast with eggs or yogurt and fruit. Rice can become a bowl with beans, greens, and salsa.",
                    ],
                ),
                (
                    "Create a Busy-Day Backup Meal",
                    [
                        "Every meal plan needs a backup. A backup meal is something you can make when the original plan collapses. It should be shelf-stable, fast, and acceptable enough that you will actually use it.",
                        "<ul><li>Beans, microwave rice, frozen vegetables, and salsa.</li><li>Whole-grain toast, eggs, and fruit.</li><li>Greek yogurt, oats, berries, and nuts.</li><li>Soup, whole-grain bread, and a simple side.</li></ul>",
                    ],
                ),
                (
                    "Prep Ingredients Instead of Full Meals",
                    [
                        "Ingredient prep is often easier than full meal prep. Cook one grain, wash produce, prepare one protein, and keep a sauce ready. These components can become bowls, wraps, plates, or leftovers.",
                        "This method gives flexibility. If you do not want Monday's planned meal, you can still use the prepared ingredients in a different way. The plan supports you without trapping you.",
                    ],
                ),
                (
                    "Make Lunch Easier First",
                    [
                        "Lunch is often where busy weeks become expensive or chaotic. Choose one lunch formula you can repeat for two or three days. A bowl, wrap, salad plate, or snack plate can work.",
                        "Pack an add-on such as fruit, yogurt, nuts, or whole-grain crackers. This helps adjust for hunger without buying an extra meal or skipping food until dinner.",
                    ],
                ),
                (
                    "Use Theme Nights Lightly",
                    [
                        "Theme nights can simplify planning if they feel helpful. Try bowl night, soup night, breakfast-for-dinner night, leftovers night, or sheet-pan night. The theme gives direction without requiring a specific recipe.",
                        "Keep themes loose. If taco night becomes stressful because you need ten ingredients, simplify it into beans, vegetables, tortillas, salsa, and one protein or dairy option.",
                    ],
                ),
                (
                    "Plan Leftovers on Purpose",
                    [
                        "Leftovers are easier when they have a job. Cook extra rice for lunch bowls. Roast extra vegetables for wraps. Make extra lentils for soup or a snack plate.",
                        "If leftovers pile up, plan a leftover night before shopping again. Using what you already cooked saves money and reduces food waste.",
                    ],
                ),
                (
                    "Keep the Grocery List Short",
                    [
                        "A short list is more useful than a complicated one. Choose two proteins, two produce options, one or two carbohydrates, and two flavor items. Add breakfast and snack basics if needed.",
                        "You can always buy more later. Starting smaller helps you learn what you actually use during busy weeks.",
                    ],
                ),
                (
                    "Review the Week Without Judgment",
                    [
                        "At the end of the week, ask what worked. Which meal saved you time? Which ingredient went unused? Which night needed a backup? This review is not about perfection. It is about making the next plan easier.",
                        "A good meal plan improves through repetition. Each week teaches you something about your schedule, appetite, budget, and cooking energy.",
                    ],
                ),
            ],
            [
                ("Balanced Plate Printable Guide", "/balanced-plate-printable-guide"),
                ("Simple Grocery List for Healthy Eating", "/simple-grocery-list-for-healthy-eating"),
                ("Simple Meal Prep Ideas for Healthy Lunches", "/simple-meal-prep-healthy-lunches"),
                ("Healthy Snack Plate Ideas", "/healthy-snack-plate-ideas"),
            ],
        ),
    },
    {
        "title": "How to Eat More Vegetables Without Changing Everything",
        "slug": "how-to-eat-more-vegetables",
        "category": "Nutrition",
        "keyword": "how to eat more vegetables",
        "meta_title": "How to Eat More Vegetables",
        "meta_description": "Learn how to eat more vegetables with simple add-ons, frozen options, flavor strategies, and balanced meal ideas.",
        "excerpt": "Simple ways to eat more vegetables without overhauling your meals or forcing foods you do not enjoy.",
        "image": "how-to-eat-more-vegetables.png",
        "image_alt": "how to eat more vegetables",
        "content": article(
            [
                "Eating more vegetables does not require a full diet overhaul. In many cases, the easiest approach is to add vegetables to meals you already like instead of trying to build a new routine from scratch.",
                "Vegetables can add color, fiber, volume, and flavor. The key is making them convenient, enjoyable, and realistic for your budget and schedule.",
            ],
            [
                (
                    "Start With Add-Ons",
                    [
                        "Add one vegetable to a meal you already eat. Put spinach in eggs, peppers in a sandwich, frozen vegetables in soup, tomatoes on toast, or greens in a bowl. Small additions are easier to repeat.",
                        "This method works because it does not ask you to replace the whole meal. It simply improves the meal you were already going to eat.",
                    ],
                ),
                (
                    "Use Frozen Vegetables",
                    [
                        "Frozen vegetables are useful because they last longer and require less prep. They can go into stir-fries, soups, pasta, rice bowls, eggs, and casseroles.",
                        "They are especially helpful if fresh vegetables often spoil in your refrigerator. A freezer option gives you a backup on days when shopping or chopping is not realistic.",
                    ],
                ),
                (
                    "Make Vegetables Taste Better",
                    [
                        "People often think they dislike vegetables when they actually dislike bland vegetables. Try roasting, sauteing, seasoning, adding lemon, using herbs, pairing with hummus, or adding a sauce.",
                        "Texture matters too. If you dislike soft vegetables, try raw, roasted, or lightly cooked options. If raw vegetables feel hard to eat, try soups, stews, or blended sauces.",
                    ],
                ),
                (
                    "Add Vegetables to Breakfast",
                    [
                        "Breakfast vegetables can be simple. Add spinach, mushrooms, tomatoes, peppers, or onions to eggs or tofu. Put avocado and tomato on toast. Add greens to a smoothie if you enjoy the taste.",
                        "You do not need vegetables at every breakfast, but adding them sometimes can make the whole day feel more balanced.",
                    ],
                ),
                (
                    "Build a Better Lunch",
                    [
                        "Lunch is a good place to add vegetables because many lunch foods already welcome them. Add lettuce, tomato, cucumber, peppers, carrots, roasted vegetables, or greens to sandwiches, wraps, bowls, and leftovers.",
                        "If lunch is packed, keep vegetables sturdy. Carrots, cucumbers, peppers, cabbage, and roasted vegetables often hold up better than delicate greens.",
                    ],
                ),
                (
                    "Use the Half-Plate Idea Loosely",
                    [
                        "The half-plate idea can be helpful, but it does not need to be perfect. Some meals will naturally have fewer vegetables. Others can have more. Think about your day as a whole.",
                        "If dinner is the easiest time to add vegetables, do that. If lunch works better, start there. Consistency matters more than perfect plate math.",
                    ],
                ),
                (
                    "Keep Convenient Options Visible",
                    [
                        "Vegetables are easier to eat when they are visible and ready. Wash greens, cut carrots, keep frozen vegetables easy to reach, or place salad ingredients near the front of the refrigerator.",
                        "A simple container of ready vegetables can turn into a snack, side, wrap filling, or bowl topping.",
                    ],
                ),
                (
                    "Try One New Vegetable at a Time",
                    [
                        "Trying too many new foods at once can feel expensive and overwhelming. Choose one new vegetable and one familiar way to prepare it.",
                        "For example, roast cauliflower with the same seasoning you use on potatoes, add zucchini to pasta sauce, or try cabbage in a stir-fry. Familiar flavors make new foods easier.",
                    ],
                ),
                (
                    "Do Not Ignore Canned Options",
                    [
                        "Canned tomatoes, corn, peas, pumpkin, beets, and green beans can be useful. Choose options that fit your sodium and sugar needs, and rinse when helpful.",
                        "Canned vegetables can make soups, stews, sauces, and bowls faster. Convenience is part of a sustainable nutrition routine.",
                    ],
                ),
                (
                    "Make Vegetables Part of the Meal",
                    [
                        "Vegetables are easier to enjoy when they are not treated like a punishment side dish. Put them in the main meal with protein, carbohydrates, and flavor.",
                        "A vegetable rice bowl, pasta with vegetables and beans, potato with vegetables and yogurt sauce, or sandwich with extra produce can feel satisfying and normal.",
                    ],
                ),
            ],
            [
                ("Balanced Plate Printable Guide", "/balanced-plate-printable-guide"),
                ("Fiber-Rich Carbohydrates Guide", "/fiber-rich-carbohydrates-guide"),
                ("Healthy Snack Plate Ideas", "/healthy-snack-plate-ideas"),
                ("Foods That Support Better Digestion", "/foods-support-better-digestion"),
            ],
        ),
    },
    {
        "title": "Budget-Friendly Healthy Meals: Simple Balanced Ideas",
        "slug": "budget-friendly-healthy-meals",
        "category": "Nutrition",
        "keyword": "budget friendly healthy meals",
        "meta_title": "Budget-Friendly Healthy Meals",
        "meta_description": "Try budget-friendly healthy meals using beans, eggs, oats, frozen vegetables, potatoes, rice, and simple balanced plate ideas.",
        "excerpt": "Budget-friendly healthy meal ideas built around affordable staples, flexible ingredients, and balanced plate basics.",
        "image": "budget-friendly-healthy-meals.png",
        "image_alt": "budget friendly healthy meals",
        "content": article(
            [
                "Healthy meals do not have to depend on expensive specialty foods. Many budget-friendly staples can build satisfying balanced plates when you combine protein, produce, fiber-rich carbohydrates, and flavor.",
                "A practical budget approach focuses on foods you will actually use: beans, lentils, eggs, oats, potatoes, rice, frozen vegetables, canned tomatoes, yogurt, peanut butter, and seasonal produce.",
            ],
            [
                (
                    "Build Around Low-Cost Staples",
                    [
                        "Start with staples that can become multiple meals. Beans can become bowls, soups, wraps, and snack plates. Oats can become breakfast. Potatoes can become dinner. Rice can pair with vegetables and protein.",
                        "Choose staples based on your kitchen and culture. Budget-friendly eating should feel familiar and usable, not like a list of foods that do not fit your life.",
                    ],
                ),
                (
                    "Use Beans and Lentils Often",
                    [
                        "Beans and lentils are useful because they provide protein, fiber, and carbohydrates. They can be canned or dried, depending on your time and budget.",
                        "Try black bean bowls, lentil soup, chickpea salad, bean tacos, hummus plates, or lentils with rice and vegetables. Add sauce or spices so the meal feels satisfying.",
                    ],
                ),
                (
                    "Keep Frozen Vegetables on Hand",
                    [
                        "Frozen vegetables can reduce waste because you use only what you need. They work well in soups, stir-fries, pasta, rice bowls, omelets, and casseroles.",
                        "If fresh produce is expensive or spoils quickly, frozen vegetables can keep balanced meals possible during busy weeks.",
                    ],
                ),
                (
                    "Plan Meals That Share Ingredients",
                    [
                        "Ingredient overlap saves money. If you buy brown rice, beans, salsa, greens, and yogurt, you can make bowls, wraps, snack plates, and simple dinners.",
                        "Avoid buying ingredients for one recipe unless you know how to use the leftovers. The most budget-friendly ingredient is one that appears in several meals.",
                    ],
                ),
                (
                    "Try Five Budget Meal Ideas",
                    [
                        "<ul><li>Oats with peanut butter, banana, and cinnamon.</li><li>Rice bowl with beans, frozen vegetables, and salsa.</li><li>Eggs with potatoes and sauteed greens.</li><li>Lentil soup with whole-grain bread.</li><li>Greek yogurt with fruit, oats, and nuts or seeds.</li></ul>",
                        "These meals can be adjusted based on sales, preferences, and what is already in the kitchen. The structure matters more than the exact ingredient.",
                    ],
                ),
                (
                    "Shop Sales With a Plan",
                    [
                        "Sales are useful when they match foods you already eat. Buying a sale item you will not use is still wasted money. Before shopping, check what you have and choose meals that use those foods.",
                        "If a staple is on sale and you have storage space, stocking up can help. This works best for oats, rice, beans, lentils, canned tomatoes, frozen vegetables, and other foods you use regularly.",
                    ],
                ),
                (
                    "Make Flavor Affordable",
                    [
                        "Flavor does not need to be expensive. Herbs, spices, lemon, vinegar, salsa, garlic, onions, hot sauce, and yogurt sauce can make simple staples feel different.",
                        "Choose a few flavors you enjoy and use them often. A bean bowl can taste very different with salsa, curry spices, pesto, or lemon-herb dressing.",
                    ],
                ),
                (
                    "Reduce Food Waste",
                    [
                        "Food waste quietly raises grocery costs. Plan one leftover meal, freeze extra portions, and use produce before buying more. Keep a small area in the refrigerator for foods that need attention.",
                        "If vegetables are close to spoiling, add them to soup, eggs, rice, pasta, or a roasted tray. If fruit is soft, use it in oatmeal, yogurt, or smoothies.",
                    ],
                ),
                (
                    "Use Convenience Carefully",
                    [
                        "Convenience foods can still fit a budget if they prevent takeout or skipped meals. Microwave rice, canned beans, frozen vegetables, and prewashed greens may cost more than raw ingredients but save time.",
                        "Choose convenience where it solves a real problem. If chopping vegetables stops you from cooking, frozen vegetables may be worth it.",
                    ],
                ),
                (
                    "Keep Budget Meals Balanced",
                    [
                        "A very cheap meal may not keep you satisfied if it lacks protein or fiber. Add beans, eggs, yogurt, tofu, fish, poultry, nuts, or seeds where possible. Add vegetables or fruit when you can.",
                        "Balanced meals help stretch food because they are more satisfying. The goal is not the cheapest possible plate. The goal is affordable food that supports your day.",
                    ],
                ),
            ],
            [
                ("Balanced Plate Printable Guide", "/balanced-plate-printable-guide"),
                ("Simple Grocery List for Healthy Eating", "/simple-grocery-list-for-healthy-eating"),
                ("Beginner Meal Prep Checklist", "/beginner-meal-prep-checklist"),
                ("How to Add Protein to Every Meal", "/add-protein-to-every-meal"),
            ],
        ),
    },
    {
        "title": "Mindful Eating for Beginners: A Simple Non-Diet Guide",
        "slug": "mindful-eating-for-beginners",
        "category": "Nutrition",
        "keyword": "mindful eating for beginners",
        "meta_title": "Mindful Eating for Beginners",
        "meta_description": "Learn mindful eating for beginners with simple hunger check-ins, slower meals, non-diet awareness, and practical reflection prompts.",
        "excerpt": "A beginner-friendly mindful eating guide focused on awareness, hunger cues, satisfaction, and calmer meals without diet pressure.",
        "image": "mindful-eating-for-beginners.png",
        "image_alt": "mindful eating for beginners",
        "content": article(
            [
                "Mindful eating is a way to pay attention to food, hunger, fullness, satisfaction, and emotions without turning meals into another strict rule system. For beginners, it works best when it stays simple and nonjudgmental.",
                "This guide is not a weight-loss plan. It is a set of awareness practices that may help you slow down, notice patterns, and build a calmer relationship with everyday meals.",
            ],
            [
                (
                    "Start With One Meal",
                    [
                        "Do not try to eat every meal mindfully at once. Choose one meal or snack per day for a short check-in. Breakfast, lunch, or an afternoon snack can be a good starting point.",
                        "The practice can be as simple as pausing before eating and asking: how hungry am I, what would feel satisfying, and what does my body need right now?",
                    ],
                ),
                (
                    "Notice Hunger Without Judging It",
                    [
                        "Hunger is information, not a failure. It can show up as stomach emptiness, low energy, irritability, difficulty focusing, or thinking about food. Different people experience hunger differently.",
                        "Try rating hunger from one to ten before a meal. The number is not for control. It is for awareness. Over time, you may notice patterns, such as waiting too long to eat or choosing snacks that do not satisfy.",
                    ],
                ),
                (
                    "Slow Down the First Few Bites",
                    [
                        "You do not need to eat slowly for the entire meal. Start by slowing down the first few bites. Notice texture, temperature, flavor, and whether the food tastes the way you expected.",
                        "This small pause can make the meal feel more intentional. It can also help you notice whether you are eating from hunger, stress, habit, distraction, or a mix of reasons.",
                    ],
                ),
                (
                    "Reduce One Distraction",
                    [
                        "Mindful eating does not require silent meals. Real life includes work, family, phones, and noise. Instead of removing every distraction, reduce one. Put the phone face down, close the laptop, or take three breaths before eating.",
                        "Even a small reduction in distraction can help you notice the meal more clearly. The goal is awareness, not perfection.",
                    ],
                ),
                (
                    "Check Satisfaction, Not Just Fullness",
                    [
                        "Fullness is physical. Satisfaction includes taste, texture, comfort, and whether the meal felt complete. A meal can be filling but not satisfying, which may lead to grazing later.",
                        "Balanced meals often support satisfaction because they include protein, produce, fiber-rich carbohydrates, and flavor. If you finish a meal and still feel unsatisfied, ask what was missing.",
                    ],
                ),
                (
                    "Use Gentle Reflection Prompts",
                    [
                        "<ul><li>What did I notice before eating?</li><li>Did this meal feel satisfying?</li><li>Was I distracted, rushed, calm, or stressed?</li><li>What helped me feel more present?</li><li>What would make the next meal easier?</li></ul>",
                        "These prompts are not meant to create guilt. They are meant to help you learn from meals the same way you might learn from sleep, stress, or energy patterns.",
                    ],
                ),
                (
                    "Avoid Turning Mindful Eating Into a Diet Rule",
                    [
                        "Mindful eating can become stressful if it turns into a demand to eat perfectly, chew a certain number of times, or never eat emotionally. Humans eat for many reasons, including hunger, pleasure, culture, convenience, and comfort.",
                        "The practice is to notice with kindness. If you eat quickly or emotionally, you can still learn from it without shame.",
                    ],
                ),
                (
                    "Practice With Snacks",
                    [
                        "Snacks are a low-pressure place to practice. Before a snack, ask whether you need energy, comfort, a break, hydration, or a more complete meal. Then choose something that matches the need as well as possible.",
                        "A snack plate with protein, produce, and a fiber-rich carbohydrate can be useful when you need steadier energy between meals.",
                    ],
                ),
                (
                    "Know When Extra Support Matters",
                    [
                        "If eating feels highly stressful, rigid, chaotic, or tied to intense guilt, mindful eating prompts may not be enough. A registered dietitian, therapist, or qualified healthcare professional can provide support.",
                        "This is especially important for anyone with a history of eating disorders or medical conditions requiring nutrition guidance.",
                    ],
                ),
                (
                    "Keep the Practice Small",
                    [
                        "A small mindful eating practice is more sustainable than a complicated one. Pause once, notice hunger once, slow down the first few bites, or reflect after one meal.",
                        "Over time, these small check-ins can make meals feel less automatic and more connected to your actual needs.",
                    ],
                ),
            ],
            [
                ("Balanced Plate Printable Guide", "/balanced-plate-printable-guide"),
                ("Healthy Snack Plate Ideas", "/healthy-snack-plate-ideas"),
                ("Journaling for Mental Clarity", "/journaling-mental-clarity"),
                ("Daily Wellness Routine for Beginners", "/daily-wellness-routine-beginners"),
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
