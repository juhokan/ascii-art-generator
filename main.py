import tkinter as tk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import PIL.Image

# Change characters for different results
ASCII_CHARS = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."]

def toGreyscale(image):
    return image.convert("L")

def generateAscii(image):
    pixels = image.getdata()
    asciiStr = ""

    for pixel in pixels:
        if pixel // 25 == 10:
            asciiStr += " "
        else:
            asciiStr += ASCII_CHARS[pixel // 25]
    return asciiStr

def splitAsciiStr(asciiStr, imgWidth):
    asciiImg = ""
    asciiStrLen = len(asciiStr)

    # Split string based on image width to create ascii image
    for i in range(0, asciiStrLen, imgWidth):
        asciiImg += asciiStr[i:i + imgWidth] + "\n"
    
    return asciiImg

def saveAsciiToFile(asciiImg):
    with open("ascii.txt", "w") as f:
        f.write(asciiImg)

# UI for selecting file
def selectFile():
    path = fd.askopenfilename()
    try:
        image = PIL.Image.open(path)

        greyscaleImage = toGreyscale(image)

        #Change the maxSize for higher resolution
        maxSize = (50, 50)
        greyscaleImage.thumbnail(maxSize, PIL.Image.ANTIALIAS)

        asciiStr = generateAscii(greyscaleImage)
        imgWidth = greyscaleImage.width

        asciiImg = splitAsciiStr(asciiStr, imgWidth)
        
        saveAsciiToFile(asciiImg)

        showinfo(title='Success', message='Image converted and ASCII saved to ascii.txt')

    except Exception as e:
        showinfo(title='Error', message=f'Unable to convert image: {e}')

# Base application
root = tk.Tk()
root.title('ASCII Art Generator')
root.geometry('300x150')

openButton = tk.Button(
    root,
    text='Open File',
    command=selectFile
)

openButton.pack(expand=True)

root.mainloop()