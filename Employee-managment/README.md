# Employee Management System

This is a simple Employee Management System built using Python and SQLite.

I created this project to practice working with databases in Python, including creating tables, inserting data, retrieving records, searching, deleting, and using SQL queries.

## Features

* Create an SQLite database
* Create an employees table
* Add employees
* View all employees
* View employees with salary of 40000 or higher
* Calculate average salary
* Search for an employee
* Delete an employee
* Menu-driven program

## Technologies Used

* Python
* SQLite
* Python `sqlite3` module

## Database Structure

The program creates a database named:

```text
company.db
```

The `employees` table contains:

| Column | Type                |
| ------ | ------------------- |
| id     | INTEGER PRIMARY KEY |
| name   | TEXT                |
| age    | INTEGER             |
| salary | INTEGER             |

## SQL Operations Practiced

This project uses SQL queries for:

* Creating the database table
* Inserting employees
* Selecting employee records
* Filtering employees by salary
* Calculating average salary
* Searching employees
* Deleting employees

## Menu

```text
===== Employee Management System =====

1. Add employee
2. View all employees
3. View employees with salary >= 40000
4. Show average salary
5. Search employee
6. Delete employee
7. Exit
```

The program uses a `while` loop to keep the menu running until the user selects **Exit**.

## Example Output

### View All Employees

```text
1 - John - Age: 25 - Salary: 30000
2 - Sarah - Age: 28 - Salary: 45000
3 - Michael - Age: 32 - Salary: 55000
4 - David - Age: 24 - Salary: 28000
5 - Emma - Age: 30 - Salary: 50000
```

### Employees with Salary >= 40000

```text
Sarah - 45000
Michael - 55000
Emma - 50000
```

### Average Salary

```text
Average salary: 41600.0
```

## What I Practiced

* Python and SQLite connection
* Creating database tables
* SQL `CREATE TABLE`
* SQL `INSERT`
* SQL `SELECT`
* SQL `WHERE`
* SQL `AVG()`
* SQL `DELETE`
* Parameterized queries
* Python loops
* Functions
* User input
* Committing database changes
* Closing database connections

## Project Structure

```text
Employee-Management-System/
│
├── employee.py
├── company.db
└── README.md
```

## Purpose

The purpose of this project was to practice Python database programming using SQLite and understand how Python programs interact with SQL databases.

This is a practice project created for learning Python and database concepts.

## Author

Nidhin
