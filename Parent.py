import sqlite3

# Open a connection to the database (creates the database if it doesn't exist)
conn = sqlite3.connect('employer_parent.db')
cursor = conn.cursor()

# Create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS employers (
        employerid INTEGER PRIMARY KEY,
        employername TEXT
    )
''')

# Read employer names from the text file
with open('employer_names.txt', 'r') as file:
    employer_names = file.read().splitlines()

# Insert data into the table
for idx, employer_name in enumerate(employer_names, start=1):
    cursor.execute('''
        INSERT INTO employers (employerid, employername)
        VALUES (?, ?)
    ''', (idx, employer_name))

# Commit changes and close the connection
conn.commit()
conn.close()
