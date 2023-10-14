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
SHEET = GSPREAD_CLIENT.open('care-plus')

# test = SHEET.worksheet('wellness')

# data = test.get_all_values()
# print(data)

def start_selection():
    """
    Select from menu options
    """
    while True:
        print(" Press 1 - To select existing students")
        print(" Press 2 - To create new students")
        print(" Press 3 - To view instructions\n")
        
        # main_input = input(int(("Enter: \n"))) 
        main_input = input("Enter your selection: \n")
        
        if main_input == 1:
            view_students()
        elif main_input == 2:
            create_students()
        elif main_input == 3:
            view_instructions()
        else:
            print("Invalid Selection")
            start_selection()
    
   

def main():
    """
    Run all program functions
    """
    print("==========================")
    print("Welcome to Care Plus App\n")
    print("--------------------------")
    start_selection()
    



main()
    
    