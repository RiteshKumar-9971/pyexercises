"""Exercise 6.1 — Small functions working together

WHAT THE PROGRAM MUST DO
    Write three small functions, each doing one thing, and a fourth that uses the other
    three to answer one question about your data.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?  (say which function does what, in order)
    3. What comes out?
    4. What question does your fourth function answer, and why does splitting it into
       three make it easier to check?

WHAT THE AI CANNOT KNOW
    Your question and your split. Ask an assistant for "three functions" and it will
    invent three; they will not be the three your question needs. Decide the split first,
    on paper, then ask.

    One function, one job. If you cannot describe what one of yours does in a single
    sentence without using the word "and", it is doing two things.

CHECK IT YOURSELF
    Test each of the three small functions on its own before combining them. Write in a
    comment the input and expected output you used for each. That is three test cases,
    and they are part of the deliverable.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A list of numbers representing expenses
# 2. Process, function by function:
#    - Function 1: Sums all the numbers in the list
#    - Function 2: Calculates the average of the numbers in the list
#    - Function 3: Counts the number of elements in the list
#    - Function 4: Uses the results of the first three functions to provide a summary of the expenses
# 3. Out: The total, average, and count of the expenses
# 4. The question my fourth function answers: What are the total, average, and count of the expenses?

# Your code below

# Our data
expenses = [25, 40, 15, 60, 30]

# Function 1: Calculate total expenses
def get_total(expenses):
    return sum(expenses)


# Function 2: Calculate average expense
def get_average(expenses):
    return sum(expenses) / len(expenses)


# Function 3: Count the expenses
def get_count(expenses):
    return len(expenses)

# Function 4: Use the other three to answer a question
def analyze_expenses(expenses):
    total = get_total(expenses)
    average = get_average(expenses)
    count = get_count(expenses)
    return total, average, count

answer = analyze_expenses(expenses)
print("Total expenses:", answer[0])
print("Average expense:", answer[1])
print("Number of expenses:", answer[2])