from manager import Manager
from customer import Customer

def main():
    manager = Manager()
    customer = Customer()

    while True:
        print("\nWelcome to the Fruit Store!")
        print("1. Manager")
        print("2. Customer")
        print("3. Exit")
        choice = input("Select your role: ")

        if choice == "1":
            manager.menu()
        elif choice == "2":
            customer.menu()
        elif choice == "3":
            print("Thank you for visiting the Fruit Store!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
