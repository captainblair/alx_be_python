# Monthly income
monthly_income = int(input("Enter your monthly income: "))
total_monthly_expenses = int(input("Enter your total monthly expenses: "))

# Arithmetic operations
monthly_savings = monthly_income - total_monthly_expenses
annual_savings = monthly_savings * 12
interest = annual_savings * 0.05
projected_savings = annual_savings + interest

# Output results
print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest is: ${int(projected_savings)}.")
