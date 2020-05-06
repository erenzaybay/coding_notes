 

Basic editing:


to view a file in read only mode 

view filename

use ! to overide :w! when needed



using help file can be usefull:  :help :s   This shows the help file for the command :s

Ctrl +d it means down, It jumps half a screen down
Ctrl +u it means up, It jumps half a screen up
Ctrl +f it means full, It jumps full screen down
Ctrl + b it means backwards, It jumps full screenup

M move cursor to the middle of the current screen
H move cursor to the head of the current screen
L move cursor to the last line of the current screen

3L     3 lines above the bottom
3H     3 lines below the head

zt this command will modify the current window so that the current cursor position will stay on top of the screen
zb this command will modify the current window so that the current cursor position will stay on the bottom of the screen
zz  this command will modify the current window so that the current cursor position will stay in the middle of the screen




Indentation and folds

>>     it is one indentation

<<  it is one indentation back

3>> indent current line and next 2 lines from the current line

You can enter visual mode to selected part you wish to indent

In visual mode, you can jump to the other side of the visual selection by pressing o

You can you Ctrl-T and Ctrl-D to indent and indent back,but it is not supported in cmder

gv reselect the part you selected in visual mode



Basic movement: 
j	move cursor up a character  
k	move cursor down a character
h	move cursor left a character
l	move cursor right a character

w move forward one word, cursor at the first letter
b move afterward one word, cursor at the first letter
e move forward one word, cursor at the last letter
B move forward on real word, ignoring the punctuation marks, it is <shift-b>

$ move to the end of the line
0 move to the beginning of the line, the real beginning
^ move to the beginning of the line, the first none-space letter

gg move to the beginning of the file
G   move to the end of the file,it is <shift-g>
{  move to the last paragraph
} move to the next paragraph

x delete the letter at the current cursor
u undo your last action
<ctrl-u> cancel the last undo
. repeat the last action

o start a new line below and into the insert mode
O start a new line above and into the insert mode
p paste
P paste before the cursor , which is extremly useful,it is <shift+p>

f  it means find word begin with target letter fa find the first word begin with a within the current line, it only searches forward
F same with f, but works backwards
t it also looks for word begin with target letter, but it puts cursor before the word
T same with t, but works backwards

/    this search for word          
/function <Enter> search for word "function"

n  go to next search result
N go to last search result
:nohl  it means no hight light , it remove the highlighted search result

so you have to goto the top of the file if you hope to search the full file

? backward search 
?function <Enter>   search for word "function"

d  delete  when you delete stuff , they are also copied
dw delete the word at the cursor 
db delete the word before the cursor

d/target <Enter>  delete until the word "target"
c/target <Enter>  change until the word "target"
y/target <Enter>  change until the word "target"

cw change the current word, delete the word at the current cursor and into the insert mode
cb change the last word, delete the word before the cursor and into the insert mode
dd delete the current line
cc change the current line
yy copy the current line , y stands for yank, means copy
yw yank word
y0 yank everything before the cursor





11G goto line 11

3gg and 3G all goto the third line form the top of the file
:14             go to line 14



2fw 2b 2e 2j 2k   repeater actions
2dw 2db
5dd 7cc

/\n\n  this search for black line
Basic commanline:
:set list         This would list the invisable characters (tavs   newline )  ^I is tab  $ is newline

:set nolist       hid the effect of set list


Advanced editing topics:
Advanced content change:

ct"   change until "                      
"this is a test"         

ci"  change inside the "
"this is a test"

ca" change around " This would include both of the "
"this is a test"

REPLACEMENT:
s stand for substitute 
% stand for the whole file
/g g stands for global

:s/Ember/Amber   replace Ember to Amber in current line
:%s/Ember/Amber replace Ember to Amber in the whole file , but it only replace the first occurrence of the word Ember
:%s/Ember/Amber/g replace Ember to Amber in the whole file ,every single one of them
You do not have to go to the top of the file to make it work
