"""Exercise 4.1 — Reordering without losing the original (homework)

WHAT THE PROGRAM MUST DO
    Starting from the list you built in exercise 4.0, display it in four different
    orders, and prove at the end that the original list has not been damaged.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four orders did you choose, and in which of them is your original list
       modified rather than copied?

WHAT THE AI CANNOT KNOW
    That your original must survive. Some ways of reordering a list change it in place,
    others return a new one. Find out which is which, and say so in your comments.
    That distinction is the entire exercise.

CHECK IT YOURSELF
    The last line of your program must display the original list. Compare it, item by
    item, with what you wrote in 4.0. If it has moved, your program is wrong even
    though it ran.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A list of at least eight items
# 2. Process: Reorder the list in four different ways (original order, reversed order, sorted order, and shuffled order) without modifying the original list.
# 3. Out: The reordered lists in four different ways, and the original list at the end to prove it has not been modified.
# 4. My four orders, and which ones modify the original: 
#    - Original order: Does not modify the original list.
#    - Reversed order: Does not modify the original list.
#    - Sorted order: Does not modify the original list.
#    - Shuffled order: Does not modify the original list.


# Your code below
list = [2, 4, 6, 8, 10, 12, 14, 16]
# Display the original list
print("Original list:", list)

# Display the list in reversed order
reversed_list = list[::-1]
print("Reversed list:", reversed_list)

# Display the list in sorted order
sorted_list = sorted(list)
print("Sorted list:", sorted_list)

# Display the list in shuffled order
import random
shuffled_list = list[:]
random.shuffle(shuffled_list)
print("Shuffled list:", shuffled_list)

# Display the original list to prove it has not been modified
print("Original list (unchanged):", list)
