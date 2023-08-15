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


# Menu function
def main_menu():
    """
    Displays Main Menu for user.
    Gives options to user and calls next function accordingly.
    If input is invalid, shows error and ask for valid option.
    """

    print("Main Menu")
    print("Enter 1, 2 or 3 for option you would like to do: \n")
    print("--------------")
    print("1. Enter New Player and Shots")
    print("2. Update Current Player")
    print("3. Display Current Shot's")
    print("--------------")
    while True:
        try:
            option = int(input("Option: \n"))
        except ValueError:
            print("Not a valid Option, Enter 1 or 2.")
            continue
        if option == 1:
            get_data()
            break
        elif option == 2:
            get_name()
            break



    # Enter new_data()

    # Update current_player()
    
    # Display current_menu
        
        # Show all_data()
        
        # Show single_player
            
            # Enter players name 

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
    return name_input.isalpha()


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


print("Welcome To Shooting Spreadsheet")
main_menu()
