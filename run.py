import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('shooting_chart')


# Main Menu function
def main_menu():
    """
    Displays Main Menu for user.
    Gives options to user and calls next function accordingly.
    If input is invalid, shows error and ask for valid option.
    """

    print("MAIN MENU")
    print("Enter 1, 2, 3 or 4 for option you would like to do: \n")
    print("*********************")
    print("1. Enter New Player and Shot's")
    print("2. Update Current Player")
    print("3. Display Current Shot's")
    print("4. Quit")
    print("********************* \n")
    while True:
        option = int(input("Option: \n"))
        if option == 1:
            get_data()
            # calculate_percentage()
            # update_sheet()
            # display_updated_sheet()
            break
        elif option == 2:
            get_data()
            # calculate_percentage
            # update_player()
            # display_updated_player()
            break
        elif option == 3:
            current_menu()
            break
        elif option == 4:
            exit()
            break
        else:
            print("Option is Invalid...")

    # Enter new_data()

    # Update current_player()

    # Display current_menu
     
        # Show all_data()

        # Show single_player

            # Enter players name


def calculate_percentage():
    


def current_menu():
    """
    Display current shots meny options
    """
    print("DISPLAY MENU")
    print("What would you like to see? \n")
    print("****************")
    print("0. Return to Main Menu")
    print("1. All Player's Shot's")
    print("2. Individual Player's Shot's")
    print("3. Quit")
    print("****************")
    while True:
        try:
            option = int(input("Option: \n"))
        except ValueError:
            print("Not a valid Option, Enter 1 or 2.")
            continue
        if option == 1:
            # show_all_data()
            break
        elif option == 2:
            get_name()
            # show_single_player()
            break
        elif option == 3:
            exit()
            break
        elif option == 0:
            main_menu()
            break
        else:
            print("Option is Invalid...")

    # return current menu when functions are done
    # current_menu()


def get_name():
    """
    Get name of player and validate as a string.
    """
    while True:
        name_input = input("Enter name of player: ")
        if validate_name(name_input):
            break
        else:
            print("Name should contain only letter's. Please try again.")
            continue

    name = name_input

    return name


def get_data():
    """
    Get name of player and shooting data and validate each are correct type.
    """
    while True:
        name_input = input("Enter name of player: ")
        if validate_name(name_input):
            break
        else:
            print("Name should contain only letter's. Please try again.")
            continue

    shot_data = get_shots()
    input_data = name_input, shot_data

    return input_data


def validate_name(name_input):
    """
    Inside while loop, will verify name_data is a string.
    Will raise a Error if name_data is not a string
    """
    if all(name.isalpha() or name.isspace() for name in name_input):
        return name_input


def get_shots():
    """
    Uses 2 while loops to get shot's made and attempted data.
    Loops will validate data is an integer
    """
    while True:
        shots_made = input("Enter number of shot's made: ")
        if shots_made.isdigit():
            shots_made = int(shots_made)
            break
        else:
            print("Made shot's should be number's only, Please try again.")
            continue

    while True:
        shots_attempted = input("Enter number of shot's attempted: ")
        if shots_attempted.isdigit():
            shots_attempted = int(shots_attempted)
            break
        else:
            print("Attempted should be number's only, Please try again.")
            continue

    return shots_made, shots_attempted


def calculate_percentage():
    """
    Takes shots made and shots attempted to calculate a percentage.
    Percentage will be used for new player statistics or to 
    update a current player.
    """


print("Welcome To Shooting Spreadsheet")
main_menu()
