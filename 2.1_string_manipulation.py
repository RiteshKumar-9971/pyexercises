"""Exercise 2.1 — Transforming text (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a sentence, then display four different transformations of it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four transformations did you choose, and in what situation would each of
       them be useful? One line each.

WHAT THE AI CANNOT KNOW
    Your four transformations. Pick them yourself. Open ../examples/strings/string_methods.py
    to see what is available, then choose, then justify.

    A transformation that produces the same thing as another one does not count as two.

CHECK IT YOURSELF
    Run it with a sentence that has spaces at both ends and a capital in the middle.
    For each of your four results, say in a comment whether it is what you expected.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A sentence provided by the user.
# 2. Process: Apply four different string transformations.
# 3. Out: The transformed sentences.
# 4. My four transformations, and when each is useful:

# Transformation 1: Convert to uppercase
# Useful for displaying text in a more prominent way.

# Transformation 2: Convert to lowercase
# Useful for case-insensitive comparisons.

# Transformation 3: Capitalize the first letter of the sentence
# Useful for formatting titles or headings.

# Transformation 4: Strip leading and trailing spaces
# Useful for cleaning up user input.


# Your code below
sentence = input("Enter a sentence: ")

# Transformation 1: Convert to uppercase
uppercase_sentence = sentence.upper()
print("Uppercase:", uppercase_sentence)

# Transformation 2: Convert to lowercase
lowercase_sentence = sentence.lower()
print("Lowercase:", lowercase_sentence)

# Transformation 3: Capitalize the first letter of the sentence
capitalized_sentence = sentence.capitalize()
print("Capitalized:", capitalized_sentence)

# Transformation 4: Strip leading and trailing spaces
stripped_sentence = sentence.strip()
print("Stripped:", stripped_sentence)

