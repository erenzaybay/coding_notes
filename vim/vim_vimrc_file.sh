# .vimrc:




# alway and vital

#setting indentation to 4 spaces, look for more answers
#current answer comes from https://stackoverflow.com/questions/234564/tab-key-4-spaces-and-auto-indent-after-curly-braces-in-vim
# don't use smartindent
filetype plugin indent on  # all of the "filetype","plugin", and "indent" is on , why???
set expandtab              # sets indentation to a certain number of spaces 
set tabstop=4              # makes new tab with 4 spaces width, expandtab should be set before using the feature
set shiftwidth=4           # when indenting with '>', use 4 spaces width



# always in .vimrc
:set number         #show line numbers of the file, it could be added to the .vimrc file
#:set foldmethod=syntax  :set fdm=syntax    they are the same Automatic folding according to the syntax
:set foldmethod=marker  :set fdm=maker         using marker method  Using markers to fold:
:set foldmaker={{{,}}}  #set the marker to be the designated symbols.



# situational .vimrc
:se ft=python       # This set the file type to python highlight
:retab  # change all the existing tab characters to match the current tab settings



# never .vimrc
:set smartindent  # (not recomented,why) it puts cursor at the right position when you press enter at any time,for example ,when you are in a function


# wtf is this
#:set softtabstop=4 
# :set noexpandtab      