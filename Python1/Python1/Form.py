from tkinter import *
class Handler:
   def _init_(self,start):
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
   def ConvertToPixels(image):
      from PIL import Image
      pixels = {}
      paint = Image.open(image)
      paint = paint.convert("P")
      pixels = paint.histogram()
      return pixels   
   pixels = ConvertToPixel(image)
root = Tk()
Handler(root)   
   # def GetNumbers():
   # def CompareNumbers(numbers,usernumbers):








