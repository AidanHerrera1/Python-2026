"""
ASSIGNMENT 9B: SPRINT 2 - FUNCTIONAL STUBS
Project: Quacken Coffee POS (V1.0)
Developer: Monty PyDuck
"""


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
