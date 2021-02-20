#Create an intro message for the user :) Come up with a good name

print ("\n ------------------Map & Cheese------------------")
print("Welcome to Map & Cheese! Been around since '21")
print("visit our website -> www.mapandcheese.com")
print("Our business hours are at the bottom of our page :)")
print("--------------------------------------------------\n")

# Ask user for first and last name and age

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your age: "))
print(f"Full Name: {first_name} {last_name}")
correct_name = input("Is your name entered correctly?")

if correct_name != "yes":
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    print(f"Updated Full Name: {first_name} {last_name}")

# Ask user for phone number
phone_number = input("Enter your phone number: ")
print(f"You entered {phone_number} for your number.")

# Ask user if they want takeout/delivery
