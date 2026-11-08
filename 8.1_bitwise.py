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

#1. Input: Three permissions represented by numbers.
#2. Process: Combine, check, add and remove permissions using bitwise operators.
#3. Output: Permission values in binary.
#4. Context: Digital marketing campaign permissions.
#   1 = View, 2 = Edit, 4 = Publish.

# Your code below

VIEW = 1
EDIT = 2
PUBLISH = 4

# Combine permissions
permissions = VIEW | EDIT
print("Initial:", format(permissions, "03b"))

# Check publish permission
print("Can publish:", (permissions & PUBLISH) != 0)

# Add publish permission
permissions = permissions | PUBLISH
print("After adding publish:", format(permissions, "03b"))

# Remove edit permission
permissions = permissions & ~EDIT
print("After removing edit:", format(permissions, "03b"))