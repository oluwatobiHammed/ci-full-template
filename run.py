
# import gspread
# from google.oauth2.service_account import Credentials

# SCOPE = [
#     "https://www.googleapis.com/auth/spreadsheets",
#     "https://www.googleapis.com/auth/drive.file",
#     "https://www.googleapis.com/auth/drive"
# ]

# # Load credentials from the file
# CREDS = Credentials.from_service_account_file('creds.json')

# # Authorize the client
# SCOPE_CREDS = CREDS.with_scopes(SCOPE)
# GSPREAD_CLIENT = gspread.authorize(SCOPE_CREDS)

# # Open the spreadsheet
# # SHEET = GSPREAD_CLIENT.open('love_sandwiches')

# try:
#     SHEET = GSPREAD_CLIENT.open('love_sandwiches')
# except gspread.exceptions.SpreadsheetNotFound as e:
#     print("Spreadsheet 'love_sandwiches' not found:", e)

# # Access the worksheet
# sales = SHEET.worksheet('sales')

# # Get all values from the worksheet
# data = sales.get_all_values()

# def get_sales_data():
#     """
#     Get sales figures input from the user.
#     We run a while loop to collect a valid string of data from the user
#     via the terminal, which must be a string of 6 numbers separated
#     by commas. The loop will repeatedly request data, until it is valid.
#     """

#     while True:
#         print("Please enter sales data from the last market.")
#         print("Data should be six numbers, separated by commas.")
#         print("Example: 10,20,30,40,50,60\n")
#         data_str = input("Enter your data here: \n")

#         sales_data = list(data_str.split(","))

#         if validate_data(sales_data):
#             break

#     return sales_data


# def validate_data(values):
#     """
#     Inside the try, converts all string values into integers.
#     Raises ValueError if strings cannot be converted into int,
#     or if there aren't exactly 6 values.
#     """

#     try:
#         [int(value) for value in values]
#         if len(values) != 6:
#             raise ValueError(
#                 f"Exactly 6 values are required, you provided {len(values)}")

#     except ValueError as e:
#         print(f"Invalid data: {e}, please try again\n")
#         return False

#     return True


# def update_worksheet(new_row, worksheet):
#     """
#     Update the specified worksheet,
#     adding a new row with the list data provided.
#     """
#     print(f"Updating {worksheet} worksheet...\n")
#     worksheet_to_update = SHEET.worksheet(worksheet)

#     # adds new row to the end of the current data
#     worksheet_to_update.append_row(new_row)

#     print(f"{worksheet} worksheet updated successfully\n")


# def calculate_surplus_data(sales_row):
#     """
#     Compare sales with stock and calculate the surplus for each item type.

#     The surplus is defined as the sales figure subtracted from the stock:
#     - Positive surplus indicates waste.
#     - Negative surplus indicates extra made when stock was sold out.
#     """
#     print("Calculating surplus data...\n")
#     stock = SHEET.worksheet("stock").get_all_values()
#     stock_row = stock[-1]

#     surplus_data = []

#     for stock, sales in zip(stock_row, sales_row):
#         surplus = int(stock) - sales
#         surplus_data.append(surplus)

#     return surplus_data


# def get_last_5_entires_sales():
#     """
#     Collect columns of data from sales worksheet.
#     Get the last 5 entries for each sandwich and return the data
#     as a list of lists.
#     """

#     sales = SHEET.worksheet("sales")

#     columns = []
#     for ind in range(1, 7):
#         column = sales.col_values(ind)
#         columns.append(column[-5:])

#     return columns


# def calculate_stock_data(data):
#     """
#     Calculate the average stock for each item type, adding 10%.
#     """
#     print("Calculating stock data...\n")
#     new_stock_data = []

#     for column in data:
#         int_column = [int(num) for num in column]

#         average = sum(int_column) / len(int_column)
#         stock_num = average * 1.1
#         new_stock_data.append(round(stock_num))

#     return new_stock_data

# def get_stock_values(data):
#     # Get the 'stock' worksheet
#     worksheet = SHEET.worksheet("stock")
    
#     # Get the headers (first row)
#     headings = worksheet.row_values(1)

#    # Check if the number of data values matches the number of headings
#     if len(data) != len(headings):
#         raise ValueError("The number of data values must match the number of headings")
    
#      # Create a dictionary by merging headings and data
#     data_dict = dict(zip(headings, data))
    
#     return data_dict

# def main():
#     """
#     Run all program functions.
#     """
#     data = get_sales_data()
#     sales_data = [int(num) for num in data]
#     update_worksheet(sales_data, "sales")

#     new_surplus_row = calculate_surplus_data(sales_data)
#     update_worksheet(new_surplus_row, "surplus")

#     sales_columns = get_last_5_entires_sales()
#     stock_data = calculate_stock_data(sales_columns)
#     update_worksheet(stock_data, "stock")
   
#     return stock_data

# stock_data = main()
# stock_values = get_stock_values(stock_data)

# print("Welcome to Love Sandwiches data automation.\n")

# print(stock_values)
# # 