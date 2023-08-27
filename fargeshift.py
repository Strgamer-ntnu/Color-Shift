import glob
from PIL import Image
import math
from tkinter import filedialog
from tkinter.filedialog import askopenfile

def make_gif(frame_folder):
    #makes a gif from images
    frame_one = frames[0]
    gifpath = filedialog.asksaveasfilename(defaultextension=".gif")
    frame_one.save(gifpath, format="GIF", append_images=frames,
    save_all=True, duration=100, loop=0)

def farge_shift(path,num):
    global lastImage
    if 'jpg' in path[-4:]:
        end='.jpg'
    elif 'JPG' in path[-4:]:
        end='.jpg'
    else:
        end='.png'
    imgname=path[:-4]
 
    #opens image first time, loads last image otherwise
    if num!=0:
        img=lastImage
    else:
        img = Image.open(path)

    #loads pixels and makes new image
    pixels = img.load()
    newimg = Image.new('RGB', (img.width, img.height))
    newpixels = newimg.load()

    #changes the r,g,and b values
    for i in range(img.width):
        for j in range(img.height):
            try:
                r, g, b = pixels[i, j]
                if r>235:r=235
                if g>235:g=235
                if b>235:b=235
                newpixels[i, j] =((r+r_gain),(g+g_gain),(b+b_gain))
            except:
                #runs if the image has alpha values
                r,g,b,a= pixels[i,j]
                if r>235:r=235
                if g>235:g=235
                if b>235:b=235
                newpixels[i, j] =((r+r_gain),(g+g_gain),(b+b_gain),a)
    #adds new image to frames list, and updates last image
    frames.append(newimg)
    lastImage=newimg
    #saves filler images if needed
    if savefiller:
        navn=savepath+str(num)+end
        newimg.save(navn)

def upload_file():
    #lets the user upload an image, and returns the path to the image
    f_types = [('PNG Files', '*.png'),('JPG Files', '*.jpg')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    return filename

#sets the gain for each color value
r_gain=1
g_gain=18
b_gain=2

#15, 189, 21

path=upload_file()
imgname=path.split('/')[-1][:-4]

#decides if and where temporary images will be saved (only to preview progress)
savepath='savedimage/output/filler/'+imgname
savefiller=False

#declares lastImage
lastImage=''


#adds the first image to frames
frames=[]
frames.append(Image.open(path))
#makes images
for a in range(41):
    farge_shift(path,a)

#makes gif
make_gif("/path/to/images")
