import threading

"""
Exercism Python practice problem: Simulate a bank account. 
This is a python program to simulate a actions of a regular bank transaction i.e., Open, Close, Deposit and Withdraw. 
Locks are put in place to avoid concurrent requests possible without corrupting the data. 
"""


class BankAccount:
    # Constructor declaring the variables used through out the program.
    def __init__(self):
        self.balance = 0
        self.accOpen = False
        self.lock = threading.RLock()

    # Get balance is a method used to get the account balance of a given account.
    def get_balance(self):
        self.lock.acquire()
        try:
            if self.accOpen:
                return self.balance
            elif self.accOpen is False:
                raise ValueError("Account is closed")
        finally:
            self.lock.release()

    # Open method is used to open a bank account at the same time, making sure that the account is not already open.
    def open(self):
        self.lock.acquire()
        try:
            if self.accOpen:
                raise ValueError("Account already open!")
            self.accOpen = True
        finally:
            self.lock.release()

    # Deposit method deposits the amount passed to the method as an argument.
    # It also incorporates right checks such that amount is not negative.
    def deposit(self, amount):
        self.lock.acquire()
        try:
            if self.accOpen:
                if amount > 0:
                    self.balance += amount
                else:
                    raise ValueError("Deposit amount cannot be less than zero")
            else:
                raise ValueError("Account is closed")
        finally:
            self.lock.release()

    # Withdraw money from a given account. Amount to withdraw is passed as an argument.
    # It has some checks such that the balance does not become negative and also the amount cannot be negative.
    def withdraw(self, amount):
        self.lock.acquire()
        try:
            if amount > self.balance:
                raise ValueError("Requested amount is greater than the balance.")
            if amount < 0:
                raise ValueError("Amount cannot be negative")
            self.balance -= amount
        finally:
            self.lock.release()

    # Close a bank account and reset the balance to zero.
    def close(self):
        self.lock.acquire()
        try:
            if self.accOpen:
                self.balance = 0
                self.accOpen = False
            else:
                raise ValueError("Account already closed")
        finally:
            self.lock.release()
