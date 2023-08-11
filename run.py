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

    print(f'Name and shooting info is {data_str}')


get_data()