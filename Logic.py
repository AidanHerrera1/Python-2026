"""
-----------------------------------------------------------------------
ASSIGNMENT: 3B - The Buffet Calculator (Daily Specials)
DATE: [Insert Date]
FILE: buffet.py
-----------------------------------------------------------------------
REQUIREMENTS:
1. Ask the user for their age (convert to int) and the day of the week (convert to string).
2. Calculate the base price using if/elif/else:
   - Under 1: FREE ($0.00)
   - 1 to 12: $1.00 per year of age (Example: 5 years = $5.00)
   - 13 to 64: $16.95 (Standard Adult)
   - 65 and older: $12.95 (Senior Discount)
3. Use a match/case statement to handle special daily rules based on the day entered:
   - Tuesday: Children through age 12 are half price!
   - Sunday: Drinks are free!
   - Other days: Standard buffet pricing in effect.
4. Print the final price formatted as currency and display any applicable daily special notices.
-----------------------------------------------------------------------
"""

age = int(input("\n\nHow old are you? "))
day_of_week = input("\n\nWhat day of the week is it? ").lower()

# match day_of_week:
#     case "tuesday":
#         child_price_per_year = 0.50
#     case "sunday":
#         print("Drinks are free today!")
#         set child_price_per_year = 1.00    
#     case
#         set child_price_per_year = 1.00

# NOTE - working on a mac. python 3.9.6 match doesn't work

if age < 1:
   price = 0.00
elif age <= 12:
   price = age * 1.00
elif age <= 64:
   price = 16.95
else:
   price = 12.95

if day_of_week == "tuesday":
   if age <= 12:
      price *= 0.50
      print("\n\nChildren through age 12 are half price today!")
   else:
      print("\n\nStandard buffet pricing in effect.")
elif day_of_week == "sunday":
   print("\n\nDrinks are free today!")
else:
   print("\n\nStandard buffet pricing in effect.")

print(f"\n\nFinal price: ${price:.2f}")


















