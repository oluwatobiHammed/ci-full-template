
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
