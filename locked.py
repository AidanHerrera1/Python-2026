"""
-----------------------------------------------------------------------
ASSIGNMENT 6B: THE DEPARTMENT SECURITY TERMINAL
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Department constant defined in ALL_CAPS.
[ ] 3. Username tuple and password list defined.
[ ] 4. While loop runs interactively.
[ ] 5. Try/except catches TypeError and tells user to email help desk.
-----------------------------------------------------------------------
"""
#Define Constants 
Department = "Department of Tech"

USER_NAMES = list(("admin", "user1", "user2", "user3", "user4"))
PASSWORDS = list(["password123", "password321", "idontknow", "letmein", "123456"])


#Display menu and while loop 
while True:
    print("1. Look up user")
    print("2. change password")
    print("3. change username")
    print("4. exit")

    selection = input("Please select an option (1-4): ")
    if selection == "1":
        try:
            user_index = int(input("Enter the index of the user you want to look up (0-4): "))
            print(f"Username: {USER_NAMES[user_index]}")
            print(f"Password: {PASSWORDS[user_index]}")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
        except IndexError:
            print("index error occurred. Please contact the help desk.")
    elif selection == "2":
        try:
            user_index = int(input("Enter user you want to change the password for (0-4): "))
            new_password = input("Enter the new password: ")
            PASSWORDS[user_index] = new_password
            print(f"Password for {USER_NAMES[user_index]} has been changed.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
        except TypeError:
            print("Type error occurred. Please contact the help desk.")
    elif selection == "3":
        print("You cannot change your username, Contact HELP DESK")
    elif selection == "4":
        print("Exiting the program.")
        break

