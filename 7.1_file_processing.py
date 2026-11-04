"""Exercise 7.1 — Loading a file, cleaning it, saving the result (homework)

This is the direct rehearsal for the final exam. Session 8 starts with it.

WHAT THE PROGRAM MUST DO
    Load names.txt, clean what is inside, sort it by last name, and write the result to
    a new file. The original file must not be modified.

DO THIS BEFORE ANYTHING ELSE
    Open names.txt and read it with your eyes. Then write, in comments at the top of
    your file, everything that is wrong with it. There are at least four different
    problems. Find them yourself.

    This step is not optional and it is graded. An assistant cannot see your file.

ANSWER THESE, in comments, after the list of problems
    1. What goes in?
    2. What happens to it?  (one line per problem you found, and how you deal with it)
    3. What comes out?
    4. What does "sort by last name" mean when a line contains two words, and how do you
       know which one is the last name?

WHAT THE AI CANNOT KNOW
    The actual content of names.txt. If you paste this brief into an assistant without
    describing the file, it will write a program for a clean file, and that program will
    crash or produce nonsense on the real one.

    Describe the file to it. That description is the exercise.

CHECK IT YOURSELF
    Count the lines in names.txt, then in your output file. The numbers should differ,
    and you should be able to say exactly why. Then check the first and last name of
    your sorted list by hand.

DELIVERABLE
    This file, plus the output file your program produced.
"""

# What is wrong with names.txt (found by reading it, not by guessing):
# - There are two blank lines (lines 3 and 9).
# - Alan Turing and Linus Torvalds have extra spaces at the beginning.
# - Capitalisation is inconsistent: names are lowercase, uppercase or mixed.
# - "GUIDO van rossum" has a three-word name; "van Rossum" is a compound surname.
#    Sorting only by the final word would split the surname incorrectly.

# 1. In:
# The input is names.txt. It contains 10 physical lines: 8 names and 2 blank
# lines. Some names have extra leading spaces and inconsistent capitalisation.

# 2. Process, problem by problem:
# - Read names.txt in read mode so the original file stays unchanged.
# - Strip spaces from each line.
# - Skip empty lines.
# - Standardise capitalisation, keeping "van" lowercase in "Guido van Rossum".
# - Use the second word as the surname in two-word names.
# - Treat "van Rossum" as one compound surname for the three-word entry.
# - Sort by surname alphabetically, ignoring capitalisation.
# - Save the result in a separate file named cleaned_names.txt.

# 3. Out:
# A new file, cleaned_names.txt, containing 8 cleaned names sorted by surname.
# The original names.txt is not changed. The output has 2 fewer lines because
# the 2 blank lines are removed.

# 4. How I decide which word is the last name:
# In two-word entries, the first word is the first name and the second is the
# surname. In "Guido van Rossum", "van Rossum" is the full compound surname,
# so both words are kept together when sorting.


# Your code below

def read_names(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.readlines()


# Remove extra spaces, skip blank lines and make the capitalisation consistent.
def clean_names(lines):
    cleaned = []

    for line in lines:
        name = line.strip()

        # Blank lines do not contain a name, so skip them.
        if name == "":
            continue

        words = name.split()

        # Keep the surname particle "van" lowercase in Guido van Rossum.
        if len(words) == 3 and words[1].lower() == "van":
            cleaned_name = (
                words[0].capitalize()
                + " van "
                + words[2].capitalize()
            )
        else:
            cleaned_name = " ".join(word.capitalize() for word in words)

        cleaned.append(cleaned_name)

    return cleaned


# Get the surname used to alphabetise each name.
def get_last_name(name):
    words = name.split()

    # "van Rossum" is a compound surname in this file.
    if len(words) == 3 and words[1].lower() == "van":
        return (words[1] + " " + words[2]).casefold()

    return words[-1].casefold()


# Sort the names alphabetically using the surname returned above.
def sort_by_last_name(names):
    return sorted(names, key=get_last_name)


# Write the sorted names to a new file, not back into names.txt.
def save_names(names, output_filename):
    with open(output_filename, "w", encoding="utf-8") as file:
        for name in names:
            file.write(name + "\n")


# Run the functions in order and show the line-count check.
def main():
    input_filename = "names.txt"
    output_filename = "cleaned_names.txt"

    original_lines = read_names(input_filename)
    cleaned_names = clean_names(original_lines)
    sorted_names = sort_by_last_name(cleaned_names)
    save_names(sorted_names, output_filename)

    print("Original physical lines:", len(original_lines))
    print("Names in output file:", len(sorted_names))
    print("Blank lines removed:", len(original_lines) - len(sorted_names))
    print("First name after sorting:", sorted_names[0])
    print("Last name after sorting:", sorted_names[-1])
    print("Saved to:", output_filename)


if __name__ == "__main__":
    main()