import sqlite3

# Sample data
sample_data = [
    {'name': 'John', 'position': 'Data Scientist', 'salary': 100000, 'joining_date': '2022-01-15'},
    {'name': 'Jane', 'position': 'Project Manager', 'salary': 110000, 'joining_date': '2021-05-20'},
    {'name': 'Bob', 'position': 'Frontend Developer', 'salary': 95000, 'joining_date': '2020-03-10'},
    {'name': 'Johnson', 'position': 'Backend Developer', 'salary': 105000, 'joining_date': '2020-12-05'},
    {'name': 'Alice', 'position': 'Frontend Developer', 'salary': 85000, 'joining_date': '2019-08-22'},
    {'name': 'Williams', 'position': 'Data Scientist', 'salary': 120000, 'joining_date': '2018-06-15'},
    {'name': 'Charlie', 'position': 'Project Manager', 'salary': 90000, 'joining_date': '2021-02-10'},
    {'name': 'Brown', 'position': 'Backend Developer', 'salary': 95000, 'joining_date': '2022-09-30'},
    {'name': 'Eva', 'position': 'Frontend Developer', 'salary': 95000, 'joining_date': '2019-12-15'},
    {'name': 'Martinez', 'position': 'Data Scientist', 'salary': 88000, 'joining_date': '2020-08-05'},
]

# Connect to SQLite database (creates a new database if it doesn't exist)
conn = sqlite3.connect('employee_database.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Create a table with the specified schema
cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        position TEXT NOT NULL,
        salary INTEGER NOT NULL,
        joining_date DATE NOT NULL
    )
''')

# Insert data into the table
for employee in sample_data:
    cursor.execute('''
        INSERT INTO employees (name, position, salary, joining_date)
        VALUES (?, ?, ?, ?)
    ''', (employee['name'], employee['position'], employee['salary'], employee['joining_date']))

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database created and data inserted successfully.")
