# This app CRUD employee information
# remenber to refactor it with "with as " statement
# rename some of the variable to make it more readable
# uses dictionary in the populate_table function
# use class to represent employees

import sqlite3               # only one "l"

def main():


    database_location=''':memory:'''    #This is what you do for testing , it create database only in memory

    #database_location='''employee.db''' This is what you do in real life, a separate database file to store you data 

    con_obj=connect_database(database_location)           # our function ,it connect to the database acording to the location you give it

    create_table(con_obj,"employee")                      # our function, it create a table named employee ,you can create the same table only once !

    populate_table(con_obj)                               # our function, it ask you for information to polulte the table

    print_table(con_obj,"employee","pay",1)               # our function , it print all the record WHERE pay=1 in three different ways

    update_table(con_obj,1,"Eren","Bay",2000)             # it update the table, change the content where pay=1 to ("id_not_changed",Eren,Bay,2000)
    print_table(con_obj,"employee","pay",2000)            # let's print the updated content 

    
    drop_table(con_obj,"employee")                        # our function, it DROP the table, delete the table

    con_obj.close()                                       # close the connection to the database ,you have to do it in the end


# connect the database acording to the location you give
def connect_database(database_location):

    con_obj=sqlite3.connect(database_location)     # you make a connect object to represent the database, similar to file handel object
                                                   # it connect the file if it exist, if not ,it create a new one
    return con_obj                                 # it return a connect object


# create table 
def create_table(con_obj,table_name):
    csr=con_obj.cursor()                   # it is a cursor object use for executing sql queery, it carries the sql queery content
    csr.execute("""CREATE TABLE {}(
                       id integer,
                       first text,
                       last text,
                       pay integer
                    )""".format(table_name))   # there could be four type of data in sqlite, integer,real,text,blob
    con_obj.commit()                           # This commit the change ,similar to git ,rememmer to do it


# ask you information , so it can fill the records in the table, it asks the help of another function write_talbe()
def populate_table(con_obj):
    print(" Please input the record in order, enter \"end\" when asking for fistname when you are done.")
    count=1
    while True:
        firstname=input("ID:{}.The first name:".format(count))
        if firstname=="end": break
        lastname=input("ID:{}.The last name:".format(count))
        pay=input("ID:{}.The pay is:".format(count))

        write_table(con_obj,count,firstname,lastname,pay)
        count+=1

# it write the information you get into the talbe
def write_table(con_obj,theid,first,last,pay):
    csr=con_obj.cursor()  
    csr.execute('''INSERT INTO employee VAlUES (:keyid,:keyfirst,:keylast,:keypay)''',{"keyid":theid,"keyfirst":first,"keylast":last,"keypay":pay})
    #csr.execute('''INSERT INTO employee VAlUES (?,?,?,?)''',(theid,first,last,pay)) # This also works , the first one is better
    con_obj.commit()

# it print the content of the talbe met your describtion
def print_table(con_obj,table,column,content):

    csr=con_obj.cursor()
    
    csr.execute('''SELECT * FROM {} WHERE {} ={}'''.format(table,column,content)) 
    # csr.execute('''SELECT * FROM ? WHERE ? =?''',(table,column,content)) This does not work
    # csr.execute('''SELECT * FROM employee WHERE last =:key''',{"key":content})  This works

    one_row=csr.fetchone()        # it fetch only one row from the result,fetch once and move the cursor down one unit
    print(one_row)

    many_row=csr.fetchmany(5)     # similar to fetchone ,but it fetchmany, it also move the cursor
    print(many_row)

    all_row=csr.fetchall()        # it fetchall , but only after the current cursor
    print(all_row)



# update the content of the table where pay=1 to eren,bay,2000
# always use a dictionary to refer to the variable in the sql querry to avoid sql injacktion attack
def update_table(con_obj,old_pay,first,last,new_pay):
    csr=con_obj.cursor()
    csr.execute("""UPDATE employee
                   SET first=:keyfirst,
                   last=:keylast,
                   pay=:keynewpay
                   WHERE pay =:keyoldpay""",{"keyoldpay":old_pay,"keyfirst":first,"keylast":last,"keynewpay":new_pay})
    con_obj.commit()

"""  # it do exactely the same thing , but with different syntax
def update_table(con_obj,theid,first,last,pay):
    csr=con_obj.cursor()
    csr.execute('''UPDATE employee
                   SET first={},
                   last={},
                   pay={}
                   WHERE id ={}'''.format(first,last,pay,theid))
    con_obj.commit()
"""


# it delete the talbe
def drop_table(con_obj,table):
    csr=con_obj.cursor()
    csr.execute('''DROP TABLE {}'''.format(table))
    con_obj.commit()


if __name__=="__main__":main()    # The "if __name__..." should be at the end ," def main()" at the begining
                                  # The construct is helpful, i will explain in person
                                  # When you write non-trivial code, always use the construct

