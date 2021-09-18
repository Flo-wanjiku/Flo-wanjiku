import sys


# create the main menu
def mainMenu():
    while True:   # ensures that the main menu pops up again
        print()
        print("""
              ###SHOPPING LIST### 
              Select a number for the action to do:
               1. View the shopping list 
               2. Add item to shopping list 
               3. Remove item from shopping list
               4. Check if item is on shopping list 
               5. How many items on shopping list
               6. Clear shopping list. 
               7. Exit 
               """)

        selection = input("Make your selection: ")   # ask the user to make a selection

        # Determine which action to perform  based on the user's selection
        if selection == "1":
            displayList()
        elif selection == "2":
            addItem()
        elif selection == "3":
            removeItem()
        elif selection == "4":
            checkItem()
        elif selection == "5":
            listLength()
        elif selection == "6":
            clearList()
        elif selection == "7":
            sys.exit()
        else:
            print("You did not make a valid selection.")
    
shopping_list = {
"sugar": 110, 
"bread" : 50,
"butter" : 250,
"mangoes" : 10
}

# Displays all items on the shopping list
def displayList():
    print()
    print("--- SHOPPING LIST ---")
    for x, y in shopping_list.items():
        print(x, y)
     
# Adds in items on the shopping list
def addItem():
    item = input("Enter item : ")
    price = input("Enter  price of item: ")
# Displaying the dictionary 
    if item in shopping_list:
        print(item + " is already on the shopping list.")
    else:
        print(item + " has been added to the shopping list") 
    shopping_list[item] = price
    print(shopping_list)
    
# Removes an item from the shopping list    
def removeItem():
    item = input("Enter the item you wish to remove from the shopping list: ")
    if item not in shopping_list:
    	print(item + " was not on the shopping list and cannot be removed.")
    else:
        del shopping_list[item]
        print(shopping_list)
        
# Checks to see if a particular item is on the shopping list
def checkItem():
    print()
    item = input("What item would you like to check on the shopping list: ")
    if item in shopping_list.keys():
        print("Yes, " + item + " is on the shopping list.")
    else:
        print("No, " + item + " is not on the shopping list.")
    print(shopping_list) 
    
# How many items are on the shopping list    
def listLength():
    print()
    print("There are",len(shopping_list.keys()), "items on the shopping list.")

# Remove everything from the shopping list
def clearList():
    shopping_list.clear()
    print()
    print("The shopping list is empty.")


# Run the function mainMenu which - will run the app
mainMenu()