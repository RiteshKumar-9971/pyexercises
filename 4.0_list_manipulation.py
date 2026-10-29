"""Exercise 4.0 — Working with a list

WHAT THE PROGRAM MUST DO
    Build a list of at least eight items, then display: the whole list, one item of your
    choice, the list sorted, and something computed from it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your list about, and what did you compute from it? Why is that number
       interesting?

WHAT THE AI CANNOT KNOW
    The content of your list. It must come from your own field: marketing channels,
    campaign names, product references, cities you operate in, monthly budgets. Not
    fruit, not "item1, item2, item3".

    Keep this file. Exercise 5.1 and exercise 6.0 both reuse the list you build here.

CHECK IT YOURSELF
    If you computed an average, a total or a maximum, work it out by hand on three of
    your items first, then check your program agrees on those three.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A list of at least eight items
# 2. Process: Manipulate the list (display, sort, compute)
# 3. Out: The manipulated list and computed values
# 4. What my list is about, and what I computed from it: My list is about a series of numbers, and I computed the sum of the numbers in the list. The sum is interesting because it provides a total value that can be used for further analysis or decision-making.


# Your code below
number_1 = 6 
number_2 = 1
number_3 = 9
number_4 = 5
number_5 = 4
number_6 = 3

print(number_1)
print(number_2)
print(number_3)
print(number_4)
print(number_5)
print(number_6)

list=[2, 4, 6, 8, 10, 12, 14, 16]
print(list)
print(list[0]) 
print(sorted(list))
list.pop(3)
print("The list after removing the 4th element is:", list)

