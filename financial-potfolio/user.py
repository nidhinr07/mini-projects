from database import connection, cursor

class Users:

    def __init__(self, username):
        self.username = username

    def user_menu(self):
        print("\n=============================================================================")
        print("                   Financial Portfolio User Dashboard 🏦📈💸                  ")
        print("===============================================================================")
        print("\n1. View Available Investments")
        print("2. Buy Investments")
        print("3. Sell Investments")
        print("4. View My Transactions")
        print("5. View My Portfolio")
        print("6. Calculate My Profit/Loss")
        print("7. Logout\n")

    def view_available_investments(self):

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

        except sqlite3.Error:
            print("\n⚠️ Something went wrong. Please try again.")

    def buy_investments(self):
        try:
            print("\n-------------------  Buy Investments 📊🛒 -------------------\n")
            company_name = input("Enter Company Name : ").strip().upper()

            cursor.execute("""SELECT * FROM investment WHERE company_name = ? """, (company_name,))
            investment = cursor.fetchone()

            if not investment:
                print("No Investments Found 🚫")
                return

            print(f"\n--------------- {investment[1]}  Investment ---------------")
            print(f"Investment Type       : {investment[2]}")
            print(f"Investment Price      : {investment[3]}")
            print(f"Investment Quantity   : {investment[4]}\n")

            buy_quantity=int(input("Enter the Quantity you want to Buy : "))
            if buy_quantity<1:
                print("Minimum Quantity Must Be 1")
                return

            if buy_quantity > investment[4]:
                print("\nNot Enough Quantity Available 🚫")
                return

            total_price = buy_quantity * investment[3]

            print("\n------------- Purchase Details 🧾💳-------------\n")
            print(f"Company Name        : {investment[1]}")
            print(f"Quantity            : {buy_quantity}")
            print(f"Price Per Unit      : {investment[3]}")
            print(f"Total Amount        : {total_price}")

            cursor.execute('''
                        SELECT balance FROM users WHERE user_name = ?
                    ''', (self.username,))

            user = cursor.fetchone()

            if not user:
                print("\nUser Account Not Found 🚫")
                return

            balance = user[0]

            if balance < total_price:
                print("\n❌ Insufficient Balance")
                print(f"Your Balance : {balance}")
                print(f"Required     : {total_price}")
                return

            confirm = input("\nDo you want to confirm this purchase? (yes/no): ").strip().lower()

            if confirm != "yes":
                print("\nPurchase Cancelled ❌")
                return

            cursor.execute('''UPDATE investment
                        SET quantity = quantity - ? WHERE investment_id = ?
                    ''', (buy_quantity, investment[0]))

            cursor.execute('''
                        UPDATE users
                        SET balance = balance - ? WHERE user_name = ?
                    ''', (total_price, self.username))

            cursor.execute('''
                SELECT * FROM portfolio WHERE user_name = ? AND investment_id = ?
            ''', (self.username, investment[0]))

            portfolio = cursor.fetchone()

            if portfolio:
                new_quantity = portfolio[2] + buy_quantity

                cursor.execute('''
                            UPDATE portfolio SET quantity = ? WHERE user_name = ? AND investment_id = ?
                        ''', (new_quantity,self.username,investment[0]))

            else:
                cursor.execute('''
                INSERT INTO portfolio(user_name, investment_id, quantity, purchase_price)
                VALUES (?, ?, ?, ?)
                        ''', (self.username,investment[0],buy_quantity,investment[3]))

            cursor.execute('''
                        INSERT INTO transactions(user_name, investment_id, transaction_type,quantity, price, total_amount)
                        VALUES (?, ?, ?, ?, ?, ?)
                    ''', (self.username,investment[0],"BUY",buy_quantity,investment[3],total_price))

            connection.commit()

            print("\n🎉 Investment Purchased Successfully! ✅📈\n")
            print(f"Company Name       : {investment[1]}")
            print(f"Quantity Purchased : {buy_quantity}")
            print(f"Amount Paid        : {total_price}")
            print(f"Remaining Balance  : {balance - total_price}")

        except ValueError:
            print("\nEnter a valid choice ❌🔄")

        except sqlite3.Error as e:
            print(f"\n⚠️ Something went wrong. Please try again.{e}")

    def sell_investments(self):
        try:
            print("\n-------------------   Sell Investments 💰💸  --------------------\n")
            company_name = input("Enter Company Name : ").strip().upper()

            cursor.execute("""SELECT * FROM investment WHERE company_name = ? """, (company_name,))
            investment = cursor.fetchone()

            if not investment:
                print("\nNo Investments Found 🚫")
                return

            cursor.execute('''SELECT * FROM portfolio WHERE user_name = ? AND investment_id = ?
            ''',(self.username,investment[0]))

            portfolio=cursor.fetchone()

            if not portfolio:
                print("\nYou Don't have any  Investment in this Company 😭💔")
                return

            print("\n-----------------  Investment Details  📝   ----------------\n")
            print(f"Company Name        : {company_name}")
            print(f"Purchase Price      : {portfolio[3]}")
            print(f"Quantity Purchased  : {portfolio[2]}")

            sell_quantity = int(input("Enter Quantity you need to sell : "))
            if sell_quantity < 1:
                print("\nMinimum Quantity Must Be 1")
                return

            if sell_quantity > portfolio[2]:
                print("\nYou cannot sell more than you have 🤭🫵")
                return

            selling_amount = sell_quantity * investment[3]
            purchase_amount = sell_quantity * portfolio[3]

            if selling_amount > purchase_amount:
                sale = "Profit"
            elif selling_amount < purchase_amount:
                sale = "Loss"
            else:
                sale = "No Profit No Loss"

            print("\n-----------------  Profit 📈 and Loss 📉   ----------------\n")
            print(f"Company Name        : {company_name}")
            print(f"Purchase Price      : {portfolio[3]}")
            print(f"Selling Price       : {investment[3]}")
            print(f"\nYou Have {sale} in this Investment Sale")

            confirm = input("\nDo you want to confirm this Sale? (yes/no): ").strip().lower()

            if confirm != "yes":
                print("\nSale Cancelled ❌")
                return

            cursor.execute('''UPDATE investment SET quantity = quantity + ? WHERE investment_id = ?
            ''',(sell_quantity,investment[0]))

            cursor.execute('''UPDATE users SET balance = balance + ? WHERE user_name = ?
            ''', (selling_amount, self.username))

            remaining_quantity = portfolio[2] - sell_quantity

            if remaining_quantity == 0:
                cursor.execute('''DELETE FROM portfolio WHERE user_name = ? AND investment_id = ?
                        ''', (self.username, investment[0]))

            else:
                cursor.execute('''UPDATE portfolio SET quantity = ?
                            WHERE user_name = ? AND investment_id = ?
                        ''', (remaining_quantity, self.username, investment[0]))

            cursor.execute('''INSERT INTO transactions (user_name, investment_id, transaction_type, quantity, price, total_amount)
            VALUES (?, ?, ?, ?, ?, ?)
            ''',(self.username,investment[0],"SELL",sell_quantity,investment[3],selling_amount))

            connection.commit()

            print("\n🎉 Investment Sold Successfully! ✅💰")
            print(f"\nCompany Name       : {company_name}")
            print(f"Quantity Sold      : {sell_quantity}")
            print(f"Selling Amount     : {selling_amount}")
            print(f"Remaining Quantity : {remaining_quantity}")

        except ValueError:
            print("\nEnter a valid choice ❌🔄")

        except sqlite3.Error:
            print("\n⚠️ Something went wrong. Please try again.")

    def view_my_transactions(self):
        try:
            print("\n====================================================================")
            print("                       📜 My Transactions                           ")
            print("====================================================================\n")

            cursor.execute('''
                SELECT
                    transactions.transaction_id,
                    investment.company_name,
                    transactions.transaction_type,
                    transactions.quantity,
                    transactions.price,
                    transactions.total_amount,
                    transactions.transaction_date
                FROM transactions
                JOIN investment
                ON transactions.investment_id = investment.investment_id
                WHERE transactions.user_name = ?
                ORDER BY transactions.transaction_id DESC
            ''', (self.username,))

            transactions = cursor.fetchall()

            if not transactions:
                print("No Transactions Found 🚫")
                return

            for transaction in transactions:
                print("------------------------------------------------------------")
                print(f"Transaction ID   : {transaction[0]}")
                print(f"Company Name     : {transaction[1]}")
                print(f"Transaction Type : {transaction[2]}")
                print(f"Quantity         : {transaction[3]}")
                print(f"Price            : {transaction[4]}")
                print(f"Total Amount     : {transaction[5]}")
                print(f"Date             : {transaction[6]}")
                print("------------------------------------------------------------")

        except sqlite3.Error:
            print("\n⚠️ Something went wrong. Please try again.")

    def view_my_portfolio(self):
        try:
            print("\n====================================================================")
            print("                         📊 My Portfolio                            ")
            print("====================================================================\n")

            cursor.execute('''
                SELECT
                    investment.company_name,
                    investment.type,
                    portfolio.quantity,
                    portfolio.purchase_price,
                    investment.price
                FROM portfolio
                JOIN investment
                ON portfolio.investment_id = investment.investment_id
                WHERE portfolio.user_name = ?
            ''', (self.username,))

            portfolio = cursor.fetchall()

            if not portfolio:
                print("Your Portfolio is Empty 🚫")
                return

            for item in portfolio:

                company_name = item[0]
                investment_type = item[1]
                quantity = item[2]
                purchase_price = item[3]
                current_price = item[4]

                purchase_amount = quantity * purchase_price
                current_amount = quantity * current_price

                profit_loss = current_amount - purchase_amount

                if profit_loss > 0:
                    status = "Profit 📈"
                elif profit_loss < 0:
                    status = "Loss 📉"
                else:
                    status = "No Profit / No Loss"

                print("------------------------------------------------------------")
                print(f"Company Name       : {company_name}")
                print(f"Investment Type    : {investment_type}")
                print(f"Quantity Owned     : {quantity}")
                print(f"Purchase Price     : ₹{purchase_price}")
                print(f"Current Price      : ₹{current_price}")
                print(f"Total Invested     : ₹{purchase_amount}")
                print(f"Current Value      : ₹{current_amount}")
                print(f"Profit/Loss        : ₹{profit_loss}")
                print(f"Status             : {status}")
                print("------------------------------------------------------------")

        except sqlite3.Error:
            print("\n⚠️ Unable to load your portfolio. Please try again later.")

    def calculate_my_profit(self):
        try:
            print("\n====================================================================")
            print("                    📈 My Profit / Loss 📉                         ")
            print("====================================================================\n")

            cursor.execute('''
                SELECT
                    portfolio.quantity,
                    portfolio.purchase_price,
                    investment.price
                FROM portfolio
                JOIN investment
                ON portfolio.investment_id = investment.investment_id
                WHERE portfolio.user_name = ?
            ''', (self.username,))

            investments = cursor.fetchall()

            if not investments:
                print("Your Portfolio is Empty 🚫")
                return

            total_invested = 0
            current_value = 0

            for investment in investments:
                quantity = investment[0]
                purchase_price = investment[1]
                current_price = investment[2]

                total_invested += quantity * purchase_price
                current_value += quantity * current_price

            profit_loss = current_value - total_invested

            print(f"Total Invested Amount : ₹{total_invested}")
            print(f"Current Portfolio Value : ₹{current_value}")
            print(f"Profit / Loss : ₹{profit_loss}")

            if profit_loss > 0:
                print("\n📈 You are currently in PROFIT.")
            elif profit_loss < 0:
                print("\n📉 You are currently in LOSS.")
            else:
                print("\n➖ No Profit / No Loss.")

        except sqlite3.Error:
            print("\n⚠️ Unable to calculate profit/loss. Please try again later.")

    def user_run(self):
        while True:
            try:
                self.user_menu()
                choice = int(input("Enter your choice : "))

                if choice > 7 or choice <= 0:
                    print("\nInvalid Choice ❌ Choose from 1-7")
                    continue

                elif choice == 1:
                    self.view_available_investments()

                elif choice == 2:
                    self.buy_investments()

                elif choice == 3:
                    self.sell_investments()

                elif choice == 4:
                    self.view_my_transactions()

                elif choice == 5:
                    self.view_my_portfolio()

                elif choice == 6:
                    self.calculate_my_profit()

                elif choice == 7:
                    print("\nSuccessfully Logout ✅🚶‍♂️")
                    break

            except ValueError:
                print("Invalid Choice ❌")

