"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Task 1: While Loop (The Nagging Kid)
       - Repeats "Are we there yet?" until user types "yes".
       - Uses a boolean variable to control the loop.
[ ] 3. Task 2: For Loop (99 Bottles of Beer)
       - Counts backwards from 99 to 1.
       - Prints "[number] bottles of beer on the wall!"
[ ] 4. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------
"""


while_asking = True

while while_asking:
    answer = input("Are we there yet? ").lower()
    if answer == "yes":
        while_asking = False



for bottle_count in range(99, 1, -1):
    print(f"{bottle_count} bottles of beer on the wall!")
    if bottle_count <= 2:
        print("1 bottle of beer on the wall!")
