"""
-----------------------------------------------------------------------
ASSIGNMENT 7B: THE MAGIC 8 BALL
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. RESPONSES is a tuple containing at least 8 string options.
[ ] 3. Program uses a 'while True' loop to keep the game running.
[ ] 4. random.choice() selects the answer from the tuple.
[ ] 5. Logic checks if "quit" is in the user input to break the loop.
-----------------------------------------------------------------------
"""
# Random Responses
import random

responses = (
    "Yes",
    "No",
    "Maybe",
    "Ask Again Later",
    "Definitely",
    "Probably Not",
    "It Is Possible",
    "Absolutely",
)



# Magic 8ball loop
print("\nWelcome To The Magic 8ball!\n")
while True:
    question = input("\nAsk The Magic 8 Ball anything (Type 'quit' to exit): \n")
    if "quit" in question.lower():
        print("\nGoodbye!\n")
        break

    answer = random.choice(responses)
    print("Magic 8ball says:", answer )

