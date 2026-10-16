# Syntecxhub AI Internship - Week 1
## Project 2: Rule-Based Expert System

### Overview
A beginner-friendly Python command-line project demonstrating a rule-based expert system using a plant-health example. The user selects observations, the program applies IF-THEN rules using forward chaining, and displays conclusions with an inference log.

### Requirements covered
- Facts base: observations selected by the user.
- IF-THEN rule engine: rules are stored in `RULES`.
- Forward chaining: rules repeatedly add new facts until no new fact can be inferred.
- Multi-step inference: `dry_soil` -> `soil_is_dry` -> `water_stress` -> possible conclusion.
- Inference log: each applied rule and its reason are displayed.

### Requirements
Python 3.8 or newer. No external libraries required.

### Run on Windows
1. Extract the ZIP.
2. Open the extracted project folder.
3. Click the folder address bar, type `cmd`, and press Enter.
4. Run `python main.py`. If that fails, run `py main.py`.

### Example test
Enter `1,2` to select Yellow leaves and Dry soil. The system should infer Soil is dry, Water stress, and Possible underwatering.

### Forward chaining
1. Start with facts selected by the user.
2. Check each rule.
3. If all conditions are known, add the rule's conclusion as a new fact.
4. Repeat until no rule adds a new fact.
5. Display conclusions and the inference log.

### GitHub repository name
`Syntecxhub_Rule_Based_Expert_System`

Upload `main.py` and `README.md` to the repository, then submit the repository link using the official internship Submission Form.

### Note
This is an educational demonstration, not a definitive plant diagnosis. Verify real plant problems with a trusted gardening or agricultural source.
