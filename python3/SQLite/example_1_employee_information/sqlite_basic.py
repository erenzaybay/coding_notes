# import sqlite3 , which is a part of standard library
import sqlite3

# create a connect object to interact with a database
# ":memory" only make the database exist in memory, which only exist in runtime, which is perfect for testing
connect_object = sqlite3.connect(":memory")

# connect to a database ,if not exist ,create one
connect_object = sqlite3.connect("employees.db")

# create a cursor object to execute sql commands
cursor = connect_object.cursor()

# create a table with 3 columns
# only 4 class:null,integer,real,text,blob
cursor.execute("""CREATE TABLE employees(
                name text,
                income integer
                )""")

# commit after each creating ,updating ,deleting
connect_object.commit()

# inserting values
# use different quotation marks
cursor.execute("INSERT INTO employees Values ('Jack',80000)")
cursor.execute("INSERT INTO employees Values ('Marry',80000)")
cursor.execute("INSERT INTO employees Values ('Echo',80000)")
cursor.execute("INSERT INTO employees Values ('Eugene',80000)")
cursor.execute("INSERT INTO employees Values ('Vincent',80000)")
cursor.execute("INSERT INTO employees Values ('Jerome',80000)")
cursor.execute("INSERT INTO employees Values ('Dave',100000)")
cursor.execute("INSERT INTO employees Values ('Tom',90000)")

# selecting data
cursor.execute("SELECT * FROM employees WHERE income = 80000")
cursor.execute("SELECT * FROM employees WHERE name="Jack"")

# iterating through the selected object,
# return next row as a tuple from our query
# if no rows available, return None
cursor.fetchone()

# return next 3 rows as a list of tuples
# if no rows available ,return an empty list
# last 2?
cursor.fetchmany(3)

# return all the remaining rows as a list of tuples
# if no rows available, return an empty list
cursor.fetchall()


# close the connect object when you are done with the database in the end
connect_object.close()
