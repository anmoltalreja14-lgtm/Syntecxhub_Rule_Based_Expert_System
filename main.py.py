RULES = [
    {"name": "Rule 1", "if": {"dry_soil"}, "then": "soil_is_dry",
     "explanation": "Dry soil means the soil is currently dry."},
    {"name": "Rule 2", "if": {"soil_is_dry"}, "then": "water_stress",
     "explanation": "Dry soil may cause water stress in a plant."},
    {"name": "Rule 3", "if": {"yellow_leaves", "water_stress"}, "then": "possible_underwatering",
     "explanation": "Yellow leaves together with water stress may indicate underwatering."},
    {"name": "Rule 4", "if": {"wet_soil"}, "then": "soil_is_wet",
     "explanation": "Wet soil means the soil is currently wet."},
    {"name": "Rule 5", "if": {"yellow_leaves", "soil_is_wet"}, "then": "possible_overwatering",
     "explanation": "Yellow leaves together with wet soil may indicate overwatering."},
    {"name": "Rule 6", "if": {"white_powder_on_leaves"}, "then": "possible_powdery_mildew",
     "explanation": "A white powder-like coating can be a sign of powdery mildew."},
    {"name": "Rule 7", "if": {"dark_leaf_spots"}, "then": "possible_leaf_spot",
     "explanation": "Dark spots on leaves can be a sign of a leaf-spot problem."},
    {"name": "Rule 8", "if": {"brown_leaf_edges", "soil_is_dry"}, "then": "possible_dryness_stress",
     "explanation": "Brown leaf edges together with dry soil may indicate dryness stress."}
]

LABELS = {
    "yellow_leaves": "Yellow leaves", "dry_soil": "Dry soil", "wet_soil": "Wet soil",
    "white_powder_on_leaves": "White powder on leaves", "dark_leaf_spots": "Dark spots on leaves",
    "brown_leaf_edges": "Brown leaf edges", "soil_is_dry": "Soil is dry",
    "water_stress": "Water stress", "possible_underwatering": "Possible underwatering",
    "soil_is_wet": "Soil is wet", "possible_overwatering": "Possible overwatering",
    "possible_powdery_mildew": "Possible powdery mildew", "possible_leaf_spot": "Possible leaf-spot problem",
    "possible_dryness_stress": "Possible dryness stress"
}
SUGGESTIONS = {
    "possible_underwatering": "Check soil moisture and water appropriately if needed.",
    "possible_overwatering": "Check drainage and avoid watering without checking soil moisture.",
    "possible_powdery_mildew": "Inspect the plant and consult a trusted gardening resource.",
    "possible_leaf_spot": "Inspect affected leaves and avoid wetting foliage unnecessarily.",
    "possible_dryness_stress": "Check soil moisture, temperature, and watering conditions."
}
OBSERVATIONS = [
    ("yellow_leaves", "Yellow leaves"), ("dry_soil", "Dry soil"),
    ("wet_soil", "Wet soil"), ("white_powder_on_leaves", "White powder on leaves"),
    ("dark_leaf_spots", "Dark spots on leaves"), ("brown_leaf_edges", "Brown leaf edges")
]

def forward_chain(initial_facts, rules):
    facts = set(initial_facts)
    log = []
    changed = True
    while changed:
        changed = False
        for rule in rules:
            if rule["if"].issubset(facts) and rule["then"] not in facts:
                facts.add(rule["then"])
                changed = True
                conditions = ", ".join(LABELS.get(x, x) for x in sorted(rule["if"]))
                conclusion = LABELS.get(rule["then"], rule["then"])
                log.append(f'{rule["name"]}: IF {conditions} THEN {conclusion}.\n  Reason: {rule["explanation"]}')
    return facts, log

def main():
    print("=" * 54)
    print("     PLANT HEALTH RULE-BASED EXPERT SYSTEM")
    print("        Syntecxhub AI Internship - Week 1")
    print("=" * 54)
    print("\nSelect the observations you notice in your plant.")
    print("Enter numbers separated by commas, e.g. 1,2. Enter 0 for none.\n")
    for number, (_, label) in enumerate(OBSERVATIONS, start=1):
        print(f"{number}. {label}")
    print("0. No listed observations")
    while True:
        raw = input("\nYour choice: ").strip()
        if raw == "0" or raw == "":
            numbers = []
            break
        try:
            numbers = sorted(set(int(item.strip()) for item in raw.split(",")))
            if any(n < 1 or n > len(OBSERVATIONS) for n in numbers):
                raise ValueError
            break
        except ValueError:
            print(f"Please enter numbers from 1 to {len(OBSERVATIONS)}, separated by commas.")
    initial = {OBSERVATIONS[n - 1][0] for n in numbers}
    print("\n--- Initial Facts ---")
    print("\n".join("- " + LABELS[x] for x in sorted(initial)) if initial else "- No observations entered.")
    facts, log = forward_chain(initial, RULES)
    print("\n--- Inference Log (Forward Chaining) ---")
    if log:
        for i, item in enumerate(log, start=1):
            print(f"\nStep {i}: {item}")
    else:
        print("No rules were triggered by the selected observations.")
    conclusions = ["possible_underwatering", "possible_overwatering", "possible_powdery_mildew",
                   "possible_leaf_spot", "possible_dryness_stress"]
    found = [x for x in conclusions if x in facts]
    print("\n--- Final Conclusions ---")
    if found:
        for item in found:
            print(f"- {LABELS[item]}\n  Suggested action: {SUGGESTIONS[item]}")
    else:
        print("No specific conclusion could be inferred from these observations.")
    print("\nNote: Educational demo only, not a definitive plant diagnosis.")
    print("Verify real plant problems with a trusted gardening or agricultural source.")

if __name__ == "__main__":
    main()
