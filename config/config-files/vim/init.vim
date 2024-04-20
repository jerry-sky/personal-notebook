
set title
set number

set path+=**
set wildmenu

set formatoptions=tcqrn1
set tabstop=4
set shiftwidth=4
set softtabstop=4
set expandtab
set noshiftround

set clipboard+=unnamedplus

nnoremap j jzz
nnoremap k kzz
nnoremap { {zz
nnoremap } }zz
nnoremap G Gzz
nnoremap <C-d> <C-d>zz
nnoremap <C-u> <C-u>zz
map , @@
nnoremap < @:


function Runman(n)
    for i in range(1, a:n)
        execute "normal @@"
    endfor
endfunction


function Runmanx(n, macro)
    for i in range(1, a:n)
        execute "normal " . a:macro
    endfor
endfunction


function! TitlePath(path)
    let l:bufname = a:path
    let l:max_length = 50
    let l:buflen = len(l:bufname)
    if l:buflen > l:max_length
        let l:short_bufname =  '...' . strpart(l:bufname, l:buflen - l:max_length + 3)
    else
        let l:short_bufname = l:bufname
    endif
    return l:short_bufname
endfunction


set titlestring=%r\ %t\ \ %{TitlePath(expand('%f'))}:%l

