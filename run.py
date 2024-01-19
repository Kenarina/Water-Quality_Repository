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
    print("Please enter your raw data below.\n")
    print("Please enter the date and your measurements in the following order:\n")
    print("Day of the month (e.g. 1, 2, 3,...), pH, Lead, Cadmium, Zinc, Mercury, Arsenic, Chromium, Nickel.\n")
    print("Please make sure your units are in mg/L.\n")

    raw_data = input("Enter your raw data here:")
    print(f"You have entered: {raw_data}")

get_raw_data()