 
Recording Macro and calling Register

Press q and the register name character and record the content of the macro and press q to finish recording.
To call the register, press @ and then press the register name charactor
Recording Macro:    q{registername}{actions}q
Calling register: @{registername}
for example:
qaithis is the content of the macro(Esc)q      /recording macro (use 
@a                                    /calling the register
@@                                   /execute the last macro
:reg    checking the register , show all the register and their according actions


Using Marker:
Press m and the register name to record the position of the line       m{regisername}
To call the marker, press ' and the name of the marker             ‘{registername}


Using command line from the Vim without leaving the Vim
:!      anything following this will be executed as command line command
for example :!ls             /list the content of the directory



folding methods:



Manual fold:

zf5j   Fold the current line and the next 5 lines, 6 lines in total

zo open current folding where the cursor is

zO open everything

zc close current folding where the cursor is

zC close everything

zd delete fold

folding the current bracket:

1.place the cursor at the bracket
2.press zf%              % means current

zi enable or unenable folds, show folds or not show folds.

Automatic folding according to the syntax

:set foldmethod=syntax        :set fdm=syntax    they are the same

Using markers to fold:

:set fdm=maker         using marker method

:set foldmaker={{{,}}}






File structure,tab and windows:

Buffer:
:ls list all the file in the buffer , %a current buffer, # last visited buffer
:ls list all the file in the buffer , %a current buffer, # last visited buffer
:bn  go to the next buffer
:bp  go to the previous buffer
:b# go to the last buffer we visited 
:e filename  this loads a file into the buffer
:bd delete the current buffer
:bd 12   delete the buffer 12	


Tablets:

:tabe pathofthefile  It means tabedit  ,it opens a new tab
 
You can use split within the tab

gt      move one tab forward
gT     move one tab backward




Windows:

:vs pathofthefile (vsplite)       load a new file into the buffer and open a new window for it from the left    this is vertical split

Ctrl-w + L  go to the left window   using HJIK

Ctrl-w + H go to the right window

:sp pathofthefile   this split the window horizontally (scrren up and down)

Ctrl-w +  bigger by one vertically

Ctrl-w -  smaller by one vertically

Ctrl-w > bigger by one horizontally

Ctrl-w 10< smaller by one horizontally

Ctrl-w 10+   Ctrl-w 10-        Ctrl-w 10>     Ctrl-w 10<

Ctrl-w e        This equally distribute the window sizes

:sb14         open buffer 14 horrizontally

:vert sb14     open buffer 14 vertically









Practical Tips base on known knowledge

Replaceing all the target keyword within a bracket:
If you want to change all the occurrences in a bracket, do the following:
1.move the cursor to one of the bracket.
2.press v to enter the visual mode.
3.press % to make vim select all the content with in the bracket.
4.enter :s/Ember/Amber/gc             (g is global fag, c is confirm flag, it make you able to confirm all the change)
5.note:In reality , it would not show as :s/Ember/Amber/gc but rather '<,'>:s/Ember/Amber/gc


:r !curl --silent url       /This is very useful, it fetch the code from line directly to you file

:read !ls     /read the content of the directory into the current file


checking the spelling:
:set spell spelllang=en_us      /It check the spelling in english US,
=z                              / move the curser to the misspelled word, and use this to look for the right word. and press enter.
:set nospell                    / disableing the spell checker.


Less useful tips:

If you want to make all the indentation within the file corrent, you can select all the content of the file and press =, this would auto indent all the indentation correctly, for example in C,but maybe not in python. 
Or go to the top of the file and press =G . it would auto indent the whole file.

=3g correct the indents for the next 3 lines


