########################### Baisc Commands ###########################





1.initializing git :
# You go into a directory to type this to iniialize an repository either with files or an empty one
git init    


2. adding a README file for the first commit
# it musk has a readme file correctly named as "README" (There is no added ".txt")
touch README

3. checking the status
# tell our current stage which produce a rather detailed report
git status             

4. adding file to the staging area
#The add the file with the filename to the staging area 
git add filename 

#The add all the edited files in current directory to the staging area
git add .     

# this  undo the git add file action
git rest FILENAME   

# This undo all the added file
git rest            

5. commit files

# This commit the change with adding aditional information
git commit -m "editted README"   

# add and commit at the same time
# it only works when all current fle are tracked
# it doesn't work when there is new file just have been created
git commit -am "editted README again"   


# This add the current edited files and edit the last commit messege, it amend the last commit. 
git commit -a --amend  

6. checking git log

# checking the log
git log

# This only display comment message
git log --oneline 

# This show the most recent one commit  or 2  (changeing the -1 to -2)
git log -1   

# This gives us a very detailed the change log , p stands for patch , this is very useful
git log -1 -p        

# This shows the commit graph which show you the structure of the commit
git log --graph 

7. branches

# it creates the new branch, you need to be in the master branch to do it
git branch new_branch       

# This go to the branch of your choosihng
git checkout new_branch 
  
# deleting certain branch,You have to do it outside of that branch.
# for example master branch after deleting ,there is still compressed file left
git branch -d new-branch     

# Important note! added files in other branches will be commited within the current branch in which you were editting !!!!!! 

#this shows all the branches
git branch -a  


8.Pulling Actions

# this only get change information but not files
# "." measns we are fulling from the local repository.
git fetch . master         #local
git fetch origin master    #remote


# it merge the branches acording to the fectch file you received, it works When you are at the master branch  
# git merge new_branch    

# pull get the information and the files from the master branch    pull is basically fetch and merge
# git pull . master   
# git pull origin master

9.Pushing actions

# pusing the local branch to the the remote master branch "-u" mean track the change in the remote branch
git push -u origin 


10.diffing actions

# using it without any other content when new change is not commited 
# it show the differecne between the old status and the new status(difference between now and the last commit)
git diff 

# This checkout the difference between the two branches ,and uses the latter one as base
git diff new_branch master    

# This show a little more and is more useful, it show which file changed how much
git diff master new_branch --stat  

11. adding tags

git tag:

# git has two kinds of tage  the light weight tag and the anotated tag,
# never use a light weigh tag on important projects
# This lists all the tags
git tag 

# creating a anoted tag , create a tag called v.14 and anote information in it
git tag -a v1.4 -m "my version 1.4"


 This show the details concerning this tag  
git show v1.4    

#remenber always use a anotated tag in remote
#when push to the remote place ,tag is not push by default ,you need to manually do it
#one way is to push a single tag:
git push origin <tag_name>

# another way is to only push all the anotated hash and ingore the light weight tags, this is better
git push --follow-tags

# check out the tag, Do not change any thing ,just look around
# if you want to make change ,better to use a new branch
git checkout 2.0.0


# if you have made change but didn't add them to the stage.
# you can reset to the last commit
git reset --hard

########################### Less Frequent Tasks ###########################

1.configuring git (configuring new user)


	There are 3  levels of configuation we can make,we prefer global.
		system level(all user on this conputer), 
		global  level(one user of all the repositories),
		local level(one user at a spesific repository), 

# setup a user with the name of "Ken Clark"
git config --global user.name "Ken Clark"

# Setup the email fo the user ,you have to ,it is important
git config --global user.email "erenzaybay@gmail.com"  


2. adding ignore files:

#This is the local method , edit the file to tell git to ignore certain files,
# for example #ignore the files    #ingore the jquery  it can be used to ignore todo file
vim .gitignore 

sample file:
		#untracked folder
		thisisajokefolder/
		jquery/

		#untracked files
		Thumbs.db
		*.jokefix

# use config file to change the global ignored file filter  *.exe Tumbs.db
git config --global --edit  



3.push an existing repository from the command line to github

# For example you local git repository is in the folder named as "gittest"
# Creat a github repository named as the same (You don't have to ,but it would be easier)
# When creating the github repository, Do Not check "initializing with a README file"
# copy the url github provided you with, for example,git@github.com:erenzaybay/gittest.git
# When choosing the url ,remenber to choose the ssh ,and not https
# Enter you local repository
# link the local with the remote repository with the following command
git remote add origin git@github.com:erenzaybay/gittest.git  
#it is traditional to call remote origin , though you don't have to 
# push the local repository to github remote
git push -u origin master
# OK done.
# you can check the remote
git remote -v



4.Pull a existing repository form github to local computer，the best way to start a new git repository

# enter folderone ,if you want the repository to be in your folderone folder
# for example , folderone\gittest
# clone from the remote using ssh way
git clone  git@github.com:erenzaybay/gittest.git
# OK done.


5.setting up ssh key pair

#onlinux it is easier,on windows it was messy,you can use git bash 

5.1 linux ssh key pair setup (best way)

# make sure it is you computer
# generate key pair
ssh-keygen 
# it will ask for the location to save the key pair
# usually accept the defaut settings, but if you already have a kay pair, change the location
# remenber the location
# you will get a file with public and local keys ,they are a pair
# got to github to settup the public key , remember to name it properly
# goto your github account ,settings,SSH and GPG keys,new SSH keys,	copy the public key
# start ssh-agent , from now on it wil automaticaly start ssh-agent
ssh-agent -s                
# adding github as the remote pair
ssh -T git@github.com     
# test it when you finish

5.2 in gitbash on windows 10

#adding ssh in git bash with the method of
#https://gist.github.com/bsara/5c4d90db3016814a3d2fe38d314f9c23
#Setup SSH Authentication for Git Bash on Windows

5.3 in cmder on windows 10(never do it again, the worst way)
ssh-add YOURRCSKEY  it didnt work  it did not work for me in cmder , i used a method from online, as follows
1.Open C:\Program Files\cmder\config\user-profile
2. uncomment the line  call "%GIT_INSTALL_ROOT%/cmd/start-ssh-agent.cmd"
3.ssh-add c:/users/erenzaybay/.ssh/id_rsa.pub
4.I can access the github but have to use password everytime because I was using https url as remote, this can be solved by inputing following content and then do a push
git config --global credential.helper wincred
The logic as follows
https://help.github.com/articles/why-is-git-always-asking-for-my-password/
https://help.github.com/articles/caching-your-github-password-in-git/
https://help.github.com/articles/which-remote-url-should-i-use/#cloning-with-https-urls-recommended
    

6. setup github personal page

# You can set up github personal pages or page for some famous repository
# the certain rules about the name
# it has to be started with you github account name
# for example erenzaybay.github.io
# This create a repository in current directory
git clone git@github.com:erenzaybay/erenzaybay.github.io.git  
# add a index page as index.html in this repository
# for example
<!DOCTYPE html>
<html>
<head>
<title>Eren Bay</title>
</head>
<body>
<h1>Erens Test!</h1>
</body>
# do a push,in first push add -u will make git track the remote repository
git push -u origin master           

7.setup github project pages

# You can also set up pages for your repository, you have to 
# make a new branch namde gh-pages ,
# pull the gh-pages to the local repository, add index.html, get rid of everythin else. 
# then push the change to the remote repositoryand the content you pushed to the branch would become the repository page, 
# you can access the page by typing youraccountname.github.io/yourrepositoryname
git pull origin gh-pages
git checkout gh-pages
rm -rf *                   (This is dangerous, be care full, use it within the repository folder)
vim index.html
git add .
git commit -m "commit message"
git push origin -u
# check the updated site https://erenzaybay.github.io/githubtest/
you can use Jekyll as a static site generatorto generate the page , goto pages for more information

8. revert the current head to the last or any previous commit

# first get the commit hash you wanted
git log --oneline

# then revert the the commit you want ,you will loose all the change after the revert, it is dangrous
git reset --hard 0d1d7fc32     # last numbers are the commit hash number




########################### Unimportant Stuff ###########################
# checking git versions

git --version

# config file is in user folder in windows and in home directory in Mac with the name .gitconfig
# You can edit global config file directly by using the following command
git config --global --edit

# This provids the help about config
git config --help    

# This show all the config setting and list the origin of these setting
git config --list --show-origin   

# go into the local .git directory to find the discription file to change the name of the repository (why name it?)

#The is another way to initialize an empty repository
git init "thisisthenameofthedirectoryhelloworld"   

# Other currently useless git log parameters:
 
			git log --decorate 

			git log  --pretty=oneline

			git log --pretty=short

			git log --pretty=full

			git log --pretty-fuller

			git log --stat        # This  gives us a detailed log but not including the actual detail of content change

# creation and enter at the same time
git checkout -b new-branch                            


# You can force delete even if there are un commited changes in the new-braches
git branch -D new-branch 

# git cat-file -p 345f344f   The show the hash content

#This show only what is added to the new_branch
git diff new_branch...master  

#This only show the name of the file that is changed
git diff master new_branch --name-only  

# This tags current status as tag "0.1.0"  This is light tag,never use them
git tag 0.1.0 

# the following command should push all tags to the remote,never do it (not recommended):
git push --tags

#Tagging Later This enable you to add tag message and select a Hash for the tag. you get the hash from log
# frist you get the hash
git log --pretty=oneline
# second you tag the hash    
git tag -a 0.0.1  HASHSEQUENCE  

Pull a existing repository form github to local computer,my old way (ignore this)
#creat a local folder with the same name, do not add any file
# initilize it
git init
# add the remote
git remote add origin git@github.com:erenzaybay/gittest.git
# pull the change from the github
git pull origin master


Testing if github could be successfully connected
# testing the ssh authentication
ssh -T git@github.com


########################### THEORY AND KNOWLEDGE ###########################


Git Objects have 40 character SHA-1 hash, we usually use 7 character shortn version.

The concept of the staging area or the index is the place you have editted and added file that is ready to be commited  so edit file to add(stage) file  to commite file

recursive strategy   git move the pointed back then start to record the change,
this is adopted when there is change in both of the repositories

fast forward strategy   git just simply move the pointer of the head file,
this is adopted when there is change in only one of the repositories


gist is snipit of file you gererate and can be shared with other people ,
it is associate with your name but will not be shown in your github account profile
gist public and private  you can search for the public gist in github but not private one ,
but it is accessable by url if you know it

contributing in github
go to others github repository  and press fork, it would get their repository for you 
make a new branch and work on it 
work on something and change something , and commit
press green button which is a pull request

Usefull .gitignore file knowledge
https://help.github.com/articles/ignoring-files/
https://github.com/github/gitignore
https://github.com/github/gitignore/blob/master/Python.gitignore

Usefull git tip collections
https://github.com/git-tips/tips
