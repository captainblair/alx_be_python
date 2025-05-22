#Monthly income 

monthly_income = int(input("Enter your monthly income: "))
total_monthly_expenses = int(input("Enter your total monthly expenses: "))

#Arithmetic operations
monthly_savings = monthly_income - total_monthly_expenses

#Projection
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

#output results
print(f"your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest is: ${int(projected_savings)}.")

