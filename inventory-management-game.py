list1 = ["SHOP to enter shop", "EXIT to end program", "INV to view/edit inventory"]

list2 = ["Wood", "Steel", "Bricks", "Clay"]

commandList = "\n".join(list1)

shopItems = " ".join(list2)

userInventory = []

def startGame():
    print("Welcome to the inventory management game. Your inventory is currently empty. List of commands: ")
    print(commandList)

def editInventory():
    print("Your current inventory: ")
    print(userInventory)
    userInput = input("EDIT to edit inventory | BACK to return: ")
    if userInput == "EDIT":
        print(userInventory)
        removeFromInv = input("Select an item to remove from inventory: ")
        try:
            userInventory.remove(removeFromInv)
            print("Item removed")
        except ValueError:
            print("Item not in inventory")
    elif userInput == "BACK":
        print("Returning to main screen")

def takeFromShop():
    print(shopItems)
    userAddItem = input("This is the shop. Enter an item from the shop to put in your inventory: ")
    if userAddItem in shopItems: 
        userInventory.append(userAddItem)
        print("Item added to inventory")
    elif userAddItem not in shopItems:
        print("Item not in shop. Please select another item")

startGame()

while True:
    userInput = input("What would you like to do next? ")
    print(commandList)
    if userInput == "SHOP": 
        takeFromShop()
    elif userInput == "INV":
        editInventory()
    elif userInput == "EXIT":
        print("Exiting Program")
        break
    else: 
        print("invalid input. Please enter a valid command")
