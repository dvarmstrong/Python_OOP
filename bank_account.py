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
        

acct1 = BankAccount(.02, 0)
acct2 = BankAccount(.05, 0)

# acct1.deposit(100).deposit(200).withdrawl(25).withdrawl(5).yield_interest().display_account_info()
# acct2.deposit(500).deposit(100).withdrawl(30).withdrawl(5).withdrawl(15).withdrawl(1000).yield_interest().display_account_info()
acct2.deposit(200).yield_interest()

BankAccount.print_all_accounts()

""" 
Need help understanding why I can't get the yield_interest method to work properly also
need help undestanding the class attribute of the empty list as well as understanding a few
more OOP related topics 
"""

