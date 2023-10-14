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
        menu_input = input("Enter your selection: ")
        menu_inputed = int(menu_input)
        validate_menu(menu_inputed)
        
        if menu_inputed == 1:
            view_students()
            break
        elif menu_inputed == 2:
            create_students()
            break
        elif menu_inputed == 3:
            view_instructions()
            break
        else:
            print("Invalid Selection")
            # start_selection()
            
    return menu_inputed
            
def validate_menu(value):
    """
    Checks for int value of inputed data from start menu input,
    raises ValueError of string cannot be converted into int, or if the input is wrong
    """
    try:
        # [int(value)]
        if value > 3:
            raise ValueError(
                f"Invalid Input: {value} is greater than 3, please try again.\n"
            )
    except ValueError as e:
        print(f"Invalid input: {e}, Please try again.\n")
        return False
        
    return True
    
def view_students():
    """
    View existing students in the database
    """
    print("Welcome to Student Portal")
    
    all_students = SHEET.worksheet("student_list").col_values(1)
    for student in all_students:
        print(student)
    select_student = input("Enter your New Student Name: \n")
    print(f"Welcome to {select_student} info")
    health_indicator = input("Enter Health Score (1-10): \n")
    education_indicator = input("Enter Education Score (1-10): \n")
           
    
def create_students():
    """
    Student creation
    """
    print("Welcome to Student Creation") 
    studentName = input("Enter your New Student Name: ")
    validate_student_name(studentName)
    studentName = studentName.upper()
    worksheet = SHEET.add_worksheet(title = studentName, rows=1000, cols=3)
    print(f"Creating {studentName}...")
    worksheet_to_update = SHEET.worksheet(studentName)
    headers = ["education", "health"]
    worksheet_to_update.append_row(headers)
    worksheet_to_update2 = SHEET.worksheet("student_list")
    studentName_list = [studentName]
    worksheet_to_update2.append_row(studentName_list)
    
    print(f"{studentName} has been created successfully as a student in the database!\n")
    main()

def validate_student_name(studentName):
    print("Validating inputed name...")
    

def view_instructions():
    """
    App Instructions3
    """
    print("This is instruction for how to use this application")
    


def main():
    """
    Run all program functions
    """
    print("==========================")
    print("Welcome to Care Plus App\n")
    print("--------------------------")
    start_selection()
    


main()
    
    