"""Exercise 8.0 — Operators (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Take two values of your choice and display, as a readable table, the result of every
    comparison between them and of the logical combinations of those results.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two values did you pick, and which comparison result surprised you?

WHAT THE AI CANNOT KNOW
    Your two values. Pick a pair where the answer is not obvious: two strings with
    different capitalisation, a number and the same number written as text, or zero and
    an empty string.

CHECK IT YOURSELF
    Predict each result before running. Count how many you got right.

DELIVERABLE
    This file, with your comments and your code.
"""

#1. What goes in?
#   Two strings: "Python" and "python".

#2. What happens to it?
#   The program performs six comparison operations and five
#   logical operations on the comparison results.

#3. What comes out?
#   A readable table showing each expression and its Boolean result.

#4. Which two values did you pick, and which comparison result surprised you?
#   I picked "Python" and "python".
#   The surprising result is that "Python" < "python" is True
#   because Python compares strings using character order,
#   and uppercase letters come before lowercase letters.



# Your code below

# My predictions before running the program:
# ==  False
# !=  True
# <   True
# <=  True
# >   False
# >=  False
#
# Logical predictions:
# == and <       False
# == or <        True
# not ==         True
# != and <       True
# > or >=        False
#
# I will count how many predictions I got right after running.

value1 = "Python"
value2 = "python"

comparisons = {
    "==": value1 == value2,
    "!=": value1 != value2,
    "<": value1 < value2,
    "<=": value1 <= value2,
    ">": value1 > value2,
    ">=": value1 >= value2,
}   

results = {
    "== and <": comparisons["=="] and comparisons["<"],
    "== or <": comparisons["=="] or comparisons["<"],
    "not ==": not comparisons["=="],
    "!= and <": comparisons["!="] and comparisons["<"],
    "> or >=": comparisons[">"] or comparisons[">="],
}

print("Values:", value1, "and", value2)
print("-" * 48)
print(f"{'Expression':<32} {'Result':<10}")
print("-" * 48)

for expression, result in comparisons.items():
    print(f"{expression:<32} {result}")

print("-" * 48)
print("Logical combinations")
print("-" * 48)

for expression, result in results.items():
    print(f"{expression:<32} {result}")

print("-" * 48)