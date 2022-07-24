from time import sleep
import time
import cv2
import mss
import translators as ts
import numpy
import pytesseract as pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from tkinter import *  
  

root = Tk()

label = Label(text='Попчка', font=("Arial Bold", 18))
label.pack()

monitoring_screen = {"top": 890, "left": 650, "width": 635, "height": 190}
sct = mss.mss()
white = numpy.array([255,255, 255])
text1 = ""


while(True):
    time.sleep(0.1)
    img = numpy.asarray(sct.grab(monitoring_screen))
    temp = pytesseract.image_to_string(img)
    if (text1 != temp):
        text1 = temp
        label.config(text=ts.google(text1, from_language='en', to_language='ru'))
        root.update()
        
    
    
    

