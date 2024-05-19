
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

# Load credentials from the file
CREDS = Credentials.from_service_account_file('creds.json')

# Authorize the client
SCOPE_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPE_CREDS)

# Open the spreadsheet
# SHEET = GSPREAD_CLIENT.open('love_sandwiches')

try:
    SHEET = GSPREAD_CLIENT.open('love_sandwiches')
except gspread.exceptions.SpreadsheetNotFound as e:
    print("Spreadsheet 'love_sandwiches' not found:", e)

# Access the worksheet
sales = SHEET.worksheet('sales')

# Get all values from the worksheet
data = sales.get_all_values()

# Print the data
print(data)

def get_sales_data():
    """
    Get sales input from the users
    """

    print("Please enter sales data from the last market.")
    print("Data should be 6 digit numbers, seperated by commas.")
    print("Example: 10,20,30,40,50,60\n")

    data_str = input("Enter your data here: ")

    sales_data = data_str.split(',')
    validate_data(sales_data)

def validate_data(values):
    """
    Indside the try, converts all string values to integers.
    Rasies ValueError if string cannot be converted into int,
    or if there aren't exactly 6 values.
    """
    try:
        [value for value in values]
        if len(values) != 6:
            raise ValueError(f"Exactly 6 values is required, you provided {len(values)} ")
    except ValueError as e:
        print(f"Invalid data: {e}, please try again")



get_sales_data()