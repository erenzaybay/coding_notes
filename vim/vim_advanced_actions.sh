 
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

