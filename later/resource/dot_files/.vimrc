"This is how you comment on a .vimrc file

set number       " it shows the number on the left collum

"searching related
set incsearch    " start searching from the first character of the search string. more characters will refine the match
set ignorecase   " ingnore the upper or lowwer case when you search
set hlsearch     " high light the search result

"look and color related
syntax enable    " enable the systax color without vim overriding you own settings ,'syntax on' comtrast
colorscheme monokai " using monokai using the method of 'https://github.com/sickill/vim-monokai' it did not work cmder

"setting tab to 4 spaces
"best explanation  http://vimcasts.org/episodes/tabs-and-spaces/
"best explanation https://federico-lox.github.io/development/tabs-stop-the-truth-about-vim-tab-spaces.html
"I don't fully understand my current tab and space settings
set tabstop=4    "showing existing tab with 4 spaces width
set shiftwidth=4  "when indenting with '>',use 4 spaces
set expandtab "when pressing tab,insert 4 spaces
"set smartindent   " should I use smartindent or not?



"keybinding,           don't overdo it and don't overrule vim's own major keys
" key map the kj to Esc in insert  mod to avoid pressing Esc all the time
inoremap kj <Esc>
" key map the kj to Esc in command mod to avoid pressing Esc all the time
cnoremap kj <Esc>


" To correctly encode and decode chinese characters
set fileencodings=utf-8,gbk,utf-16le,cp1252,iso-8859-15,ucs-bom
set termencoding=utf-8
set encoding=utf-8
