#display a welcoming message to show the customer they are currently using the vending machine
print("Welcome to the school vending machine!")

#create a variable for getting money from customer 
cashamount = int (input("please enter (cash) to buy items: ")) 

#if the amount is less than 1 (less than the cheapest item), then display an error message and end the program
if cashamount < 1:
    print("Error: Insufficient funds, you don't have enough to purchase an item from the vending machine!")
    exit() 

#display the available items to the customer 
print("\n Available items:")
print("\n ______________________________________") #display a line to seperate the heading and menu and make it more visually appealing 
print("") #display another blank space to create a better seperation

#create lists of items available for the customer to purchase using dictionary
items = {
    "Drinks": { #categorize the items (into drinks, snacks, and meals)
        "1": {"name": "Water", "price": 1}, #every food item should have a unique key (numbers) as well as details
        "2": {"name": "Orange soda", "price": 2}, # e.g. item 2 is orange soda, price is €2
        "3": {"name": "Chocolate milk", "price": 3},
         "4": {"name": "Mango juice", "price": 3} 
    },
    "Snacks": {
        "5": {"name": "Chips", "price": 2},
        "6": {"name": "Cookie", "price": 1},
        "7": {"name": "Chocolate bar", "price": 3}
    },

    "Meals": {
        "8": {"name": "Chicken Sandwich", "price": 4},
        "9": {"name": "Burger", "price": 4},
        "10": {"name": "Hotdog", "price": 3}
    },
}


#use a for loop to go through all the availabe items and display them
for category, products in items.items(): #for category (e.g. drinks) and products (e.g. water) in the menu
    print(f"{category}:")                #display the catagory names
    for key, value in products.items():  # for keys (name, price) in products from menue
        print(f"  {key}. {value['name']} - €{value['price']}") #display the item names and their prices


while True: #use a while loop to repeat code until condition breaks the loop to allow the customer to make multiple purhcases
    selection = input("\nPlease enter the item number you want to purchase: ") # allow the customer input to enter the item number they want to purchase

    # create a loop to go through all items in dictionary to find the selected item based on the customer's input
    selected_item = None  
    for products in items.values():  # for products in the available items
        if selection in products:    # if the selected item number is available in the menu
            selected_item = products[selection] # then get the values of the item number that is selected 
            break #break from the loop

    if not selected_item: # if customer has not selected from the given options of items, then print and error message and ask them to insert the number again 
        print("Invalid selection. Please try again.")
        continue

    #create variables to get and store the item name and it's price 
    item_price = selected_item["price"]
    item_name = selected_item["name"]

#if the cash amount is greater than or same as price of the item (eough to purchase the item) 
#then minus the cash amount inserted by the item price and display a message of item purchased and the amount left to be returned to the customer 
    if cashamount >= item_price:
        cashamount -= item_price
        print(f"You purchased {item_name}. Remaining balance: €{cashamount}.")
    else: # if the amount inserted less than item's price, program displays an error message and gives the item's 
          # actual price and tells the customer the amount that was inserted into the vending machine (which is not enough to purchase the item)
        print(f"Insufficient funds. {item_name} costs €{item_price}, but you only have €{cashamount}.")
        break #break from the loop if condition not met

# create another variable to allow customer to input message to allow purchase another item and give options of yes or no 
    anotherselection = input("Would you like to purchase something else? (yes/no): ").lower() #convert the anser to lower case in case to avoid error
    if anotherselection != "yes": #if the customer's anwer is yes then continue with the cycle, if not then...
        break            # end/break the loop

# once the customer is done with purchasing the items, display a thank you message 
print("Thank you for using the vending machine, please come and use our service again!")
