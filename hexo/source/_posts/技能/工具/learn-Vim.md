---
title: learn-Vim
date: 2020-10-03 16:47:04
tags:
- Vim
- Editor
categories:
- 技能
- 工具
mathjax: true
---

some usage tips.

<!--more-->


# 1 Install and Basics 
## 1.1 install
`sudo apt-get update && do apt-get install vim`

## 1.2 Basic Usage
Just run `vimtutor` and complete it.

## 1.3 Basic Config
### 1.3.1 temporary runtime
Use the `:set ${setting}` command in line mode, press `tab` for auto-completion, e.g. `set number`.

Use `:help ${setting}` if needed.

### 1.3.2 permanent runtime
Vim loads `/etc/vim/vimrc`(and possibly some other global files) as default runtime configurations. To add user-specific runtime configs/commands, append commands to `~/.vimrc` file. A typical setting is 
```vim
set nocompatible "vi features only under compatible mode"

"visual"
colorscheme default
set number "line number"
set cursorline
filetype on 
syntax on "enable vim sytax-highlighting" 

"format"
set cindent "indent standard"
set tabstop=4 "tab indent amount"
set noexpandtab
set shiftwidth=4 "auto indent amount"

"search"
set history=1000
set hlsearch
set incsearch
set showmatch

"file"
set encoding=utf-8
set nobackup
set noundofile "use at your own risk"
```

# 2 Plugin 
## 2.0 Plugin Manager
### Vim-plug
Download `plug.vim` and put it in `~/.vim/autoload/`, for example
```bash
curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
	"https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim"
```

See comments in `vim ~/.vim/autoload/plug.vim` (or Github readme) for tutorial. A typical usage:
```vim
call plug#begin('~/.vim/plugged')

" make sure to use single quotes "
Plug 'vim-airline/vim-airline'
Plug 'altercation/vim-colors-solarized'

call plug#end()
```

## 2.1 Visual plugins
### colorscheme
Note: run `cp ~/.vim/plugged/vim-colors-solarized/colors -r ~/.vim/` after `:PlugInstall`
```vim
Plug 'altercation/vim-colors-solarized'

": let g:solarized_termtrans = 1 " adapt the terminal transparency
let g:solarized_visibility = "high"
let g:solarized_termcolors=256 "for terminal usage, must degrade 16bit gui color to 8bit terminal color

colorscheme solarized
```

## 2.2 Markdown plugins
Add plugin via Vim-plug (which is called in `vimrc`) 

Use `:help vim-markdown` or `markdown-preview`.

```vim
Plug 'plasticboy/vim-markdown'
Plug 'iamcco/markdown-preview.vim'
Plug 'iamcco/mathjax-support-for-mkdp'

"vim-markdown config
let g:vim_markdown_math = 1
let g:vim_markdown_strike_through = 1
let g:vim_markdown_new_list_item_indent = 4

" markdown-preview.vim config
nmap <silent> <F8> <Plug>MarkdownPreview        "for normal mode
imap <silent> <F8> <Plug>MarkdownPreview        "for insert mode
nmap <silent> <F9> <Plug>StopMarkdownPreview    "for normal mode
imap <silent> <F9> <Plug>StopMarkdownPreview    "for insert mode
```


## 2.3 $\LaTeX$ plugins

### 2.3.1 vimtex

#### 2.3.1.1 install & config

```vim
"Tex Support{{{
Plug 'lervag/vimtex'
let g:tex_flavor='lualatex'
let g:vimtex_view_method='zathura'
" let g:vimtex_quickfix_mode=0
" set conceallevel=1
" let g:tex_conceal='abdmg'
"}}}
```

To specify $\TeX$ verison, add `% ! TEX program = <xxx_tex>` as the first line.

`man zathurarc` to learn to specify zathura behavior.

```vim
# .config/zathura/zathurarc
# zathurarc
set render-loading false

# colors
set statusbar-bg "#000000"
set statusbar-fg white

# settings
set window-height 1024
set window-width 768
set adjust-open width

# use sqlite as bookmarks database backend
# set database sqlite

# key bindings
map <PageUp> navigate previous
map <PageDown> navigate next

map + zoom in
map - zoom out

map <C-q> quit

```

#### 2.3.1.2 basic usage

- `:h vimtex` help
- `\ll` complie
- `\lk` stop
- `\lc`,`\lC` clean


#### 2.3.1.3 Highlighting problems

**Problem** : If `$`, `_`, ... appear in `lstlisting` environment, the following highlighting would be terribly missformed.

**Solve** : add these vim commands to `~/.vim/after/syntax/tex.vim`(vim post-processing feature, see `:h after-directory`)

```vim
syn region texZone start=+\\begin{lstlisting}+ end=+\\end{lstlisting}\|%stopzone+
" other syn groups like texMathZoneA can be used, though.
" %stopzone is a zone-closing keyword for vimtex 
```

**Steps** : 

1. `:h syntax`, read `syntax.txt:syn-define` 

**Further** :

```vim
syn region texZone  start="\\lstinputlisting" end="{\s*[a-zA-Z/.0-9_^]\+\s*}"
syn match texInputFile "\\lstinline\s*\(\[.*\]\)\={.\{-}}" contains=texStatement,texInputCurlies,texInputFileOpt
" \{-} repeat as few as possible
```

#### 2.3.1.4 live preview

It **seems** that `vimtex` only compiles when file is written to disk, so there's never a 'live' preview.

Still, auto saving by `autocmd TextChanged,TextChangedI <buffer> silent write` will make vimtex 'live'. BUT, multiple compilations triggered by frequent changes really mess things up.

**NOTE**: This command automatically WRITES file, be cautious!


### 2.3.2 latex-live-preview

No auto write, controllable update frequency. BAD quickfix support.

#### 2.3.2.1 install & config

```vim
Plug 'xuhdev/vim-latex-live-preview', { 'for': 'tex' }
let g:livepreview_previewer = 'zathura -c ~/.config/zathura/'
let g:livepreview_engine = 'xelatex' " . ' [options]'
" <cr> for carriage-return
nmap <silent> <F10> :LLPStartPreview<cr>
imap <silent> <F10> <Esc>:LLPStartPreview<cr>
autocmd Filetype tex setl updatetime=500
```

#### 2.3.2.2 basic usage

- `:LLPreview` preview



# 4

## 4.4 syntax hilite

---
basics:

syntax alias: `:syntax`, `:syn`, `:sy`

Toggle syntax:
- current file: `:sy enable`,`:sy clear`
- all buffers: `:sy on`,`:sy off`

Set filetype: `:set filetype=C`

syntax rules location: `$VIMRUNTIME/syntax/${language}.vim`

---

define syntax: 
- keyword: `:sy keyword key1 key2` (untested)
- match: `:sy match $grp +regex+ [contains=grp1,grp2,...]`
- region: `:sy region $grp start=+regex+ end=+regex+ [contains=grp1,grp2,...]` 
- cluster: `:sy cluster $cluster contains=grp1,grp2`

---

define hilite

`hi grp cterm=cyan guifg=#144026`, `hi def link grp`

---

**further customize**

post processing

`:h after-directory`

`~/.vim/after/syntax/${language}.vim`


new filetype

`:h filetype`

```vim
augroup filetypedetect
autocmd BufNewFile,BufRead *.my setfiletype my
augroup END
```
