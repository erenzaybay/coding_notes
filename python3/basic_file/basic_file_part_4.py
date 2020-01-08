# the code write a picture jpg file into another jpg file

picture=open(r"example_input\earthseenfrommars.jpg","rb")           # "rb" means read binary mode
newpicture=open(r"example_output\newearthseenfrommars.jpg","wb")    # "wb" means write binary mode
                                                                    # the rest is similar to the txt copy example
buffersize=500
thebuffer=picture.read(buffersize)
while len(thebuffer):
    newpicture.write(thebuffer)
    print(".")
    thebuffer=picture.read(buffersize)
print("Done")
