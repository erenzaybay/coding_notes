# using pip and virtual enviroment


1. basic actions
#finding help documentation for "install"
pip help install

# find a package
pip search flask

# checking whether we have the lasted version -o means -outdated
pip list -o

# updating the packages to the lated version
pip install -U flask

2 freeing a package list so others can use it

#check the current package list
pip list

#freez the list and output to a requirement file for other to use
pip freeze > requirements.txt

#using the requirement file -r means using requirement file
pip install -r requirements.txt

3.virtual enviroment

#!!!!!!!!!!!remenber to init a repo and add .gitignore file to ignore you virtualenv before creating a new virtualenv
# if you forget to do it , you can search online 

# make a directory and enter it
mkdir the_project
cd the_project
# make a new virtual enviroment and give it a name of flask_project
virtualenv flask_project
#activate the target virtual enviroment
source flask_project/Script/activate 
# list the packages
pip list
# install the flask
pip install flask
# generate a requirement file
pip freeze --local > requirement.txt
#deactivate the virtualenv
deactivate
#if you want to get rid of the virtualenv you created
rm -rf the the_project

# reinstall using the requiremtn file
pip install -r requirements.txt







4. advance actions

#upgrading all packages with pip
pip freeze --local | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 pip install -U


# If you want to use certain kind of python
#virtualenv -p thisispathofthepython nameofthevirtualenviroment
virtualenv -p C:/user/erenzaybay/python3.6 the_flask_project



testtesttest delete this line ,this line is only a test
