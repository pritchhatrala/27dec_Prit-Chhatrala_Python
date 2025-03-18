from file_database import FileDatabase

class Customer(FileDatabase):
    def register_customer(self, username, password, balance):
        self.data["customers"].append({"username": username, "password": password, "balance": balance})
        self.save_data()
        print("Customer registered successfully!")

    def view_balance(self, username):
        for customer in self.data["customers"]:
            if customer["username"] == username:
                print(f"Current Balance: {customer['balance']}")
                return
        print("User not found!")

    def deposit(self, username, amount):
        for customer in self.data["customers"]:
            if customer["username"] == username:
                customer["balance"] += amount
                self.save_data()
                print("Amount deposited successfully!")
                return
        print("User not found!")

    def withdraw(self, username, amount):
        for customer in self.data["customers"]:
            if customer["username"] == username:
                if customer["balance"] >= amount:
                    customer["balance"] -= amount
                    self.save_data()
                    print("Amount withdrawn successfully!")
                else:
                    print("Insufficient balance!")
                return
        print("User not found!")
