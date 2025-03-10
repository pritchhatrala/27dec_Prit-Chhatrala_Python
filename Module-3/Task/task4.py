class BankAccount:
    def __init__(self, account_number, account_holder_name, account_type, balance):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.account_type = account_type
        self.balance = balance

    def bankdata(self):
        print("Account Number:", account_number)
        print("Account Holder Name:", account_holder_name)
        print("Account Type:", account_type)
        print("Current Balance: Rs.", balance)
        print("----------------------------\n")
     
    
    def deposit(self):
        amount = int(input("Enter deposit amount: "))
        if amount >= 2000:
            balance += amount
            print(f"Rs. {amount} deposited successfully! New balance: Rs. {balance}\n")
        else:
            print("Deposit failed! Minimum deposit amount is Rs. 2000.\n")
        return balance


    def withdraw(self):
        amount = int(input("Enter withdrawal amount: "))
        if amount > balance:
            print("Withdrawal failed! Insufficient balance.\n")
        else:
            balance -= amount
            print(f"Rs. {amount} withdrawn successfully! New balance: Rs. {balance}\n")
        return balance



account_number = input("Enter Account Number: ")
account_holder_name = input("Enter Account Holder Name: ")

while True:
    print("\nSelect Account Type:")
    print("1. Saving")
    print("2. Current")
    account_type_choice = input("Enter your choice (1 or 2): ")
    if account_type_choice == '1':
        account_type = "Saving"
        break
    elif account_type_choice == '2':
        account_type = "Current"
        break
    else:
        print("Invalid choice! Please enter 1 for Saving or 2 for Current.")



while True:
    balance=int(input("Enter amount (min. deposit amount is 2000):"))
    if balance>=2000:
        break
    else:
        print("Invalid choice! Please enter amount greater than or equal to 2000.")

bank_account = BankAccount(account_number, account_holder_name, account_type, balance)

while True:
    print("\n----- Banking Menu -----")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. View Statement")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        bank_account.deposit()
    elif choice == '2':
        bank_account.withdraw()
    elif choice == '3':
        bank_account.bankdata()
    elif choice == '4':
        print("Thank you for using our banking system! Have a great day!\n")
        break
    else:
        print("Invalid choice! Please enter a valid option (1-4).\n")
