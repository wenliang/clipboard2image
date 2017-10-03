function! Clip2Image()
	silent execute "! python /home/lwl/project/clipboard2image/clip2image.py ../figure"
    read /tmp/clip2image.temp
endfunc
command! Clip call Clip2Image()

map <c-v> :call Clip2Image()<CR><c-l>
imap <c-v> <ESC>:call Clip2Image()<CR><c-l>
