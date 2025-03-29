class MenuItem:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return f"{self.name} -{self.price:.2f}"

class Order:
    def __init__(self):
        self.items = []
        self.discount = 10

    def add_item(self, menu_item):
        self.items.append(menu_item)
    
    def calculate_total(self):
        return sum(item.price for item in self.items)

    def apply_discount(self, percentage):
        return self.calculate_total() * (1- self.discount/100)

    def print_receipt(self):
        print("\n----Receipt----")
        for item in self.items:
            print(item)

        subtotal = self.calculate_total()
        discount_amount = subtotal * (self.discount / 100)
        total_after_discount = subtotal - discount_amount
        print(f"Subtotal: ${subtotal:.2f}")
        print(f"Discount amount ({self.discount}%) - ${discount_amount:.2f}")
        print(f"Total after Discount: ${total_after_discount:.2f}")

class Restaurant:
    def __init__(self):
        self.menu = []
        self.order = []

    def add_menu_item(self, name, price,category):
        self.menu.append(MenuItem(name, price, category))

    def show_menu(self):
        print("\n--Menu---")
        for item in self.menu:
            print(item)

    def take_order(self):
        order = Order()
        while True:
            self.show_menu()
            choice = input("Enter menu item name to order (or 'done' to finish);")
            if choice.lower()== "done":
                break
            found = next((item for item in self.menu if item.name.lower()== choice.lower()),None)
            if found:
                order.add_item(found)
                print(f"Added {found.name}to order.")
            else:
                print("No item found!")

            # try:
            #     discount = float(input("Enter discount percentage (0 for none): "))
            #     if discount < 0:
            #         print("Invalid discount! Setting discount to 0%.")
            #         discount = 0
            # except ValueError:
            #     print("Invalid input! Setting discount to 0%.")
            #     discount = 0
        self.order.append(order)
        order.print_receipt()
    
    def run(self):
        print("Welcome to the Restaurant!")
        while True:
            action = input("Enter 'order' to take an order, 'exit'to quit:")
            if action.lower()== "order":
                self.take_order()
            elif action.lower() =="exit":
                print("Thankyou for Visiting.")
                break
            else:
                print("Invalid choice , Try again.")

restaurant = Restaurant()
restaurant.add_menu_item("Pizza",13.55,"Main Product")
restaurant.add_menu_item("Cake", 16.33, "Main Product")
restaurant.run()