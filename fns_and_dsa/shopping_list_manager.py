# a Python script named shopping_list_manager.py that implements a simple 
# interface for managing a shopping list. This task focuses on using lists
#  to store and manipulate data dynamically.


def display_menu():
    print("Shopping List Manager: ")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("\nItem: ")
            shopping_list.append(item)
            print("Item added successfully.")
            pass
        elif choice == '2':
            item = input("\nRemove: ")
            shopping_list.remove(item)
            print("Item removed successfully.")
            pass
        elif choice == '3':
            print(f"\nList: \n {shopping_list}")
            pass
        elif choice == '4':
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()
