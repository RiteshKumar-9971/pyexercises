"""Exercise 10.0 — Checking the shape of text (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Validate three pieces of information typed by the user, and only save them when all
    three are acceptable.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What are your three fields, and what makes a value acceptable for each? Write the
       rule in plain English before writing any pattern.

WHAT THE AI CANNOT KNOW
    Your three rules. "A valid email" is not a rule, it is a wish. Say what you accept
    and what you reject, and be ready to defend a borderline case.

WHAT TO WATCH
    An assistant will hand you a pattern that looks like line noise. Do not accept it
    until it has explained it to you piece by piece, and you have written that
    explanation in your own words above it.

CHECK IT YOURSELF
    For each field, prepare one value that must pass and two that must fail. Run all
    nine. Any surprise goes in a comment.

DELIVERABLE
    This file, with your comments and your code.
"""

#1. Input: Name, email address and employee ID.
#2. Process: Validate all three fields using regular expressions.
#3. Output: Save and display the information only if all fields are valid.

#4. Validation rules:
#   Name: Only letters and spaces, at least 2 characters.
#   Email: Must contain text before and after @, and a dot in the domain.
#   Employee ID: Must contain exactly 5 digits.

# Your code below

import re

name_pattern = r"^[A-Za-z ]{2,}$"
email_pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
password_pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$!]).{8,}$"

name = input("Enter your name: ").strip()
email = input("Enter your email: ").strip()
password = input("Create a password: ")

if (re.fullmatch(name_pattern, name)
    and re.fullmatch(email_pattern, email)
    and re.fullmatch(password_pattern, password)):

    print("All information is valid!")
else:
    print("Invalid information.")

    if not re.fullmatch(name_pattern, name):
        print("Invalid name.")

    if not re.fullmatch(email_pattern, email):
        print("Invalid email.")

    if not re.fullmatch(password_pattern, password):
        print("Password must have 8 characters, uppercase, lowercase, a number and a special character.")