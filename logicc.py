"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included with assignment title.
[ ] 2. Ask user for two integers (num1 and num2).
[ ] 3. Perform 6 logical checks: (Both > 0, Both > 100, Either Even, Either < 100, Not Equal, Not Zero).
[ ] 4. Use if/elif/else to categorize num1 (Positive/Negative/Zero).
[ ] 5. Code is clean and uses descriptive variable names.
[ ] 6. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------
"""

num_1 = int(input("Please enter any number: "))
num_2 = int(input("Please enter a second number: "))

if num_1 > 0:
    print("num_1 is a positive number.")
elif num_1 < 0:
    print("num_1 is a negative number.")
else:
    print("num_1 is zero.")

if num_2 > 0:
    print("num_2 is a positive number.")
elif num_2 < 0:
    print("num_2 is a negative number.")
else:
    print("num_2 is zero.")

both_greater_than_zero = num_1 > 0 and num_2 > 0
both_greater_than_hundred = num_1 > 100 and num_2 > 100
either_even = num_1 % 2 == 0 or num_2 % 2 == 0
either_less_than_hundred = num_1 < 100 or num_2 < 100
not_equal = num_1 != num_2
not_zero = num_1 != 0 and num_2 != 0

print(f"\nBoth numbers are greater than 0: {both_greater_than_zero}")
print(f"\nBoth numbers are greater than 100: {both_greater_than_hundred}")
print(f"\nEither number is even: {either_even}")
print(f"\nEither number is less than 100: {either_less_than_hundred}")
print(f"\nThe numbers are not equal: {not_equal}")
print(f"\nNeither number is zero: {not_zero}")
