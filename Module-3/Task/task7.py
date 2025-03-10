class Withdraw:
    def withdrawl(self, balance):
        amount = int(input("Enter withdrawal amount: "))
        if amount > balance:
            print("Withdrawal failed! Insufficient balance....")
        else:
            balance -= amount
            print(f"Rs. {amount} withdrawn successfully! New balance: Rs. {balance}\n")
        return balance

class BankData:
    def display_data(self, account_number, account_holder_name, account_type, balance):
        print("Account Number:", account_number)
        print("Account Holder Name:", account_holder_name)
        print("Account Type:", account_type)
        print("Current Balance: Rs.", balance)
        print("----------------------------\n")

class Deposit:
    def deposit(self, balance):
        amount = int(input("Enter deposit amount: "))
        if amount >= 2000:
            balance += amount
            print(f"Rs. {amount} deposited successfully! New balance: Rs. {balance}\n")
        else:
            print("Deposit failed! Minimum deposit amount is Rs. 2000.\n")
        return balance

class allbank:
        account_number = input("Enter Account Number: ")
        account_holder_name = input("Enter Account Holder Name: ")

        print("\nSelect Account Type:")
        print("1. Saving")
        print("2. Current")
        account_type_choice = input("Enter your choice (1 or 2): ")

        if account_type_choice == '1':
            account_type = "Saving"
        elif account_type_choice == '2':
            account_type = "Current"
        else:
            print("Invalid choice! Defaulting to Saving account.")
            account_type = "Saving"

        balance = int(input("Enter amount (min. deposit amount is 2000): "))
        if balance < 2000:
            print("Invalid choice! Minimum deposit amount is Rs. 2000. Setting balance to Rs. 2000.")
            balance = 2000

        withdraw_instance = Withdraw()
        deposit_instance = Deposit()
        bankdata_instance = BankData()

        print("\n----- Banking Menu -----")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. View Statement")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            balance = deposit_instance.deposit(balance)
        elif choice == '2':
            balance = withdraw_instance.withdrawl(balance)
        elif choice == '3':
            bankdata_instance.display_data(account_number, account_holder_name, account_type, balance)
        elif choice == '4':
            print("Thank you for using our banking system! Have a great day!\n")
        else:
            print("Invalid choice! Please restart the program and enter a valid option.")
