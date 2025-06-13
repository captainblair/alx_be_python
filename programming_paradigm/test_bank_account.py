import unittest
from bank_account import BankAccount

class TestBankAccount(unittest.TestCase):
    def test_initial_balance(self):
        acc = BankAccount(100)
        self.assertEqual(acc._BankAccount__balance, 100)  # Check initial balance

    def test_deposit(self):
        acc = BankAccount()
        acc.deposit(50)
        self.assertEqual(acc._BankAccount__balance, 50)  # Check deposit works

    def test_withdraw_success(self):
        acc = BankAccount(100)
        result = acc.withdraw(50)
        self.assertTrue(result)
        self.assertEqual(acc._BankAccount__balance, 50)

    def test_withdraw_fail(self):
        acc = BankAccount(30)
        result = acc.withdraw(50)
        self.assertFalse(result)
        self.assertEqual(acc._BankAccount__balance, 30)

if __name__ == '__main__':
    unittest.main()
