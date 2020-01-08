# try make a testing.txt file with content in it to see what would happen if there is no error
# also try without the testing.txt file to see how the exception is handeled

# In real world code, there would be many tries and exception clauses

def main():
    try:                                                                 # if the try failed ,it goes to the except clause ,
        testing_file=open('testing.txt')                                 # when failed ,rest of the code in the structure won't run
        print("This will only be shown if the the Error is not raised.") # print will run when there is no error
    except FileNotFoundError as e:                                       # "FileNotFoundError" is the error name in the system
        print("The Error is The file is not there,the details are:",e)   # we pass the content of error message to the variable e
    else:                                                                # else will run only when there is no error
        for line in testing_file: print(line.strip())                    # This print the file line by line, google strip()

if __name__=="__main__":main()
