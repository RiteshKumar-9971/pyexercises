"""Exercise 8.1 — Bitwise operators (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Represent a set of permissions as bits, combine two of them, test whether a third is
    present, then add it and remove one.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What are your permissions about? Not files: invent a set from your own field,
       such as who may view, edit and publish a campaign.

WHAT THE AI CANNOT KNOW
    Your permission set and what each one means in your context.

CHECK IT YOURSELF
    Display the value in binary at each step and read the bits yourself.

DELIVERABLE
    This file, with your comments and your code.
"""

#Exercise 8.0 — Operators

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
