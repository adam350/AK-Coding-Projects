class MenuItem:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

class Menu:
    def __init__(self):
        self.menu_items = []
    
    def add_items(self, menu_item):
        self.menu_items.append(menu_item)

    def remove_item(self, menu_item):
        self.menu_items.remove(menu_item)

    def display_menu(self):
        for menu_item in self.menu_items:
            print(f"{menu_item.name}: {menu_item.description} - {menu_item.price}")
    
class Table:
    def __init__(self, table_number, number_of_guests):
        self.table_number = table_number
        self.number_of_guests = number_of_guests
        self.order = []

    def add_to_order(self, menu_item):
        self.order.append(menu_item)

    def calculate_bill(self):
        total = 0
        for item in self.order:
            total += item.price
        return total

class Restaurant:
    def __init__(self):
        self.tables = []

    def add_table(self, table):
        self.tables.append(table)

    def remove_table(self, table_number):
        for table in self.tables:
            if table.table_number == table_number:
                self.tables.remove(table)
                return True
        return False
    
    def take_order(self, table_number, menu_item):
        for table in self.tables:
            if table.table_number == table_number:
                table.add_to_order(menu_item)
                return True
        return False
    
    def calculate_bill(self, table_number):
        for table in self.tables:
            if table.table_number == table_number:
                bill = table.calculate_bill()
                print(f"Table {table.table_number} - total bill: {bill}")
                return True
        return False
    
    def display_tables(self):
        for table in self.tables:
            print(f"Table {table.table_number} - number of guests: {table.number_of_guests}")
            print("Order: ")
            for item in table.order:
                print(f"{item.name} - {item.description} - {item.price}")
            print("")

restaurant = Restaurant()
menu = Menu()

menu.add_items(MenuItem("Spaghetti Carbonara", "Spaghetti with bacon, eggs, and Parmesan cheese", 12.99))
menu.add_items(MenuItem("Margherita Pizza", "Tomato sauce, fresh mozzarella, and basil", 10.99))
menu.add_items(MenuItem("Grilled Salmon", "Grilled salmon with roasted vegetables", 15.99))

while True:
    action = input("Please choose an action (add table, remove table, take order, calculate bill, display tables, or exit): ")

    if action == 'exit':
        break
    elif action == 'add table':
        table_number = int(input("Please enter the table number: "))
        number_of_guests = int(input("Please enter the number of guests: "))
        table = Table(table_number, number_of_guests)
        restaurant.add_table(table)
    elif action == 'remove table':
        table_number = int(input("Please enter the table number: "))
        if restaurant.remove_table(table_number):
            print(f"Table {table_number} removed")
        else:
            print("Error. Table not found.")
    elif action == 'take order':
        table_number = int(input("Please enter the table number: "))
        menu.display_menu()
        item_name = input("Please enter the name of the menu item: ")
        for item in menu.menu_items:
            if item.name == item_name:
                if restaurant.take_order(table_number, item):
                    print(f"Order {item.name} added to table {table_number}")
                else:
                    print("Error. Table not found.")
                break
        else:
            print("Menu item not found.")
    elif action == 'calculate bill':
        table_number = int(input("Please enter the table number: "))
        if not restaurant.calculate_bill(table_number):
            print("Table not found.")
    elif action == 'display tables':
        restaurant.display_tables()
    else:
        print("Error. Invalid action.")