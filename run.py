import gspread
from google.oauth2.service_account import Credentials
from allowed_characters import *
from logo import *
from instructions import *
import os


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
    """Select from the main programme menu options"""
    # Clears the terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        print("""
            Press 1 - To select existing students
            print("Press 2 - To create a new student
            print("Press 3 - To view instructions
        """)
        menu_input = input("Enter your selection: \n")
        if menu_input.lower() == 'exit':
            custom_exit()
        validate_menu(menu_input)


def validate_menu(menu_input):
    """
    Checks for int value of inputed data from start menu input,
    raises ValueError of string cannot be converted
    into int, or if the input is wrong.
    """
    try:
        value = int(menu_input)

        if value not in [1, 2, 3]:
            print(f"{value} is not an option, please try again.\n")
    except ValueError as e:
        print(f"""
    The key entered in an invalid character.
    Enter only 1, 2, or 3.
    """)
        return False
    return start_selection_stage_2(value)


def start_selection_stage_2(value):
    """Receives the validate input for processing"""
    menu_inputed = value
    if menu_inputed == 1:
        view_students()
    elif menu_inputed == 2:
        create_students()
    elif menu_inputed == 3:
        view_instructions()
    else:
        print("Invalid Selection")


def view_students():
    """View existing students in the database"""
    print("Welcome to Student Portal")
    all_students = SHEET.worksheet("student_list").col_values(1)[1:]
    n = 1
    for student in all_students:
        print(f"{n}. {student}")
        n += 1
    print()
    select_student = input("Enter your Existing Student Name: \n")
    if select_student.lower() == 'exit':
        custom_exit()
    print()
    validate_student_record(all_students, select_student)


def validate_student_record(all_students, select_student):
    """Validate student selection"""
    if select_student.upper() in all_students:
        print(f"""
    Welcome to {select_student.upper()}'s management portal.

                Here you can do any of the following:

    Enter 1 to Input a new record for {select_student.upper()}
    Enter 2 to View {select_student.upper()}'s overall progress
    Enter 3 to Rename {select_student.upper()}
    Enter 4 to Delete {select_student.upper()}'s name and record from the app


    """)
        sub_view_menu = input("Choose option 1, 2, 3 or 4: \n")
        if sub_view_menu.lower() == 'exit':
            custom_exit()
        # if int(sub_view_menu) == 3:
        #     rename_student(select_student)
        # if int(sub_view_menu) == 4:
        #     delete_student(select_student)
        validate_sub_view_menu(sub_view_menu, select_student)
    else:
        print("Invalid Entry! Ensure your entry exists in the database.")
        return view_students()


def validate_sub_view_menu(sub_view_menu, select_student):
    """Validate Sub view Menu"""
    try:
        value = int(sub_view_menu)
        if value not in [1, 2, 3, 4]:
            print(f"{value} is not an option, please try again.\n")
    except ValueError as e:
        print(f"""
    The key entered in an invalid character.
    Enter only 1, 2, or 3.\n""")
        return False
    return sub_view_menu_stage_2(value, select_student)


def sub_view_menu_stage_2(value, select_student):
    """Receives the validated input for processing"""
    menu_inputed = value
    if menu_inputed == 1:
        student_progress_entry(select_student)
    elif menu_inputed == 2:
        select_student = select_student.upper()
        health_list = SHEET.worksheet(select_student).col_values(1)[1:]
        education_list = SHEET.worksheet(select_student).col_values(2)[1:]
        print()
        if len(education_list) == 0:
            print("This student has no records yet!\n")
            return student_progress_entry(select_student)
        else:
            view_student_summary(select_student)
    elif menu_inputed == 3:
        rename_student(select_student)
    elif menu_inputed == 4:
        delete_student(select_student)
    else:
        print("Invalid Selection")


def student_progress_entry(select_student):
    """For inputing student's progress on health and educaation"""
    print(f"""

    Welcome to {select_student.upper()}'s Care Progress

    """)
    student = select_student.upper()
    health_score(student)


def health_score(student):
    """Input Student Health Indicator"""
    while True:
        print(f"Enter Health Progress Value for {student}\n")
        health_indicator = input("Enter Health Score (0-10): \n")
        if health_indicator.lower() == 'exit':
            custom_exit()
        print()
        indicator = health_indicator
        validate_student_progress_input(student, indicator)


def education_score(student, validated_health_indicator):
    """
    Input Student Health Indicator
    """
    print(f"""
    Note: You entered '{validated_health_indicator}' for Health Indicator
    """)

    while True:
        print(f"Enter Education Progress Value for {student}\n")
        education_indicator = input("Enter Education Score (0-10): \n")
        if education_indicator.lower() == 'exit':
            custom_exit()
        print()
        validate_student_progress_education_input(
            student, validated_health_indicator, education_indicator
        )


def validate_student_progress_education_input(
    student, validated_health_indicator, education_indicator
):
    """Student validator input for Education"""
    try:
        validated_education_indicator = int(education_indicator)

        if validated_education_indicator not in [
            0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
        ]:
            print(f"""
    {validated_education_indicator} is not an option,
    please try again. Enter only numbers 0 to 10
    """)
    except ValueError as e:
        print(f"""
    The key entered in an invalid character.
    Enter only numbers 0 to 10.
    """)
        return False

    return insert_health_and_education_column(
        student, validated_health_indicator, validated_education_indicator
        )


def validate_student_progress_input(student, indicator):
    """Student progress input validator"""
    try:
        indicator_value = int(indicator)

        if indicator_value not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
            print(f"{indicator_value} is not an option, please try again.\n")
    except ValueError as e:
        print(f"""
    The key entered in an invalid character.
    Enter only numbers 0 to 10.
    """)
        return False

    return insert_health_column(student, indicator_value)


def insert_health_column(student, indicator_value):
    """
    Collect and hold validated Health indicator value
    """
    print()
    validated_health_indicator = indicator_value
    education_score(student, validated_health_indicator)


def insert_health_and_education_column(
    student, validated_health_indicator, validated_education_indicator
):
    """Health and Education column entries - done simultaneously"""
    print(f"""

    Entries for {student}:
    Health Indicator = {validated_health_indicator}
    Education Indicator = {validated_education_indicator}

    """)
    data = [validated_health_indicator, validated_education_indicator]
    worksheet_to_update = SHEET.worksheet(student)
    worksheet_to_update.append_row(data)
    print(f"Indicators for {student} have been successfully uploaded!\n")
    input("Press Enter to continue...")
    start_selection()


def view_student_summary(select_student):
    """Hold and Display student summary of Health and Education values"""
    print()
    select_student = select_student.upper()

    health_list = SHEET.worksheet(select_student).col_values(1)[1:]
    health_list = [int(char) for char in health_list]
    education_list = SHEET.worksheet(select_student).col_values(2)[1:]
    education_list = [int(char) for char in education_list]
    health_average = sum(health_list) / len(health_list)
    education_average = sum(education_list) / len(education_list)

    print(f"""

    The Health average for {select_student} is {round(health_average, 1)}

    """)

    data = health_list
    create_bar_chart(data)

    print(f"""
    The Education average for
    {select_student} is {round(education_average, 1)}
    """)

    data = education_list
    create_bar_chart(data)

    print("." * 35)
    input("Press Enter to continue...")
    start_selection()


# ChatGPT assisted in creating this function
def create_bar_chart(data):
    """Pictorial record display"""
    max_value = max(data)

    for i in range(max_value, 0, -1):
        row = ""
        for value in data:
            if value >= i:
                row += "██"
            else:
                row += "  "
        print(row)

    # Print x-axis
    print("-" * (2 * len(data)))


def create_students():
    """
    Create new student name and stores it in the database(google sheets)
    """
    print("Welcome to Student Creation")
    while True:
        studentName = input("Enter your New Student Name: \n")
        if studentName.lower() == 'exit':
            custom_exit()
        elif len(studentName) > 30:
            print("Student name cannont be more than 30 characters")
            return False
        if validate_student_name(studentName):
            studentName = studentName.upper()
            worksheet = SHEET.add_worksheet(
                title=studentName, rows=1000, cols=3
            )
            print(f"Creating {studentName}...")
            worksheet_to_update = SHEET.worksheet(studentName)
            headers = ["education", "health"]
            worksheet_to_update.append_row(headers)
            worksheet_to_update2 = SHEET.worksheet("student_list")
            studentName_list = [studentName]
            worksheet_to_update2.append_row(studentName_list)

            print(f"""
    {studentName} has been created successfully as a student
    in the database!
  
    """)
            input("Press Enter to continue...")
            start_selection()
        else:
            print("""
    Invalid input: Enter only a combination of leters and dot(.)
    """)


def rename_student(select_student):
    """Change Student name"""
    select_student = select_student.upper()
    print(f"Your have chosen to Rename {select_student} in the app.\n")
    while True:
        new_student_name = input("Enter a New Student Name: \n")
        if new_student_name.lower() == 'exit':
            custom_exit()
        if validate_student_name(new_student_name):
            new_student_name = new_student_name.upper()
            print(f"Renaming {select_student}...")
            # Rename Student in the Sheet
            worksheet_to_update = SHEET.worksheet(str(select_student))
            print(f"Updating {select_student} to {new_student_name}...")
            # worksheet_to_update.title = str(new_student_name)
            worksheet_to_update.update_title(new_student_name)

            # Rename Student in the list
            worksheet_to_update2 = SHEET.worksheet("student_list")
            value_to_find = str(select_student)
            cell = worksheet_to_update2.find(value_to_find)
            row_number = cell.row
            column_number = cell.col
            rename_student_name(new_student_name, row_number, column_number)

            print(f"""
    {new_student_name} has been successfully renamed in the database!
    """)
            input("Press Enter to continue...")
            start_selection()
        else:
            print("""
            nvalid input: Enter only a combination of leters and dot(.)
            """)


def delete_student(select_student):
    """Delete student name and record from app"""
    print(f"""
    Your have chosen to delete {select_student}'s name and record from the app!
    """)
    user_input = input("Are you sure?\nY- Yes or N- No: \n")
    if user_input.lower() == "n" or user_input.lower() == "no":
        custom_exit()
    elif user_input.lower() == "y" or user_input.lower() == "yes":
        print("""

              This can not be  undone!

              """)
        confirmation_input = input(
            f"Type {select_student.upper()} to delete: \n"
        )
        if confirmation_input.upper() == select_student.upper():
            select_student = select_student.upper()
            print(f"""
    Deleting {select_student.upper()} from the application...
    """)
            worksheet_to_delete = SHEET.worksheet(select_student)
            SHEET.del_worksheet(worksheet_to_delete)

            worksheet_to_update2 = SHEET.worksheet("student_list")
            value_to_find = str(select_student)
            cell = worksheet_to_update2.find(value_to_find)
            row_number = cell.row
            column_number = cell.col

            delete_student_name(row_number, column_number)

            print("""
            Student Record deleted...
            print("Student profile deletion is complete.
            Application would now restart
            """)
            restart()
        else:
            print("Invalid input...Program would now exit\n\n")
            custom_exit()
    else:
        print("Invalid input...Program would now exit")
        custom_exit()


def rename_student_name(studentName, row, col):
    """Rename the existing student name in the database"""
    worksheet = SHEET.worksheet("student_list")
    worksheet.update_cell(row, col, str(studentName))
    print("Student Name Changed....\n")


def delete_student_name(row, col):
    """Delete the existing student name in the database"""
    worksheet = SHEET.worksheet("student_list")
    worksheet.delete_rows(row)
    print("Student Name Deleted....\n")


def validate_student_name(student_name_input):
    """Student creation string validation"""
    import re
    print("Validating inputed name...")

    pattern = r'^[a-zA-Z]{2,}'
    while True:
        for char in student_name_input:
            if char not in allowed_characters:
                print("""
                      Invalid Characters detected...Try again
                      Only a combination of letters and '.' can be entered
                      """)
                return False
        if re.match(pattern, student_name_input):
            return True
        else:
            print("""
                  Your student name combination is not allowed.
                  Use a combination of at least 2 letters & no more than 1 dot
                  You also cannot start your input with two dot(..)
                  """)
            return False


def restart():
    """Restart or exit the Application"""
    while True:
        user_input = input(f"""
    Press enter to restart the program
    or type 'exit' to Terminate:
    """)
        if user_input.lower() == 'exit':
            custom_exit()
        if user_input.lower() == '':
            print("Restarting the application...\n")
            os.system('cls' if os.name == 'nt' else 'clear')
            main()
        elif user_input.lower() == 'exit':
            os.system('cls' if os.name == 'nt' else 'clear')
            custom_exit()
        else:
            print("Invalid seclection\n")


def view_instructions():
    """Display Instructions for using the Care Plus App"""
    print(instructions)

    user_input = input("Enter 'm' or any key to return to the main menu: ")
    if user_input.lower() == 'exit':
        custom_exit()
    if user_input.lower() == 'm':
        return_to_main_menu()
    else:
        print("Returning to the main menu...\n")
        return_to_main_menu()


def return_to_main_menu():
    """Back to Main menu"""
    # Clears the terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    start_selection()


def custom_exit():
    """Special exit for leaving the program from all input fields"""
    print("""
        Exiting application.........

        Goodbye.
        """)
    quit()


def welcome():
    """Welcome area containing logo and message"""
    print(logo)
    welcome = "Welcome to Care Plus App!"
    print("=" * len(welcome))
    print(welcome)
    print("=" * len(welcome))

    print("""
    This application helps you manage student data and track their progress.
    It was designed to help solve the WellTree model of
    health & social care management.

    Whether you're a teacher, guardian, or student, Care Plus
    is designed to make tracking educational and health indicators a breeze.

    Press Enter to embark on a journey of streamlined student management!
    """)


def main():
    """Run all program functions"""
    welcome()
    input("Press Enter to continue...")
    start_selection()


if __name__ == "__main__":
    main()
