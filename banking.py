import random

class Bank:
    accounts = {"account_no": ["username", "balance"]}

    def generate_account(self):
        """
        generate new 5 digit acount no and prevent duplicates
        """
        self.account_no = random.randint(10000, 99999)
        while self.account_no in self.accounts.keys():
            self.account_no = random.randint(10000, 99999)

class CheckingAccount(Bank):
    def create_account(self, username, deposit):
        """
        create new checking account and provide user account no
        """
        self.generate_account()
        self.accounts[self.account_no] = [username, deposit]
        print("Your new checking account number is", self.account_no)
        self.account_balance()

    def verify_account(self, username, account_no):
        """
        verify that the username and account # match our stored values
        """
        if account_no not in self.accounts.keys():
            print("Authentication failed")
            return False
        elif self.accounts[account_no][0] == username:
            print("Account verified.")
            self.account_no = account_no
            return True
        else:
            print("Authentication failed")
            return False

    def account_balance(self):
        """
        provide user the current account balance
        """
        print("Your account balance is $" + str(self.accounts[self.account_no][1]))

    def withdraw(self, withdraw_amount):
        """
        ensure the withdraw amount won't bring the account negative, if not perform the withdraw
        """
        if self.accounts[self.account_no][1] < withdraw_amount:
            print("Insufficient funds")
        else:
            self.accounts[self.account_no][1] -= withdraw_amount
            print("You have withdrawn $" + str(withdraw_amount))
            self.account_balance()

    def deposit(self, deposit_amount):
        """
        deposit the amount into the checking account
        """
        self.accounts[self.account_no][1] += deposit_amount
        print("You have deposited $" + str(deposit_amount))
        self.account_balance()

class Customer:
    def get_username(self):
        print("Please enter your username: ")
        return input()

    def get_deposit(self):
        print("Please enter your deposit amount: ")
        return int(input())

    def get_withdraw(self):
        print("How much would you like to withdraw?")
        return int(input())

    def get_account_no(self):
        print("Please enter your account number: ")
        return int(input())

customer = Customer()
checking = CheckingAccount()

while True:
    print("Enter 1 if you would like to create a new checking account")
    print("Enter 2 if you would like to access an existing account")
    print("Enter 3 if you would like to exit")
    user_choice = int(input())
    if user_choice == 1:
        username = customer.get_username()
        deposit = customer.get_deposit()
        checking.create_account(username, deposit)
    elif user_choice == 2:
        username = customer.get_username()
        account_no = customer.get_account_no()
        if checking.verify_account(username, account_no):
            while True:
                print("Enter 1 to withdraw")
                print("Enter 2 to deposit")
                print("Enter 3 for account balance")
                print("Enter 4 to go back to the previous menu")
                user_choice2 = int(input())
                if user_choice2 == 1:
                    withdraw_amount = customer.get_withdraw()
                    checking.withdraw(withdraw_amount)
                elif user_choice2 == 2:
                    deposit_amount = customer.get_deposit()
                    checking.deposit(deposit_amount)
                elif user_choice2 == 3:
                    checking.account_balance()
                elif user_choice2 == 4:
                    break
        else:
            pass
    elif user_choice == 3:
        quit()
    else:
        print("Please enter 1, 2 or 3")
