function! Clip2Image()
    read ! python ${HOME}/.vim/bundle/clipboard2image/tools/clip2image.py ../figure 2> /dev/null
endfunc
command! Clip call Clip2Image()

map <c-s-i> :call Clip2Image()<CR><c-l>
imap <c-s-i> <ESC>:call Clip2Image()<CR><c-l>
