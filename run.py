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

    # get_shots()

    print(name_input)
    # print(get_shots)
    
    # data = name_input # +data_str # will have other variable names for shots
    # return data


def validate_name(name_input):
    """
    Inside while loop, will verify name_data is a string.
    Will raise a Error if name_data is not a string
    """
    return name_input.isalpha()


get_data()
