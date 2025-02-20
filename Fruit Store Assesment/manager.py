import json

class Manager:
    def __init__(self):
        self.file = "fruits.json"
        self.load_fruits()

    def load_fruits(self):
        try:
            with open(self.file, "r") as f:
                self.fruits = json.load(f)
        except FileNotFoundError:
            self.fruits = {}

    def save_fruits(self):
        with open(self.file, "w") as f:
            json.dump(self.fruits, f, indent=4)

    def add_fruit(self):
        name = input("Enter fruit name: ").strip()
        if name in self.fruits:
            print(f"{name} already exists. Use update option.")
            return
        price = float(input("Enter fruit price: "))
        self.fruits[name] = price
        self.save_fruits()
        print(f"{name} added successfully!")

    def update_fruit(self):
        name = input("Enter fruit name to update: ").strip()
        if name in self.fruits:
            price = float(input("Enter new price: "))
            self.fruits[name] = price
            self.save_fruits()
            print(f"{name} updated successfully!")
        else:
            print("Fruit not found!")

    def view_fruits(self):
        if not self.fruits:
            print("No fruits available!")
        else:
            for fruit, price in self.fruits.items():
                print(f"{fruit}: ${price}")

    def menu(self):
        while True:
            print("\nManager Menu")
            print("1. Add Fruit")
            print("2. Update Fruit")
            print("3. View Fruits")
            print("4. Exit")
            choice = input("Enter choice: ")
            if choice == "1":
                self.add_fruit()
            elif choice == "2":
                self.update_fruit()
            elif choice == "3":
                self.view_fruits()
            elif choice == "4":
                break
            else:
                print("Invalid choice!")
