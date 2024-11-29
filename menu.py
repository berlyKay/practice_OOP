from store import Store
from inventory import Inventory
from customers import Customers

class Menu:
    def __init__(self, store):
        self.store = store

    def view_menu(self):
            while True:
                print("\nPress enter for the main menu.")
                x = input()
                print(
                    "== Code Platoon Video - Main menu ==\n"
                    "1. View store video inventory\n"
                    "2. View store customers\n"
                    "3. View customer rented videos\n"
                    "4. Add new customer\n"
                    "5. Rent video\n"
                    "6. Return video\n"
                    "7. Exit"
                )
                print("Please enter an option.")
                menu_item = input()
                if menu_item == "1": 
                    self.store.inventory.view_titles_and_copies()
                elif menu_item == "2": 
                    self.store.customers.view_customer_list()
                elif menu_item == "3": 
                    self.store.customers.view_customer_rentals()
                elif menu_item == "4": 
                    self.store.customers.add_customer()
                elif menu_item == "5":
                    self.store.rent_video()
                elif menu_item == "6":
                    self.store.return_video()
                elif menu_item == "7":
                    self.store.inventory.update_inventory()
                    self.store.customers.update_customer_data()
                    
                    break
                else:
                    print("Invalid option. Please try again.")



