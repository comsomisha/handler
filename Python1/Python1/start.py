from PIL import Image
import hashlib
import time

im = Image.open("examples/12581.gif")
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
    
im2.save("output.gif")

inletter = False
foundletter=False
start = 0
end = 0

letters = []


for y in range(im2.size[0]): 
  for x in range(im2.size[1]): 
    pix = im2.getpixel((y,x))
    if pix != 255:
      inletter = True

  if foundletter == False and inletter == True:
    foundletter = True
    start = y

  if foundletter == True and inletter == False:
    foundletter = False
    end = y
    letters.append((start,end))

  inletter=False

count = 0
for letter in letters:
  m = hashlib.md5()
  im3 = im2.crop(( letter[0] , 0, letter[1],im2.size[1] ))
  line = "%s%s"%(time.time(),count)
  m.update(line.encode('utf-8'))
  im3.save("numbers/%s.gif"%(m.hexdigest()))
  count += 1