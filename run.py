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
    Get name of player and shooting numbers to input from user
    """
    print("Please enter name and shooting info")
    print("Data should be name with shot's made and shot's attempted seperated by commas.")
    print("Example: John Doe, 34, 50\n")
    
    data_str = input("Enter name and shots here: ")

    shot_data = data_str.split(",")
    validate_data(shot_data)


def validate_data(values):
    """
    Inside the try statement, will verify the data given is in the proper form.
    Will raise a ValueError if data is not in correct form, or given too many value's.
    """
    try:
        if len(values) != 3:
            raise ValueError(
                f"Only name, shot's made and shot's attempted please,  your input was {values}")
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")



get_data()