"""
-----------------------------------------------------------------------
ASSIGNMENT 6A: TICKET SALES
-----------------------------------------------------------------------
[ ] 1. Create a list of 20 seats (numbered 1-20).
[ ] 2. Display the list of available seats.
[ ] 3. Ask user for a seat number (0 to quit).
[ ] 4. Remove the selected seat from the list.
[ ] 5. Handle invalid inputs (seat taken or doesn't exist).
[ ] 6. Repeat until user quits or seats are empty.
-----------------------------------------------------------------------
"""
# print seats
seats = list(range(1, 21))
while seats:
    print("\nAvailable seats:\n", seats)
    try:
        input_seat = int(input("\nPlease select a seat number (1-20) or enter 0 to quit: "))
    except ValueError:
        print("Invalid input. Please enter a valid seat number.")
        continue
    if input_seat == 0:
        print("\nThank you for using the ticket booking system. Goodbye!")
        break
    if input_seat in seats:
        seats.remove(input_seat)
        print(f"\nSeat {input_seat} has been successfully booked.")
    else:
        print(f"\nSeat {input_seat} is either taken or does not exist. Please select a valid seat.")
    if not seats:
        print("\nAll seats are booked. Goodbye!")
        break
1