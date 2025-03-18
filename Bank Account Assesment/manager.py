from file_database import FileDatabase

class Manager(FileDatabase):
    def register_banker(self, username, password):
        self.data["bankers"].append({"username": username, "password": password})
        self.save_data()
        print("Banker registered successfully!")

    def view_customers(self):
        print("\nList of Customers:")
        for customer in self.data["customers"]:
            print(f"Username: {customer['username']}, Balance: {customer['balance']}")

    def delete_customer(self, username):
        self.data["customers"] = [c for c in self.data["customers"] if c["username"] != username]
        self.save_data()
        print("Customer deleted successfully!")
