from manager import Manager
from customer import Customer

def main():
    manager = Manager()
    customer = Customer()
    
    while True:
        print("\nWelcome to the Banking System")
        print("1. Manager Section")
        print("2. Customer Section")
        print("3. Exit")
        
        user_choice = input("Enter your choice: ")
        
        if user_choice == "1":
            while True:
                print("\nManager Menu:")
                print("1. Register as Banker")
                print("2. View Customers")
                print("3. Delete Customer")
                print("4. Back to Main Menu")
                
                manager_choice = input("Enter your choice: ")
                
                if manager_choice == "1":
                    username = input("Enter banker username: ")
                    password = input("Enter banker password: ")
                    manager.register_banker(username, password)
                elif manager_choice == "2":
                    manager.view_customers()
                elif manager_choice == "3":
                    username = input("Enter customer username to delete: ")
                    manager.delete_customer(username)
                elif manager_choice == "4":
                    break
                else:
                    print("Invalid choice. Please try again.")
                    
        elif user_choice == "2":
            while True:
                print("\nCustomer Menu:")
                print("1. Register as Customer")
                print("2. View Balance")
                print("3. Deposit Amount")
                print("4. Withdraw Amount")
                print("5. Back to Main Menu")
                
                customer_choice = input("Enter your choice: ")
                
                if customer_choice == "1":
                    username = input("Enter customer username: ")
                    password = input("Enter customer password: ")
                    balance = float(input("Enter initial balance: "))
                    customer.register_customer(username, password, balance)
                elif customer_choice == "2":
                    username = input("Enter customer username: ")
                    customer.view_balance(username)
                elif customer_choice == "3":
                    username = input("Enter customer username: ")
                    amount = float(input("Enter amount to deposit: "))
                    customer.deposit(username, amount)
                elif customer_choice == "4":
                    username = input("Enter customer username: ")
                    amount = float(input("Enter amount to withdraw: "))
                    customer.withdraw(username, amount)
                elif customer_choice == "5":
                    break
                else:
                    print("Invalid choice. Please try again.")
        
        elif user_choice == "3":
            print("Exiting the Banking System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
