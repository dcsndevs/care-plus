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

def start_selection():
    """
    Select from menu options
    """
    while True:
        print(" Press 1 - To select existing students")
        print(" Press 2 - To manage students")
        print(" Press 3 - To view instructions\n")
        
        # main_input = input(int(("Enter: \n"))) 
        menu_input = input("Enter your selection: ")
        
        validate_menu(menu_input)
        print("after_validate")
        
            
    
            
def validate_menu(menu_input):
    """
    Checks for int value of inputed data from start menu input,
    raises ValueError of string cannot be converted into int, or if the input is wrong
    """
    try:
        value = int(menu_input)

        if value not in [1, 2, 3]:
            print(f"{value} is not an option, please try again.\n"
            )
    except ValueError as e:
        print(f"The key entered in an invalid character. Enter only 1, 2, or 3.\n")
        return False
        
    return start_selection_stage_2(value)

def start_selection_stage_2(value):
    """
    Receives the validate input for processing
    """
    menu_inputed = value
    print("checking")
    if menu_inputed == 1:
        view_students()
    elif menu_inputed == 2:
        create_students()
    elif menu_inputed == 3:
        view_instructions()
    else:
        print("Invalid Selection")
        # start_selection()

def view_students():
    """
    View existing students in the database
    """
    print("Welcome to Student Portal")
    
    all_students = SHEET.worksheet("student_list").col_values(1)[1:]
    n = 1
    for student in all_students:
        
        print(f"{n}. {student}")
        n += 1
        
    select_student = input("Enter your Existing Student Name: \n")
    validate_student_record(all_students, select_student)
    
    
def validate_student_record(all_students, select_student):
    """
    Validate student selection
    """
    if select_student.upper() in all_students:
        print("Bingo!")
        return student_progress_entry(select_student)
    else:
        print("Invalid Entry! Ensure your entry exists in the database.")
        return view_students()
           
def student_progress_entry(select_student):
    """
    For inputing student's progress on health and educaation
    """
    print(f"Welcome to {select_student.upper()} Care Progress")
    student = select_student.upper()
    health_score(student)
    
    
def health_score(student):
    """
    Inpur Student Health Indicator
    """
    while True:
        print(f"Ready to input Health Progress Value for {student}")
        health_indicator = input("Enter Health Score (0-10): ")
        indicator = health_indicator
        validate_student_progress_input(student, indicator)
        
    
        
    

def education_score(student, validated_health_indicator):
    """
    Input Student Health Indicator
    """
    print(f"Note: You entered '{validated_health_indicator}' for Health Indicator")
          
    while True:
        print(f"Ready to input Education Progress Value for {student}")
        education_indicator = input("Enter Health Score (0-10): ")
        validate_student_progress_education_input(student, validated_health_indicator, education_indicator)
    
def validate_student_progress_education_input(student, validated_health_indicator, education_indicator):
    """
    Student validator input for Education
    """
    try:
        validated_education_indicator = int(education_indicator)

        if validated_education_indicator not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
            print(f"{validated_education_indicator} is not an option, please try again.\n"
            )
    except ValueError as e:
        print(f"The key entered in an invalid character. Enter only numbers 0 to 10.\n")
        return False
        
    return insert_health_and_education_column(student, validated_health_indicator, validated_education_indicator)
    
def validate_student_progress_input(student, indicator):
    """
    Student progress input validator
    """    
    try:
        indicator_value = int(indicator)

        if indicator_value not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
            print(f"{indicator_value} is not an option, please try again.\n"
            )
    except ValueError as e:
        print(f"The key entered in an invalid character. Enter only numbers 0 to 10.\n")
        return False
        
    return insert_health_column(student, indicator_value)

def insert_health_column(student, indicator_value):
    print("Hello WorlD")
    validated_health_indicator = indicator_value
    education_score(student, validated_health_indicator)
    
def insert_health_and_education_column(student, validated_health_indicator, validated_education_indicator):
    print("Hurray`!")
    print()
    print(student)
    print(validated_health_indicator)
    print(validated_education_indicator)
    data = [validated_health_indicator, validated_education_indicator]
    worksheet_to_update = SHEET.worksheet(student)
    worksheet_to_update.append_row(data)
    print(f"Indicators for {student} have been successfully uploaded!")
    restart()
    
def create_students():
    """
    Student creation
    """
    print("Welcome to Student Creation") 
    while True:
        studentName = input("Enter your New Student Name: ")
        if validate_student_name(studentName):
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
        else:
            print("Invalid input: Enter only a combination of leters and dot(.)")
            
    

def validate_student_name(student_name_input):
    """
    Student creation string validation
    """
    import re
    print("Validating inputed name...")

    allowed_characters = ['.', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    pattern = r'^[a-zA-Z]{2,}'
    while True:
        print()
        # student_name_input = input('Enter New Student Name\nYou can use dot "." to seperate firstname and surname: ')
        for char in student_name_input:
            if char not in allowed_characters:
                print("Invalid Characters detected...Try again\nOnly a combination of letters and '.' can be entered\n")
                return False
        if re.match(pattern, student_name_input):
            return True
        else:
            print("Your student name combination is not allowed.\nEnter a combination of at least 2 letters and no more than 1 dot.\nYou also cannot start your input with two dot(..)")
            return False
    
    print(f'You have entered {student_name_input}')
    
    
def restart():
    """
    Restart or exit the Application
    """
    while True:
        user_input = input(f"Press enter to restart the program or type 'exit' to Terminate: ")
        if user_input.lower() == '':
            print("Restarting the application...\n")
            main()
        elif user_input.lower() == 'exit':
            print("Exiting...")
            exit()
        else:
            print("Invalid seclection\n")
            
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
   
    