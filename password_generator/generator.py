import string   # To import module constants.
import random   # Module to return random values.

# Password format design.
chars = list(string.ascii_letters + string.digits + "¬!£$%^&*_+")


def generate_password():
    """
    Generates a random password based on user input.
    """
    password_length = int(input("""Enter the number of characters for your \
password: """))
    random.shuffle(chars)   # Returning chars in random order.
    password = []   # Variable to store generated password.
    for x in range(password_length):
        password.append(random.choice(chars))
    random.shuffle(password)  # Returns password in random order.
    password = "".join(password)
    print("Generated Password:", password)  # Password is generated.


# Menu initialisation.
menu = input("""Would you like to generate a random password? Type '1' \
to generate or type '2' to quit the program: """).strip()

# 4 options added to cover a range of possible inputs.
if menu == "1":
    generate_password()
elif menu == "2":
    print("Program closed.")
elif menu.strip() == "":
    print("No input was entered. Please try again.")
else:
    print("Incorrect input. Please try again.")
