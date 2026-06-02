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
        "title": "Healthy Eating on a Budget",
        "url": "https://www.myplate.gov/web/eat-healthy/healthy-eating-budget",
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
    html.append("<p>Disclaimer: This article is for general educational purposes only and is not a substitute for professional medical or nutrition advice.</p>")
    return "\n".join(html)


POSTS = [
    {
        "title": "Healthy Pantry Staples for Beginners: Build Balanced Meals Faster",
        "slug": "healthy-pantry-staples-for-beginners",
        "category": "Nutrition",
        "keyword": "healthy pantry staples for beginners",
        "meta_title": "Healthy Pantry Staples for Beginners",
        "meta_description": "Stock healthy pantry staples for beginners with beans, grains, oats, sauces, canned foods, and simple balanced meal ideas.",
        "excerpt": "A beginner pantry staples guide for building balanced meals faster with shelf-stable foods and flexible flavor basics.",
        "image": "healthy-pantry-staples-for-beginners.png",
        "image_alt": "healthy pantry staples for beginners",
        "content": article(
            [
                "Healthy eating becomes easier when your pantry contains foods that can turn into real meals quickly. A beginner pantry does not need to be expensive, huge, or perfectly organized. It just needs a few staples you understand and actually use.",
                "The best pantry staples support balanced plates: protein, produce, fiber-rich carbohydrates, and flavor. They also help on days when fresh groceries are low, cooking energy is low, or the original meal plan falls apart.",
            ],
            [
                ("Start With Foods That Solve Real Problems", [
                    "Before buying new pantry items, think about the moments when meals usually get difficult. Maybe breakfast is rushed, lunch becomes takeout, or dinner feels impossible after work. Pantry staples should answer those moments.",
                    "If breakfast is the problem, oats, nut butter, seeds, and shelf-stable milk may help. If lunch is the problem, canned beans, tuna packets, whole-grain crackers, and soup can help. If dinner is the problem, rice, lentils, pasta, canned tomatoes, and frozen vegetables can become quick meals.",
                ]),
                ("Choose Protein Staples", [
                    "Protein helps pantry meals feel more satisfying. Good beginner options include canned beans, lentils, chickpeas, tuna or salmon packets, nut butter, nuts, seeds, shelf-stable tofu where available, and protein-rich pasta.",
                    "Keep at least two protein staples you enjoy. Beans and lentils are flexible because they work in bowls, soups, wraps, salads, and snack plates. Nut butter can support breakfast, snacks, smoothies, and toast.",
                ]),
                ("Add Fiber-Rich Carbohydrates", [
                    "Fiber-rich carbohydrates help pantry meals feel complete. Oats, brown rice, quinoa, whole-grain pasta, whole-grain crackers, potatoes, sweet potatoes, beans, and lentils can all fit depending on your budget and preferences.",
                    "Choose staples you know how to prepare. A food is not useful just because it is healthy. It becomes useful when you can turn it into a meal on a tired day.",
                ]),
                ("Keep Canned and Jarred Foods Useful", [
                    "Canned tomatoes, beans, lentils, corn, pumpkin, beets, tuna, salmon, soups, and lower-sodium broth can make cooking faster. Jarred salsa, marinara, roasted peppers, olives, and curry sauces can add flavor with little effort.",
                    "If sodium is a concern, compare labels and rinse canned beans or vegetables when helpful. If budget is the main concern, buy the options you use most often and rotate gradually.",
                ]),
                ("Use Frozen Foods as Pantry Helpers", [
                    "Frozen foods are not technically pantry items, but they serve the same purpose: backup ingredients that last. Frozen vegetables, fruit, edamame, fish, and whole-grain bread can help build balanced meals without relying only on fresh food.",
                    "Frozen produce is especially helpful if fresh produce spoils before you use it. It lets you add color and fiber to rice bowls, soups, pasta, eggs, smoothies, and snack plates.",
                ]),
                ("Stock Flavor Basics", [
                    "Flavor basics are what make simple pantry meals enjoyable. Keep a few spices, herbs, vinegar, olive oil, hot sauce, salsa, lemon juice, soy sauce, tahini, or shelf-stable dressings that match the foods you like.",
                    "You do not need a huge spice collection. Start with three flavors you already enjoy. For example, salsa for bowls, cinnamon for oats, and garlic or Italian seasoning for pasta.",
                ]),
                ("Build Three Emergency Meals", [
                    "<ul><li>Bean bowl: canned beans, rice, frozen vegetables, salsa, and yogurt or avocado if available.</li><li>Quick pasta: whole-grain pasta, canned tomatoes, lentils, herbs, and frozen spinach.</li><li>Breakfast plate: oats, nut butter, fruit, seeds, and milk or yogurt.</li></ul>",
                    "Emergency meals are important because they prevent the all-or-nothing feeling. Even if the meal is simple, it can still include protein, fiber, produce, and flavor.",
                ]),
                ("Avoid Buying Too Many New Staples", [
                    "It is tempting to buy many healthy pantry foods at once, but crowded shelves can create confusion. Start with five to eight staples and learn how to use them. Add new foods only when you know what meal they will support.",
                    "This keeps the pantry useful instead of decorative. A smaller pantry that gets used is better than a full pantry that makes every meal feel complicated.",
                ]),
                ("Organize by Meal Type", [
                    "Group breakfast staples together, bowl ingredients together, soup or pasta items together, and snack items together. This makes it easier to see meal possibilities instead of staring at random packages.",
                    "A simple shelf label or clear bin can help, but organization does not need to be perfect. Visibility matters most. If you can see the food, you are more likely to use it.",
                ]),
                ("Review the Pantry Before Shopping", [
                    "Before buying groceries, check what you already have. Choose one pantry item that needs to be used and build a meal around it. This saves money and reduces waste.",
                    "For example, if you have lentils, buy vegetables and a sauce. If you have oats, buy fruit and yogurt. If you have rice, buy beans and greens. The pantry becomes the starting point, not the forgotten corner.",
                ]),
            ],
            [
                ("Balanced Plate Printable Guide", "/balanced-plate-printable-guide"),
                ("Simple Grocery List for Healthy Eating", "/simple-grocery-list-for-healthy-eating"),
                ("Budget-Friendly Healthy Meals", "/budget-friendly-healthy-meals"),
                ("Beginner Meal Prep Checklist", "/beginner-meal-prep-checklist"),
            ],
        ),
    },
    {
        "title": "Easy Balanced Dinner Formula for Busy Weeknights",
        "slug": "easy-balanced-dinner-formula",
        "category": "Nutrition",
        "keyword": "easy balanced dinner formula",
        "meta_title": "Easy Balanced Dinner Formula",
        "meta_description": "Use an easy balanced dinner formula with protein, produce, fiber-rich carbs, and flavor for practical weeknight meals.",
        "excerpt": "A simple balanced dinner formula for weeknights when you want a satisfying meal without complicated recipes.",
        "image": "easy-balanced-dinner-formula.png",
        "image_alt": "easy balanced dinner formula",
        "content": article(
            [
                "Dinner can become stressful when every night feels like a brand-new decision. An easy balanced dinner formula gives you a repeatable structure: protein, produce, fiber-rich carbohydrate, and flavor.",
                "This formula is not a strict rule. It is a quick way to build meals that feel satisfying and realistic, especially on busy weeknights when time and energy are limited.",
            ],
            [
                ("The Four-Part Dinner Formula", [
                    "Start with one protein, one produce option, one fiber-rich carbohydrate, and one flavor element. Protein might be beans, eggs, tofu, fish, chicken, lentils, yogurt sauce, or cottage cheese. Produce can be fresh, frozen, canned, raw, or cooked.",
                    "Fiber-rich carbohydrates might include potatoes, rice, quinoa, whole-grain pasta, whole-grain bread, beans, lentils, or fruit. Flavor might come from salsa, herbs, spices, dressing, lemon, hummus, pesto, or a sauce.",
                ]),
                ("Choose the Protein First", [
                    "Protein often takes the most planning, so choose it first. If you have cooked chicken, tofu, lentils, beans, eggs, or fish, dinner already has a direction. If you have no prepared protein, choose a quick option.",
                    "Quick protein options include canned beans, eggs, Greek yogurt sauce, tuna packets, tofu, lentils, hummus, cottage cheese, or leftovers. Keeping one fast protein ready can save many weeknight dinners.",
                ]),
                ("Add Produce Without Overcomplicating It", [
                    "Produce can be simple. Use frozen vegetables in rice bowls, bagged greens with pasta, tomatoes on toast, carrots with hummus, or roasted vegetables from earlier in the week.",
                    "The produce part does not need to be perfect or huge. Adding one colorful option is a good start. Over time, you can add more variety or larger portions if that feels natural.",
                ]),
                ("Pick the Carbohydrate That Fits the Night", [
                    "Some nights need fast carbohydrates, such as microwave rice, toast, potatoes, pasta, or tortillas. Other nights allow slower options like roasted sweet potatoes or cooked grains.",
                    "Carbohydrates help dinner feel complete and can support energy. Pairing them with protein and produce usually feels steadier than eating one part alone.",
                ]),
                ("Use Flavor to Tie the Meal Together", [
                    "A meal can have good ingredients and still feel boring without flavor. Choose one sauce, seasoning, or dressing to connect the plate. Salsa can connect beans, rice, and vegetables. Pesto can connect pasta, greens, and protein. Lemon-herb yogurt can connect potatoes, fish, and vegetables.",
                    "If dinner often feels bland, do not add more complicated recipes first. Add better flavor tools.",
                ]),
                ("Try Five Balanced Dinner Templates", [
                    "<ul><li>Bowl: rice, beans, vegetables, salsa, and yogurt sauce.</li><li>Plate: eggs, potatoes, greens, and fruit.</li><li>Pasta: whole-grain pasta, lentils, tomatoes, spinach, and herbs.</li><li>Wrap: tofu or chicken, vegetables, hummus, and whole-grain tortilla.</li><li>Soup: lentils, vegetables, broth, herbs, and bread.</li></ul>",
                    "Templates are useful because they give direction without locking you into exact ingredients. Swap based on what you have.",
                ]),
                ("Make Dinner Easier With Prep", [
                    "Dinner prep does not need to mean full meals. Cook a grain, wash greens, prepare one protein, or mix one sauce. Even one prepared component can make dinner feel more possible.",
                    "If you have 15 minutes, prepare the part of dinner that usually slows you down. For some people that is chopping vegetables. For others it is cooking protein or choosing a sauce.",
                ]),
                ("Plan Low-Energy Dinners", [
                    "Low-energy dinners are not failures. They are part of a sustainable routine. Keep two dinners that require almost no cooking, such as yogurt bowls, hummus plates, bean bowls, eggs and toast, or soup with bread.",
                    "These meals can still follow the formula. The point is to reduce friction, not to make every dinner impressive.",
                ]),
                ("Use Leftovers Creatively", [
                    "Leftovers become easier when you change the format. Roasted vegetables can become a bowl, wrap, pasta add-in, or breakfast side. Beans can become soup, salad, tacos, or a snack plate.",
                    "Changing the sauce or carbohydrate can make leftovers feel new. This helps reduce waste and makes dinner faster.",
                ]),
                ("Know When Simple Is Enough", [
                    "A balanced dinner does not need ten ingredients. Beans, rice, frozen vegetables, and salsa can be enough. Eggs, toast, fruit, and greens can be enough. Pasta, lentils, tomatoes, and spinach can be enough.",
                    "If dinner supports your evening and fits your life, it is doing its job.",
                ]),
            ],
            [
                ("Balanced Plate Printable Guide", "/balanced-plate-printable-guide"),
                ("Meal Planning for Busy Weeks", "/meal-planning-for-busy-weeks"),
                ("How to Add Protein to Every Meal", "/add-protein-to-every-meal"),
                ("Fiber-Rich Carbohydrates Guide", "/fiber-rich-carbohydrates-guide"),
            ],
        ),
    },
    {
        "title": "Simple Breakfast Meal Prep for Busy Mornings",
        "slug": "simple-breakfast-meal-prep",
        "category": "Nutrition",
        "keyword": "simple breakfast meal prep",
        "meta_title": "Simple Breakfast Meal Prep",
        "meta_description": "Try simple breakfast meal prep ideas with protein, fiber, fruit, oats, yogurt, eggs, and realistic busy-morning routines.",
        "excerpt": "Simple breakfast meal prep ideas for busy mornings, built around protein, fiber, fruit, and low-stress planning.",
        "image": "simple-breakfast-meal-prep.png",
        "image_alt": "simple breakfast meal prep",
        "content": article(
            [
                "Breakfast meal prep can make mornings calmer, especially when you wake up rushed or start work quickly. The goal is not to create perfect breakfasts. The goal is to make a balanced option easier to reach.",
                "A useful breakfast includes some combination of protein, fiber-rich carbohydrates, fruit or vegetables, and flavor. With a little prep, those pieces can come together in minutes.",
            ],
            [
                ("Choose Your Breakfast Style", [
                    "Some people like a grab-and-go breakfast. Others prefer something warm. Some need a small breakfast and a later snack. Start by choosing the style that fits your morning instead of copying someone else's routine.",
                    "Good styles include overnight oats, yogurt bowls, egg plates, smoothies, toast, breakfast wraps, cottage cheese bowls, or simple snack plates.",
                ]),
                ("Prep One Component First", [
                    "You do not need to prep five full breakfasts. Start with one component. Wash fruit, portion oats, boil eggs, mix yogurt bowls, prepare chia pudding, or set out whole-grain bread and nut butter.",
                    "One prepared component can reduce morning decisions. If fruit is washed and yogurt is ready, breakfast takes less effort.",
                ]),
                ("Include Protein for Staying Power", [
                    "Protein can help breakfast feel more satisfying. Options include Greek yogurt, eggs, cottage cheese, tofu, milk, soy milk, nut butter, nuts, seeds, or protein-rich leftovers.",
                    "If your breakfast leaves you hungry quickly, check whether it includes enough protein and fiber. Adding yogurt, eggs, nuts, seeds, or beans may help.",
                ]),
                ("Add Fiber-Rich Carbohydrates", [
                    "Oats, whole-grain toast, fruit, beans, potatoes, and whole-grain cereal can support energy and fullness. Pairing them with protein usually feels more complete than eating them alone.",
                    "For example, oats can pair with yogurt and fruit. Toast can pair with eggs or nut butter. Potatoes can pair with eggs, tofu, or beans.",
                ]),
                ("Try Five Prep-Friendly Breakfasts", [
                    "<ul><li>Overnight oats with yogurt, berries, and chia seeds.</li><li>Boiled eggs with toast and fruit.</li><li>Greek yogurt with oats, nuts, and cinnamon.</li><li>Breakfast wrap with eggs or tofu and vegetables.</li><li>Smoothie pack with fruit, greens, oats, and a protein source.</li></ul>",
                    "Pick one option for the week instead of trying all five. Repetition helps you learn what actually works.",
                ]),
                ("Make Breakfast Portable", [
                    "If you commute or start work early, portable breakfast matters. Use containers that are easy to clean and foods that travel well. Yogurt bowls, wraps, fruit, boiled eggs, oats, and snack plates can all work.",
                    "Pack an add-on if your morning appetite changes. Nuts, fruit, crackers, or yogurt can help when breakfast is smaller than expected.",
                ]),
                ("Plan for Low-Appetite Mornings", [
                    "Some people are not hungry right after waking. In that case, prep a small option and a later snack. A smoothie, yogurt, fruit with nut butter, or toast may be easier than a full meal.",
                    "Pay attention to energy later in the morning. If skipping breakfast leads to intense hunger or low focus, a small prepared option may help.",
                ]),
                ("Keep Flavor Simple", [
                    "Flavor makes breakfast repeatable. Cinnamon, berries, banana, peanut butter, salsa, herbs, lemon, vanilla, or cocoa can make basic foods more appealing.",
                    "Choose flavors that match the breakfast. Salsa works with eggs and beans. Cinnamon works with oats and yogurt. Herbs work with tofu or egg plates.",
                ]),
                ("Avoid Over-Prepping", [
                    "Breakfast prep can backfire if you make more than you want to eat. Start with two or three days at a time. This keeps food fresher and lets you adjust if your appetite or schedule changes.",
                    "If you get bored, prep ingredients instead of finished meals. Washed fruit, cooked eggs, oats, and yogurt can combine in different ways.",
                ]),
                ("Use Breakfast to Support the Whole Day", [
                    "A steady breakfast can make the rest of the day easier. It may reduce decision fatigue, make caffeine feel less necessary, and help lunch choices feel calmer.",
                    "The best breakfast is not the most elaborate one. It is the one you can repeat during real mornings.",
                ]),
            ],
            [
                ("High-Fiber Breakfast Ideas", "/high-fiber-breakfast-ideas"),
                ("Healthy Breakfast Ideas", "/healthy-breakfast-ideas"),
                ("How to Add Protein to Every Meal", "/add-protein-to-every-meal"),
                ("Simple Grocery List for Healthy Eating", "/simple-grocery-list-for-healthy-eating"),
            ],
        ),
    },
    {
        "title": "How to Build a Filling Salad That Actually Feels Like a Meal",
        "slug": "how-to-build-a-filling-salad",
        "category": "Nutrition",
        "keyword": "how to build a filling salad",
        "meta_title": "How to Build a Filling Salad",
        "meta_description": "Learn how to build a filling salad with protein, fiber-rich carbs, vegetables, healthy fats, texture, and satisfying dressing.",
        "excerpt": "A practical guide to building filling salads with protein, fiber, texture, and flavor so they feel like real meals.",
        "image": "how-to-build-a-filling-salad.png",
        "image_alt": "how to build a filling salad",
        "content": article(
            [
                "A salad can be a satisfying meal, but only if it has enough substance. A bowl of lettuce alone may leave you hungry quickly. A filling salad includes protein, fiber-rich carbohydrates, produce, healthy fats, texture, and dressing.",
                "The goal is not to make salads perfect. The goal is to make them useful, enjoyable, and filling enough for the meal you need.",
            ],
            [
                ("Start With the Base", [
                    "The base can be leafy greens, chopped vegetables, cabbage, grains, beans, or a mix. Greens are common, but they do not have to be the whole salad.",
                    "If leafy salads do not keep you full, add a grain or bean base. Brown rice, quinoa, lentils, chickpeas, potatoes, or whole-grain pasta can make the salad feel more like a meal.",
                ]),
                ("Add a Protein Anchor", [
                    "Protein is one of the biggest differences between a side salad and a meal salad. Good options include beans, lentils, chickpeas, eggs, tofu, tempeh, fish, poultry, Greek yogurt dressing, cottage cheese, nuts, or seeds.",
                    "Choose a protein that fits the flavor. Chickpeas work with lemon dressing. Eggs work with potatoes and greens. Tofu works with sesame or peanut-style dressing.",
                ]),
                ("Include Fiber-Rich Carbohydrates", [
                    "Many people skip carbohydrates in salads and then feel hungry soon after. Fiber-rich carbohydrates can make a salad more satisfying. Try beans, lentils, roasted potatoes, quinoa, brown rice, corn, fruit, or whole-grain crackers on the side.",
                    "This does not make the salad less healthy. It can make it more complete and easier to use as a real meal.",
                ]),
                ("Use Vegetables for Color and Crunch", [
                    "Vegetables add volume, color, and texture. Try carrots, cucumbers, peppers, tomatoes, cabbage, roasted broccoli, corn, beets, onions, or leftover roasted vegetables.",
                    "Mix raw and cooked vegetables if you like contrast. A salad with only soft ingredients or only crunchy ingredients may feel less satisfying.",
                ]),
                ("Add Fat and Flavor", [
                    "Healthy fats and dressing help carry flavor and make salads more enjoyable. Options include olive oil, avocado, nuts, seeds, tahini, hummus, cheese, olives, or yogurt-based dressing.",
                    "Dressing is not the enemy of a good salad. A salad you do not enjoy is not useful. Choose a dressing that makes the ingredients taste connected.",
                ]),
                ("Think About Texture", [
                    "Texture can make salads feel more satisfying. Add crunch with nuts, seeds, crispy chickpeas, cabbage, carrots, or whole-grain crackers. Add creaminess with avocado, hummus, yogurt dressing, cheese, or beans.",
                    "A filling salad usually has at least two textures. This keeps it from feeling flat.",
                ]),
                ("Try Five Filling Salad Templates", [
                    "<ul><li>Chickpea salad: greens, chickpeas, cucumbers, tomatoes, quinoa, feta, and lemon dressing.</li><li>Egg and potato salad: greens, eggs, roasted potatoes, carrots, and yogurt-herb dressing.</li><li>Tofu bowl salad: cabbage, tofu, brown rice, edamame, carrots, and sesame dressing.</li><li>Bean taco salad: beans, lettuce, corn, salsa, avocado, and tortilla strips.</li><li>Fruit and yogurt salad plate: greens, berries, nuts, chicken or tofu, and vinaigrette.</li></ul>",
                    "Use these as templates, not strict recipes. The formula matters more than the exact ingredients.",
                ]),
                ("Pack Salads Without Sogginess", [
                    "If packing lunch, keep dressing separate or place it at the bottom of the container with sturdy ingredients. Put delicate greens at the top. Add crunchy items right before eating when possible.",
                    "Sturdy vegetables like cabbage, carrots, cucumbers, peppers, and roasted vegetables often hold up better than delicate greens.",
                ]),
                ("Use Leftovers in Salads", [
                    "Leftovers can make salads faster. Add roasted vegetables, cooked grains, beans, chicken, tofu, potatoes, or pasta. A salad can be the easiest way to turn leftovers into a new meal.",
                    "Change the dressing to make leftovers feel different. Rice and beans can become a taco salad, while roasted vegetables can become a lemon-herb salad bowl.",
                ]),
                ("Check Whether the Salad Is Enough", [
                    "After eating, notice whether the salad kept you satisfied. If not, add more protein, fiber-rich carbohydrates, fat, or overall portion next time.",
                    "A filling salad should support your energy. It should not feel like a meal you have to recover from with snacks immediately afterward.",
                ]),
            ],
            [
                ("Balanced Plate Printable Guide", "/balanced-plate-printable-guide"),
                ("How to Eat More Vegetables", "/how-to-eat-more-vegetables"),
                ("How to Add Protein to Every Meal", "/add-protein-to-every-meal"),
                ("Healthy Snack Plate Ideas", "/healthy-snack-plate-ideas"),
            ],
        ),
    },
    {
        "title": "Healthy Snacks for Work: Simple Ideas for Steady Energy",
        "slug": "healthy-snacks-for-work",
        "category": "Nutrition",
        "keyword": "healthy snacks for work",
        "meta_title": "Healthy Snacks for Work",
        "meta_description": "Plan healthy snacks for work with protein, fiber, produce, shelf-stable options, and simple snack plates for busy days.",
        "excerpt": "Healthy snacks for work that use protein, fiber, produce, and practical storage options for busy days.",
        "image": "healthy-snacks-for-work.png",
        "image_alt": "healthy snacks for work",
        "content": article(
            [
                "Healthy snacks for work can make long days feel steadier. A good snack is not just low in calories or quick to grab. It should match your hunger, schedule, storage options, and energy needs.",
                "The most useful work snacks combine protein, fiber-rich carbohydrates, produce, and flavor. This helps the snack feel satisfying instead of leaving you searching for another snack ten minutes later.",
            ],
            [
                ("Use a Snack Formula", [
                    "A simple formula is protein plus fiber plus flavor. Protein might come from yogurt, cheese, eggs, nuts, seeds, hummus, beans, tuna, tofu, or cottage cheese. Fiber might come from fruit, vegetables, oats, whole-grain crackers, beans, or whole-grain bread.",
                    "Flavor makes the snack enjoyable. That might be cinnamon, salsa, herbs, hummus, nut butter, dark chocolate, or a dressing you like.",
                ]),
                ("Match the Snack to the Workday", [
                    "A meeting-heavy day may need portable snacks. A desk day may allow yogurt or a snack plate. A commute day may need shelf-stable options. Choose snacks for the day you actually have.",
                    "If you do not have refrigeration, choose fruit, nuts, roasted chickpeas, whole-grain crackers, nut butter packets, shelf-stable tuna, or other safe options. If you do have a refrigerator, yogurt, hummus, cheese, boiled eggs, and cut vegetables become easier.",
                ]),
                ("Plan Before You Are Over-Hungry", [
                    "Snacks work best when they prevent extreme hunger. If you wait until you are shaky, irritable, or distracted, it may be harder to choose something satisfying.",
                    "Look at your workday and pick one snack window. Midmorning or midafternoon is common. The goal is not rigid timing; it is having a plan before your energy drops.",
                ]),
                ("Try Easy Work Snack Ideas", [
                    "<ul><li>Greek yogurt with berries and oats.</li><li>Apple with peanut butter.</li><li>Hummus with carrots and whole-grain crackers.</li><li>Boiled egg with fruit.</li><li>Cottage cheese with tomatoes and pepper.</li><li>Nuts, fruit, and a few whole-grain crackers.</li><li>Roasted chickpeas with grapes or vegetables.</li></ul>",
                    "Choose two options per week so you do not need to decide every morning.",
                ]),
                ("Keep Shelf-Stable Backups", [
                    "Shelf-stable backups are useful when you forget lunch, meetings run long, or the workday changes. Keep options like nuts, dried fruit, roasted chickpeas, tuna packets, whole-grain crackers, nut butter packets, or low-sugar granola bars if they work for you.",
                    "Backups do not need to be perfect. They need to be available and satisfying enough to help you avoid running on caffeine alone.",
                ]),
                ("Build a Work Snack Drawer", [
                    "A snack drawer can reduce daily packing. Keep a few shelf-stable items in a drawer, bag, or locker. Rotate them so they do not become stale or forgotten.",
                    "If you work from home, create a visible snack area. This helps you choose a planned snack instead of grazing randomly while distracted.",
                ]),
                ("Watch the Caffeine-Snack Loop", [
                    "Sometimes the afternoon slump is treated with more caffeine when the body may need food, water, movement, or a break. Before another coffee, ask whether a snack and water would help.",
                    "Caffeine can fit many routines, but using it instead of food may leave you more tired later. A snack with protein and fiber may feel steadier.",
                ]),
                ("Make Snacks More Filling", [
                    "If snacks never keep you satisfied, add more structure. Fruit alone may not be enough for everyone. Pair fruit with yogurt, nuts, cheese, peanut butter, or crackers. Crackers alone may feel better with hummus or tuna.",
                    "A filling snack usually has at least two parts. Three parts can be even better on long days: protein, produce, and a fiber-rich carbohydrate.",
                ]),
                ("Keep Food Safety in Mind", [
                    "Perishable snacks need safe storage. Use a refrigerator, insulated lunch bag, or ice pack when needed. If a food smells, looks, or tastes off, do not eat it.",
                    "Choose snacks that match your workplace reality. If refrigeration is unreliable, lean on shelf-stable options and pack fresh foods only when you can store them safely.",
                ]),
                ("Use Snacks Without Guilt", [
                    "Snacks are not a failure of willpower. They are one way to meet your body's needs during a long day. A planned snack can support focus, mood, and calmer meal choices later.",
                    "The goal is to build a snack routine that feels useful and flexible, not another rule to follow perfectly.",
                ]),
            ],
            [
                ("Healthy Snack Plate Ideas", "/healthy-snack-plate-ideas"),
                ("Add Protein to Every Meal", "/add-protein-to-every-meal"),
                ("Hydration Tracker Printable", "/hydration-tracker-printable"),
                ("Remote Worker Wellness Checklist", "/remote-worker-wellness-checklist"),
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
