#! /bin/python

import pygtk
pygtk.require('2.0')
import gtk
import hashlib

import os

def convert(DIR_FIG='../figure'):

    # get the clipboard
    clipboard = gtk.clipboard_get()
    # reference: http://www.pygtk.org/pygtk2reference/class-gtkclipboard.html

    image = clipboard.wait_for_image()
    if image:

        # folder to save
        if not os.path.exists(DIR_FIG):
            os.makedirs(DIR_FIG)

        fn_md5 = hashlib.md5(image.get_pixels()).hexdigest()
        link_image = '%s/%s.png' % (DIR_FIG, fn_md5)
        image.save(link_image, 'png')
        return '![](%s)' % (link_image)

    text = clipboard.wait_for_text()
    if text:
        # TODO: if url

        # just return itself
        return text

    return None

if __name__ == "__main__":
    import sys
    this_str = convert(sys.argv[1])
    if this_str:

        # below works for pygtk > 2.2
        # gtk.Clipboard.set_text(this_str)

        # with open('/tmp/clip2image.temp','w') as f:
        #    f.write(this_str)

        print(this_str)
