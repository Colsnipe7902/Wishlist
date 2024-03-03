wish_list = {
    "Laptop": 1500,
    "Headphones": 200,
    "Books": 100
}

def view_all_items():
    if wish_list:
        for item, price in wish_list.items():
            print(f"{item}: ${price}")
    else:
        print("Wishlist is empty.")

def view_item(item_name):
    if item_name in wish_list:
        print(f"{item_name}: ${wish_list[item_name]}")
    else:
        print("Item not found in wishlist.")

def add_item(item_name, item_price):
    if item_name not in wish_list:
        wish_list[item_name] = item_price
        print(f"{item_name} added to wishlist.")
    else:
        print("Item already exists in wishlist.")

def delete_item(item_name):
    if item_name in wish_list:
        del wish_list[item_name]
        print(f"{item_name} removed from wishlist.")
    else:
        print("Item not found in wishlist.")

def main():
    while True:
        print("\nWishlist Menu:")
        print("1. View all items")
        print("2. View an item")
        print("3. Add an item")
        print("4. Delete an item")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            view_all_items()
        elif choice == '2':
            item_name = input("Enter the name of the item to view: ")
            view_item(item_name)
        elif choice == '3':
            item_name = input("Enter the name of the item to add: ")
            item_price = float(input("Enter the price of the item: "))
            add_item(item_name, item_price)
        elif choice == '4':
            item_name = input("Enter the name of the item to delete: ")
            delete_item(item_name)
        elif choice == '5':
            print("Exiting Wishlist app.")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
