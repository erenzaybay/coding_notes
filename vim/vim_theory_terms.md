
# Knowledge:

Vim is a fancy text editor with superpower.

These notes are based on Venture into vim course provided by tutsplus

## .vimrc introduction

* .vimrc is a vim configuration file that saves your vim preference.

* .vimrc file in windows is located in the user directory C:\Users\erenzaybay\.vimrc

* .vimrc file in linux is located in the user folder ~\.vimrc

## 4 Modes

There are three mode:

* i    insert mode for inserting

* v    visual mode for yanking

* vl   visual line mode yanking

* Esc  normal mode, aka command mode for giving command

## Terms

* Repeater: numbers can be used as repeater.

* Buffer:Buffer is a place in memory, which is showed as a list of files , you need to save the file to goto the next buffer.

* Tabs and Windows: When opening tabs and windows, the tabs are one level higher in structural logic.Basically windows are nested in tabs.

* .swp files: the temporarily save files that exists only when there is an abnormal exit, you can retrieve unsaved file from the file, and you need to manually remove the file when they are not useful any more.

## Notation

Notation used in this note ( the same is used in vim official doc file ):

* dap: in sequence , press d , then a then p

* <C-n>: hold down Ctrl and then n at the same time

* G<C-n>: press and release G, then press Ctrl and n at the same time

* placeholders: {motion} {a-zA-z} {char} {int} {repeater} {register_name}

* \<Esc>  Escape key
* \<CR>  Carriage return key or enter key
* \<Ctrl>   Ctrl key
* \<Tab> tab key
* \<Shift> shift key
* \<S-Tab> press the shift and tab key at the same time
* \<space> space bar
* Using space as indication of mode change: cw replacement \<Esc>

## Things to remember
write :set fdm=marker not :set fdm = marker  (no space)