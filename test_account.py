import pytest
from account import *

class Test:
    def setup_method(self):
        self.account = Account('Frank')

    def teardown_method(self):
        del self.account


    def test_init(self):
        assert self.account.get_name() == "Frank"
        assert self.account.get_balance() == 0


    def test_deposit(self):
        assert self.account.deposit(100) == True
        assert self.account.get_balance() == 100


    def test_negative_deposit(self):
        assert self.account.deposit(-50) == False
        assert self.account.get_balance() == 0


    def test_withdraw(self):
        self.account.deposit(200)
        assert self.account.withdraw(150) == True
        assert self.account.get_balance() == 50


    def test_incorrect_withdraw(self):
        self.account.deposit(50)
        assert self.account.withdraw(100) == False
        assert self.account.get_balance() == 50

