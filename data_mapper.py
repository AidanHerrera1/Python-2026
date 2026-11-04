
"""
-----------------------------------------------------------------------
ASSIGNMENT 8A: OPTION A - NATO TRANSLATOR
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. NATO_ALPHABET constant is a dictionary (Full A-Z).
[ ] 3. Program takes a word and uppercases it.
[ ] 4. Program loops through letters and prints NATO words.
[ ] 5. A 'try/except' block handles punctuation or numbers.
-----------------------------------------------------------------------
"""

# TODO: Loop through each character
# TODO: try to print the NATO code, except if character is missing
#alphabet

nato_alphabet = {
    "A": "ALPHA",
    "B": "BRAVO",
    "C": "CHARLIE",
    "D": "DELTA",
    "E": "ECHO",
    "F": "FOXTROT",
    "G": "GOLF",
    "H": "HOTEL",
    "I": "INDIA",
    "J": "JULIET",
    "K": "KILO",
    "L": "LIMA",
    "M": "MIKE",
    "N": "NOVEMBER",
    "O": "OSCAR",
    "P": "PAPA",
    "Q": "QUEBEC",
    "R": "ROMEO",
    "S": "SIERRA",
    "T": "TANGO",
    "U": "UNIFORM",
    "V": "VICTOR",
    "W": "WHISKEY",
    "X": "X-RAY",
    "Y": "YANKEE",
    "Z": "ZULU",
}
#menu loop
while True:
    print("\nNATO TRANSLATOR\n")
    print("1. Enter English Word")
    print("2. Enter Coded Word")
    print("3. Quit\n")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        word = input("Enter word to spell: \n").upper()
        for letter in word:
            try:
                print(nato_alphabet[letter])
            except KeyError:
                print(f"'{letter}' is not a valid letter in the NATO alphabet.")
    if choice == "2":
        coded_word = input(
            "Enter NATO words separated by spaces: "
        ).upper()
        
