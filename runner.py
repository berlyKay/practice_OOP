from menu import Menu
from store import Store
from inventory import Inventory
from customers import Customers

print("Welcome to the Code Platoon Video Management System.")
inventory = Inventory()
inventory.load_inventory()

customers = Customers()
customers.load_customer_data()

store = Store(inventory, customers)

menu = Menu(store)
menu.view_menu()
