import csv

class Inventory:
    def __init__(self):
        self.inventory = {} 

    def load_inventory(self):
        with open("data/inventory.csv") as cust_file:
            csv_reader = csv.DictReader(cust_file)
            self.inventory = {row["title"]: row for row in csv_reader}

    def get_movie_data(self, title):
        return self.inventory.get(title) 

    def view_titles_and_copies(self):
        if not self.inventory.values():
            print("No inventory data available.")
            return

        print("\nList of current inventory: \n")
        print("Title: Copies available")
        for movie in self.inventory.values():
            title = movie["title"]
            copies = movie["copies_available"]
            print(f"{title}: {copies}")

    def adjust_for_rentals(self, title): 
        for movie in self.inventory:
            if movie["title"] == title:
                movie["copies_available"] -= 1

    def adjust_for_returns(self, title): 
        for movie in self.inventory:
            if movie["title"] == title:
                movie["copies_available"] += 1

    def update_inventory(self):
        with open("data/inventory.csv", "w", newline="") as csv_file:
            fieldnames = ["id", "title", "copies_available"]
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            csv_writer.writeheader()
            csv_writer.writerows(self.inventory.values())

        print("Thank you for using Code Platoon Management System. Have a good day!")







