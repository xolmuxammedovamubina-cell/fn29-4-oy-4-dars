from abc import ABC, abstractmethod


class BankAccount(ABC):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, account_number, owner, balance):
        self._account_number = account_number
        self._owner = owner
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value >= 0:
            self._balance = value
        else:
            print("Balans 0 dan kichik bo'lmasligi kerak")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Balansga pul qo'shildi")
        else:
            print("0 dan katta summa kiriting")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print("Balansdan pul yechildi")
            else:
                print("Balansda yetarli pul yo'q")
        else:
            print("0 dan katta summa kiriting")

    @abstractmethod
    def get_info(self):
        pass

    def __str__(self):
        return f"{self._owner} | Balance: {self.balance}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self._account_number}, '{self._owner}', {self.balance})"

    def __bool__(self):
        return self.balance > 0

    def __eq__(self, other):
        if isinstance(other, BankAccount):
            return self.balance == other.balance
        return False

    def __ne__(self, other):
        return not self == other

    def __gt__(self, other):
        return self.balance > other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __le__(self, other):
        return self.balance <= other.balance


class SavingsAccount(BankAccount):
    def get_info(self):
        return f"Savings Account: {self._owner}, Balance: {self.balance}"


class BusinessAccount(BankAccount):
    def get_info(self):
        return f"Business Account: {self._owner}, Balance: {self.balance}"


account1 = SavingsAccount(1, "Mubina", 2000)
account2 = BusinessAccount(2, "Munisa", 2100)

print(account1)
print(repr(account1))
print(bool(account1))
print(account1 == account2)
print(account1 != account2)
print(account1 > account2)
print(account1 <= account2)

print(account1.get_info())
print(account2.get_info())