
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()



conn= psycopg2.connect(
    dbname= os.getenv('DBname'),
    user= os.getenv('User'),
    password= os.getenv('Password'),
    host=os.getenv('Host')
)
cursor= conn.cursor()

create_students= """ 
CREATE TABLE IF NOT EXISTS students(
id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
name VARCHAR(50) NOT NULL,
email VARCHAR(100)
);
"""

create_courses="""
CREATE TABLE IF NOT EXISTS courses(
id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
course_name VARCHAR(50) NOT NULL,
credits INT
);
"""

create_enrollments="""
CREATE TABLE IF NOT EXISTS enrollments(
id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
student_id INT NOT NULL,
course_id INT NOT NULL,

FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE,
FOREIGN KEY (course_id) REFERENCES courses(id) ON DELETE CASCADE,

UNIQUE(student_id, course_id) );
"""

cursor.execute(create_students)
conn.commit()
cursor.execute(create_courses)
conn.commit()
cursor.execute(create_enrollments)
conn.commit()

def add_students(name,email):
    try:
        cursor.execute("INSERT INTO students(name,email) VALUES(%s,%s)",(name,email))
        conn.commit()
    except Exception as e:
        print("ERROR OCCURED:", e)
        conn.rollback()

def add_courses(cname,credits):
    try:
        cursor.execute("INSERT INTO courses(course_name,credits) VALUES(%s,%s)",(cname,credits))
        conn.commit()
    except Exception as e:
        print("ERROR:", e)
        conn.rollback()

def enroll_student(student_id, course_id):
    try:
        cursor.execute("INSERT INTO enrollments(student_id,course_id) VALUES(%s,%s)",(student_id,course_id))
        conn.commit()
    except Exception as e:
        print("ERROR:", e)
        conn.rollback()

def view_all():
    try:
        cursor.execute("SELECT id,name FROM students ")
        students= cursor.fetchall()
        for student in students:
            print(student)
    except Exception as e:
        print("ERROR:",e)
        conn.rollback()

cursor.execute("""
CREATE OR REPLACE VIEW student_course AS
               SELECT s.name, c.course_name
               FROM enrollments e
               JOIN students s ON e.student_id = s.id
               JOIN courses c on e.course_id= c.id

 """)
conn.commit()


while True:
    print("""   --MENU--
             1. Add student
             2. Add course
             3. Enroll student in course
             4. View all students
             5. View students in a course
             6. View student's courses
             7. Delete student
             8. Quit""")
    
    try:
        choice= int(input("Enter task to continue: "))
    except ValueError:
        print("invalid input! try again!!")
        continue

    if choice==1:
        name=input("Enter name of student: ")
        email= input("Enter student Email: ")

        add_students(name,email)

    elif choice==2:
        try:
            course_name= input("Enter name of course: ")
            credits= int(input("Enter total credits: "))
        except ValueError:
            print("invalid input! try again!!")
            continue

        add_courses(course_name,credits)

    elif choice==3:

        name=input("Enter name to enroll: ")
        cursor.execute("SELECT id FROM students WHERE name=%s",(name, ))
        result= cursor.fetchone()

        if result is None:
            print("no such students exist!")
            continue
        else:
            student_id= result[0]
        
        cname= input("enter course to enroll in: ")
        cursor.execute("SELECT id FROM courses WHERE course_name=%s",(cname, ))
        result2= cursor.fetchone()
        
        if result2 is None:
            print("No such courses exist!")
            continue
        else:
            course_id= result2[0]

        enroll_student(student_id,course_id)

    elif choice==4:
        view_all()

    elif choice==5:
        course_name= input("Enter course name to see all enrolled students: ")
        cursor.execute("SELECT * FROM student_course WHERE course_name=%s",(course_name, ))
        rows=cursor.fetchall()
        for row in rows:
            print(row)

    elif choice==6:
        student_name= input("Enter student name to see all of the student's course: ")
        cursor.execute("SELECT * FROM student_course WHERE name=%s",(student_name, ))
        rows=cursor.fetchall()
        for row in rows:
            print(row)
 
    elif choice==7:
        name_of_student= input("enter student name to delete: ")
        cursor.execute("DELETE FROM students WHERE name=%s",(name_of_student, ))
        conn.commit()
    
    elif choice==8:
        cursor.close()
        conn.close()
        break

    

        
    
















