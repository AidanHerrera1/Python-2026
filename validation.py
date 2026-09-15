"""
-----------------------------------------------------------------------
ASSIGNMENT 5A: INPUT VALIDATION
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. All 5 inputs have 'while' loop validation.
[ ] 3. The more tickets loop uses .upper() and correct Boolean logic.
[ ] 4. Include a try and except statement around the entire program. Should have one defined 
       exception (probably value error) and a generic exception
[ ] 5. Have pinned a variable in the WATCH window and took a screenshot.
-----------------------------------------------------------------------
"""
#First Name & Last Name: Cannot be blank.
#Age: Must be a number; also check whether they are older or younger than 21 to determine whether they get a drink ticket.
#Phone Number: Cannot be blank.
#Ticket Count: Must be a valid integer > 0 (Crash-Proof!).
#Additional Tickets? (Y/N)

try: 
    fname = ""
    while not fname:
        fname = input("Please enter your first name: ")
        fname = fname.strip() 

    last_name = ""
    while not last_name:
        last_name = input("Please enter your last name: ")
        last_name = last_name.strip()
   
    age = -1
    while age <= 0:
            age = int(input("Please enter your age: (Whole years, round down)"))
except ValueError: 
        print("Im sorry, that is not a valid value")
except Exception as e:
        print(f"Error: {e}")
if age < 21:
        print("\nYou are not old enough to receive a drink ticket.\n")
else:
        print("\nYou are old enough to receive a drink ticket.\n")
tickets = 1
while True:
        try:
            tickets = int(input("How many tickets would you like to purchase? (Must be a whole number greater than 0)"))
            if tickets > 0:
                break
            else:
                print("Please enter a valid number of tickets greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")
print("You have purchased", {tickets}, "ticket(s).")
