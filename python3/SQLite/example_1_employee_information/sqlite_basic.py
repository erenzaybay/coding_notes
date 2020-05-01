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
cursor.execute("""CREATE TABLE emplyees(
                name text
                income integer
                )""")

# commit after each creating ,updating ,deleting
connect_object.commit()
