<h1 align="center">Vertical Image Scroller</h1>

<font size="3">

<a href="https://github.com/Aeonss/VerticalImageScroller/releases/latest/">VerticalImageScroller</a> is a custom python class which creates seamless scrollable vertical images using Tkinter. Originally created for webtoon/manga chapters, but can be adapted for anything else.


## 🔨 &nbsp; Installation
Install python:
``` bash
https://www.python.org/downloads/
```

Download source file and add to your project folder
``` bash
https://github.com/Aeonss/VerticalImageScroller/blob/main/VerticalScroller.py
```

## 🚀 &nbsp; Usage


Get figure information with figure id
``` bash
from VerticalScroller import ImageScroller

...
window = tk.Tk()
frame = ImageScroller(window, path=IMAGE_FOLDER_PATH, scrollbarwidth=15, width=WIDTH, height=HEIGHT, speed=SCROLL_SPEED)
```

## 📘 &nbsp; License
VerticalImageScroller is released under the [MIT license](https://github.com/Aeonss/VerticalImageScroller/blob/main/LICENSE.md).

</font>