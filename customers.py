import csv

class Customers:
    def __init__(self):
        self.customer_data = {} 

    def load_customer_data(self):
        with open("data/customers.csv") as cust_file:
            csv_reader = csv.DictReader(cust_file)
            self.customer_data = {row["id"]: row for row in csv_reader}

    def get_customer_data(self, cust_id):
        return self.customer_data.get(cust_id)

    def view_customer_list(self): 
        print("\nCurrent customer list:")
        for customer in self.customer_data.values():
            first_name = customer["first_name"]
            last_name = customer["last_name"]
            cust_id = customer["id"]
            print(f'{cust_id}: {customer["first_name"]} {customer["last_name"]}')


    def view_customer_rentals(self):
        print("Enter customer ID: ")
        customer_id = input()
        if customer_id not in self.customer_data:
            print("This customer ID does not exist.")
            return
        cust_data = self.get_customer_data(customer_id)
        # print(cust_data)
        if cust_data['current_video_rentals'] == '':
            print("This person currently has no videos rented.")
        cust_rentals = cust_data['current_video_rentals'].split("/")
        for movie in cust_rentals:
            print(movie)
        return cust_rentals
    
    def get_number_rented(self, customer_id):
        cust_data = self.get_customer_data(customer_id)
        if self.customer_data[customer_id]['current_video_rentals'] == '':
            return []
        cust_rentals = cust_data['current_video_rentals'].split("/")
        return cust_rentals
         
    def add_customer(self):
            print("Enter first name.")
            customer_first_name = input()
            print("Enter last name.")
            customer_last_name = input()
            while True:
                print("Enter account type. (sx or px)")
                customer_account_type = input()

                if customer_account_type.lower() != "sx" and customer_account_type.lower() != "px":
                    print("You must enter either sx or px.")
                    continue
                else:
                    max_id = max(int(key) for key in self.customer_data.keys())
                    new_customer_id = str(max_id + 1)
                    self.customer_data[new_customer_id] = {'id': new_customer_id, 'account_type': customer_account_type.lower(), 'first_name': customer_first_name, 'last_name': customer_last_name, 'current_video_rentals': ''}
                    print(f"{customer_first_name} {customer_last_name} has been successfully added.")
                    return


    def update_customer_data(self):
         with open("data/customers.csv", "w", newline="") as csv_file:
            fieldnames = ["id", "account_type", "first_name",  "last_name", "current_video_rentals"]
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            csv_writer.writeheader()
            csv_writer.writerows(self.customer_data.values())


