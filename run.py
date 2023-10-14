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
        menu_input = input("Enter your selection: \n")
        menu_inputed = int(menu_input)
        validate_menu(menu_inputed)
        
        if menu_inputed == 1:
            view_students()
            break
        elif menu_input == 2:
            create_students()
            break
        elif menu_input == 3:
            view_instructions()
            break
        else:
            print("Invalid Selection")
            start_selection()
            
    return menu_inputed
            
def validate_menu(value):
    """
    Checks for int value of inputed data from start menu input,
    raises ValueError of string cannot be converted into int, or if the input is wrong
    """
    try:
        [int(value)]
        if value > 3:
            raise ValueError(
                f"Invalid Imput: {value} is greater than 3, please try again.\n"
            )
    except ValueError as e:
        print(f"Invalid input: {e}, Please try again.\n")
        
    return True
    
def view_students():
    print("Welcome to Student Selection*****")   

def main():
    """
    Run all program functions
    """
    print("==========================")
    print("Welcome to Care Plus App\n")
    print("--------------------------")
    start_selection()
    
    



main()
    
    