import sqlite3

connection = sqlite3.connect("student.db")

#creating cursor object to insert record, create table
cursor = connection.cursor()

#creating a table
table_info = """
create table student(name varchar(25), class varchar(25),
section varchar(25), marks int)
"""

cursor.execute(table_info)

#insert more records 
cursor.execute("""Insert into student values('Jacob', 'Data Science', 'A', '90')""")
cursor.execute("""Insert into student values('Zoro', 'Data Science', 'B', '100')""")
cursor.execute("""Insert into student values('Luffy', 'Data Science', 'A', '86')""")
cursor.execute("""Insert into student values('Sanji', 'Devops', 'A', '50')""")
cursor.execute("""Insert into student values('Chopper', 'Devops', 'B', '35')""")

#Display all the records
print("The inserted records are")
data = cursor.execute('''Select * from student''')
for row in data:
    print(row)

#commit changes in your database
connection.commit()
connection.close()