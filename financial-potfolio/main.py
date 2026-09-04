from admin import Admin
from user import Users
from database import connection, cursor

def main_menu():
    print("\n===================================================================================")
    print("                    FINANCIAL PORTFOLIO MANAGEMENT SYSTEM  📈🏦                      ")
    print("=====================================================================================")
    print("\n1. Admin Login")
    print("2. User Login")
    print("3. User Registration")
    print("4. Exit\n")


def admin_login():

    admin_username="admin"
    admin_password=1234

    print("\n=====================================================================")
    print("                         Admin Login System 🧑‍💻                         ")
    print("=====================================================================\n")

    username = input("Enter your username: ").strip().lower()
    password = int(input("Enter your password: "))

    if username == admin_username and password == admin_password:
        print("\n✅ Successfully logged in. 🔑 Access granted.\n")
        admin1=Admin()
        admin1.admin_run()

    else:
        print("\nIncorrect username or password ❌. Please try again.")

def user_login():
    try:
        print("\n===================================================================")
        print("                     User Registration Panel 🧑‍💻🔒                   ")
        print("===================================================================\n")

        username = input("Enter your username: ").strip().lower()
        password=input("Enter your password: ").strip()

        cursor.execute("SELECT * FROM users")
        for i in cursor:
            if i[0]==username and i[4]==password:
                print("\n✅ Successfully logged in. 🔑 Access granted.")
                user=Users(username)
                user.user_run()
                break

            elif i[0]==username and i[4]!=password:
                print("\n⚠️ Invalid Password. Please try again. 🔒")
                break

        else:
            print("\nAccount Not Found 🚫")

    except ValueError:
        print("\nEnter Valid Input ❌🔄")

    except sqlite3.OperationalError:
        print("\n ⚠️ An Database Error Occurred ❌ . Try Again later")


def user_register():
    try:
        print("\n=======================================================================")
        print("                      User Registration Panel 🧑‍💻🔒                      ")
        print("=======================================================================\n")

        username = input("Please enter your username: ").strip().lower()
        name=input("Please enter your name: ").strip()

        if username=="" or name=="":
            print("Error ❌ : All Fields Required.")
            return

        age=int(input("Please enter your age: "))

        if age<13 or age>100:
            print("🛑 You are not eligible for registration. Please try again. ❌")
            return

        email=input("Please enter your email: ").strip().lower()

        if email=="":
            print("Error ❌ : Email Field Required.")
            return

        password = input("Please enter your password: ").strip()

        if len(password)<4:
            print("🔑 Minimum Length is 4 Digit password! 🔒")
            return

        balance=int(input("Please enter your balance: "))

        if balance<500:
            print("💰 Minimum Balance is 500! 🛑")
            return

        cursor.execute("SELECT * FROM users")
        for i in cursor:
            if i[0]==username:
                print("Username Already Existed")
                return

            if i[3]==email:
                print("Email Already Existed")
                return

        cursor.execute('''
        INSERT INTO users (user_name, name, age, email, password,balance)
        VALUES (?,?,?,?,?,?)''',(username,name,age,email,password,balance))
        connection.commit()

        print("\n✅ Registered successfully ! You can now log in.")

    except ValueError:
        print("\nEnter Valid Input ❌🔄")

    # except sqlite3.OperationalError as e:
    #     print(f"\n ⚠️ Database Error Details: {e}")

    except sqlite3.OperationalError:
        print("\n ⚠️ An Database Error Occurred ❌ . Try Again later")


def main_run():
    while True:
        try:
            main_menu()
            choice = int(input("Enter your choice : "))

            if choice>4 or choice<=0:
                print("Invalid Choice ❌ Choose from 1-4")
                continue

            elif choice==1:
                admin_login()

            elif choice==2:
                user_login()

            elif choice==3:
                user_register()

            elif choice==4:
                print("\n Thanks For Visiting Our Portfolio Management System 🥰🫶")
                break

        except ValueError:
            print("\nEnter Valid Choice 👊")

main_run()
