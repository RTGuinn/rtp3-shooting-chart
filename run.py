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

# shots = SHEET.worksheet('shots')

# data = shots.get_all_values()

# print(data)


def get_data():
    """
    Get name of player and shooting data to input into spreadsheet
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
    

def get_shots():
    """
    Will have 2 while loops to get shot's made and attempted data.
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


def validate_name(name_input):
    """
    Inside while loop, will verify name_data is a string.
    Will raise a Error if name_data is not a string
    """
    return name_input.isalpha()


get_data()
