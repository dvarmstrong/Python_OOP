#Practicing with Object Oriented Programming

class BankAccount:
    accounts = []

    def __init__(self,int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)


    # Instance Method for deposit 
    def deposit (self,amount):
        self.balance += amount 
        return self 

    #  Instance Method for withdrawl 

    def withdrawl (self, amount):
        if (self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Insufficient Funds Charging a 5 dollar fee")
            self.balance -= 5
        return self
        

    # Instance Method for displaying the account balance

    def display_account_info(self):
        print(f"The balance: {self.balance}")
        return self
        

    # Instance Method for yeilding Intrest 

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.int_rate * self.balance )
        return self

    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

class User:

    def __init__(self, name):     # Instance attributes 
        self.name = name
        self.account = {
            "checking" : BankAccount(.02, 0),
            "savings" : BankAccount(.05, 0)
        }

# So the User class associates the parent BankAccount's banking methods ?????  

    def display_user_balance(self):
        print(f"User: {self.name}, Checking Balance: {self.account['checking'].balance}")
        print(f"User: {self.name}, Savings Balance: {self.account['savings'].display_account_info()}")
        return self

    def make_deposit(self,amount, acct):
        self.account[acct].deposit(amount)


    def transfer(self, other_user, amount):
        self.withdrawl(amount)
        other_user.make_deposit(amount)
        self.display_user_balance()
        return self

# Could not add or access the savings account??????
        
# sammy = User("Sammy").account['checking'].deposit(100).account['savings'].deposit(100)
sammy = User("Sammy")
sammy.make_deposit(100, "checking")
sammy.display_user_balance()

# print(sammy.accounts)


# print(help(User))


