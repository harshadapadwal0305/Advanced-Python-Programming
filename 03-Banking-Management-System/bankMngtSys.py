# Parent Class
class BankAccount:

    def __init__(self, account_no, name, balance):
        self.account_no = account_no
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self.balance += amount
        print("Amount deposited successfully.")
        print("Current Balance:", self.balance)

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount
        print("Amount withdrawn successfully.")
        print("Current Balance:", self.balance)

    # Display Account Details
    def display(self):
        print("\nAccount Number :", self.account_no)
        print("Name           :", self.name)
        print("Balance        :", self.balance)


# Child Class - Savings Account
class SavingsAccount(BankAccount):

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")

        if amount > self.balance:
            raise ValueError("Insufficient balance in Savings Account.")

        self.balance -= amount
        print("Amount withdrawn successfully.")
        print("Current Balance:", self.balance)


# Child Class - Current Account
class CurrentAccount(BankAccount):

    def __init__(self, account_no, name, balance, overdraft_limit):
        super().__init__(account_no, name, balance)
        self.overdraft_limit = overdraft_limit

    # Method Overriding
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")

        if amount > self.balance + self.overdraft_limit:
            raise ValueError("Withdrawal exceeds overdraft limit.")

        self.balance -= amount
        print("Amount withdrawn successfully.")
        print("Current Balance:", self.balance)


# Dictionary to store multiple accounts
accounts = {}


# Main Menu
while True:

    print("\n========== BANKING SYSTEM ==========")
    print("1. Create Savings Account")
    print("2. Create Current Account")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. View Account Details")
    print("6. Exit")

    try:
        choice = int(input("Enter your choice: "))

        # Create Savings Account
        if choice == 1:

            account_no = int(input("Enter Account Number: "))

            if account_no in accounts:
                raise ValueError("Account number already exists.")

            name = input("Enter Customer Name: ")
            balance = float(input("Enter Initial Balance: "))

            if balance < 0:
                raise ValueError("Balance cannot be negative.")

            accounts[account_no] = SavingsAccount(
                account_no, name, balance
            )

            print("Savings Account created successfully.")


        # Create Current Account
        elif choice == 2:

            account_no = int(input("Enter Account Number: "))

            if account_no in accounts:
                raise ValueError("Account number already exists.")

            name = input("Enter Customer Name: ")
            balance = float(input("Enter Initial Balance: "))
            overdraft_limit = float(input("Enter Overdraft Limit: "))

            if balance < 0:
                raise ValueError("Balance cannot be negative.")

            if overdraft_limit < 0:
                raise ValueError("Overdraft limit cannot be negative.")

            accounts[account_no] = CurrentAccount(
                account_no,
                name,
                balance,
                overdraft_limit
            )

            print("Current Account created successfully.")


        # Deposit
        elif choice == 3:

            account_no = int(input("Enter Account Number: "))

            if account_no not in accounts:
                raise ValueError("Invalid account number.")

            amount = float(input("Enter Deposit Amount: "))

            accounts[account_no].deposit(amount)


        # Withdraw
        elif choice == 4:

            account_no = int(input("Enter Account Number: "))

            if account_no not in accounts:
                raise ValueError("Invalid account number.")

            amount = float(input("Enter Withdrawal Amount: "))

            accounts[account_no].withdraw(amount)


        # View Account Details
        elif choice == 5:

            account_no = int(input("Enter Account Number: "))

            if account_no not in accounts:
                raise ValueError("Invalid account number.")

            accounts[account_no].display()


        # Exit
        elif choice == 6:

            print("Thank you for using the Banking System.")
            break


        else:
            raise ValueError("Invalid menu choice. Please choose 1 to 6.")


    except ValueError as e:
        print("Error:", e)

    except Exception as e:
        print("Something went wrong:", e)