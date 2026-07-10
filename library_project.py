from library import create_demo_library
from library_item import LibraryItem


def print_items(items: list[LibraryItem]) -> None:
    if not items:
        print("No items found.")
        return
    for item in items:
        status = "Available" if item.available else "Borrowed"
        print(f"{item.item_id}: {item.get_description()} [{status}]")


def run_library_app() -> None:
    library = create_demo_library()
    print("Welcome to the Student Library App")
    print("This project demonstrates OOP with classes, encapsulation, inheritance, abstraction, and polymorphism.")

    while True:
        print("\nChoose an option:")
        print("1. Show available items")
        print("2. Search by title")
        print("3. Borrow an item")
        print("4. Return an item")
        print("5. Exit")

        choice = input("Enter choice (1-5): ")
        if choice == "1":
            print_items(library.list_available_items())
        elif choice == "2":
            term = input("Enter title search term: ")
            print_items(library.find_item_by_title(term))
        elif choice == "3":
            try:
                item_id = int(input("Enter item ID to borrow: "))
            except ValueError:
                print("Please enter a valid number.")
                continue
            if library.borrow_item(item_id):
                print("Item borrowed successfully.")
            else:
                print("Could not borrow item. It may already be borrowed or the ID is invalid.")
        elif choice == "4":
            try:
                item_id = int(input("Enter item ID to return: "))
            except ValueError:
                print("Please enter a valid number.")
                continue
            if library.return_item(item_id):
                print("Item returned successfully.")
            else:
                print("Could not return item. It may already be available or the ID is invalid.")
        elif choice == "5":
            print("Thank you for using the Student Library App. Goodbye!")
            break
        else:
            print("Invalid choice. Please use 1-5.")


if __name__ == "__main__":
    run_library_app()
