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
            print("Data is valid.\n")
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

def export_to_worksheet(data, worksheet):
    """
    Receives raw data from the user and exports it to a spreadsheet.
    """
    print(f"Exporting raw data to {worksheet} worksheet...\n")
    raw_data_worksheet = SHEET.worksheet(worksheet)
    raw_data_worksheet.append_row(data)
    print(f"{worksheet} worksheet updated successfully\n")

    """
    Calculates mean, median, min and max for week 1 of the month.
    """
def get_week1_metal_data():
    """
    Collects columns of data from the metals_only worksheet and returns the data
    as a list of lists.
    """
    week1_metal_data = SHEET.worksheet("metals_only")

    columns = []
    for ind in range(1, 8):
        column = week1_metal_data.col_values(ind)
        columns.append(column[1:8])

    return columns

def compute_week1_average(data):
    """
    Calculates the average concentration for each metal for week1
    """
    print("Calculating week 1 averages...\n")
    
    week1_average = []

    for column in data:
        float_column = [float(num) for num in column]
        average = sum(float_column) / len(float_column)
        week1_average.append(average)

    return week1_average

def compute_week1_median(data):
    """
    Calculates the median  concentration for each metal for week1
    """
    print("Calculating week 1 medians...\n")
    
    week1_median = []

    for column in data:
        float_column = [float(num) for num in column]
        median = sorted(float_column)[len(float_column) // 2]
        week1_median.append(median)

    return week1_median

def compute_week1_minima(data):
    """
    Calculates the minimum  concentration for each metal for week1
    """
    print("Calculating week 1 minima...\n")
    
    week1_minima = []

    for column in data:
        float_column = [float(num) for num in column]
        minimum = min(float_column)
        week1_minima.append(minimum)

    return week1_minima

def compute_week1_maxima(data):
    """
    Calculate the maximum  concentration for each metal for week1
    """
    print("Calculating week 1 minima...\n")
    
    week1_maxima = []

    for column in data:
        float_column = [float(num) for num in column]
        maximum = max(float_column)
        week1_maxima.append(maximum)

    return week1_maxima

def compare_mean_with_MCL():
    """
    Compares calculated average metal concentration with 
    Maximum Contamination Limit (MCL) of the metals and prints
    an appropriate message to the terminal.
    """

    print("Comparing your weekly average with recommended MCLs...\n")

    sheet1 = GSPREAD_CLIENT.open('Water-Quality-Advisory').worksheet('Week1_Summary')
    sheet2 = GSPREAD_CLIENT.open('Water-Quality-Advisory').worksheet('MCLs')

    # Compare the values in cell A2 of each sheet


    if sheet1.acell('A2').value == sheet2.acell('A2').value:
        print("The concentration of Lead is at the maximum contamination limit."
        "Your water may not be safe for consumption.\n")
    elif sheet1.acell('A2').value > sheet2.acell('A2').value:
        print(f"The concentration of Lead exceeds the maximum contamination limit."
            "Your water is not safe for consumption.\n")
    else:
        print(f"The concentration of Lead is below maximum contamination limit.\n")


    if sheet1.acell('B2').value == sheet2.acell('B2').value:
        print("The concentration of Cadmium is at the maximum contamination limit."
        "Your water may not be safe for consumption.\n")
    elif sheet1.acell('B2').value > sheet2.acell('B2').value:
        print(f"The concentration of Cadmium exceeds the maximum contamination limit."
            "Your water is not safe for consumption.\n")
    else:
        print(f"The concentration of Cadmium is below maximum contamination limit.\n")


    if sheet1.acell('C2').value == sheet2.acell('C2').value:
        print("The concentration of Zinc is at the maximum contamination limit."
        "Your water may not be safe for consumption.\n")
    elif sheet1.acell('C2').value > sheet2.acell('C2').value:
        print(f"The concentration of Zinc exceeds the maximum contamination limit."
            "Your water is not safe for consumption.\n")
    else:
        print(f"The concentration of Zinc is below maximum contamination limit.\n")

    if sheet1.acell('D2').value == sheet2.acell('D2').value:
        print("The concentration of Mercury is at the maximum contamination limit."
        "Your water may not be safe for consumption.\n")
    elif sheet1.acell('D2').value > sheet2.acell('D2').value:
        print(f"The concentration of Mercury exceeds the maximum contamination limit."
            "Your water is not safe for consumption.\n")
    else:
        print(f"The concentration of Mercury is below maximum contamination limit.")

    if sheet1.acell('E2').value == sheet2.acell('E2').value:
        print("The concentration of Arsenic is at the maximum contamination limit."
        "Your water may not be safe for consumption.\n")
    elif sheet1.acell('E2').value > sheet2.acell('E2').value:
        print(f"The concentration of Arsenic exceeds the maximum contamination limit."
            "Your water is not safe for consumption.\n")
    else:
        print(f"The concentration of Arsenic is below maximum contamination limit.\n")

    if sheet1.acell('F2').value == sheet2.acell('F2').value:
        print("The concentration of Chromium is at the maximum contamination limit."
        "Your water may not be safe for consumption.\n")
    elif sheet1.acell('F2').value > sheet2.acell('F2').value:
        print(f"The concentration of Chromium exceeds the maximum contamination limit."
            "Your water is not safe for consumption.\n")
    else:
        print(f"The concentration of Chromium is below maximum contamination limit.\n")

    if sheet1.acell('G2').value == sheet2.acell('G2').value:
        print("The concentration of Nickel is at the maximum contamination limit."
        "Your water may not be safe for consumption.\n")
    elif sheet1.acell('G2').value > sheet2.acell('G2').value:
        print(f"The concentration of Nickel exceeds the maximum contamination limit."
            "Your water is not safe for consumption.\n")
    else:
        print(f"The concentration of Nickel is below maximum contamination limit.\n")


def main():
    """
    Runs all program functions.
    """
    raw_data = get_raw_data()
    export_to_worksheet(raw_data, "user-data")
    formatted_data = [round(float(value), 3) for value in raw_data[-7:]]
    export_to_worksheet(formatted_data, "metals_only")
    metal_data = get_week1_metal_data()
    average_for_week1 = compute_week1_average(metal_data)
    export_to_worksheet(average_for_week1, "Week1_Summary")
    median_for_week1 = compute_week1_median(metal_data)
    export_to_worksheet(median_for_week1, "Week1_Summary")
    minimum_for_week1 = compute_week1_minima(metal_data)
    export_to_worksheet(minimum_for_week1, "Week1_Summary")
    maximum_for_week1 =  compute_week1_maxima(metal_data)
    export_to_worksheet(maximum_for_week1, "Week1_Summary")
    compare_mean_with_MCL()

main()