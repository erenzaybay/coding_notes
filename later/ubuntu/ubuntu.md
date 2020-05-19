
# command line course

#change diretory
cd mybag

#list the files
ls

# list all the files, including the hidden files
ls -a

# give me detailed list
ls -l

# maka a new directory
mkdir my_folder

# make a new file
touch my_folder

# copying files 
cp oldfiel.txt newfile

# coping directories
cp -u old_folder new_location

# moving files
mv mytext.txt mybag/smallbag

# renaming files
mv mytest.txt yourtest.txt

# viewing file , it show file page by page ,enter "q" to get out of it
less myfiel.txt

# streaming a file
cat myfile.txt

# removing a file
rm myfile.txt

# removing a directory    -r recursive  -f force
rm -rf the_directory

#exit
exit

# print working directory
pwd

# cleaner the screen
cleaner

# pushd and popd
# goto the temp directory
pushd my/temp/visit/directory
popd   #back to the old location

################################################# Advanced Actions ###############################

#make the hello.py editable and excutable
chmod 755 hello.py


