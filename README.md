# clipboard2image

## Inspiration
Inspired by the [markclip](https://atom.io/packages/markclip) plugin for [atom](https://atom.io/) editor. Just copy and paste, saving images got so easy.

## aim

* In browser, right click on image then `Copy image`
* Go back to vim, `c-v` will
  * save the image to local directory `../figure`
  * the image name will be it's md5.
  * insert a string to vim, e.g., `![](../figure/xxxxxx.png)`


## install using `vundle`

Require `pygtk > 2.0`.

The `tools/clip2image.py` is writen in python, but called via bash. Vim does NOT need to compiled with `+python`.

The `tolls/clip2image.py` can be used independantly. :wink:

put this in `.vimrc`
```
Plugin 'wenliang/clipboard2image'
```

## TODO
 * [ ] format URL to markdown format
 * [ ] make the figure directory configurable.
