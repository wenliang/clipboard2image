function! Clip2Image()
    read ! python ${HOME}/.vim/bundle/clipboard2image/tools/clip2image.py ../figure 2> /dev/null
endfunc
command! Clip call Clip2Image()

" not working: c-v, conflict with column edit mode
" not working: c-s-i, why c-i also works?
map <F2> :call Clip2Image()<CR><c-l>
imap <F2> <ESC>:call Clip2Image()<CR><c-l>
