class BankAccount:  # Class for bank account operations
    def __init__(self, initial_balance=0):  # Constructor with optional initial balance
        self.__balance = initial_balance  # Encapsulated balance attribute

    def deposit(self, amount):  # Method to add money
        self.__balance += amount  # Add amount to balance

    def withdraw(self, amount):  # Method to remove money
        if amount <= self.__balance:  # Check if balance is enough
            self.__balance -= amount  # Subtract amount
            return True  # Success
        else:
            return False  # Not enough funds

    def display_balance(self):  # Method to show balance
        print(f"Current Balance: ${self.__balance}")  # Display balance with exact wording
