function! Clip2Image()
    read ! python ${HOME}/.vim/bundle/clipboard2image/tools/clip2image.py ../figure 2> /dev/null
endfunc
command! Clip call Clip2Image()

" not working: c-s-i, conflict with neocomplete
" not working: c-v, conflict with column edit mode
map <c-s-r> :call Clip2Image()<CR><c-l>
imap <c-s-r> <ESC>:call Clip2Image()<CR><c-l>
