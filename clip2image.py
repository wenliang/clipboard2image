#! /bin/python

import pygtk
pygtk.require('2.0')
import gtk
import hashlib

# get the clipboard
clipboard = gtk.clipboard_get()
image = clipboard.wait_for_image()

if image:
    fn_md5 = hashlib.md5(image.get_pixels()).hexdigest()
    image.save('%s.png' % (fn_md5), 'png')
else:
    print('No image in clipboard')
