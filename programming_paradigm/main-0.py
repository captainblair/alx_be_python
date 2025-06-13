import sys  # Import sys to handle command line arguments
from bank_account import BankAccount  # Import the BankAccount class

def main():
    account = BankAccount(100)  # Create an account with 100 as the starting balance

    if len(sys.argv) < 2:  # Check if at least one command is passed
        print("Usage: python main-0.py <command>:<amount>")  # Instruction
        print("Commands: deposit, withdraw, display")  # Valid commands
        sys.exit(1)  # Exit the script

    command, *params = sys.argv[1].split(':')  # Split command and value
    amount = float(params[0]) if params else None  # Convert amount to float

    if command == "deposit" and amount is not None:  # Deposit case
        account.deposit(amount)  # Call deposit method
        print(f"Deposited: ${amount}")  # Show deposit

    elif command == "withdraw" and amount is not None:  # Withdraw case
        if account.withdraw(amount):  # Attempt withdrawal
            print(f"Withdrew: ${amount}")  # Success message
        else:
            print("Insufficient funds.")  # Failure message

    elif command == "display":  # Display case
        account.display_balance()  # Show current balance

    else:
        print("Invalid command.")  # Handle unknown commands

if __name__ == "__main__":  # Check if script is run directly
    main()  # Call main function
