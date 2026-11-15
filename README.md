Leave Management System
Python and SQLite Database Project
1. Project Overview
The Leave Management System is a console-based application developed using Python and SQLite. It is designed to simplify employee leave management by allowing administrators to manage employee records and leave requests, while employees can submit leave applications and check their leave status.
The application uses SQLite for storing employee information and leave request records.
2. Project Requirements
Software Requirements
•	Python 3.x
•	SQLite3 database
•	Visual Studio Code / PyCharm / Python IDLE
•	Windows, Linux or macOS
Python Modules Used
•	sqlite3 – Database connectivity and database operations.
•	getpass – Secure password input.
•	input() – Accepting user input.
•	Exception handling – Managing invalid inputs and database errors.
No external Python packages are required.
3. Functional Requirements
Admin Module
1.	Admin login authentication.
2.	Add new employees.
3.	View all employee records.
4.	Search employees using Employee ID.
5.	Edit employee information.
6.	Delete employee records.
7.	View all employee leave requests.
8.	Approve leave requests.
9.	Reject leave requests.
Employee Module
1.	Employee access to the system.
2.	Apply for leave.
3.	Provide leave reasons.
4.	View personal leave requests.
5.	Check leave approval status.
4. Database Schema
The application uses an SQLite database named LeaveManagement.db.
It contains two primary tables.
Table 1: user
Stores employee information.
Column	Data Type	Description
ID	INTEGER	Primary Key
Name	VARCHAR(20)	Employee name
Designation	TEXT	Employee designation
Department	TEXT	Employee department
Table 2: Leave_Request
Stores employee leave application details.
Column	Data Type	Description
ID	INTEGER	Primary Key, Auto Increment
Name	TEXT	Employee name
Reason	TEXT	Reason for leave
status	TEXT	Pending / Approved / Rejected
user_id	INTEGER	Employee reference ID
Relationship: The user_id column identifies the employee associated with a leave request. The intended relationship is one-to-many: one employee can submit multiple leave requests.
Note: The original database code does not yet enforce this relationship through a foreign key constraint. Add the foreign key definition and migrate the existing table if you want database-level enforcement.
5. Application Workflow
Admin Workflow
1.	Launch the application.
2.	Select Admin Login.
3.	Enter administrator credentials.
4.	Access the Admin Menu.
5.	Select the required employee or leave management operation.
6.	View, update or manage records.
Employee Workflow
1.	Launch the application.
2.	Select Employee.
3.	Enter Employee ID when prompted.
4.	Select Apply for Leave.
5.	Enter the employee name and reason.
6.	Submit the leave request.
7.	View the leave status.
6. How to Run the Project
Step 1: Install Python
Download Python from:
https://www.python.org/downloads/
Verify installation:
python --version
Step 2: Open the project folder
Open the project folder using Visual Studio Code or your preferred Python editor.
Step 3: Run the application
Open the terminal and execute:
python main.py
Step 4: Login
The application displays three options:
[Login]

1. Admin
2. Employee
3. Exit
For administrator access, the current sample credentials are:
Username: admin
Password: admin123
Step 5: Use the application
Select the appropriate menu options to manage employee details and leave requests.
7. Error Handling and Database Management
The application uses Python exception handling to manage errors.
Examples include:
•	Invalid employee ID.
•	Duplicate employee records.
•	Invalid menu selections.
•	Database constraint violations.
•	Missing employee records.
SQLite transaction management uses commit() to save changes and rollback() to reverse uncommitted changes after database errors.
8. Screenshots
Add screenshots demonstrating the following operations:
Screenshot	Description
Screenshot 1	Application Login Screen
Screenshot 2	Admin Menu
Screenshot 3	Add Employee
Screenshot 4	View Employee Records
Screenshot 5	Employee Menu
Screenshot 6	Apply for Leave
Screenshot 7	View Leave Status
Screenshot 8	Admin Approving Leave
Screenshot 9	Admin Rejecting Leave
Screenshot 10	Delete Employee
Save screenshots in the screenshots folder.
9. Testing
The following test cases can be used to verify the application.
Test Case	Expected Result
Add employee with valid details	Employee added
Add duplicate Employee ID	Error message displayed
Search existing employee	Employee details displayed
Search invalid Employee ID	Employee not found
Submit valid leave request	Leave request submitted
Approve leave request	Status changes to Approved
Reject leave request	Status changes to Rejected
View employee leave requests	Relevant records displayed
Delete employee	Employee record deleted
10. GitHub Version Control
GitHub can be used to store and manage the project source code.
Steps to upload the project
1.	Create a GitHub account.
2.	Create a new repository named LeaveManagementSystem.
3.	Open the project folder in VS Code.
4.	Open the terminal.
5.	Execute the following commands:
git init

git add main.py README.md screenshots/

git commit -m "Initial Leave Management System project"

git branch -M main

git remote add origin YOUR_GITHUB_REPOSITORY_URL

git push -u origin main
Replace YOUR_GITHUB_REPOSITORY_URL with your actual GitHub repository URL.
Do not upload passwords, sensitive employee information or a database containing real employee records.
11. Project Submission
The final submission should include:
•	Python source code (main.py).
•	Project documentation (README.md).
•	Database schema documentation.
•	Application screenshots.
•	Short project demonstration video (optional if README is accepted).
•	GitHub repository link.
GitHub Repository
Repository URL: https://github.com/pripay94/PythonMiniProject 
12. Conclusion
The Leave Management System provides a simple and structured approach to managing employee information and leave requests. It demonstrates the practical implementation of Python programming, SQLite database connectivity, CRUD operations, exception handling and basic authentication.
The project can be further enhanced with additional features such as leave balance calculation, date-based leave applications, role-based authentication and reporting.

