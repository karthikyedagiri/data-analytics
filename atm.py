'''
class ATM:
    def __init__(self):
        self.name = "Karthi"
        self.mobile = "9030924118"
        self.pin = "2817"
        self.balance = 200000
        self.transaction_history = []

    def check_balance(self):
        print("\nAvailable Balance: ", self.balance)

    def deposit(self):
        amount = int(input("Enter Deposit Amount: "))
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited {amount}")
            print("Amount Deposited Successfully")
            print("Updated Balance: ", self.balance)
        else:
            print("Invalid Amount")

    def withdraw(self):
        amount = int(input("Enter Withdraw Amount: "))
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawn {amount}")
            print("Please Collect Your Cash")
            print("Remaining Balance: ", self.balance)
        else:
            print("Insufficient Balance or Invalid Amount")

    def mini_statement(self):
        print("\n========== MINI STATEMENT ==========")

        if len(self.transaction_history) == 0:
            print("No Transactions Available")
        else:
            for transaction in self.transaction_history:
                print(transaction)

        print("Current Balance: ", self.balance)

    def change_pin(self):
        old_pin = input("Enter Old PIN: ")

        if old_pin == self.pin:
            new_pin = input("Enter New 4-Digit PIN: ")

            if len(new_pin) == 4 and new_pin.isdigit():
                confirm_pin = input("Confirm New PIN: ")

                if new_pin == confirm_pin:
                    self.pin = new_pin
                    print("PIN Changed Successfully")
                else:
                    print("PIN Confirmation Failed")
            else:
                print("PIN Must Contain Exactly 4 Digits")
        else:
            print("Wrong Old PIN")

    def forgot_pin(self):
        mobile = input("Enter Registered Mobile Number: ")

        if mobile == self.mobile:
            new_pin = input("Enter New 4-Digit PIN: ")

            if len(new_pin) == 4 and new_pin.isdigit():
                self.pin = new_pin
                print("PIN Reset Successfully")
            else:
                print("PIN Must Be 4 Digits")
        else:
            print("Mobile Number Not Matched")
    def menu(self):
        while True:
            choice = int(input(
                "\n========== ATM MENU =========="
                "\n1. Check Balance"
                "\n2. Deposit"
                "\n3. Withdraw"
                "\n4. Mini Statement"
                "\n5. Change PIN"
                "\n6. Forgot PIN"
                "\n7. Exit"
                "\n\nEnter Your Choice: "))
            if choice == 1:
                self.check_balance()

            elif choice == 2:
                self.deposit()

            elif choice == 3:
                self.withdraw()

            elif choice == 4:
                self.mini_statement()

            elif choice == 5:
                self.change_pin()

            elif choice == 6:
                self.forgot_pin()

            elif choice == 7:
                print("Thank You For Using ATM")
                break

            else:
                print("Invalid Choice")

    def login(self):
        print("========== WELCOME TO ATM ==========")
        print("Insert Your ATM Card")

        attempts = 3

        while attempts > 0:

            user_pin = input("Enter ATM PIN: ")

            if len(user_pin) == 4 and user_pin.isdigit():

                if user_pin == self.pin:
                    print("\nLogin Successful")
                    self.menu()
                    break

                else:
                    attempts -= 1

                    if attempts > 0:
                        print(f"Invalid PIN. You Have {attempts} Attempts Left")
                    else:
                        print("Card Blocked")

            else:
                print("PIN Must Contain Exactly 4 Digits")



atm = ATM()


atm.login()
'''
import time

class Account:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited ₹{amount}")
            print(f" Successfully deposited ₹{amount}")
        else:
            print(" Invalid deposit amount")

    def withdraw(self, amount):
        if amount <= 0:
            print(" Invalid withdrawal amount")
        elif amount > self.balance:
            print(" Insufficient funds")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdrew ₹{amount}")
            print(f" Successfully withdrew ₹{amount}")

    def transfer(self, target_account, amount):
        if amount <= 0:
            print(" Invalid transfer amount")
        elif amount > self.balance:
            print(" Insufficient funds")
        else:
            self.balance -= amount
            target_account.balance += amount
            self.transactions.append(f"Transferred ₹{amount} to {target_account.account_number}")
            target_account.transactions.append(f"Received ₹{amount} from {self.account_number}")
            print(f" Successfully transferred ₹{amount} to {target_account.account_number}")

    def check_balance(self):
        print(f" Current Balance: ₹{self.balance}")

    def show_transactions(self):
        print("\n Transaction History:")
        if not self.transactions:
            print("No transactions yet.")
        else:
            for t in self.transactions:
                print(f"- {t}")


class ATM:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, pin, balance=0):
        if account_number in self.accounts:
            print(" Account already exists")
        else:
            self.accounts[account_number] = Account(account_number, pin, balance)
            print(f" Account {account_number} created successfully with balance ₹{balance}")

    def authenticate(self, account_number, pin):
        account = self.accounts.get(account_number)
        if account and account.pin == pin:
            print(" Authentication successful")
            return account
        else:
            print(" Authentication failed")
            return None



atm = ATM()
atm.create_account("12345", "2817", 5000)


print("\n--- Welcome to Advanced ATM ---")
acc_num = input("Enter account number: ")
pin = input("Enter PIN: ")

account = atm.authenticate(acc_num, pin)

if account:
    while True:
        print("\nChoose an option:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Balance Inquiry")
        print("4. Transfer")
        print("5. Transaction History")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            amt = float(input("Enter deposit amount: "))
            account.deposit(amt)

        elif choice == "2":
            amt = float(input("Enter withdrawal amount: "))
            account.withdraw(amt)

        elif choice == "3":
            account.check_balance()

        elif choice == "4":
            target_acc = input("Enter target account number: ")
            amt = float(input("Enter transfer amount: "))
            target = atm.accounts.get(target_acc)
            if target:
                account.transfer(target, amt)
            else:
                print(" Target account not found")

        elif choice == "5":
            account.show_transactions()

        elif choice == "6":
            print(" Thank you for using Advanced ATM. Goodbye!")
            break

        else:
            print(" Invalid choice, try again.")

        time.sleep(1)













































