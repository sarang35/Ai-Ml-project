import json
from pathlib import Path

output_path = Path(__file__).parent / "notes_dataset.json"

entries = [
    {"topic": "Photosynthesis", "notes": "- Process by which plants make food using sunlight\n- Takes place in chloroplasts\n- Equation: CO2 + H2O + light → glucose + O2\n- Two stages: light reactions and Calvin cycle"},
    {"topic": "Cellular respiration", "notes": "- Process by which cells convert glucose into energy\n- Takes place in mitochondria\n- Uses oxygen to make ATP\n- Produces carbon dioxide and water as waste"},
    {"topic": "DNA structure", "notes": "- Double helix made of nucleotides\n- Each nucleotide has a sugar, phosphate, and base\n- Base pairs: A-T and C-G\n- Carries genetic information for living organisms"},
    {"topic": "Mitosis", "notes": "- Type of cell division producing two identical daughter cells\n- Phases: prophase, metaphase, anaphase, telophase\n- Used for growth and tissue repair\n- Maintains the same chromosome number"},
    {"topic": "Meiosis", "notes": "- Cell division that produces four non-identical gametes\n- Includes two rounds of division\n- Reduces chromosome number by half\n- Important for sexual reproduction"},
    {"topic": "Ecosystems", "notes": "- Community of organisms and their environment\n- Includes producers, consumers, and decomposers\n- Energy flows from sunlight to plants to animals\n- Balanced ecosystems support biodiversity"},
    {"topic": "The water cycle", "notes": "- Continuous movement of water through Earth's systems\n- Stages: evaporation, condensation, precipitation, collection\n- Driven by solar energy and gravity\n- Essential for distributing freshwater across the planet"},
    {"topic": "Climate change", "notes": "- Long-term change in Earth's temperature and weather patterns\n- Caused by greenhouse gas emissions\n- Effects: rising seas, extreme weather, ecosystem stress\n- Reducing emissions helps slow climate change"},
    {"topic": "World War 2", "notes": "- Fought from 1939 to 1945\n- Major powers: Allies vs Axis\n- Started with Germany invading Poland\n- Ended with atomic bombs on Hiroshima and Nagasaki"},
    {"topic": "French Revolution", "notes": "- Began in 1789 in France\n- Key ideas: liberty, equality, fraternity\n- Ended absolute monarchy and started a republic\n- Led to major political and social changes"},
    {"topic": "Supply and demand", "notes": "- Demand is how much consumers want\n- Supply is how much producers offer\n- Price changes when demand and supply shift\n- Equilibrium is where market supply equals demand"},
    {"topic": "Simple harmonic motion", "notes": "- Repetitive back-and-forth motion around equilibrium\n- Example: pendulum, spring mass system\n- Restoring force proportional to displacement\n- Has a constant period and frequency"},
    {"topic": "Electric circuits", "notes": "- Path for electric current to flow\n- Comprised of voltage source, conductors, and load\n- Series circuits have one path, parallel circuits have multiple paths\n- Measured by current, voltage, and resistance"},
    {"topic": "Ohm's Law", "notes": "- Relationship between voltage, current, and resistance\n- Formula: V = I * R\n- If resistance increases, current decreases for the same voltage\n- Widely used in circuit analysis"},
    {"topic": "Periodic table", "notes": "- Organizes elements by atomic number\n- Groups share similar chemical properties\n- Rows are called periods\n- Metals, nonmetals, and metalloids are arranged systematically"},
    {"topic": "States of matter", "notes": "- Common states: solid, liquid, gas\n- Solids have fixed shape and volume\n- Liquids have fixed volume but change shape\n- Gases expand to fill their container"},
    {"topic": "Pythagorean theorem", "notes": "- In right triangles, a^2 + b^2 = c^2\n- c is the hypotenuse\n- Useful for finding missing side lengths\n- Applies only to right-angled triangles"},
    {"topic": "Latitude and longitude", "notes": "- Latitude measures north-south position\n- Longitude measures east-west position\n- Coordinates locate places on Earth\n- The equator is latitude 0°, prime meridian is longitude 0°"},
    {"topic": "Magnetic fields", "notes": "- Region around a magnet where force is felt\n- Field lines go from north to south poles\n- Moving charges create magnetic fields\n- Used in motors, generators, and compasses"},
    {"topic": "Gravity", "notes": "- Force that attracts objects toward each other\n- Depends on mass and distance\n- Keeps planets in orbit around the Sun\n- Responsible for objects falling to Earth"},
    {"topic": "Newton's first law", "notes": "- Objects stay at rest or move at constant velocity unless acted on\n- Also called the law of inertia\n- Explains why seatbelts are important\n- Applies to objects in space and on Earth"},
    {"topic": "Newton's second law", "notes": "- Force equals mass times acceleration\n- Describes how motion changes with force\n- Larger mass needs more force for same acceleration\n- Basis for many physics calculations"},
    {"topic": "Newton's third law", "notes": "- Every action has an equal and opposite reaction\n- Rockets push exhaust backward to move forward\n- Explains how swimmers push water to move\n- Important in collisions and mechanics"},
    {"topic": "Chemical reactions", "notes": "- Process where substances change into new substances\n- Reactants become products\n- Energy can be released or absorbed\n- Examples include combustion and rusting"},
    {"topic": "Acids and bases", "notes": "- Acids taste sour and release H+ ions\n- Bases taste bitter and release OH- ions\n- pH scale measures acidity\n- Neutralization produces salt and water"},
    {"topic": "Ecosystem food chains", "notes": "- Show how energy flows between organisms\n- Producers create food from sunlight\n- Consumers eat producers or other consumers\n- Decomposers break down dead organisms"},
    {"topic": "Renewable energy", "notes": "- Comes from sources that do not run out\n- Includes solar, wind, hydro, and geothermal\n- Reduces greenhouse gas emissions\n- Helps make energy more sustainable"},
    {"topic": "Human circulatory system", "notes": "- Carries blood, oxygen, and nutrients around the body\n- Includes heart, arteries, veins, and capillaries\n- Heart pumps blood continuously\n- Essential for keeping cells alive"},
    {"topic": "Human respiratory system", "notes": "- Brings oxygen into the body\n- Removes carbon dioxide from the blood\n- Includes lungs, trachea, and diaphragm\n- Works with the circulatory system"},
    {"topic": "Plate tectonics", "notes": "- Earth's crust is divided into moving plates\n- Plate boundaries cause earthquakes and volcanoes\n- Types: divergent, convergent, transform\n- Drives mountain building and ocean trench formation"},
    {"topic": "Volcanoes", "notes": "- Formed when magma reaches Earth's surface\n- Can erupt lava, ash, and gases\n- Often found along plate boundaries\n- Can change landscapes quickly"},
    {"topic": "Earthquakes", "notes": "- Sudden shaking of Earth's crust\n- Caused by movement along faults\n- Measured with a seismograph\n- Can cause damage to buildings and roads"},
    {"topic": "Weather vs climate", "notes": "- Weather is short-term atmospheric conditions\n- Climate is long-term weather patterns\n- Weather can change daily\n- Climate describes trends over years"},
    {"topic": "The greenhouse effect", "notes": "- Gases trap heat in Earth's atmosphere\n- Keeps the planet warm enough for life\n- Too much can cause global warming\n- Important to balance greenhouse gas levels"},
    {"topic": "The digestive system", "notes": "- Breaks down food into nutrients\n- Includes mouth, stomach, intestines, and liver\n- Nutrients are absorbed into the blood\n- Waste is removed from the body"},
    {"topic": "Photosynthesis vs respiration", "notes": "- Photosynthesis builds glucose from CO2 and water\n- Respiration breaks glucose into energy\n- Photosynthesis occurs in plants, respiration in all cells\n- They form a cycle in ecosystems"},
    {"topic": "Probability basics", "notes": "- Probability measures how likely an event is\n- Range is 0 to 1\n- Simple probability = favorable outcomes / total outcomes\n- Used in games and statistics"},
    {"topic": "Ratios", "notes": "- Show how the relationship between two quantities\n- Can be written as a:b or a/b\n- Used to compare parts of a whole\n- Help solve proportion problems"},
    {"topic": "Percentages", "notes": "- Part of a hundred\n- Useful for comparing quantities\n- Found in discounts, grades, and statistics\n- Convert by dividing by 100"},
    {"topic": "Fractions", "notes": "- Represent part of a whole\n- Numerator is the top number\n- Denominator is the bottom number\n- Convert to decimals or percentages"},
    {"topic": "Basic geometry", "notes": "- Study of shapes and space\n- Includes points, lines, angles, and figures\n- Area and perimeter measure size\n- Important for solving real-world problems"},
    {"topic": "Force and motion", "notes": "- Force makes objects speed up, slow down, or change direction\n- Measured in newtons\n- Motion depends on speed and direction\n- Newton's laws describe these relationships"},
    {"topic": "Speed and velocity", "notes": "- Speed is how fast something moves\n- Velocity includes direction\n- Calculated as distance divided by time\n- Important in physics and navigation"},
    {"topic": "Energy forms", "notes": "- Energy exists as kinetic, potential, thermal, and chemical\n- Kinetic is energy of motion\n- Potential is stored energy\n- Energy can change forms but is conserved"},
    {"topic": "The Solar System", "notes": "- Includes the Sun, eight planets, moons, and smaller bodies\n- Terrestrial planets are rocky\n- Gas giants are large and mostly gas\n- Earth is the third planet from the Sun"},
    {"topic": "The moon phases", "notes": "- Moon phases change as the moon orbits Earth\n- Includes new moon, crescent, quarter, gibbous, full moon\n- Caused by sunlight reflecting off the moon\n- Takes about 29.5 days to cycle"},
    {"topic": "The carbon cycle", "notes": "- Carbon moves between air, plants, animals, oceans, and soil\n- Photosynthesis removes CO2 from the air\n- Respiration and decomposition return CO2 to the air\n- Important for life and climate balance"},
    {"topic": "Animal adaptation", "notes": "- Adaptations help animals survive in their habitat\n- Examples include fur, camouflage, and migration\n- Adaptations can be physical or behavioral\n- Evolve over many generations"},
    {"topic": "Food groups", "notes": "- Include fruits, vegetables, grains, protein, and dairy\n- Each group provides important nutrients\n- Balanced diet includes a variety of foods\n- Helps maintain health and energy"},
    {"topic": "Healthy eating", "notes": "- Choose fruits, vegetables, lean proteins, and whole grains\n- Limit sugar, salt, and saturated fats\n- Drink plenty of water\n- Balance portions with physical activity"},
    {"topic": "The nervous system", "notes": "- Carries messages between the brain and body\n- Includes brain, spinal cord, and nerves\n- Controls senses, movement, and thoughts\n- Responds quickly to changes in the environment"},
    {"topic": "The skeletal system", "notes": "- Provides support and protects organs\n- Made of bones and cartilage\n- Helps the body move with muscles\n- Produces blood cells in bone marrow"},
    {"topic": "The endocrine system", "notes": "- Uses hormones to control body functions\n- Includes glands like thyroid and adrenal\n- Regulates growth, metabolism, and reproduction\n- Works with the nervous system"},
    {"topic": "Sound waves", "notes": "- Vibrations that travel through air, water, or solids\n- Measured by frequency and amplitude\n- Humans hear sounds between certain frequencies\n- Sound needs a medium to travel"},
    {"topic": "Light behavior", "notes": "- Light travels in straight lines\n- Can reflect, refract, or be absorbed\n- White light is made of many colors\n- Used in optics, cameras, and eyes"},
    {"topic": "The digestive process", "notes": "- Begins in the mouth with chewing and saliva\n- Continues in the stomach with acids\n- Nutrients are absorbed in the small intestine\n- Waste exits through the large intestine"},
    {"topic": "Cell division", "notes": "- Cells split to make new cells\n- Mitosis makes identical body cells\n- Meiosis makes sex cells with half the chromosomes\n- Essential for growth, repair, and reproduction"},
    {"topic": "Computer programming", "notes": "- Writing instructions for a computer to follow\n- Uses code in languages like Python, Java, and JavaScript\n- Programs solve problems or perform tasks\n- Debugging finds and fixes errors"},
    {"topic": "Algorithms", "notes": "- Step-by-step instructions to solve a problem\n- Used for sorting, searching, and computing\n- Efficiency is measured by time and space\n- Important in computer science"},
    {"topic": "Data structures", "notes": "- Ways to organize data for efficient use\n- Examples include lists, stacks, queues, and trees\n- Choose the right one for the task\n- Helps programs run faster and use less memory"},
    {"topic": "Internet basics", "notes": "- Network of computers around the world\n- Uses protocols like HTTP and TCP/IP\n- Websites are stored on servers\n- Browsers request and display web pages"},
    {"topic": "HTML fundamentals", "notes": "- Markup language for creating webpages\n- Uses tags like <html>, <head>, <body>, <p>, <a>\n- Structures content and adds links\n- Used with CSS and JavaScript"},
    {"topic": "The scientific method", "notes": "- Ask a question and make a hypothesis\n- Conduct an experiment\n- Collect and analyze results\n- Draw conclusions and share findings"},
    {"topic": "Hypothesis", "notes": "- A testable prediction about what will happen\n- Based on prior knowledge or research\n- Used in scientific experiments\n- Can be supported or rejected by data"},
    {"topic": "Accuracy vs precision", "notes": "- Accuracy is how close measurements are to the true value\n- Precision is how close measurements are to each other\n- Both matter in science\n- A result can be precise without being accurate"},
    {"topic": "Cell organelles", "notes": "- Parts of a cell with specific jobs\n- Examples: nucleus, mitochondria, ribosomes\n- Nucleus stores DNA and controls the cell\n- Mitochondria produce energy"},
    {"topic": "Space exploration", "notes": "- Study and travel beyond Earth\n- Includes rockets, satellites, and space probes\n- Helps us learn about planets and stars\n- Advances technology and science"},
    {"topic": "Renewable resources", "notes": "- Natural resources that can be replenished\n- Examples: sunlight, wind, water, biomass\n- More sustainable than fossil fuels\n- Help reduce environmental damage"},
    {"topic": "Nonrenewable resources", "notes": "- Resources that take millions of years to form\n- Examples: coal, oil, natural gas\n- Can be depleted with use\n- Careful use is needed for sustainability"},
    {"topic": "Historical timelines", "notes": "- Show events in the order they happened\n- Help understand causes and effects\n- Use dates and short descriptions\n- Useful for studying history"},
    {"topic": "Geological time", "notes": "- Divides Earth's history into eras and periods\n- Includes Precambrian, Paleozoic, Mesozoic, Cenozoic\n- Shows when major events occurred\n- Helps scientists study ancient life"},
    {"topic": "The rock cycle", "notes": "- Rocks change form over time\n- Igneous, sedimentary, and metamorphic rocks\n- Weathering and heat drive changes\n- Cycle repeats over millions of years"},
    {"topic": "Friction", "notes": "- Force that opposes motion between surfaces\n- Can slow objects down\n- Depends on surface texture and force\n- Useful in brakes and walking"},
    {"topic": "Density", "notes": "- Mass per unit volume\n- Formula: density = mass / volume\n- Determines whether objects float or sink\n- Different materials have different densities"},
    {"topic": "Solutions", "notes": "- Homogeneous mixtures of solute and solvent\n- Saltwater is a common example\n- Concentration measures how strong the solution is\n- Important in chemistry and biology"},
    {"topic": "Reactions rates", "notes": "- Speed at which chemical reactions occur\n- Affected by temperature, concentration, and catalysts\n- Faster reactions produce products more quickly\n- Important in industry and biology"},
    {"topic": "Density and buoyancy", "notes": "- Buoyancy is upward force in fluids\n- Objects float when density is less than fluid density\n- Ships use buoyancy to stay afloat\n- Important in physics and engineering"},
    {"topic": "The immune system", "notes": "- Protects the body from germs and disease\n- Includes white blood cells, antibodies, and lymph nodes\n- Recognizes and destroys pathogens\n- Helps the body recover from illness"},
    {"topic": "Vaccines", "notes": "- Train the immune system to recognize germs\n- Contain weakened or inactive parts of a pathogen\n- Help prevent serious illnesses\n- Have saved millions of lives"},
    {"topic": "Organic chemistry basics", "notes": "- Study of carbon-based compounds\n- Includes hydrocarbons, alcohols, and acids\n- Important in biology, medicine, and materials\n- Carbon can form many different structures"},
    {"topic": "Inertia", "notes": "- Resistance of objects to changes in motion\n- Objects at rest stay at rest unless pushed\n- Objects in motion stay in motion unless stopped\n- Fundamental idea in Newton's first law"},
    {"topic": "Momentum", "notes": "- Product of mass and velocity\n- Heavier or faster objects have more momentum\n- Conserved in collisions without external forces\n- Important in physics and sports"},
    {"topic": "Kinetic energy", "notes": "- Energy of motion\n- Formula: 1/2 m v^2\n- Faster or heavier objects have more kinetic energy\n- Converts to other energy forms during collisions"},
    {"topic": "Potential energy", "notes": "- Stored energy based on position\n- Examples: height, stretched springs\n- Can convert to kinetic energy\n- Depends on mass, height, and gravity"},
    {"topic": "Newton's cradle", "notes": "- Demonstrates conservation of momentum and energy\n- Balls transfer motion through collisions\n- Shows how energy moves from one object to another\n- Common physics classroom demonstration"},
    {"topic": "The ozone layer", "notes": "- Protects Earth from harmful UV rays\n- Located in the stratosphere\n- Damaged by some chemicals like CFCs\n- Important for life on Earth"},
    {"topic": "The nervous system", "notes": "- Carries messages between brain and body\n- Includes brain, spinal cord, and nerves\n- Controls movement, senses, and thoughts\n- Helps respond to the environment"},
    {"topic": "The endocrine system", "notes": "- Uses hormones to regulate body functions\n- Includes glands like thyroid and pancreas\n- Controls growth, metabolism, and reproduction\n- Works with the nervous system"},
    {"topic": "The skeletal system", "notes": "- Provides structure and support for the body\n- Made of bones and cartilage\n- Protects internal organs\n- Works with muscles for movement"},
    {"topic": "The muscular system", "notes": "- Moves the body and maintains posture\n- Includes skeletal, smooth, and cardiac muscles\n- Uses energy from food\n- Important for breathing and circulation"},
    {"topic": "The water cycle", "notes": "- Evaporation turns water into vapor\n- Condensation forms clouds\n- Precipitation falls as rain or snow\n- Collection returns water to oceans, lakes, and soil"}
]

replacement_sets = [
    [
        (" uses ", " requires "),
        (" Uses ", " Requires "),
        (" is ", " is mainly "),
        (" can ", " may "),
        (" helps ", " supports "),
        (" important", " essential"),
        (" includes ", " contains "),
        (" produced ", " generated "),
        (" produces ", " generates "),
        (" occurs ", " happens "),
        (" called ", " known as "),
        (" part of ", " component of "),
    ],
    [
        (" uses ", " relies on "),
        (" Uses ", " Relies on "),
        (" is ", " becomes "),
        (" can ", " is able to "),
        (" helps ", " assists "),
        (" important", " key"),
        (" includes ", " involves "),
        (" produced ", " created "),
        (" produces ", " creates "),
        (" occurs ", " takes place "),
        (" called ", " referred to as "),
        (" part of ", " within "),
    ]
]

def rewrite_notes(notes: str, variant: int) -> str:
    lines = notes.strip().splitlines()
    replacements = replacement_sets[variant - 1]
    new_lines = []

    for line in lines:
        prefix = "- " if line.startswith("- ") else ""
        content = line[2:].strip() if line.startswith("- ") else line.strip()

        for old, new in replacements:
            content = content.replace(old, new)

        # Add a small sentence-level variation for the second variant.
        if variant == 2 and content.startswith("- "):
            content = content.replace("- ", "")

        new_lines.append(f"{prefix}{content}")

    return "\n".join(new_lines)

full_entries = []
for entry in entries:
    full_entries.append(entry)
    full_entries.append({
        "topic": f"{entry['topic']} (overview)",
        "notes": rewrite_notes(entry['notes'], 1)
    })
    full_entries.append({
        "topic": f"{entry['topic']} (summary)",
        "notes": rewrite_notes(entry['notes'], 2)
    })

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(full_entries, f, indent=2, ensure_ascii=False)

print(f"Generated {len(full_entries)} dataset entries at {output_path}")
