from database import connection, cursor

class Admin:
    def admin_menu(self):
        print("\n=====================================================================")
        print("                         Admin Panel 🔒⚙️🧑‍💻                         ")
        print("=====================================================================")
        print("\n1. Add Investment")
        print("2. View Investments")
        print("3. Search Investment")
        print("4. Update Investment")
        print("5. Delete Investment")
        print("6. View Users")
        print("7. View Transactions")
        print("8. Logout\n")

    def add_investment(self):
        try:
            print("\n====================================================================")
            print("                    ✨📋 𝔽𝕚𝕝𝕝 𝕋𝕙𝕚𝕤 𝔻𝕖𝕥𝕒𝕚𝕝𝕤 📋✨                    ")
            print("====================================================================\n")


            investment_id=int(input("Enter your Investment ID : "))
            cursor.execute('''Select * from investment where investment_id = ?
            ''',(investment_id,))

            inv_id = cursor.fetchone()

            if inv_id :
                print("\n🚫🔄 Investment ID  Already Exists ❌")
                return

            company_name=input("Enter your Company Name : ").strip().upper()

            cursor.execute('''Select * from investment where company_name = ?
            ''',(company_name,))

            inv_id = cursor.fetchone()

            if inv_id :
                print("\n🚫🔄 Company Name  Already Exists ❌")
                return

            investment_type=input("Enter your Investment Type : ").strip()
            price=int(input("Enter your Investment Price : "))

            if price<500:
                print("🛑 Minimum Amount is 500 💰")
                return

            quantity=int(input("Enter your Investment Quantity : "))
            if quantity<1:
                print("🛑 Minimum Quantity is 1 ")
                return

            cursor.execute('''INSERT INTO investment (investment_id, company_name, type, price, quantity)
            VALUES (?,?,?,?,?)
            ''',(investment_id,company_name,investment_type,price,quantity))

            connection.commit()

            print("\n🎉📈 Successfully Added Investment! 💰✨")

        except ValueError:
            print("\nEnter Valid Input ❌🔄")

        except sqlite3.Error:
            print("\n⚠️ Something went wrong. Please try again.")

    def view_investments(self):
        try:
            print("\n=============================================================")
            print("                    📊💼 All Investments")
            print("=============================================================\n")

            cursor.execute('''SELECT * FROM investment''')

            investments = cursor.fetchall()

            if not investments:
                print("\nNo Investments Found 🚫")
                return

            for i in investments:
                print(f"\n------------- {i[1]} Investment -------------")
                print(f"Investment ID       : {i[0]}")
                print(f"Company Name        : {i[1]}")
                print(f"Investment Type     : {i[2]}")
                print(f"Investment Price    : {i[3]}")
                print(f"Investment Quantity : {i[4]}")

        except sqlite3.OperationalError:
            print("\n⚠️ A Database Error Occurred ❌. Try Again Later.")

    def search_investment(self):
        try:
            print("\n-----------------  Search Investment  ----------------------\n")
            inv_id=int(input("Enter your Investment ID : "))
            cursor.execute('''Select * from investment where investment_id = ?''',(inv_id,))

            investment=cursor.fetchone()
            if not investment:
                print("\nNo Investments Found 🚫")
                return

            print(f"\n---------------  {investment[1]} Investment  ---------------")
            print(f"Investment ID         : {investment[0]}")
            print(f"Company Name          : {investment[1]}")
            print(f"Investment Type       : {investment[2]}")
            print(f"Investment Price      : {investment[3]}")
            print(f"Investment Quantity   : {investment[4]}")

        except ValueError:
            print("\nEnter a valid choice ❌🔄")

        except sqlite3.Error:
            print("\n⚠️ Something went wrong. Please try again.")

    def update_investment(self):
        try:
            print("\n-------------------  Update Investment  ---------------------")

            inv_id = int(input("\nEnter your Investment ID : "))

            cursor.execute('''
                SELECT * FROM investment
                WHERE investment_id = ?
            ''', (inv_id,))

            investment = cursor.fetchone()

            if not investment:
                print("\nNo Investments Found 🚫")
                return

            print(f"\nCompany Name     : {investment[1]}")
            print(f"Current Price    : ₹{investment[3]}")
            print(f"Available Quantity : {investment[4]}")

            new_price = int(input("\nEnter your New Investment Price : "))

            if new_price < 500:
                print("\nMinimum Price is ₹500 💰")
                return

            cursor.execute('''
                UPDATE investment
                SET price = ?
                WHERE investment_id = ?
            ''', (new_price, inv_id))

            connection.commit()

            cursor.execute('''
                SELECT * FROM investment
                WHERE investment_id = ?
            ''', (inv_id,))

            investment = cursor.fetchone()

            print(f"\n------------- {investment[1]} Investment -------------")
            print(f"Investment ID       : {investment[0]}")
            print(f"Company Name        : {investment[1]}")
            print(f"Investment Type     : {investment[2]}")
            print(f"Updated Price       : ₹{investment[3]}")
            print(f"Available Quantity  : {investment[4]}")

            print("\nUpdated Successfully 🆙✅")

        except ValueError:
            print("\nEnter a valid input ❌🔄")

        except sqlite3.Error:
            print("\n⚠️ A Database Error Occurred ❌. Please Try Again Later.")

    def delete_investment(self):
        try:
            print("\n-----------------  Delete Investment  ---------------------\n")

            inv_id = int(input("Enter your Investment ID : "))

            cursor.execute('''
                SELECT * FROM investment
                WHERE investment_id = ?
            ''', (inv_id,))

            investment = cursor.fetchone()

            if not investment:
                print("\nNo Investments Found 🚫")
                return

            cursor.execute('''
                SELECT * FROM portfolio
                WHERE investment_id = ?
            ''', (inv_id,))

            portfolio = cursor.fetchone()

            if portfolio:
                print("\n❌ Cannot Delete This Investment")
                print("Users still own this investment. 🚫📊")
                return

            cursor.execute('''
                DELETE FROM investment
                WHERE investment_id = ?
            ''', (inv_id,))

            connection.commit()

            print("\n🗑️ Successfully Deleted Investment From Database ✅")

        except ValueError:
            print("\nEnter a valid Investment ID ❌🔄")

        except sqlite3.Error:
            print("\n⚠️ Something went wrong. Please try again.")

    def view_users(self):
        try:
            print("\n===============================================================")
            print("                    👥 All Users 👥                           ")
            print("===============================================================")

            cursor.execute('''Select * from users''')
            users=cursor.fetchall()

            if not users:
                print("🔍 No User Data Found 🚫")
                return

            for i in users:
                print(f"\n-------------  {i[1]} Details   ----------------")
                print(f"\nUsername    :  {i[0]}")
                print(f"Name        :  {i[1]}")
                print(f"Age         :  {i[2]}")
                print(f"Email       :  {i[3]}")

        except sqlite3.OperationalError:
            print("\n⚠️ A Database Error Occurred ❌. Try Again Later.")

    def view_transactions(self):
        try:
            print("\n====================================================================")
            print("                      📜 All Transactions                          ")
            print("====================================================================\n")

            cursor.execute('''
                SELECT
                    transactions.transaction_id,
                    transactions.user_name,
                    investment.company_name,
                    transactions.transaction_type,
                    transactions.quantity,
                    transactions.price,
                    transactions.total_amount,
                    transactions.transaction_date
                FROM transactions
                JOIN investment
                ON transactions.investment_id = investment.investment_id
                ORDER BY transactions.transaction_id DESC
            ''')

            transactions = cursor.fetchall()

            if not transactions:
                print("No Transactions Found 🚫")
                return

            for transaction in transactions:
                print("------------------------------------------------------------")
                print(f"Transaction ID   : {transaction[0]}")
                print(f"Username         : {transaction[1]}")
                print(f"Company Name     : {transaction[2]}")
                print(f"Transaction Type : {transaction[3]}")
                print(f"Quantity         : {transaction[4]}")
                print(f"Price            : ₹{transaction[5]}")
                print(f"Total Amount     : ₹{transaction[6]}")
                print(f"Date             : {transaction[7]}")
                print("------------------------------------------------------------")

        except sqlite3.Error:
            print("\n⚠️ Unable to load transactions. Please try again later.")

    def admin_run(self):
        while True:
            try:
                self.admin_menu()
                choice = int(input("Enter your choice : "))

                if choice > 8 or choice <= 0:
                    print("\nInvalid choice ❌ Choose From 1-8")
                    continue

                elif choice == 1:
                    self.add_investment()

                elif choice == 2:
                    self.view_investments()

                elif choice == 3:
                    self.search_investment()

                elif choice == 4:
                    self.update_investment()

                elif choice == 5:
                    self.delete_investment()

                elif choice == 6:
                    self.view_users()

                elif choice == 7:
                    self.view_transactions()

                elif choice == 8:
                    print("\nSuccessfully Logged Out ✅🚶‍♂️")
                    break

            except ValueError:
                print("Enter a valid choice")
