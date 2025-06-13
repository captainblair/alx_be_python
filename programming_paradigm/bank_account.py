class BankAccount: #Defining a class to represent bank account 

    def __init__(self, initial_balance=0):
        self.__account_balance = initial_balance #Encapsulated balance
        
    def deposit(self,amount):
        self.__account_balance += amount
    
    def withdraw(self,amount):
        if amount <= self.__account_balance:
            self.__account_balance -= amount
            return True #Successful withdrawal 
        else:
            return False #Not enough funds 
        
    def display_balance(self): # Method to show the current balance 
        print(f"Current balance: ${self.__account_balance}") #Print balance
        


