import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('credentials.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Water-Quality-Advisory')

def get_raw_data():
    """
    Gets raw data from the user.
    """
    while True:
        print("Please enter your raw data below.\n")
        print("Please enter your measurements in the following order:\n")
        print("Day of the month (e.g. 1, 2, 3,...), pH, Lead, Cadmium, Zinc, Mercury, Arsenic, Chromium, Nickel.\n")
        print("Please make sure your units are in mg/L.\n")

        raw_data_str = input("Enter your raw data here:")
        raw_data = raw_data_str.split(",")
        validate_raw_data(raw_data)

        if validate_raw_data(raw_data):
            print("Data is valid.")
            break
    return raw_data
    

def validate_raw_data(entries):
    """
    Validates data using a try statement. 
    Ensures that entered values are are exactly 9 entries.
    """
    try:
        if len(entries) != 9:
            raise ValueError(
                f"Exactly 9 entries are required, you provided {len(entries)} entries"
                )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
    
    return True

get_raw_data()