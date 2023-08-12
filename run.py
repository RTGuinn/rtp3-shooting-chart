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
    print("Please enter name")

    name_str = input("Enter name of player: ")

    name_data = name_str

    print("Shot data should be two numbers, seperated by comma's.")
    print("Example: 22, 54\n")
    data_str = input("Enter shot data: ")

    shot_data = data_str
    print(f'{name_data} {data_str}')


get_data()

# validate_data(shot_data)

'''
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
'''
