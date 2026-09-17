import sqlite3
conn = sqlite3.connect('school.db')
cursor = conn.cursor()

#TABLE CREATION CODE

# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS students (
#         student_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         student_name TEXT NOT NULL,
#         age INTEGER NOT NULL,
#         grade INTEGER NOT NULL
#     )
# ''')

# conn.commit()

def menu():
    print("\n======================================================")
    print("               Student Management System              ")
    print("======================================================\n")
    print("1. Add Student")
    print("2. View Student")
    print("3. View Passing Student")
    print("4. Show Average Grade")
    print("5. Search Student")
    print("6. Delete Student")
    print("7. Exit\n")

def add_student():
    try:
        print("\n-------- Fill this Details --------\n")
        name=input("Enter your name: ")
        age=int(input("Enter your age: "))
        if age<13:
            print("Minimum age is 13 years old")
            return

        marks=int(input("Enter your marks: "))
        if marks<0:
            print("Minimum marks is 0")
            return

        cursor.execute(''' INSERT INTO  students (student_name,age,grade)
        VALUES (?,?,?)
        ''',( name,age,marks))

        conn.commit()

        print("\n SuccessFully Added Student Details in Our Database")

    except sqlite3.OperationalError as e:
        print(e)

def view_student():
    try:
        print("================   All Students ================")
        cursor.execute(''' SELECT * FROM students''')
        for row in cursor.fetchall():
            print(f"\n----------  {row[1]} details  ----------\n")
            print(f"Student ID     : {row[0]}")
            print(f"Student Name   : {row[1]}")
            print(f"Student Age    : {row[2]}")
            print(f"Student Mark   : {row[3]}")

    except sqlite3.OperationalError as e:
        print(e)

def view_passing_student():
    try:
        print("================   All Passing Students ===============")
        cursor.execute(''' SELECT * FROM students WHERE grade>=40''')
        for row in cursor.fetchall():
            print(f"\n----------  {row[1]} details  ----------\n")
            print(f"Student ID     : {row[0]}")
            print(f"Student Name   : {row[1]}")
            print(f"Student Age    : {row[2]}")
            print(f"Student Mark   : {row[3]}")
            print("Student Status  : Passed ✅")

    except sqlite3.OperationalError as e:
        print(e)

def show_average_grade():
    try:
        cursor.execute(''' SELECT AVG(grade) FROM students''')
        row=cursor.fetchone()
        average=row[0]

        if average is not None:
            print(f"\nAverage Grade: {average} 📊")
        else:
            print("No Student Data Found")

    except sqlite3.OperationalError as e:
        print(e)
def search_student():
    try:
        student_id=int(input("\nEnter student ID: "))
        cursor.execute(''' SELECT * FROM students WHERE student_id=?''', (student_id,))
        row=cursor.fetchone()

        if row is not None:
            print(f"\n----------  {row[1]} details  ----------\n")
            print(f"Student ID     : {row[0]}")
            print(f"Student Name   : {row[1]}")
            print(f"Student Age    : {row[2]}")
            print(f"Student Mark   : {row[3]}")

        else:
            print("\nNo Student Data Found")

    except sqlite3.OperationalError as e:
        print(e)

def delete_student():
    try:
        student_id=int(input("\nEnter student ID: "))
        cursor.execute("""DELETE FROM students WHERE student_id=?""", (student_id,))
        print("\n Successfully Deleted Student From Database")

        conn.commit()

    except sqlite3.OperationalError as e:
        print(e)

def run():
    while True:
        try:
            menu()
            option=int(input("Enter your choice: "))

            if option>7 or option<0:
                print("Invalid Choice !!! ")
                continue

            if option==1:
                add_student()

            elif option==2:
                view_student()

            elif option==3:
                view_passing_student()

            elif option==4:
                show_average_grade()

            elif option==5:
                search_student()

            elif option==6:
                delete_student()

            elif option==7:
                print("\nThanks For Visiting Student Management System")
                conn.close()
                break

        except ValueError as e:
            print(e)

run()
