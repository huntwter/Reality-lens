import json
import os

data = [
    {
        "query": "Does shaving make hair grow back thicker?",
        "response": "<div id=\"logic-card\"><p>This is a question about a biological mechanism. The core claim is that cutting hair at the surface alters the follicle's growth properties. Logically, the dead keratin shaft cannot signal the living follicle deep in the dermis to change its growth rate or thickness.</p></div><div id=\"origin-card\"><p>This is a timeless myth, likely arising from the blunt feel of cut hair tips. It feels coarser than the tapered natural tip, creating an illusion of thickness. The belief has persisted for nearly a century despite clinical debunking.</p></div><div id=\"context-card\"><p>The wording is neutral and inquiring. This is often spread by parents or peers as conventional wisdom. It reflects a common human tendency to mistake sensory perception (stubble feeling rough) for biological reality (hair changing structure).</p></div>"
    },
    {
        "query": "Is the Great Wall of China visible from space?",
        "response": "<div id=\"logic-card\"><p>This is a question about visual acuity and object resolution. The claim is that a specific man-made structure is uniquely visible from low Earth orbit. Physically, the wall is long but very narrow and matches the color of the surrounding terrain, making resolution difficult without aid.</p></div><div id=\"origin-card\"><p>This myth predates spaceflight, appearing in layman's literature as early as 1938 (Richard Halliburton). It is a recurring exaggeration of human achievement, often repeated in pop culture but consistently debunked by astronauts.</p></div><div id=\"context-card\"><p>The tone is curious but skeptical. This narrative serves a romanticized view of history and engineering. It persists because it sounds plausible and grand, despite being factually incorrect according to NASA visual observation data.</p></div>"
    },
    {
        "query": "Do we only use 10% of our brains?",
        "response": "<div id=\"logic-card\"><p>The claim states a specific numerical limit on neurological function. Logically, evolution would not sustain an organ that consumes 20% of the body's energy while being 90% useless. Brain mapping shows activity across the entire cerebrum, even during sleep.</p></div><div id=\"origin-card\"><p>This myth likely stems from misinterpretations of early neurological research by William James or the work of Karl Lashley in the 1920s. It is a recurring trope in self-help and fiction (e.g., the movie *Lucy*).</p></div><div id=\"context-card\"><p>The query is usually hopeful, implying potential. It appeals to the desire for self-improvement and hidden latent abilities. The communication style is often aspiring but scientifically illiterate.</p></div>"
    },
    {
        "query": "does sugar make kids hyper?",
        "response": "<div id=\"logic-card\"><p>The statement implies a direct pharmacological stimulant effect of sucrose on pediatric behavior. Double-blind studies, however, show no difference in behavior between sugar and placebo. The effect is largely psychological or environmental.</p></div><div id=\"origin-card\"><p>This concept gained traction in the 1970s with the Feingold Diet. It is a modern parenting myth, reinforced by the excitement of parties where sugar is served, rather than the sugar itself.</p></div><div id=\"context-card\"><p>The tone is often worried or explanatory. Parents use it to rationalize high-energy behavior. It reflects a confirmation bias where observers attribute normal excitement to a specific dietary cause.</p></div>"
    },
    {
        "query": "Do bulls hate the color red?",
        "response": "<div id=\"logic-card\"><p>The question assumes a specific chromatic trigger for aggression in cattle. Biologically, bulls are dichromats (red-green colorblind) and cannot distinguish red. The reaction is logically triggered by the movement of the cape, not the hue.</p></div><div id=\"origin-card\"><p>This is a cultural misconception derived from Spanish bullfighting imagery. The use of the red *muleta* obscures blood, which is a practical rather than provocational choice. The myth has persisted for centuries in folklore.</p></div><div id=\"context-card\"><p>The query poses a simple fact-check. The narrative is dramatic and visual, often used in cartoons and idioms (\"seeing red\"). It simplifies complex animal ethology into a single color-coded trigger.</p></div>"
    },
    {
        "query": "Did Napoleon have short man syndrome?",
        "response": "<div id=\"logic-card\"><p>The claim attributes a personality complex to physical stature. Historically, Napoleon was average height for his time (approx. 5'7\"). The \"shortness\" is a unit conversion error between French and British measurements.</p></div><div id=\"origin-card\"><p>This is a historical smear campaign, popularized by British propagandist James Gillray in caricatures. It is a recurring historical trope where enemies are diminished physically to diminish them politically.</p></div><div id=\"context-card\"><p>The tone is mocking or psychoanalytical. The \"Napoleon Complex\" is now a psychological idiom. The persistence reveals how political satire can override biographical fact in public memory.</p></div>"
    },
    {
        "query": "Does cracking knuckles cause arthritis?",
        "response": "<div id=\"logic-card\"><p>The inputs link a mechanical habit (cavitation of synovial fluid) to a degenerative disease. Long-term studies, including a doctor who cracked one hand for 60 years, show no correlation between the habit and osteoarthritis.</p></div><div id=\"origin-card\"><p>This is a recurring cautionary tale, likely invented by people annoyed by the sound. It lacks medical origin but has strong cultural retention as a \"grandmother's warning.\"</p></div><div id=\"context-card\"><p>The style is worried or corrective. It serves as a social control mechanism to stop an irritating behavior by invoking a fear of future health consequences.</p></div>"
    },
    {
        "query": "Do bats are blind?",
        "response": "<div id=\"logic-card\"><p>The statement posits total lack of vision in Chiroptera. Biologically, all bats have eyes and can see; many fruit bats have excellent night vision. Echolocation is an additional sense, not a replacement.</p></div><div id=\"origin-card\"><p>The phrase \"blind as a bat\" dates back to Aristotle. It constitutes a linguistic idiom that has overwritten biological fact. It appears timelessly in literature and speech.</p></div><div id=\"context-card\"><p>The statement is usually an idiom or a misconception. It reflects a misunderstanding of nocturnal adaptation. The tone is neutral, often just repeating a common saying.</p></div>"
    },
    {
        "query": "Is tomato a vegetable?",
        "response": "<div id=\"logic-card\"><p>The question requires a definition of terms. Botanically, a tomato is a fruit (ovary of a flowering plant). Culinarily and legally (Nix v. Hedden, 1893), it is classified as a vegetable due to its flavor profile and usage.</p></div><div id=\"origin-card\"><p>This is a pedantic factoid often used to show off trivia knowledge. The legal classification has existed for over a century for tax purposes. It is a recurring \"gotcha\" fact.</p></div><div id=\"context-card\"><p>The tone is often playful or argumentative. It highlights the semantic gap between scientific classification and cultural usage. The user is likely seeking the technical truth over the practical one.</p></div>"
    },
    {
        "query": "Do goldfish have a 3 second memory?",
        "response": "<div id=\"logic-card\"><p>The claim imposes a severe cognitive limit on fish. Experiments show goldfish can learn associations, recognize owners, and remember solutions to mazes for months. The biological hardware supports long-term memory.</p></div><div id=\"origin-card\"><p>This is a modern myth used to justify keeping fish in small bowls. It absolves the owner of guilt regarding animal boredom. It has circulated widely in the late 20th century.</p></div><div id=\"context-card\"><p>The tone is dismissive or curious. It often serves as a metaphor for human forgetfulness. The persistence of this myth shows a lack of empathy for non-mammalian intelligence.</p></div>"
    },
    {
        "query": "Does lightning never strike twice?",
        "response": "<div id=\"logic-card\"><p>The claim suggests a probabilistic impossibility of independent events repeating. Physically, tall structures (like the Empire State Building) are struck dozens of times a year. The path of least resistance remains constant.</p></div><div id=\"origin-card\"><p>This is an old proverb meant to offer comfort about bad luck not repeating. It is metaphorically true for rare events but scientifically false for meteorology.</p></div><div id=\"context-card\"><p>The statement is usually figurative. Taken literally, it is dangerous advice during a storm. The tone is often reassuring, using weather as an analogy for fortune.</p></div>"
    },
    {
        "query": "Is glass a slow moving liquid?",
        "response": "<div id=\"logic-card\"><p>The statement classifies glass as a liquid based on thickness at the bottom of old panes. Physically, glass is an amorphous solid. The unevenness is due to the crown glass usage method of manufacturing, not flow over time.</p></div><div id=\"origin-card\"><p>This is a persistent academic myth, often taught in schools. It arises from misinterpreting material artifacts. It has been debunked by calculating the viscosity required for such flow (longer than the universe's age).</p></div><div id=\"context-card\"><p>The tone is curious and scientific. It reflects a desire to understand the nature of matter. It persists because it offers a fascinating, counter-intuitive explanation for an observed phenomenon.</p></div>"
    },
    {
        "query": "Did Einstein fail math?",
        "response": "<div id=\"logic-card\"><p>The claim contradicts the documented academic record. Einstein mastered differential and integral calculus by age 15. The myth arises from a reversal in the grading scale of his Swiss school.</p></div><div id=\"origin-card\"><p>This is a recurring \"underdog\" narrative used to inspire struggling students. It appeared in Ripley's Believe It or Not! in the 1930s. Einstein himself laughed at the rumor.</p></div><div id=\"context-card\"><p>The tone is hopeful. It serves a clear rhetorical purpose: to suggest that current failure does not preclude future genius. It is a comforting but false biography.</p></div>"
    },
    {
        "query": "Can you see the Great Wall from the moon?",
        "response": "<div id=\"logic-card\"><p>The specific claim extends visibility to the lunar surface. If it's barely visible from LEO, it is impossible to see from the Moon (1000x further). No man-made object is visible from the Moon with the naked eye.</p></div><div id=\"origin-card\"><p>An exaggeration of the \"view from space\" myth. It represents a recurring inflation of facts. Apollo astronauts explicitly confirmed the Earth appears as a marble with no distinct architecture.</p></div><div id=\"context-card\"><p>The tone is typically wondering or incredulous. It tests the limits of human impact on the planet. The belief persists despite simple optical physics refuting it.</p></div>"
    },
    {
        "query": "Do chameleons change color for camouflage?",
        "response": "<div id=\"logic-card\"><p>The claim assigns a defensive purpose to the color change. Biologically, color change is primarily for temperature regulation (thermoregulation) and social signaling (mood, aggression, mating). Camouflage is a secondary, often accidental, benefit.</p></div><div id=\"origin-card\"><p>This is a popular cultural trope found in cartoons and fables. It simplifies complex ethology into a single \"superpower.\" Aristotle hinted at this, but modern pop culture cemented it.</p></div><div id=\"context-card\"><p>The tone is fascinated. Humans project their own desire for invisibility onto the animal. It reflects a functionalist view of nature where every trait must be for survival/hiding.</p></div>"
    },
    {
        "query": "Does gum stay in your stomach for 7 years?",
        "response": "<div id=\"logic-card\"><p>The claim asserts a specific, long duration for digestion. Logically, the gum base is indigestible, but the digestive system passes it through peristalsis like any other fiber/roughage. It exits in a few days.</p></div><div id=\"origin-card\"><p>This is a classic parent-to-child fabrication designed to prevent messy accidents. It is a recurring piece of domestic folklore without medical basis. </p></div><div id=\"context-card\"><p>The tone is cautionary. It functions as a scare tactic to enforce table manners. The specificity of \"7 years\" gives it a false air of medical precision.</p></div>"
    },
    {
        "query": "Do Vikings wear horned helmets?",
        "response": "<div id=\"logic-card\"><p>The inputs visualize Norse warriors with specific headgear. Historically, horns would be a liability in shield-wall combat (catch points). No archaeological evidence supports this; helmets were simple distinct spectacles.</p></div><div id=\"origin-card\"><p>This imagery originated in 19th-century Wagnerian opera costume design (The Ring Cycle). It is a romantic-era fabrication that became the standard visual shorthand for \"Viking.\"</p></div><div id=\"context-card\"><p>The tone is asking about historical aesthetics. The image projects barbarism and animalistic power, serving a dramatic rather than historical purpose.</p></div>"
    },
    {
        "query": "Is earth flat?",
        "response": "<div id=\"logic-card\"><p>The claim contradicts all geodetic, astronomical, and physical evidence. Gravity forms large mass objects into spheres. Shadows, horizons, and satellite imagery logically confirm a geoid shape.</p></div><div id=\"origin-card\"><p>This is a recurring conspiracy theory. While ancients arguably knew of the sphere (Eratosthenes), modern Flat Earth theory revived in the 19th and 21st centuries as a rejection of institutional science.</p></div><div id=\"context-card\"><p>The tone is often conspiratorial or questioning authority. It reflects a deep distrust of elite knowledge systems rather than a genuine inquiry into geometry.</p></div>"
    },
    {
        "query": "Do vaccines cause autism?",
        "response": "<div id=\"logic-card\"><p>The claim posits a causal link between MMR and autism. Logically, the original study was fraudulent (data manipulation) and retracted. Extensive meta-analyses of millions of children show no statistical correlation.</p></div><div id=\"origin-card\"><p>Originated from the discredited 1998 paper by Andrew Wakefield. It is a modern medical scare rooted in scientific fraud, perpetuated by celebrity endorsement and fear.</p></div><div id=\"context-card\"><p>The tone is fearful and protective. This is a high-stakes emotional narrative concerning child safety. It persists due to the difficulty of proving a negative and the coincidence of diagnosis age with vaccination schedules.</p></div>"
    },
    {
        "query": "Is vitamin C a cure for the cold?",
        "response": "<div id=\"logic-card\"><p>The claim suggests a curative effect. Clinical trials indicate Vitamin C does not prevent colds and only marginally shortens duration if taken *beforehand*. It is not a viral cure or treatment once infected.</p></div><div id=\"origin-card\"><p>Popularized by Linus Pauling in the 1970s. It is a recurring health fad. The Nobel laureate's advocacy weighed heavier than the contradictory data for decades.</p></div><div id=\"context-card\"><p>The tone is hopeful/remedial. People seek agency over illness. It reflects a desire for simple, natural cures to common, incurable annoyances.</p></div>"
    }
]

# Generate 80 more items programmatically to reach 100
# Mixing variations and new topics
topics = [
    ("bananas grow on trees", "Bananas grow on giant herbaceous plants, not trees. The 'trunk' is a pseudostem made of leaves.", "Botanical technicality."),
    ("strawberries are berries", "Botanically, strawberries are aggregate accessory fruits, not true berries (like bananas or watermelons).", "Nomenclature confusion."),
    ("humans swallow 8 spiders a year", "This is a fabrication. Spiders avoid breathing, warm, damp predators. It was likely a fake fact to test viral spread.", "Urban legend."),
    ("dogs mouth cleaner than humans", "Dogs carry different bacteria, not fewer. Their oral hygiene is generally worse. The microbiome is just different.", "Comparison fallacy."),
    ("microwave causes cancer", "Microwaves use non-ionizing radiation. They excite water molecules for heat but cannot damage DNA like UV or X-rays.", "Technophobia."),
    ("sugar causes diabetes", "Type 2 diabetes is linked to obesity and insulin resistance, not sugar intake directly, though excess sugar drives obesity.", "Oversimplification."),
    ("alcohol warms you up", "Alcohol is a vasodilator, moving blood to the skin. You feel warm but lose core heat faster. It is dangerous in cold.", "Physiological illusion."),
    ("shaving darkens hair", "Hair has a tapered tip. Cutting it leaves a blunt end that looks darker/thicker. It does not change pigment.", "Optical illusion."),
    ("cracking knuckles big knuckles", "No evidence links joint cavitation to knuckle size increases. It is purely gas bubble release.", "Old wives tale."),
    ("reading in dark hurts eyes", "It causes temporary strain and fatigue, but no permanent structural damage to the eye.", "Parental warning."),
    ("wait an hour after eating to swim", "Digestion diverts some blood, but not enough to cause drowning cramps. You might cramp, but you won't die.", "Safety myth."),
    ("blood is blue inside body", "Blood is always red (hemoglobin). Veins look blue due to light scattering through skin (Rayleigh effect).", "Visual misconception."),
    ("birds abandon babies if touched", "Most birds have poor smell. They will not abandon chicks due to human scent. They are devoted parents.", "Nature myth."),
    ("leaving phone plugged in kills battery", "Modern BMS (Battery Management Systems) stop charging at 100%. Heat is the real killer, not the plug.", "Outdated tech advice."),
    ("closing apps saves battery", "Freezing apps in RAM is efficient. Relaunching them takes more CPU/energy. Force closing hurts battery life.", "UX misunderstanding."),
    ("incognito mode is private", "It only stops local history logging. ISPs, websites, and network admins can still see all traffic.", "Privacy illusion."),
    ("macs dont get viruses", "Macs are less targeted due to market share, but susceptible to malware. Security through obscurity is not immunity.", "Brand marketing."),
    ("more megapixels better camera", "Sensor size and optics matter more. High MP on small sensors increases noise. It is a marketing number.", "Marketing gimmick."),
    ("QWERTY designed to slow typing", "Designed to prevent jam-ups on mechanical typewriters by separating frequent pairs. It wasn't to 'slow' humans.", "History of tech."),
    ("AI is conscious", "LLMs extrapolate patterns from training data. They have no subjective experience, qualia, or intent.", "Anthropomorphism."),
    ("diamonds are rare", "Diamonds are carbon (common). Scarcity is artificially maintained by cartels (De Beers).", "Economic manipulation."),
    ("money is backed by gold", "Modern fiat currency is backed by government decree and trust, not a metal standard (ended 1971 in US).", "Economic history."),
    ("printing money causes inflation", "Usually true if supply outpaces value, but velocity of money also matters. It is a complex correlation.", "Econ 101."),
    ("buying a home is always good investment", "Depends on market, interest, and maintenance. Often trails index funds when factoring in all costs.", "Financial dogma."),
    ("tax refund is free money", "It is an interest-free loan you gave to the government. You overpaid and are getting change back.", "Financial illiteracy."),
    ("Einstein failed school", "He was a top student. The myth comes from different grading scales.", "Inspirational myth."),
    ("Newton discovered gravity by apple", "He observed an apple fall and contemplated forces, he wasn't hit on the head. He refined the math later.", "Storytelling."),
    ("Van Gogh cut off ear", "He cut off a piece of the lobe, not the whole ear. The story has been dramatized.", "Art history."),
    ("Salieri killed Mozart", "They were rivals but friendly. Mozart died of illness. The murder is from the play 'Amadeus'.", "Fictionalization."),
    ("Marie Antoinette let them eat cake", "She never said 'Qu'ils mangent de la brioche'. It was a pre-existing trope about oblivious royals.", "Political propaganda."),
    ("water flushes opposite down under", "Coriolis effect works on hurricanes, not toilets. Jets and bowl shape determine flush direction.", "Physics scale error."),
    ("seasons caused by distance to sun", "Caused by axial tilt. Earth is actually closer to sun in Jan (perihelion) than July.", "Astronomy misconception."),
    ("sun is yellow", "The sun is white. Atmosphere scatters blue, making it look yellow/orange/red. Space photos show white.", "Atmospheric optics."),
    ("black holes suck", "They have gravity like anything else. If sun became a black hole, orbit would not change (just get dark).", "Gravity misunderstanding."),
    ("sound in space", "Space is a vacuum. Sound waves need a medium. Sci-fi explosions are for dramatic effect.", "Movie physics."),
    ("left brain right brain", "Brain function is highly interconnected. Personality isn't split by hemisphere dominance.", "Psychology pop-sci."),
    ("lie detectors work", "Polygraphs measure stress/arousal (sweat, pulse), not truth. Sociopaths pass; nervous innocents fail.", "Pseudoscience."),
    ("learning styles", "VARK (visual/audio/etc) has no evidence. Multi-modal learning works best for everyone.", "Educational myth."),
    ("subliminal advertising works", "Flashing 'buy coke' frames has negligible effect. Conscious persuasion is far stronger.", "Cold war fear."),
    ("opposites attract", "In relationships, similarity in values/background predicts longevity better than contrast.", "Romantic cliche."),
    ("spinach has iron", "Decimal point error in 1870 gave it 10x iron. Popeye popularized it. It is average for greens.", "Data error."),
    ("MSG causes headaches", "Chinese Restaurant Syndrome is largely placebo/racism. MSG is naturally in tomatoes/cheese.", "Food stigma."),
    ("organic means pesticide free", "Organic farming uses 'natural' pesticides (copper, rotenone) which can be toxic too.", "Labeling confusion."),
    ("searing meat seals juices", "Searing creates flavor (Maillard reaction) but does not waterproof the steak. Moisture is lost.", "Cooking myth."),
    ("coffee stunts growth", "No evidence. Likely from early studies equating coffee drinkers with smokers.", "Health scare."),
    ("raining cats and dogs", "Idiom origin debated (thatched roofs, drainage), but never literal animals.", "Etymology."),
    ("rule of thumb", "Likely from using thumb for measurements, not beating wives with sticks (a false etymology).", "False history."),
    ("blood is thicker than water", "Original: 'Blood of the covenant is thicker than water of the womb'. Meaning opposite of current use.", "Quote corruption."),
    ("pull yourself up by bootstraps", "Originally meant an impossible task. Now implies self-reliance. Meaning inverted.", "Political idiom."),
    ("survival of the fittest", "Meant 'best fit for environment', not strongest/most aggressive. Cooperation is often 'fit'.", "Evolutionary nuance."),
    ("ostrich head in sand", "They lay low to hide, necks flat. They don't disconnect from reality.", "Animal behavior."),
    ("lemmings jump off cliffs", "Staged by Disney documentarians (White Wilderness). They migrate, not suicide.", "Fake nature doc."),
    ("sharks dont get cancer", "They do. The myth sells cartilage pills.", "Quack medicine."),
    ("toads give warts", "Warts are viral (HPV). Toad bumps are poison glands.", "Folklore."),
    ("camels store water in humps", "They store fat for energy. Water is in blood/cells.", "Animal anatomy."),
    ("ninja wore black", "Real ninjas (shinobi) dressed as farmers/travelers to blend in. Black is for stagehands.", " theatrical convention."),
    ("samurai sword fold 1000 times", "Folded 10-20 times to homogenize poor iron. 1000 folds would oxidize the carbon away.", "Weapon mythology."),
    ("vikings rape and pillage", "They were also traders, explorers, and settlers. History written by victims (monks).", "One-sided history."),
    ("gladiators fight to death", "They were expensive investments. Refs stopped fights. Death was rare.", "Sports history."),
    ("Columbus discovered America", "Leif Erikson was there 500 years prior. Indigenous people were there 15k years.", "Eurocentrism."),
    ("sugar causes hyperactivity", "Placebo effect in parents. No chemical link.", "Parenting myth."),
    ("warm milk sleep", "Tryptophan level is too low. It's just a comforting routine.", "Placebo."),
    ("feed a cold starve a fever", "Both need nutrition/fluids. Starving is bad.", "Old medical rhyme."),
    ("loss of body heat from head", "You lose heat from any exposed surface. Army study used hats vs no gear.", "Bad data interpretation."),
    ("8 glasses of water", "No scientific basis. Fluids come from food too. Drink when thirsty.", "Hydration hype."),
    ("palm trees are trees", "Monocots (grass family). No bark/rings.", "Botanical classification."),
    ("peanuts are nuts", "Legumes (beans). Grow underground.", "Nomenclature."),
    ("koalas are bears", "Marsupials. Not ursine.", "Naming error."),
    ("killer whales are whales", "Delphinidae (Dolphins). Largest dolphin.", "Taxonomy."),
    ("pandas are raccoons", "They are true bears (Ursidae). Red pandas are their own thing.", "Taxonomy."),
    ("Rust is better than C++", "Rust offers memory safety, C++ offers legacy/control. 'Better' is subjective.", "Tech tribalism."),
    ("Python is slow", "Slow for raw compute, fast for dev time. C-extensions (numpy) make it fast.", "Nuance."),
    ("Mac is for creatives", "Standard hardware now. Just OS preference.", "Marketing branding."),
    ("Linux is only for servers", "Desktop Linux is viable. Steam Deck proves gaming works.", "OS stigma."),
    ("Coding is math", "Mostly logic and language. Math needed for specific domains (ML/Game dev).", "Career gatekeeping."),
    ("internet in cloud", "It is underwater cables and data centers. Physical infrastructure.", "Metaphor confusion."),
    ("delete is permanent", "Just marks space as writable. Data forensics can recover until overwritten.", "Digital literacy."),
    ("private mode hides IP", "No, VPN does. Private mode is local only.", "Security misconception."),
    ("hackers wear hoodies", "They look like normal office workers or teenagers.", "media trope."),
    ("AI will kill us", "Currently just pattern matchers. AGI is theoretical.", "Sci-fi fear.")
]

for q, explanation, category in topics:
    data.append({
        "query": q,
        "response": f'<div id="logic-card"><p>Analysis of: {q}. The claim involves {category.lower()}. Logic dictates that {explanation.split(".")[0].lower()}. The premise is often misunderstood due to simplification.</p></div><div id="origin-card"><p>Originating from {category} misconceptions. This is a recurring theme in popular understanding. {explanation}</p></div><div id="context-card"><p>The tone is inquiring about {category}. The user seeks clarification on a commonly held belief. The communication reflects a desire for fact-checking.</p></div>'
    })

# Ensure we have 100
data = data[:100]

with open("a:/downloads/Realitylens/app/core/cached_responses.json", "w") as f:
    json.dump(data, f, indent=4)

print(f"Generated {len(data)} entries.")
