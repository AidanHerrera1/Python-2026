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
# First and Last name
try:
    fname = ""
    while not fname:
        fname = input("Please enter your first name: ")
        fname = fname.strip() 

    last_name = ""
    while not last_name:
        last_name = input("Please enter your last name: ")
        last_name = last_name.strip()
#Phone number
    phone = ""
    while not phone:
        phone = input("Please enter your phone number: ")
        phone = phone.strip()
#Age verification + drink ticket
    age = -1
    while age <= 0:
        try:
            age = int(input("Please enter your age: (Whole years, round down) "))
            if age <= 0:
                print("Please enter an age greater than 0.")
        except ValueError:
            print("I'm sorry, that is not a valid age.")

    if age < 21:
        print("\nYou are not old enough to receive a drink ticket.\n")
    else:
        print("\nYou are old enough to receive a drink ticket.\n")
#Ticket count and additional tickets
    tickets = 0
    while tickets <= 0:
        try:
            tickets = int(input("How many tickets would you like to purchase? (Must be a whole number greater than 0) "))
            if tickets <= 0:
                print("Please enter a valid number of tickets greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    more_tickets = ""
    while True:
        more_tickets = input("Would you like to purchase additional tickets? (Y/N) ").strip().upper()
        if more_tickets in ("Y", "N"):
            break
        else:
            print("Please enter Y or N.")

    print(f"You have purchased {tickets} ticket(s).")
    print(f"Additional tickets requested: {more_tickets}")
except ValueError:
    print("I'm sorry, that is not a valid value.")
except Exception as error:
    print(f"An unexpected error occurred: {error}")
        