# The Shopping List Maker
# Objective: The aim of this assignment is to create a program that helps users make a shopping list.

# Task 1: Write a function that lets the user add items to a list.

def create_shopping_list():
    while True:
        print("what would you like to do?")
        print("1: Add another item.")
        print("2: View shopping list.")
        print("3: Exit")
        action = input("Enter your choice: ")
        if action == "1": 
            shopping_list.append(input("Enter the item you would like to add: ").capitalize())
            print("That item has been added to the list.")
        elif action == "2":
            print(f"Current shopping list: {shopping_list}")
        elif action == "3":
            print(f"Your final shopping list: \n{shopping_list}")
            break        

shopping_list = []

create_shopping_list()


# Task 2: Include a function to remove items from the list.

def create_shopping_list():
    while True:
        print("what would you like to do?")
        print("1: Add another item.")
        print("2: View shopping list.")
        print("3: Remove an item from your shopping list.")
        print("4: Exit")
        action = input("Enter your choice: ")
        if action == "1": 
            shopping_list.append(input("Enter the item you would like to add: ").capitalize())
            print("That item has been added to the list.")
        elif action == "2":
            print(f"Current shopping list: {shopping_list}")
        elif action == "3":
            remove_item = (input("What product would you like to remove: ").capitalize())
            if remove_item in shopping_list:
                shopping_list.remove(remove_item)
                print(f"{remove_item} has been removed from your shopping list.")
            else:
                print(f"{remove_item} is not currently in your shopping list.")
        elif action == "4":
            print(f"Your final shopping list: \n{shopping_list}")
            break        

shopping_list = []

create_shopping_list()

# Task 3: Add a function that prints out the entire list in a formatted way.

def format_shopping_list():
    item_number = 1
    for item in shopping_list:
        print(f"Item {item_number}: {item}")
        item_number += 1

format_shopping_list()

# Note: The goal of this is to be a program. The recommendation is to use a while loop that will 
# allow the user to continue to add, remove, and print off their shopping list until they decide to "quit", 
# also known as breaking the loop.