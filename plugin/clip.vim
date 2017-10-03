function! Clip2Image()
	silent execute "! python ${HOME}/.vim/bundle/clipboard2image/tools/clip2image.py ../figure"
    read /tmp/clip2image.temp
endfunc
command! Clip call Clip2Image()

map <c-s-i> :call Clip2Image()<CR><c-l>
imap <c-s-i> <ESC>:call Clip2Image()<CR><c-l>
