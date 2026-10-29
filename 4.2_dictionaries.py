"""Exercise 4.2 — Working with a dictionary

WHAT THE PROGRAM MUST DO
    Describe one real object from your field using a dictionary of at least five fields,
    then read it, change it, remove one field, and display every field with its value.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What object did you describe, which five fields did you choose, and why those?
       A field you would never actually use does not count.

WHAT THE AI CANNOT KNOW
    Your object and your fields. A campaign, a customer, a product, a store, a supplier.
    Choose something you would genuinely have to describe in your job.

CHECK IT YOURSELF
    Ask your program for a field that does not exist. Note what happens in a comment,
    then make it survive that case.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: data for a person (name, age, gender, city, country)
# 2. Process: Store the data in a dictionary and manipulate it
# 3. Out: Display the person's information
# 4. My object, my five fields, and why those:
#    Object: A person
#    Fields: name, age, gender, city, country
#    Why those: These fields are commonly used to describe a person in a real-world scenario.

# Your code below
name = input("Enter your name: ")
age = input("Enter your age: ")

person = {
    "name": name,
    "age": age,
    "gender": input("Enter your gender: "),
    "city": input("Enter your city: "),
    "country": input("Enter your country: ")
}       
print("Person's information:", person)

#change a field
person["occupation"] = input("Enter your occupation: ")
print("Person's information:", person)

#remove a field
city = person.pop("city")

print("Person's information after removing city:", person)
print("City removed:", city)


