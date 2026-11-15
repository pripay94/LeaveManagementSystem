import sqlite3
from getpass import getpass

# ------------------ DB Setup ------------------
conn = sqlite3.connect('LeaveManagement.db')
conn.execute("PRAGMA foreign_keys = ON") 

cursor = conn.cursor()

# user
cursor.execute('''
        CREATE TABLE IF NOT EXISTS user (
                ID INTEGER PRIMARY KEY UNIQUE,
                Name VARCHAR(20) NOT NULL,
                Designation TEXT NOT NULL,
                Department TEXT NOT NULL)


''')

# Leave Request Table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Leave_Request (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT NOT NULL,
        Reason TEXT NOT NULL,
        status TEXT DEFAULT 'Pending',
        user_id INTEGER)
''')


conn.commit()
conn.close()

# ----------------- Employee Function -----------------

# Apply Leave 
def apply_for_leave(emp_id, name, reason):
    conn = sqlite3.connect("LeaveManagement.db")
    cursor = conn.cursor()

    
    cursor.execute("SELECT * FROM user WHERE ID = ?", (emp_id,))
    employee = cursor.fetchone()

    if not employee:
        print("Employee ID does not exist.")
    else:
        cursor.execute('''
            INSERT INTO Leave_Request (user_id, Name, Reason) 
            VALUES (?, ?, ?)
        ''', (emp_id, name, reason))
        conn.commit()
        print("Leave request submitted.")

    conn.close()

# View Leave
def view_own_leave(emp_id):
    conn = sqlite3.connect('LeaveManagement.db')
    cursor = conn.cursor()
    cursor.execute("SELECT ID, Name, Reason, status FROM Leave_Request WHERE user_id = ?", (emp_id,))
    leaves = cursor.fetchall()
    if not leaves:
        print("No leave requests found.")
    else:
        for leave in leaves:
            print(f"Leave ID - {leave[0]} | Name - {leave[1]} | Reason - {leave[2]} | Status - {leave[3]}")
    conn.close()


# ----------------- Admin Function -----------------
# Add Employee   
def emp_details():
    conn =sqlite3.connect('LeaveManagement.db')
    cursor = conn.cursor()
    
    try:
        Employee_id= input('Enter ID:-')
        Employee_name = input('Enter your Name:-')
        Employee_design = input('Enter your Designation(Associate/Analyst/Sr. Analyst/Specialist):-')
        Employee_deprt = input('Enter your Department(HR/Finance/Operations/Marketing):-')

        cursor.execute('''
            INSERT INTO user (ID,Name,Designation,Department)
                  values(?,?,?,?)
            ''',(Employee_id,Employee_name,Employee_design,Employee_deprt ))
        print('Employee Added')
    
    except ValueError:
        print("Invalid ID. Please enter a numeric value.")
    except sqlite3.IntegrityError:
        print("Employee ID already exists.")
    
    
    conn.commit()
    conn.close()
    
# View Employee 

def emp_view():
    conn = sqlite3.connect('LeaveManagement.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT * FROM user
    ''')
    
    LeaveManagement =cursor.fetchall()

    if not LeaveManagement:
        print('No Employee Found')
    else:
        print(f'{len(LeaveManagement)} Employee Found!!!')
        for user in LeaveManagement:
            print(f'ID - {user[0]} | Name - {user[1]} | Designation - {user[2]} | Department - {user[3]}')

    conn.commit()
    conn.close()

# Search Employee 

def emp_search():
    conn = sqlite3.connect('LeaveManagement.db')
    cursor = conn.cursor()
    
    ID = input('Enter Employee ID:-')
    
    
    cursor.execute('''
        SELECT * FROM user WHERE ID = ? 
        ''',(ID,))
    
    LeaveManagement =cursor.fetchall()
    
    if not LeaveManagement:
        print('No Employee Found')
    else:
        print('Employee Found!!!')
        for user in LeaveManagement:
            print(f'ID - {user[0]} | Name - {user[1]} | Department - {user[2]} | Designation - {user[3]}')

    
    conn.commit()
    conn.close()

# Edit Employee 
    
def emp_edit():
    conn = sqlite3.connect('LeaveManagement.db')
    cursor = conn.cursor()
    
    
    ID = int(input('Enter Employee ID: '))
        
    cursor.execute('SELECT * FROM user WHERE ID = ?', (ID,))
    LeaveManagement = cursor.fetchone()

    if not LeaveManagement:
            print("No employee found with this ID.")
            return

    Name = input('Enter your Name:-')
    Designation = input('Enter your Designation(Associate/Analyst/Sr. Analyst/Specialist):-')
    Department = input('Enter your Department(HR/Finance/Operations/Marketing):-')
    
    cursor.execute('''
            Update user SET Name = ?, Designation = ? ,Department = ? where ID = ?
                   ''',(Name,Designation,Department,ID))
    
    
    
    print(f"Employee with ID {ID} updated successfully.")
    
    conn.commit()
    conn.close()
    


#Delete Employee 

def emp_del():
    conn = sqlite3.connect('LeaveManagement.db')
    conn.execute("PRAGMA foreign_keys = ON")
    cursor = conn.cursor()

    try:
        ID = int(input('Enter Employee ID: '))

        cursor.execute(
            'SELECT * FROM user WHERE ID = ?', (ID,)
        )
        employee = cursor.fetchone()

        if not employee:
            print("No employee found with this ID.")
            return

        # Delete employee's leave records
        cursor.execute(
            'DELETE FROM Leave_Request WHERE user_id = ?',
            (ID,)
        )

        #Delete employee
        cursor.execute(
            'DELETE FROM user WHERE ID = ?',
            (ID,)
        )

        conn.commit()

        print(f"Employee with ID {ID} and related leave records deleted successfully.")

    except ValueError:
        print("Invalid input. Please enter a numeric ID.")

    except sqlite3.Error as e:
        conn.rollback()
        print("Database error:", e)

    finally:
        conn.close()


#View Leave

def view_leave():
    
    conn = sqlite3.connect('LeaveManagement.db')
    cursor = conn.cursor()
    
    cursor.execute('''
            select * from Leave_Request      
                   ''') 
    
    LeaveManagement =cursor.fetchall()

    if not LeaveManagement:
        print('No Leave Record Found')
    else:
        print(f'{len(LeaveManagement)} Leave Request Found!!!')
        for Leave_Request in LeaveManagement:
            print(f'ID - {Leave_Request[0]} | Name - {Leave_Request[2]} | Reason - {Leave_Request[3]} | Status - {Leave_Request[4]}')
   
    
    conn.commit()
    conn.close()
    
# Approve Leave 
  
def approve_leave():
    conn = sqlite3.connect('LeaveManagement.db')
    cursor = conn.cursor()
    
    try:
        ID = int(input("Enter Leave Request ID to approve: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        conn.close()
        return

    # To check if leave request exists
    cursor.execute("SELECT * FROM Leave_Request WHERE ID = ?", (ID,))
    leave = cursor.fetchone()

    if not leave:
        print("Invalid Leave Request ID.")
    else:
        cursor.execute("UPDATE Leave_Request SET status = 'Approved' WHERE ID = ?", (ID,))
        conn.commit()
        print(f"Leave Request {ID} Approved.")

    conn.commit()
    conn.close()

# Reject Leave

def reject_leave():
    conn = sqlite3.connect('LeaveManagement.db')
    cursor = conn.cursor()
    
    
    try:
        ID = int(input("Enter Leave Request ID to Reject: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        conn.close()
        return
    
    # To check if leave request exists
    cursor.execute("SELECT * FROM Leave_Request WHERE ID = ?", (ID,))
    leave = cursor.fetchone()
    
    if not leave:
        print("Invalid Leave Request ID.")
    else:
        cursor.execute("UPDATE Leave_Request SET status = 'Rejected' WHERE ID = ?", (ID,))
        conn.commit()
        print(f"Leave Request {ID} Rejected.")
        
    conn.commit()
    conn.close()

# ------------------ Admin Menu  ------------------
def admin_menu():
    while True:
        print("\nADMIN MENU")
        print('1.Add Employee')
        print('2.View Employee')
        print('3.Search Employee')
        print('4.Edit Employee')
        print('5.Delete Employee')
        print('6.View Leave')
        print('7.Approve Leave')
        print('8.Reject Leave')
        print('9.Exit')
        
        try:
            Select = int(input('Please choose Option: '))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if Select == 1:
            emp_details()
        elif Select == 2:  
            emp_view()
        elif Select == 3:
            emp_search()
        elif Select == 4:
            emp_edit()
        elif Select == 5:
            emp_del()
        elif Select == 6:
            view_leave()
        elif Select == 7:
            approve_leave()
        elif Select == 8:
            reject_leave()
        elif Select == 9:
            print("Exiting ADMIN Menu...")
            break
        else:
            print("Invalid option. Please select a number between 1 and 9.")
            break


# ------------------ Employee Menu  ------------------

def employee_menu():
    while True:
        print("1. Apply for Leave")
        print("2. View Leave Status")
        print("3. Exit")

        try:
            choice = int(input('Please choose Option: '))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            emp_id = int(input("Enter your Employee ID: "))
            name = input("Enter your name: ")
            reason = input("Enter reason for leave: ")
            apply_for_leave(emp_id, name, reason)
            
        elif choice == 2:
            emp_id = int(input("Enter your Employee ID: "))
            view_own_leave(emp_id)
            
        elif choice == 3:
            print("Exiting Employee Menu...")
            break
        else:
            print("Invalid option. Please choose 1 to 3.")



# *********************LOGIN**********************

def login():
    while True:
        print('[Login]')
        
        print('1.Admin')
        print('2.Employee')
        print('3.Exit')
        
        choice = int(input('Please choose Option: '))
        
        if choice ==1:
            username = input("Username: ")
            password = getpass("Password: ")
            if username == "admin" and password == "admin123":
                admin_menu()
            else:
                print("Invalid credentials")
        elif choice ==2:
            employee_menu()
            
        elif choice == 3:
            print("Exiting Leave Management System...")
            break
        else:
            print("Invalid option")
    
login()






    