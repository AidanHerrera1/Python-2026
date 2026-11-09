"""
ASSIGNMENT 9B: SPRINT 2 - FUNCTIONAL STUBS
Project: Quacken Coffee POS (V1.0)
Developer: Monty PyDuck
"""

import os

# ---------------------------------------------------------------------------
# STEP 1: Plan the program with FUNCTION STUBS
# ---------------------------------------------------------------------------

Genres = ("Action", "Horror", "Comedy", "Sci-Fi")

Showtimes = ("1:00 PM", "4:00 PM", "6:00 PM", "7:30 PM", "10:00 PM")

Ticket_type = ("Child", "Adult", "Student", "Senior Citizen")
Ticket_prices = {"Child": 5.00, "Adult": 10.00, "Student": 8.00, "Senior Citizen": 7.00}

Popcorn_prices = {"Small": 8.00, "Medium": 10.00, "Large": 12.00}
Drink_prices = {"Small": 3.00, "Medium": 4.50, "Large": 6.00}

Candy_types = ("Nerds", "Sour Patch Kids", "DOTS", "M&M's")
Candy_prices = {"Nerds": 3.00, "Sour Patch Kids": 3.00, "DOTS": 3.00, "M&M's": 3.00}

Price_file = "prices.txt"
History_file = "order_history.txt"


def get_customer():
    """Gets the customer's name."""
    pass


def load_prices():
    """Loads ticket prices from prices.txt."""
    pass


def past_orders(customer):
    """Checks saved extras and offers a reorder option."""
    pass


def select_movie():
    """Lets the customer choose a genre and then a movie."""
    pass


def select_showtime():
    """Lets the customer choose a showtime."""
    pass


def select_tickets(prices):
    """Collects ticket types and quantities."""
    pass


def check_discount(tickets):
    """Explains the ID requirement for Student and Senior discounts."""
    pass


def select_seats():
    """Displays the theater layout and collects seat choices."""
    pass


def select_extras(saved_extras):
    """Lets the customer select popcorn, drinks, and candy."""
    pass


def new_order(customer, prices, saved_extras):
    """Collects the movie, showtime, tickets, seats, and extras."""
    pass


def verify(order):
    """Displays the order and asks the customer to confirm it."""
    pass


def change_order(order):
    """Allows the customer to change parts of the order."""
    pass


def save_order(order):
    """Saves the customer's extras to order_history.txt."""
    pass


def display_order(order):
    """Displays the receipt with the total price."""
    pass


def main():
    """Organizes the program by calling the main functions."""
    prices = load_prices()
    customer = get_customer()
    saved_extras = past_orders(customer)
    order = new_order(customer, prices, saved_extras)
    approved = verify(order)
    save_order(order)
    display_order(order)

# GLOBAL CONSTANTS

Price_file = "prices.txt"
History_file = "order_history.txt"

Genres = ("Action", "Horror", "Comedy", "Sci-Fi")
Showtimes = ("1:00 PM", "4:00 PM", "6:00 PM", "7:30 PM", "10:00 PM")
Ticket_types = ("Child", "Adult", "Student", "Senior Citizen")

Movies = {
    "Action": ("The Dark Knight", "Top Gun: Maverick"),
    "Horror": ("The Night House", "Scream"),
    "Comedy": ("Elf", "School of Rock"),
    "Sci-Fi": ("Interstellar", "The Martian")
}

Popcorn_prices = {
    "None": 0.00,
    "Small": 8.00,
    "Medium": 10.00,
    "Large": 12.00
}

Drink_prices = {
    "None": 0.00,
    "Small": 3.00,
    "Medium": 4.50,
    "Large": 6.00
}

Candy_types = ("None", "Nerds", "Sour Patch Kids", "DOTS", "M&M's")
Candy_price = 3.00


def get_customer_info():
    """Asks for the customer's name."""
    name = input("Customer Name: ").title()
    return name


def load_prices():
    """Reads ticket types and prices from a text file."""
    if not os.path.exists(Price_file):
        with open(Price_file, "w") as file:
            file.write("Child,5.00\n")
            file.write("Adult,10.00\n")
            file.write("Student,8.00\n")
            file.write("Senior Citizen,7.00\n")

    prices = {}

    with open(Price_file, "r") as file:
        for line in file:
            ticket, price = line.strip().split(",")
            prices[ticket] = float(price)

    return prices


def take_order():
    """Collects movie, ticket, seat, and snack choices."""
    print("Movie Genres:", Genres)
    genre = input("Choose a genre: ").title()

    # Keep Sci-Fi formatted the same way as the dictionary key.
    if genre == "Sci-Fi":
        genre = "Sci-Fi"

    print("Available Movies:", Movies[genre])
    movie = input("Choose a movie: ").title()

    print("Showtimes:", Showtimes)
    showtime = input("Choose a showtime: ").upper()

    print("Ticket Types:", Ticket_types)
    ticket = input("Choose a ticket type: ").title()

    if ticket == "Student" or ticket == "Senior Citizen":
        print("Please show your ID at pickup to confirm your discount.")

    seat = input("Enter your seat (example: 10F): ").upper()

    popcorn = input("Popcorn (None/Small/Medium/Large): ").title()
    drink = input("Drink (None/Small/Medium/Large): ").title()

    print("Candy Choices:", Candy_types)
    candy = input("Choose candy: ").title()

    return {
        "genre": genre,
        "movie": movie,
        "showtime": showtime,
        "ticket": ticket,
        "seat": seat,
        "popcorn": popcorn,
        "drink": drink,
        "candy": candy
    }


def calculate_total(order_data, prices):
    """Adds the ticket price and selected extras."""
    total = prices[order_data["ticket"]]
    total = total + Popcorn_prices[order_data["popcorn"]]
    total = total + Drink_prices[order_data["drink"]]

    if order_data["candy"] != "None":
        total = total + Candy_price

    return total


def save_data_and_label(customer, order_data, total):
    """Saves the extras and prints the customer's receipt."""
    with open(History_file, "a") as file:
        file.write(f"Customer: {customer}\n")
        file.write(f"Popcorn: {order_data['popcorn']}\n")
        file.write(f"Drink: {order_data['drink']}\n")
        file.write(f"Candy: {order_data['candy']}\n\n")

    print("=================================")
    print("Aidan's Theater")
    print("=================================")
    print(f"CUSTOMER: {customer}")
    print(f"MOVIE: {order_data['movie']}")
    print(f"SHOWTIME: {order_data['showtime']}")
    print(f"TICKET: {order_data['ticket']}")
    print(f"SEAT: {order_data['seat']}")
    print("EXTRAS:")
    print(f"POPCORN: {order_data['popcorn']}")
    print(f"DRINK: {order_data['drink']}")
    print(f"CANDY: {order_data['candy']}")
    print(f"TOTAL: ${total:.2f}")
    print("=================================")
    print("ENJOY THE MOVIE!")


def main():
    # 1. Identity Phase
    name = get_customer_info()

    # 2. Data Collection Phase
    prices = load_prices()
    current_order = take_order()

    # 3. Calculation Phase
    final_price = calculate_total(current_order, prices)

    # 4. Handoff Phase using keyword arguments
    save_data_and_label(
        customer=name,
        order_data=current_order,
        total=final_price
    )


main()
