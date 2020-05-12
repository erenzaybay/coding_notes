# Tricks

# search for blank lines
/\n\n   # search for blank line




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