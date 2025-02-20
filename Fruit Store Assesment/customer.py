# customer.py
import json

class Customer:
    def __init__(self):
        self.file = "fruits.json"
        self.cart = {}
        self.transactions = "transactions.txt"

    def load_fruits(self):
        try:
            with open(self.file, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def buy_fruit(self):
        fruits = self.load_fruits()
        if not fruits:
            print("No fruits available!")
            return
        name = input("Enter fruit name to buy: ").strip()
        if name in fruits:
            qty = int(input("Enter quantity: "))
            self.cart[name] = self.cart.get(name, 0) + qty
            print(f"Added {qty} {name} to cart.")
        else:
            print("Fruit not found!")

    def view_cart(self):
        if not self.cart:
            print("Cart is empty!")
        else:
            for fruit, qty in self.cart.items():
                print(f"{fruit}: {qty}")

    def view_bill(self):
        fruits = self.load_fruits()
        total = 0
        print("\nBill Details:")
        for fruit, qty in self.cart.items():
            if fruit in fruits:
                price = fruits[fruit] * qty
                total += price
                print(f"{fruit} x{qty}: ${price}")
        print(f"Total Bill: ${total}")

        with open(self.transactions, "a") as f:
            f.write(f"Transaction: {self.cart}, Total: ${total}\n")
        
        self.cart.clear()

    def menu(self):
        while True:
            print("\nCustomer Menu")
            print("1. Buy Fruit")
            print("2. View Cart")
            print("3. View Bill")
            print("4. Exit")
            choice = input("Enter choice: ")
            if choice == "1":
                self.buy_fruit()
            elif choice == "2":
                self.view_cart()
            elif choice == "3":
                self.view_bill()
            elif choice == "4":
                break
            else:
                print("Invalid choice!")
