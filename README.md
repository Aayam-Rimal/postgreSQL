# Student Course Enrollment Database (Python + PostgreSQL)

This project is a **command-line interface (CLI) app** for managing students, courses, and enrollments using **Python**, **PostgreSQL**, and the **psycopg2** driver.  
You can add students or courses, enroll students in courses, view enrollments, and delete students, all from your terminal.

---

## Features

- Add new students and courses
- Enroll students in courses
- View all students
- View all students in a course
- View all courses for a student
- Delete students (with cascading enrollment deletion)
- All data stored in a PostgreSQL database

---

## Tech Stack

- **Python 3**
- **PostgreSQL**
- **psycopg2** (database driver)
- **python-dotenv** (for environment variable management)

---

## Setup Instructions

### 1. **Clone the repository**

```bash
git clone git@github.com:Aayam-Rimal/postgreSQL.git

```

### 2. **Create and activate a virtual environment**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. **Install dependencies**

```bash
pip install -r requirements.txt
```

### 4. **Set up your `.env` file**

Create a `.env` file in the project root directory with your PostgreSQL database credentials:

```
DBname=your_db_name
User=your_db_user
Password=your_db_password
Host=your_db_host
```

**Note:**  
- The database should already exist; the script will create the tables if they don't.
- Do **not** commit your `.env` file to source control! (Add `.env` to `.gitignore`).

### 5. **Run the CLI application**

```bash
python connection.py
```

---

## Usage

You’ll see a menu in your terminal similar to:

```
   --MENU--
             1. Add student
             2. Add course
             3. Enroll student in course
             4. View all students
             5. View students in a course
             6. View student's courses
             7. Delete student
             8. Quit
```

Just type the number of the operation you want, and follow the prompts.

---

## Project Structure

```
├── connection.py         # Main Python script for CLI/database logic
├── requirements.txt      # Python dependencies
├── .env                  # (Not tracked) Your PostgreSQL credentials
├── .gitignore            # Ignores .env and venv
└── README.md             # You are here!
```

---

## Notes

- The app uses descriptive error messages and transaction rollbacks for safe DB operations.
- Table setup (students, courses, enrollments) and a helpful SQL view are managed automatically.
- Enrolling or deleting students/courses will cascade related enrollments as appropriate.

---

## License

MIT License (or your preferred license)

---

## Author

Aayam Rimal
https://github.com/Aayam-Rimal

---

## Contributing

Contributions and suggestions are welcome! Open an issue or submit a pull request.

---

### **Happy learning and coding!**