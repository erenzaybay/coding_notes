# Basic editing

# navigatin basic movement: 
j	# move cursor up a character  
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


