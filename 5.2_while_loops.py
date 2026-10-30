"""Exercise 5.2 — Repeating until something changes

WHAT THE PROGRAM MUST DO
    Keep asking the user something until a condition you define is met, then display a
    summary of what happened during the loop.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your stop condition, what is your maximum number of attempts, and what
       does your summary contain?

WHAT THE AI CANNOT KNOW
    Your stop condition and your safety limit. An assistant asked for a while loop will
    write one that can run for ever if the user never gives the expected answer. Decide
    how many attempts you allow, and what your program does when that limit is reached.

    Accepting "Yes", "yes" and " yes " as the same answer is your decision too. Make it
    and write it down.

CHECK IT YOURSELF
    Run it and never give the expected answer. If your program is still running after
    your stated maximum, it is wrong. Then run it and answer with capitals and extra
    spaces.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: User input asking if they want to continue or not.
# 2. Process: Check if the input matches the expected answer.
# 3. Out: A message indicating whether the user wants to continue or not.
# 4. My stop condition, my attempt limit, my summary:
i = 20
while i < 10:
    print("This is attempt number:", i + 1)
    i = i + 1

# Your code below
while True:
   user_input = input("Do you want to continue? (yes/no): ").strip().lower()
    
   if user_input == "yes":
        print("You chose to continue.")
        break
   elif user_input == "no":
        print("You chose to stop.")
        break
   else:
        print("Invalid input. Please enter 'yes' or 'no'.")