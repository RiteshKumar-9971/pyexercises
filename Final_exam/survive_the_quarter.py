"""Survive the Quarter - Croissant Rocket marketing game, Scenario A."""

# STUDENT DETAILS
# First and last name: Ritesh Kumar
#Group: scenario_A


# 1. WHAT GOES IN?
# The program reads scenarios_A.csv. It is a comma-separated file with 14 columns:
# ID, Scenario, OptionA, OptionB, OptionC, BudgetA, BudgetB, BudgetC,
# ReputationA, ReputationB, ReputationC, FeedbackA, FeedbackB, FeedbackC.
# The budget and reputation changes are written as whole numbers.

# 2. WHAT HAPPENS?
# At the start, the player enters a name and chooses Easy or Hard difficulty.
# The program loads the scenarios, shuffles them and selects ten for the game.
# Each day it displays the situation, the three options and the two current gauges.
# The player chooses A, B or C; invalid answers are requested again.
# The program applies the chosen option, caps reputation at 100 and shows feedback.
# The game stops immediately if budget or reputation reaches zero or less.
# After the game, the program finds the best and worst reputation moves.
# Finally, it displays the result and appends one record to results.csv.

# 3. WHAT COMES OUT?
# The player sees the daily situations, choices, feedback and updated gauges.
# At the end, the player sees whether they were fired or survived, their title,
# final score (if they survived), and the best and worst moves.
# results.csv receives one row containing name, budget, reputation, title and date.

# 4. WHAT COULD GO WRONG?
# If the player types something other than A, B or C, the program asks again.
# If the budget or reputation reaches zero or less, the game ends immediately.
# If scenarios_A.csv is missing or cannot be read, the program shows an error
# and stops safely instead of crashing with an unhandled exception.
# If a scenario row has missing columns or non-numeric impacts, that row is skipped.

# FEATURE CHOSEN: D - Difficulty. Easy starts with 15,000 EUR and Hard with
# 6,000 EUR. I chose it because it gives the player a clear choice at the start
# and changes the challenge without changing the daily scenario rules.

import csv
import random
from datetime import date

SCENARIO_FILE = "scenarios_A.csv"
RESULT_FILE = "results.csv"


# Convertind options into required tuple
def load_scenarios(filename):
    required_columns = [
        "ID", "Scenario", "OptionA", "OptionB", "OptionC",
        "BudgetA", "BudgetB", "BudgetC",
        "ReputationA", "ReputationB", "ReputationC",
        "FeedbackA", "FeedbackB", "FeedbackC"
    ]

    scenarios = []

    with open(filename, "r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file, delimiter=",")

        if reader.fieldnames is None:
            raise ValueError("The scenario file has no header row.")

        missing_columns = [column for column in required_columns
                           if column not in reader.fieldnames]
        if missing_columns:
            raise ValueError("Missing CSV columns: " + ", ".join(missing_columns))

        for row_number, row in enumerate(reader, start=2):
            try:
                if not row["Scenario"].strip():
                    continue

                options = {}
                for letter in ("A", "B", "C"):
                    option = (
                        row["Option" + letter].strip(),
                        int(row["Budget" + letter].strip()),
                        int(row["Reputation" + letter].strip()),
                        row["Feedback" + letter].strip()
                    )
                    options[letter] = option

                scenarios.append({
                    "id": row["ID"].strip(),
                    "story": row["Scenario"].strip(),
                    "options": options
                })

            except (KeyError, TypeError, ValueError) as error:
                print("Skipping invalid scenario row", row_number, "-", error)

    return scenarios


# Asking name and difficulty
def get_player_details():
    name = input("Player name: ").strip()
    while not name:
        name = input("Please enter your name: ").strip()

    while True:
        difficulty = input("Choose difficulty (Easy / Hard): ").strip().lower()
        if difficulty == "easy":
            return name, "Easy", 15000
        if difficulty == "hard":
            return name, "Hard", 6000
        print("Please type Easy or Hard.")


# keep asking untill player chooses any valid option
def ask_choice():
    while True:
        choice = input("Your choice (A, B or C): ").strip().upper()
        if choice in ("A", "B", "C"):
            return choice
        print("Invalid choice. Please type A, B or C.")


# Apply one option and return the two updated gauges as a tuple.
def apply_choice(budget, reputation, option):
    option_text, budget_change, reputation_change, feedback = option
    new_budget = budget + budget_change
    new_reputation = min(100, reputation + reputation_change)
    return new_budget, new_reputation


# Convert the final score into the title shown to a surviving player.
def get_title(final_score):
    if final_score < 95:
        return "Eternal Intern"
    elif final_score < 120:
        return "Growth Hacker"
    elif final_score < 140:
        return "CMO Material"
    else:
        return "Viral Legend"


# Append one completed game to results.csv, adding a header if needed.
def save_result(name, budget, reputation, title):
    file_exists_and_has_data = False
    try:
        with open(RESULT_FILE, "r", newline="", encoding="utf-8") as existing_file:
            file_exists_and_has_data = existing_file.read(1) != ""
    except FileNotFoundError:
        pass

    with open(RESULT_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if not file_exists_and_has_data:
            writer.writerow(["name", "budget", "reputation", "title", "date"])
        writer.writerow([name, budget, reputation, title, date.today().isoformat()])


# Run the ten-day game and keep one history tuple for every day played.
def play_game():
    print("\n====================================")
    print("       CROISSANT ROCKET")
    print("        SURVIVE THE QUARTER")
    print("====================================\n")

    name, difficulty, budget = get_player_details()
    reputation = 50

    try:
        scenarios = load_scenarios(SCENARIO_FILE)
    except (OSError, ValueError, csv.Error) as error:
        print("Could not load", SCENARIO_FILE + ":", error)
        return

    if len(scenarios) < 10:
        print("The scenario file must contain at least 10 valid scenarios.")
        return

    random.shuffle(scenarios)
    selected_scenarios = scenarios[:10]
    history = []
    fired_reason = ""

    print("\nWelcome,", name + "!")
    print("Difficulty:", difficulty)
    print("Starting budget:", budget, "EUR")
    print("Starting reputation:", reputation, "/ 100")

    for day_number, scenario in enumerate(selected_scenarios, start=1):
        print("\n---------------- Day", day_number, "----------------")
        print("Budget:", budget, "EUR | Reputation:", reputation, "/100")
        print("\n" + scenario["story"])

        for letter in ("A", "B", "C"):
            option_text, budget_change, reputation_change, feedback = scenario["options"][letter]
            print(letter + ":", option_text)

        choice = ask_choice()
        chosen_option = scenario["options"][choice]
        option_text, budget_change, reputation_change, feedback = chosen_option

        old_reputation = reputation
        budget, reputation = apply_choice(budget, reputation, chosen_option)
        actual_reputation_change = reputation - old_reputation

        # Store the reputation change first so max() and min() find the
        # biggest and smallest reputation moves by comparing tuples.
        history.append((actual_reputation_change, day_number, option_text))

        print("\n" + feedback)
        print("Budget change:", budget_change, "EUR")
        print("Reputation change:", actual_reputation_change)
        print("Current budget:", budget, "EUR")
        print("Current reputation:", reputation, "/100")

        if budget <= 0 and reputation <= 0:
            fired_reason = "budget and reputation reached zero or less"
            break
        elif budget <= 0:
            fired_reason = "budget reached zero or less"
            break
        elif reputation <= 0:
            fired_reason = "reputation reached zero or less"
            break

    # Show the final outcome and calculate a score only if all ten days were survived.
    if fired_reason:
        title = "Fired"
        print("\nGAME OVER! You were fired because your", fired_reason + ".")
        print("Final budget:", budget, "EUR")
        print("Final reputation:", reputation, "/100")
    else:
        final_score = reputation + budget // 200
        title = get_title(final_score)
        print("\n====================================")
        print("       QUARTER SURVIVED!")
        print("====================================")
        print("Budget left:", budget, "EUR")
        print("Reputation:", reputation, "/100")
        print("Final score:", final_score)
        print(name + ", your title:", title)

    # Compare the history tuples to identify the best and worst reputation moves.
    if history:
        best_move = max(history)
        worst_move = min(history)
        print("\nBest move: day", best_move[1], "-", best_move[2],
              "(" + str(best_move[0]) + " reputation)")
        print("Worst move: day", worst_move[1], "-", worst_move[2],
              "(" + str(worst_move[0]) + " reputation)")

    save_result(name, budget, reputation, title)
    print("\nGame saved in", RESULT_FILE)


# Start one game when this file is run.
if __name__ == "__main__":
    play_game()
