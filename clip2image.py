#! /bin/python

import pygtk
pygtk.require('2.0')
import gtk
import hashlib

import os

# folder to save
# TODO: will make this a parameter passed in
DIR_FIG = '../figure'
if not os.path.exists(DIR_FIG):
    os.makedirs(DIR_FIG)

# get the clipboard
clipboard = gtk.clipboard_get()
# reference: http://www.pygtk.org/pygtk2reference/class-gtkclipboard.html

image = clipboard.wait_for_image()

if image:
    fn_md5 = hashlib.md5(image.get_pixels()).hexdigest()
    link_image = '%s/%s.png' % (DIR_FIG, fn_md5)
    image.save(link_image, 'png')
    print('![](%s)' % (link_image))
    exit(0)

text = clipboard.wait_for_text()
if text:
    # just return itself
    print(text)
    exit(0)
else:
    exit(1)
