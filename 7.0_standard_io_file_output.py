"""Exercise 7.0 — Collecting data and saving it

WHAT THE PROGRAM MUST DO
    Ask the user for the information needed to record one entry, then save it to a CSV
    file. Running the program twice must produce two entries, not overwrite the first.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?  (name your file, and list your columns)
    4. Which columns did you choose, and what would you actually do with this file once
       it has two hundred rows in it?

WHAT THE AI CANNOT KNOW
    Your columns. They must be the ones you would really need to collect for a purpose
    you can state. See 7.0_student_data.csv for the shape of a header line, not for
    the columns to use.

    Two behaviours are yours to decide, and an assistant will guess them wrong:
    what happens the very first time, when the file does not exist yet and needs its
    header line, and what happens when a value the user typed is not acceptable.

CHECK IT YOURSELF
    Run your program three times with different values. Then open the file and count
    the lines. You should have three entries and exactly one header line. If you have
    three header lines, or one entry, your program is wrong.

DELIVERABLE
    This file, plus the CSV your program produced.
"""

# 1. In:ask the user for their first name, last name, birth year, and student number
# 2. Process:save the information to a CSV file, appending it to the file if it already exists
# 3. Out, file name and columns: 7.0_student_data.csv with columns "First Name", "Last Name", "Birth Year", "Student Number"
# 4. Why these columns, and what this file is for: These columns capture essential student information for record-keeping and analysis purposes.


# Your code below

print("Please enter the following information to record an entry:")
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
birth_year = input("Enter your birth (DD/MM/YYYY): ")
student_number = input("Enter your student number: ")

with open("student_data.csv", "a", newline="") as file:
    file.write("First Name,Last Name,Birth Year,Student Number\n")
    file.write(first_name + "," + last_name + "," + birth_year + "," + student_number + "\n")

print("Data saved to student_data.csv")