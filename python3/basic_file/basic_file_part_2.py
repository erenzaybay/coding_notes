# The code open a file and write it into another file

infile=open(r"example_input\infile.txt","r")                        # open a file in read mode
outfile=open(r"example_output\outfile.txt","w")                      # open a file in write mode ,position is in the begining

for line in infile:
    print(line,file=outfile,end="")

print("Done wrinting into outfile.txt")



# This give us a big file with 10000 lines of text
alotofa=open(r"example_output\alotofa.txt","w")
for line in range(1,10001):
    print("a"*10,file=alotofa)                        # here we need the CR, so we don't make it ""
                                                      # if we add end="", you wil get a file with
                                                      # one line of 100000 "a"

print("Done wrring to the bigfile.txt")
