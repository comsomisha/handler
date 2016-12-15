from tkinter import *
from tkinter.filedialog import *
from Module import Module

 
class Handler:
   def __init__(self,start):
    self.start = start
    self.start.title("Number recognition")
    self.start.geometry('300x300')
    self.OpenButton = Button(self.start, text = 'Open File', command = self.ConvertToPixels)
    self.OpenButton.pack(side = BOTTOM)
    self.Result = Text(font=('times',12),width=15,height=15)
    self.Result.pack(side = LEFT, fill=BOTH)
    self.Setting = Text(font=('times',12),width=15,height=15)
    self.Setting.pack(side = LEFT, fill=BOTH)
    self.start.mainloop()
   def ConvertToPixels(self):
      from PIL import Image
      op = askopenfilename()
      im = Image.open(op)
      newim = Image.new("RGB",im.size)
      newim.paste(im)
      im2 = Image.new("P",im.size)
      im = newim.convert("P")

      temp = {}

      for x in range(im.size[1]):
       for y in range(im.size[0]):
         pix = im.getpixel((y,x))
         temp[pix] = pix
         if pix == 220 or pix == 225 or pix == 227: 
          im2.putpixel((y,x),255)
      str1 = Module.SearchNumbers(im2)
      self.Result.insert(1.0,str1)
      Handler.CompareNumbers(self,op)
   def CompareNumbers(self,op):
      x = int(self.Result.get(1.0,END))
      y = int(self.Setting.get(1.0,END))
      if x!=y and  y!="":
       Module.ChangeSamples(op);
root = Tk()              
Handler(root)  








