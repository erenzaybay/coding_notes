# the code opend a file and print the file line by line twice and letter by letter onece


file=open(r"example_input/lines.txt")          # the object file is a file handel type object
                                               # notice i use raw string , so it will understand how I'm using "\" here
                                               # it is on default open in read mode ,which is same to 
                                               # file=open("lines.txt","r")  r meand read
                                               # "w" for write only, you can not read
                                               # "a" for apend, current position is set to the end of the file when opening a file
                                               # "r+" is for read and write 
                                               # "rt" is for text file mode
                                               # "rb" is for binary file mode


# It read the file line by line and print it on the screen with only onw original CR
file.seek(0)
for line in file:
    print(line,end="")                         # we have added the ending , so it will only print the original ending
print("Done")

# It read the file line by line and print it on the screen with two CR
# here logic is little than obvious , ask me if you forget
# for each "for" iteration , the "for" line is evaluate to make sure it is not over
# so each evaluation execute the readline() method, it move the posion one line down
# each realine can be seen as a group of object with only one element
# so each "for" evaluation get a new line ,which is not done
# so it execute itself until readline() return an empty line
# my dear sister, got it?


file.seek(0)
for line in file.readlines():
    print(line)                                # if you dont't add the ending attribute ,it will print two CR
print("Done")


file.seek(0)
print(file.readline())                         # read the first line of file and print it
print(file.readline())                         # read the second line of file and print it
print(file.readline())                         # read the third line of file and print it

# It read the file line by line ,then in each line ,character by character
file.seek(0)
for line in file.readlines():
    for character in line:
        print(character)
print("Done")

