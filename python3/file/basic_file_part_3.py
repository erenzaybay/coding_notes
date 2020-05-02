# the code write a big file into a new file ,part by part

bigfile=open(r"example_input\bigfile.txt","r")
newbigfile=open(r"example_output\newbigfile.txt","w")

buffersize=500                                          # we specify a buffersize of 500 
thebuffer=bigfile.read(buffersize)                      # read() on default read the entire file, but you can specify a size
while len(thebuffer):                                   # non-zero is True, 0 is Flase ,while ran until the length is 0
    newbigfile.write(thebuffer)                         # write the buffer into the newbigfile
    print(".",end="")                                   # we get a feed back of ".", when a part is written
    thebuffer=bigfile.read(buffersize)                  # we sepecify a "buffersize" number of byte to be read and move the position
print("Done")                                           # feed back of "Done" when it is done
