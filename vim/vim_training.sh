# Vim Training

# Basic editing


j
k	# move cursor down a character
h	# move cursor left a character
l	# move cursor right a character

w   # move forward one word, cursor at the first letter, seprating words by logic
W   # move forward one word, cursor at the first letter, seprating words by space
e   # move forward one word, cursor at the last letter, seprating words by logic
E   # move forword one word, cursor at the last letter, seprating words by space
b   # move afterward one word, cursor at the first letter,seprating words by logic
B   # move forward on real word,cursor at the first letter,seprating words by space

$   # move to the end of the line
0   # move to the beginning of the line, the real beginning
^   # move to the beginning of the line, the first none-space letter

gg  # move to the beginning of the file
G   # move to the end of the file,it is <shift-g>
{   # move to the last paragraph
}   # move to the next paragraph


# navigating reletive position 
Ctrl +d  # it means down, It jumps half a screen down
Ctrl +u  # it means up, It jumps half a screen up
Ctrl +f  # it means full, It jumps full screen down
Ctrl + b # it means backwards, It jumps full screenup
M # move cursor to the middle of the current screen
H # move cursor to the head of the current screen
L # move cursor to the last line of the current screen
3L  #   3 lines above the bottom
3H  #   3 lines below the head

# navigating window position
zt # this command will modify the current window so that the current cursor position will stay on top of the screen
zb # this command will modify the current window so that the current cursor position will stay on the bottom of the screen
zz # this command will modify the current window so that the current cursor position will stay in the middle of the screen

# searching
f         # it means find word begin with target letter fa find the first word begin with a within the current line, it only searches forward
F         # same with f, but works backwards
t         # it also looks for word begin with target letter, but it puts cursor before the word
T         # same with t, but works backwards
/function <Enter> # search for word "function",cursor at the next instance down

n                 #  go to next search result
N                 #  go to last search result
:nohl             # it means no hight light , it remove the highlighted search result
?function <Enter> #  search for word "function",cursor at the next instance up

# editing
x         # delete the letter at the current cursor

o         # start a new line below and into the insert mode
O         # start a new line above and into the insert mode
p         # paste
P         # paste before the cursor , which is extremly useful,it is <shift+p>

dw        # delete the word at the cursor when you delete stuff , they are also copied
db        # delete the word before the cursor
d0 # delete everything before the cursor of current line.
d^ # delete everything before the cursor till first non space character of current line.

cw # change the current word, delete the word at the current cursor and into the insert mode
cb # change the last word, delete the word before the cursor and into the insert mode
c0 # change everything before the cursor of current line.
c^ # change everything before the cursor till first non space character of current line.

yw # yank word, y stands for yank, means copy
yb # yank the word before the current cursor
y0 # yank everything before the cursor of current line
y^ # yank everythin befor the cursor till first non space character of current line

d/target <Enter> # delete until the word "target"
c/target <Enter> # change until the word "target"
y/target <Enter> # yank until the word "target"

dd        # delete the current line
cc        # change the current line
yy        # copy the current line

.         # repeat the last action
u         # undo your last action
<ctrl-u>  # cancel the last undo

#navigation with repeater
3G         # go to line 3
3gg        # go to line 3 
:3 <Enter> # go to line 3

2fw # find the second "w" in current line
2b  # move 2 word back
2e  # move 2 word forword cursor at the end of the word
2j  # move 2 cursor down
2k  # move 2 cursor up
2h  # move 2 cursor left
2l  # move 2 cursor right
2dw # delete 2 words forward
2db # delete 2 words back
2dd # delete 2 lines down
2cc # change 2 lines down


ct" #  change until "                  
ci" #  change inside the "
ca" change around " This would include both of the ""

# replacement
:s  # stand for substitute 
%  # stand for the whole file
/g # g stands for global

:s/Ember/Amber    # replace Ember to Amber in current line
:%s/Ember/Amber   # replace Ember to Amber in the whole file , but it only replace the first occurrence of the word Ember
:%s/Ember/Amber/g # replace Ember to Amber in the whole file ,every single one of them



# indentation and folds

# >> # one indentation
# << # one indentation back

3>> # indent current line and next 2 lines from the current line


# selection
# You can you Ctrl-T and Ctrl-D to indent and indxent back,but it is not supported in cmder
# In visual mode, you can jump to the other end of the visual selection by pressing o
:v # enter visual mode to selected part you wish to indent, edit, or delete.
:vl # visual line mode
gv  # reselect the part you selected in visual mode


# command:

# writing files
:w!   # use ! to overide :w! when needed
:wq   # write and quit
:q    # quit withou writing
:q!   # quit discard any changes
:help :s   # This shows the help file for the command :s ,using help file can be usefull.


#show invisable characters
:set list         This would list the invisable characters (tavs   newline )  ^I is tab  $ is newline
:set nolist       hid the effect of set list


#advanced

 
# Recording Macro and calling Register
# Press q and the register name (one character)
# and then record the content of the macro and press q to finish recording.
q{registername}{actions}{back to normal mode} # Recording Macro  
# To call the register, press @ and then press the register name charactor
@{registername}           # Calling register
@@                        # calling the last register
:reg                      # checking the register , list all registers and their according actions

# Using Marker:
# Press m and then register name (one charater)
m{registername}           #Press m and the register name to record the position of the line   
# to call the register press ' then press the register name

# Using command line from the Vim without leaving the Vim
:!{commands}      # anything following this will be executed as command line command

# Manual fold:
:set fdm = manual # foldmethod = manual 
zf5j   # fold current and 5 lines down,6 lines in total
zf5k   # fold current and 5 lines up, 6 lines in total
zo     # open current folding where the cursor is
zO     # open recursivly all folds nested in current fold
zc     # close current folding where the cursor is
zC     # close this fold uptill the hightest folder , but not sibling if opend.(important)
zd     # delete folder
zf%    #Fold current bracket,place the cursor at the bracket  % means current, it fold lines.
zi     # enable or unenable folds, show folds or not show folds.
zf     # select in visual mode and fold them with zf

# Markers fold:
:set fdm=marker # foldmethod = marker
:set foldmaker={{{,}}} # between {{{ and }}}

#File structure,tab and windows:

# Buffer:
vim a.py b.py c.py # commandline mode , load all three fils into the buffer
:e  {filename} # loads a file into the buffer
:ls # list all the file in the buffer, %a means current buffer, # means the last buffer
:bn # go to the next buffer
:bp # go to the previous buffer
:b# # go to the last buffer we visited 
:bd # delete the current buffer
:bd {number} # delete the buffer {number}	
:e# # load the last deleted buffer back

# Tablets:
# closing the table by :wq doesn't move the file off buffer
:tabe {pathofthefile} # means tabedit, opens a new tab
gt   # move one tab forward
gT   # move one tab backward

# Windows vertical split:
:vs {pathofthefile}    # means vertial splite, load or make a new file as a window into the buffer on the left. 
Ctrl-w + l # go to the left window
Ctrl-w + h # go to the right window
Ctrl-w >  # bigger by one horizontally
Ctrl-w <  # smaller by one horizontally
Ctrl-w {reapeter} > # bigger by {reapeter} horizontally
Ctrl-w {reapeter} < # smaller by {repeater} horizontally

# Windows split:
:sp {pathofthefile}    # means splite, load or make a new file as a window into the buffer on the bottom. 
Ctrl-w + j # go to the lower window
Ctrl-w + k # go to the upper window
Ctrl-w +  # bigger by one vertically 
Ctrl-w -  # smaller by one vertically 
Ctrl-w {reapeter} + # bigger by {reapeter} horizontally
Ctrl-w {reapeter} - # smaller by {repeater} horizontally
Ctrl-w = #        This equally distribute the window sizes
Ctrl-w r # Swap top/bottom or left/right split
Ctrl-w o # Close every window in the current tabview but the current one
:sb2         #open buffer 2 horrizontally
:vert sb2    #open buffer 2 vertically

