import mysql.connector

# Connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",       # default for XAMPP
    password="",       # if you set a password in XAMPP, put it here
    database="student_management"
)

cursor = conn.cursor()

# View all students
def view_students():
    cursor.execute("SELECT * FROM students")
    for student in cursor.fetchall():
        print(student)

# Add new student
def add_student(name, age, course, grade):
    cursor.execute("INSERT INTO students (name, age, course, grade) VALUES (%s,%s,%s,%s)", (name, age, course, grade))
    conn.commit()
    print("Student added!")

# Example usage
print("All students:")
view_students()

print("\nAdding a new student:")
add_student("Kamal Perera", 24, "Cyber Security", "A")
view_students()

