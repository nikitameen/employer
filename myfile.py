import sqlite3
import json

# Open a connection to the database (creates the database if it doesn't exist)
conn = sqlite3.connect('data.db')
cursor = conn.cursor()

# Create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS companies (
        companyname TEXT,
        address1 TEXT,
        address2 TEXT,
        City TEXT,
        State TEXT,
        zipcode TEXT,
        countyname TEXT,
        msaname TEXT,
        stateOfIncorporation TEXT,
        SIC TEXT,
        sicdescription TEXT
    )
''')

# Load JSON data from file
with open('data.json') as json_file:
    data = json.load(json_file)
itr =0
# Insert data into the table
for entry in data:
    cursor.execute('''
        INSERT INTO companies (
            companyname, address1, address2, City, State,
            zipcode, countyname, msaname, stateOfIncorporation,
            SIC, sicdescription
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        entry['companyname'], entry['address1'], entry['address2'],
        entry['City'], entry['State'], entry['zipcode'],
        entry['countyname'], entry['msaname'],
        entry['stateOfIncorporation'], entry['SIC'], entry['sicdescription']
    ))
    itr=itr+1
    print(itr)
# Commit changes and close the connection
conn.commit()
conn.close()
