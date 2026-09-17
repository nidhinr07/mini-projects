# Student Management System

A simple command-line Student Management System built using **Python and SQLite**.

This project allows users to add, view, search, and delete student records. It also includes features to view passing students and calculate the average marks of all students.

## Features

* Add new student details
* View all students
* View students who passed
* Calculate average student marks
* Search student by ID
* Delete student records
* Store student data using SQLite
* Basic input validation and error handling

## Technologies Used

* Python
* SQLite
* `sqlite3`

## Database

The project uses a SQLite database named:

```text
school.db
```

The `students` table contains:

| Column         | Description       |
| -------------- | ----------------- |
| `student_id`   | Unique student ID |
| `student_name` | Student name      |
| `age`          | Student age       |
| `grade`        | Student marks     |

## Menu

```text
1. Add Student
2. View Student
3. View Passing Student
4. Show Average Grade
5. Search Student
6. Delete Student
7. Exit
```

## How to Run

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Open the project folder

```bash
cd student-management-system
```

### 3. Run the Python file

```bash
python student_management.py
```

The SQLite database will be used to store the student records.

## What I Practiced

Through this project, I practiced:

* Python functions
* `while` loops and conditional statements
* User input and validation
* Exception handling
* SQLite database connection
* SQL `INSERT`, `SELECT`, and `DELETE`
* SQL `WHERE` conditions
* SQL `AVG()` function
* Fetching data using `fetchone()` and `fetchall()`
* Committing and closing a database connection

## Project Structure

```text
Student-Management-System/
│
├── student_management.py
├── school.db
└── README.md
```

## Future Improvements

Some features that can be added later:

* Update student details
* Search students by name
* Grade calculation (A, B, C, etc.)
* Better input validation
* Student attendance management
* Separate database and application files

## Author

Nidhin
