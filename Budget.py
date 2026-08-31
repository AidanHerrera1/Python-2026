"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Ask user for Monthly Income (float).
[ ] 3. Ask user for 5 DIFFERENT expense amounts (float).
[ ] 4. Calculate Total Expenses and Remaining Balance.
[ ] 5. Calculate Percentage of Income Spent.
[ ] 6. Output formatted to 2 decimal places (:,.2f or :.2%).
-----------------------------------------------------------------------
"""
gross_income = float(input("what is your monthly income? "))
housing = float(input("what do you spend on housing? "))
Food = float(input("what do you spend on food? "))
Gas = float(input("what do you spend on gas? "))
Phone = float(input("what do you spend on your phone? "))
Entertainment = float(input("what do you spend on entertainment? "))

net_income = gross_income * .8

total_expenses = housing + Food + Gas + Phone + Entertainment
remaining_balance = net_income - total_expenses


print(f"Gross Pay:      ${gross_income:,.2f}")
print(f"Net Pay:        ${net_income:,.2f}")
print(f"Total Expenses: ${total_expenses:,.2f}")
print(f"Remaining Balance: ${remaining_balance:,.2f}")
print(f"Percentage of Income Spent: {total_expenses/gross_income:.2%}")