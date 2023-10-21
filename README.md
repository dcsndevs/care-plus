# ![Care+ logo](documentation/logo-care.png)

## Welcome,
Care Plus App is a Python-based application designed to manage student data and track their progress in health and education. The app uses Google Sheets for data storage and visualization.
 

The link to the deployed site can be found [Here](https://care-plus-e6b7c675e391.herokuapp.com/)

![Responsive views](documentation/care-responsiveness.png)

## User Stories

### First-Time Visitor Goals: 
As a first-time visitor, the goals are:

- Understand the Purpose of the Careplus App
- Gain an understanding of the app's purpose and functionality
- Navigate the Interface: Easily navigate through the menu options
- Efficient Data Management of student record
- Manage existing student records efficiently
- Create and track progress for new students and old student's health and education indicator data
- Explore the various features, including viewing instructions, creating students, and viewing existing students.
- Be able to make informed decision based on data collected over a period of time for a student

## Logic Flowchart 
# ![Flowchart](documentation/flow-chart-advance.png)

## Features 
# ![Main Menu](documentation/main-screen.png)

### Main Menu:
The app utilizes student names as usernames, ensuring a personalized experience.

- **Select Options:**
  - Press `1` to view existing students.
  - Press `2` to create a new student.
  - Press `3` to view instructions.

- **View Existing Students:**
  - After selecting option `1`, you will see a list of existing students.
  - Enter the name of the student you want to view.
  - You have the option to Input, View, Rename, and Delete Student records.
  # ![Main Features](documentation/student-management-portal.png)
  - Indicators:
There are currently two indicators (Health and Education) that are used to store and measure student progress.

- **Create a New Student:**
  - After selecting option `2`, enter the name of the new student.
  - Follow the prompts to input health and education progress indicators.

- **View Instructions:**
  - After selecting option `3`, instructions will be displayed on how to use the application effectively.

- **Progress Entry:**
  - When entering progress indicators, input values between 0 and 10.
  - For health and education, the app will visualize the progress with bar charts.

- **Viewing Student Summary:**
  - After entering progress indicators, choose to view the student's overall progress.
  - The app will display the average health and education scores, along with visual representations.
  - Progress Report: View comprehensive summaries of student progress, including averages and visualizations.

![result](documentation/student-progress.png)

- **Restart or Exit:**
  - After completing any operation, press `Enter` to restart the program.
  - Type 'exit' to terminate the application.

## Testing
Rigorous manual testing was performed to ensure the app's functionality, including user inputs, menu navigation, and data entry.

### Input Validation Testing: 
<details><summary>Menu Selection</summary>
- Enter a number other than 1, 2, 3

<img src="documentation/enter-wrong-number.png">

- Enter a string or other characters

<img src="documentation/enter-string.png">-

</details>
<details><summary>Select a student</summary>
- Anything other than the sudent record in the database

<img src="documentation/no-student-record.png">
</details>

<details><summary>Create New Student</summary>
Student creation comes with multiple validations:
- Name cannot be empty
- Name cannot start with a space
- Name must start with at least 2 letters
- Name can include at least one dot '.'
- Name can not be more than 30 Characters

<img src="documentation/student-creation-validation.png">
<img src="documentation/student-creation-validation-2.png">
</details>

### Manual Testing: 
| Feature | Key Action | Expected Result | Tested | Passed | Comments |
| --- | --- | --- | --- | --- | --- |
| *Main Menu Option 1* |  |  |  |  |  |
|Welcome|Enter 1|Select existing students|Yes|Yes|
|Welcome to Student Portal |Enter Student Name|Menu Options for student|Yes|Yes|
|Input New Record|Enter 1|Welcome to Student's Care Progress|Yes|Yes| |
|Enter Health Progress Value |Enter 0 - 10 value|Opens Education input |Yes|Yes| |
|Enter Education Progress Value |Enter 0 - 10 value|Accepts values and upload |Yes|Yes| |
|View Student Overall Progress|Enter 2|Student progress Displayed successfully|Yes|Yes|
|Rename Student Name |Enter 3 > Enter New name| Name successfully renamed|Yes|Yes|
|Delete Student Name & Record|Enter 4 > Confirm Y or N |Type Student's Name > Successfully delete|Yes|Yes|
| *Main Menu Option 2* |  |  |  |  |
|Create a new student|Enter 2|Input prompt > New student name created.|Yes|Yes|
| *Main Menu Option 3* |  |  |  |  |
|View program instructions|Enter 3|Programme Instruction displayed|Yes|Yes|
|Return to Main menu|Enter 'm' or any key| Return to main menu|Yes|Yes|
|Exit|Enter 'exit' from any input box|The application exits|Yes|Yes|
|     |     |     |     |     |   

## Bugs:
| Issue|Solution |
|-|-|
| Warning error received: /Users/dcsn/care-plus/run.py:385: DeprecationWarning: Worksheet.delete_row() is deprecated, Please use `Worksheet.delete_rows()` instead|I replaced the code with `worksheet.delete_row(row)` instead |

### CI Python Linter:
The CI Python Linter https://pep8ci.herokuapp.com/ was used to test for errors in the code. No errors were found except for warning concerning white spaces or characters being longer than the 79 characters that was originally designed for the application

![CI Python Test](documentation/ci-python-test.png)

## Lucid:
Lucid was used to draw mock-ups for the initial app design to guide the development of this project.

![Lucid Sketch](documentation/flow-chart-simple.png)

## Technologies used:
- [Python](https://python.org) is the main technology used in this application
- [Lucid](https://lucid.com) was used to create workflows for guidance in building the application
- [VScode](https://vscode.com/) was used to write and edit the codes and host the site on my local  computer
- [Git](https://github.com) was used for the version control of the application
- [Heroku](https://heroku.com) was used to host the deployed application
- [ChatGPT](https://chat.openai.com/) was often consulted regarding the usage and construction of codes
- Google Chrome's [Screenshot & Screen Recorder](https://chrome.google.com/webstore/detail/screenshot-screen-recorde/okkffdhbfplmbjblhgapnchjinanmnij) plugin was used to create the site logo
- [Code Institute Python Linter](https://pep8ci.herokuapp.com/) was used to check code for any issues

## Deployment

The template for this app was generated from Code-Institute-Org/p3-template. The repository was cloned on a local VSCode machine and then stored/managed on GitHub. 

The Heroku git URl is https://git.heroku.com/care-plus.git

The app was then deployed on Heroku via Github:

1. Heroku Account Setup:

    Log in to your existing Heroku account or create a new account.

2. Create a New App:

    On the Heroku dashboard, click "New" and select "Create new app."

3. Configure Your App:

    Choose a unique app name and select your preferred region.
    Click "Create app" to initiate the app creation process.

4. Environment Configuration:

    In the app dashboard, find the "Settings" tab and locate "Config Vars."
    Click "Reveal Config Vars" and add a new variable with the key "PORT" and the value "8000." Click "Add" to save.

5. Set Up Buildpacks:

    Scroll down to the "Buildpack" section in the settings.
    Click "Add," select "Python," and add it. Ensure that "Python" is listed first.
    Repeat the process, this time adding "Node.js" as a buildpack.

6. Deploy Your App:

    Navigate to the "Deploy" tab at the top of the dashboard.
    Choose GitHub as your deployment method and link your repository to the app.

7. Automatic or Manual Deployment:

    Scroll down to the deployment section.
    Choose either "Enable Automatic Deploys" for continuous integration or "Manual Deploy" for manual control.

Deployed site -> [Here](https://care-plus-e6b7c675e391.herokuapp.com/)


### Local Deployment:
To clone this project, you can do so using VsCode or any code editor that has an integrated development Environment (IDE), using this command: 

1. Clone the repository: `git clone https://github.com/your-username/care-plus-app.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Add your Google Sheets credentials to `creds.json` -  [Created from Google Cloud Console](https://console.cloud.google.com/)
4. Run the application: `python app.py`

     git clone https://github.com/dcsndevs/care-plus.git 


## Dependencies

- [gspread](https://gspread.readthedocs.io/en/latest/)
To instal this use: `pip3 install gspread`
- [oauth2client](https://oauth2client.readthedocs.io/en/latest/)
To instal this use: `pip3 install google-auth`

## Usage

Follow the on-screen prompts to navigate through the application. Input valid data as guided by the application.

## Future Development and Limitations
More functionalities would be handy in this application. Extra functionality to include, manually determining the period of time that a student's overall progress should be populated. It would also go further to include exporting this information to a local machine or sending it to a user provided email address.


## Credits

### Code Institute:
Special thanks to Code Institute for providing the template used in this project. The template served as a valuable foundation, streamlining the development process and contributing to the overall project structure and theref after deployment.

### Google:
The Care Plus App relies on Google Cloud services, including the Google Sheets API, for efficient data management. I extend my gratitude to Google Cloud for providing a free, robust and reliable cloud solutions that contribute to the functionality of this application.

### API: 
Also to the team that created the Gspread and its documentation, and to Google Drive and Google Sheets API. The Care Plus App utilizes the gspread library to interact with the Google Sheets API for efficient data management. We appreciate the developers of gspread for providing a convenient and Pythonic way to work with Google Sheets.

### Code Reference:
[W3schools](https://w3schools.com/) was instrumental to the success of this project. It was often used to learn quick features or to compare and see where errors are.

### CarePlus Logic: 
The logic behind the application is a real life application called [©WellTree] (https://www.welltree.info/)
WellTree inputs are manually done on an excel worksheet, but this application was built with the intention of automating the inputs and view student progress over time.

### Acknowledgments:
I like to thank [Juliia Konn](https://github.com/IuliiaKonovalova/), my mentor at Code Institute. She exemplifies her mentorship with a knack for high-quality projects. Her desire for quality has always challenged me to do better in my work. I remain grateful to her.

I also like to thank my loving wife for her continuous support. She's a source of strength as always.