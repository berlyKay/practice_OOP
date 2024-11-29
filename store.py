from inventory import Inventory
from customers import Customers


class Store:
    def __init__(self, inventory, customers):
        self.inventory = inventory
        self.customers = customers

    def rent_video(self):
        self.inventory.view_titles_and_copies()
        print("\nEnter a title.")
        rented_title = input()
        if rented_title not in self.inventory.inventory:
            print("This title is not available for rent.") 
            return
        if int(self.inventory.inventory[rented_title]["copies_available"]) < 1:
            print("No copies of this title are available for rent.")
            return
        print("Enter customer ID:")
        cust_id = input()
        if cust_id not in self.customers.customer_data:
            print("Invalid customer ID.")
            return
        account_type = self.customers.customer_data[cust_id]["account_type"]
        if self.customers.customer_data[cust_id]['current_video_rentals'] == '':
            current_rentals = 0
        else:
            current_rentals = len(self.customers.customer_data[cust_id]['current_video_rentals'].split("/"))
        if (account_type == "px" and current_rentals >= 3) or (account_type == "sx" and current_rentals >= 1):
            print("Customer has reached their maximum rental limit.")
            return
        else:
            print(f"{rented_title} has successfully been rented out.")
            self.inventory.inventory[rented_title]['copies_available'] = str(int(self.inventory.inventory[rented_title]['copies_available']) - 1)
            if self.customers.customer_data[cust_id]["current_video_rentals"] == "":
                self.customers.customer_data[cust_id]["current_video_rentals"] = rented_title
            else:
                self.customers.customer_data[cust_id]["current_video_rentals"] += f'/{rented_title}'


    def return_video(self):
        print("\nEnter a title.")
        rented_title = input()
        if rented_title not in self.inventory.inventory:
            print("Enter a valid title.")
        print("Enter customer ID:")
        cust_id = input()
        print(f"{rented_title} has successfully been returned.")
        self.inventory.inventory[rented_title]['copies_available'] = str(int(self.inventory.inventory[rented_title]['copies_available']) + 1)
