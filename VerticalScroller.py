# Referenced from: https://stackoverflow.com/a/56046307

import tkinter as tk
import os
from PIL import ImageTk, Image

# Custom infinite seamless vertical image scroller using Tkinter Canvas and Scrollbar
class ImageScroller(tk.Frame):
    def __init__(self, master=None, **kw):
        
        # Initialization
        self.path = kw.pop('path', None)
        self.width = kw.pop('width', None)
        self.height = kw.pop('height', None)
        self.bg = kw.pop('bg', None)
        sw = kw.pop('scrollbarwidth', 10)
        super(ImageScroller, self).__init__(master=master, **kw)
        self.canvas = tk.Canvas(self, width=self.width, height=self.height, bg=self.bg, highlightthickness=0, **kw)
        
        # List of images
        self.images = []
        
        # Fill the frame with images
        if self.path != "":
            self.fill()
        
        # Create vertical scrollbar
        self.v_scroll = tk.Scrollbar(self, orient='vertical', width=sw)

        # Grid and configure weight
        self.canvas.grid(row=0, column=0,  sticky='nsew')
        self.v_scroll.grid(row=0, column=1, sticky='ns')
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        
        # Set the scrollbars to the canvas
        self.canvas.config(yscrollcommand=self.v_scroll.set)
        
        # Set canvas view to the scrollbars
        self.v_scroll.config(command=self.canvas.yview)

        # Scroll to go through canvas
        self.canvas.config(scrollregion=self.canvas.bbox('all'))
        self.canvas.bind_class(self.canvas, "<MouseWheel>", self.mouse_scroll)
        self.canvas.bind("<Button-4>", self.mouse_scroll)
        self.canvas.bind("<Button-5>", self.mouse_scroll)
        
        # Click to drag through canvas
        self.canvas.bind("<Button-1>", self.start_scroll)
        self.canvas.bind("<B1-Motion>", self.update_scroll)
        self.canvas.bind("<ButtonRelease-1>", self.stop_scroll)

    # Mouse scroll handling
    def mouse_scroll(self, event):
        # Linux uses event.num
        if event.num == 4 or event.delta > 0:
            self.canvas.yview_scroll(-3, "units" )
            
        # Windows / Mac
        elif event.num == 5 or event.delta < 0:
            self.canvas.yview_scroll(3, "units" )
            
            
    # Mouse drag handling
    # https://shortrecipes.blogspot.com/2014/05/python-3-and-tkinter-scroll-canvas-with.html
    def start_scroll(self, event):
        self.canvas.config(yscrollincrement=3) 
        self.canvas.config(xscrollincrement=3) 
        self._starting_drag_position = (event.x, event.y)
        
        # https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/cursors.html
        self.canvas.config(cursor="hand2")
    
        
    def update_scroll(self, event):  
        deltaX = event.x - self._starting_drag_position[0]
        deltaY = event.y - self._starting_drag_position[1]
        self.canvas.xview('scroll', deltaX, 'units')
        self.canvas.yview('scroll', deltaY, 'units')
        self._starting_drag_position =  (event.x, event.y)
           
        
    def stop_scroll(self, event):
        self.canvas.config(xscrollincrement=0) 
        self.canvas.config(yscrollincrement=0)
        self.canvas.config(cursor="")
        
        
        
    # Fills the frame with images from the folder path
    def fill(self):
        # Gets all images from directory and adds to list
        for name in os.listdir(self.path):
            img = Image.open(os.path.join(self.path, name))
            
            # Rescales all images to width
            if img.width != self.width:
                scale = img.height / img.width
                img = img.resize((self.width, int(self.width * scale)), Image.Resampling.LANCZOS)

            # Adds to list to prevent garbage collection
            self.images.append(ImageTk.PhotoImage(img))
        
        height = 0
        # Creates each image and updates the height to place next image
        for i in range(len(self.images)):
            self.canvas.create_image(0, height, anchor=tk.NW, image=self.images[i])
            height = height + self.images[i].height()
            


if __name__ == "__main__":
    # Create window
    window = tk.Tk()
    window.title("MangaReader")
    
    # Insert path to folder of images here
    path = "C:\Solo Leveling\Chapter 0"
    
    frame = ImageScroller(window, path=path, scrollbarwidth=15, width=720, height=800, bg="white")
    frame.pack()
    window.mainloop()
