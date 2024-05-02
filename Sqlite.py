import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Create the student table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS student(
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    department TEXT
                )''')
conn.commit()

def read():
    cursor.execute("SELECT * FROM student")
    print("id\tname\tdepartment")
    for row in cursor.fetchall():
        print(str(row[0]), "\t", row[1], "\t", row[2])

def insert():
    name = input("Enter name: ")
    department = input("Enter department: ")
    
    # Use parameterized query to prevent SQL injection
    sql = "INSERT INTO student(name, department) VALUES(?, ?)"
    cursor.execute(sql, (name, department))
    conn.commit()

def delete():
    column = input("Enter column name: ")
    value = input("Enter the value: ")
    
    # Use parameterized query to prevent SQL injection
    sql = f"DELETE FROM student WHERE {column} = ?"
    cursor.execute(sql, (value,))
    conn.commit()

def update():
    column = input("Enter column name to be updated: ")
    value1 = input("Enter updated value: ")
    
    op = input("Enter 'yes' if update condition to be applied, else 'no': ")
    
    if op.lower() == 'yes':
        column2 = input("Enter conditional column name: ")
        value2 = input("Enter the value for the condition: ")
        
        # Use parameterized query to prevent SQL injection
        sql = f"UPDATE student SET {column} = ? WHERE {column2} = ?"
        cursor.execute(sql, (value1, value2))
        conn.commit()
    elif op.lower() == 'no':
        # Use parameterized query to prevent SQL injection
        sql = f"UPDATE student SET {column} = ?"
        cursor.execute(sql, (value1,))
        conn.commit()
    else:
        print("Invalid option!")

while True:
    print("Options:")
    print("1. Read")
    print("2. Insert")
    print("3. Update")
    print("4. Delete")
    print("5. Exit")

    op = input("Enter option: ")
    
    if op == '5':
        cursor.close()
        conn.close()
        break
    
    try:
        op = int(op)
        if op == 1:
            read()
        elif op == 2:
            insert()
        elif op == 3:
            update()
        elif op == 4:
            delete()
        else:
            print("Invalid option. Please enter a valid choice.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
