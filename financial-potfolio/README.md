# 📈 Financial Portfolio Management System

A simple **Python + SQLite3** based Financial Portfolio Management System.
This project allows an admin to manage investments and users to buy, sell, and manage their investments.

---

## 🛠️ Technologies Used

* Python
* SQLite3
* PyCharm

---

## 👤 Admin Login

The system has a default admin account with a predefined username and password.

### Admin Functions

1. **Add Investment** – Add a new investment with company name, type, price, and quantity.
2. **View Investments** – View all available investments.
3. **Search Investment** – Search for an investment using its ID.
4. **Update Investment** – Update the price and quantity of an investment.
5. **Delete Investment** – Delete an investment if no user currently owns it.
6. **View Users** – View registered user details.
7. **View Transactions** – View all user transactions.
8. **Logout** – Exit the admin dashboard.

---

## 👤 User Registration & Login

A new user must first register an account.

After registration, the user can log in using their **username and password**.

### User Functions

1. **View Available Investments** – View all available investments.
2. **Buy Investments** – Purchase available investment quantities using the user's balance.
3. **Sell Investments** – Sell investments owned by the user.
4. **View My Transactions** – View the user's buy and sell transaction history.
5. **View My Portfolio** – View currently owned investments and their profit/loss.
6. **Calculate My Profit/Loss** – Calculate the overall portfolio profit or loss.
7. **Logout** – Exit the user dashboard.

---

## 🗄️ Database Structure

The project uses **SQLite3** with four tables:

### 1. `users`

Stores registered user information.

* `user_name`
* `name`
* `age`
* `email`
* `password`
* `balance`

### 2. `investment`

Stores available investments.

* `investment_id`
* `company_name`
* `type`
* `price`
* `quantity`

### 3. `portfolio`

Stores the investments currently owned by users.

* `user_name`
* `investment_id`
* `quantity`
* `purchase_price`

### 4. `transactions`

Stores the history of investment purchases and sales.

* `transaction_id`
* `user_name`
* `investment_id`
* `transaction_type`
* `quantity`
* `price`
* `total_amount`
* `transaction_date`

---

## 🔄 How the System Works

**Admin →** Manages investments and views users/transactions.

**User →** Registers → Logs in → Views investments → Buys/Sells → Portfolio is updated → Transactions are recorded.

When a user **buys** an investment:

* Investment quantity decreases.
* User balance decreases.
* Portfolio is updated.
* A BUY transaction is recorded.

When a user **sells** an investment:

* Investment quantity increases.
* User balance increases.
* Portfolio is updated.
* A SELL transaction is recorded.

---

## 📂 Project Files

```text
Financial-Portfolio-Management-System/
│
├── main.py
├── admin.py
├── user.py
├── users.db
├── create_database.py
└── README.md
```

---

## 🎯 Project Purpose

This project was created as a **Python and SQLite3 mini project** to practice:

* Python OOP
* Functions and classes
* Exception handling
* SQLite database operations
* CRUD operations
* SQL queries
* Database relationships
* User and admin workflows
