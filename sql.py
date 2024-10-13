import sqlite3

## connect to sqlite
connection=sqlite3.connect("student.db")

## create cursor for crud operations
cursor=connection.cursor()

## create the table
table_info=""" 
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
                     SECTION VARCHAR(25),MARKS INT);
"""

cursor.execute(table_info)

## insert some more records
cursor.execute('''INSERT INTO STUDENT VALUES ('Krish', 'Data Science', 'A',60)''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Darius', 'Data Science', 'B',70)''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Sudhanshu', 'Devops', 'C',75)''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Vikash', 'Data Science', 'C',90)''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('SIDX', 'Data Science', 'A',90)''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('THANUJA', 'Data Science', 'A',85)''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('JAGRITI', 'Devops', 'C',75)''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('DOLL', 'Data Science', 'C',83)''') 

## display records

print("the inserted records are")

data=cursor.execute('''SELECT * FROM STUDENT''')

for row in data :
    print(row)

## close the connection 
connection.commit()
connection.close()