# A python script that calculates the future savings of a user

income = int(input("Enter your monthly income:"))
expenses = int(input("Enter your total monthly expenses:"))

monthly_savings = income - expenses
annual_savings = int((monthly_savings * 12 + (monthly_savings * 12 * 0.05)))

print("Your monthly savings are ${}.".format(monthly_savings))
print(f"Projected savings after one year, with interest, is: ${annual_savings}.")
