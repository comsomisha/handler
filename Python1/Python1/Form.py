from tkinter import *
class Handler:
   start = Tk()
   start.title("Number recognition")
   start.geometry('300x300')
   def ConvertToPixels(image):
      from PIL import Image
      pixels = {}
      paint = Image.open(image)
      paint = paint.convert("P")
      pixels = paint.histogram()
      return pixels   
   pixels = ConvertToPixel(image)








