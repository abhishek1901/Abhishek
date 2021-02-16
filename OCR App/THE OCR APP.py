from tkinter import *
import tkinter as tk
from tkinter import filedialog, Text
from PIL import Image,ImageTk
import pytesseract as pt
from pytesseract import Output
import cv2
import numpy as np


counter = 0

def choose_file():

    global filepath, img_resize
    filepath = filedialog.askopenfilename(initialdir = 'E:\\',title = 'Select an Image',filetypes = (('JPG','*.jpg'),('All files','*.*')))
    img = cv2.imread(filepath)
    img_resize = cv2.resize(img,(500,500))
    cv2.imshow('Image', img_resize)
    cv2.waitKey(0) 
    
def autocrop():
    global transform1 

    img_gray = cv2.cvtColor(img_resize, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.GaussianBlur(img_gray,(5,5),0)
    ret,img_thresh = cv2.threshold(img_blur,180,255,cv2.THRESH_BINARY)
    canny = cv2.Canny(img_thresh,150, 300)


    contour, heirarchy = cv2.findContours(canny,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    areas = [cv2.contourArea(c) for c in contour]
    max_index = np.argmax(areas)
    max_contour = contour[max_index]

    perimeter = cv2.arcLength(max_contour, True)
    coordinates = cv2.approxPolyDP(max_contour, 0.01*perimeter, True)
    
    pt1 = np.array([coordinates[1], coordinates[0], coordinates[2], coordinates[3]], np.float32)
    pt2 = np.array([(0,0), (700,0), (0,600) , (700,600)], np.float32)

    perspective = cv2.getPerspectiveTransform(pt1, pt2)
    transform1 = cv2.warpPerspective(img_resize, perspective, (700,600))
    

    cv2.imshow('Transformed', transform1)
    cv2.waitKey(0)
    

    return(transform1)




def mancrop():

    global transform2
    pts = []
    
    

    def crop(event, x, y, flags, param):
        
        if event == cv2.EVENT_LBUTTONDOWN:
            if (x,y) is not None:
                pts.append((x,y))
                

            if len(pts) == 4:
                print(pts)
                pt_1 = np.array([pts[0], pts[1], pts[3], pts[2]], np.float32)
                pt_2 = np.array([(0,0), (700,0), (0,600), (700,600)], np.float32)
                perspective1 = cv2.getPerspectiveTransform(pt_1, pt_2)
                transform2 = cv2.warpPerspective(img_resize, perspective1, (700,600)) 
                cv2.imshow('Transformed', transform2)
                close('Transformed')
                
                return(transform2)
 
    cv2.namedWindow('Image')
    cv2.imshow('Image', img_resize)
    
    cv2.setMouseCallback('Image', crop)
    

    

def ocr():

    pt.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    global data

  
    if autocrop() is None:
        img = mancrop()
    
    elif mancrop() is None:
        img = autocrop()

    img_gray = cv2.cvtColor(img_resize, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.GaussianBlur(img_gray,(5,5),0)
    ret,img_thresh = cv2.threshold(img_blur,170,300,cv2.THRESH_BINARY)

    data =  pt.image_to_string(img_thresh)
    

    text = pt.image_to_data(img_thresh, output_type=Output.DICT)

    no_word = len(text['text'])

    for i in range(no_word):
        if int(text['conf'][i]) > 50:
            x,y,width,height = text['left'][i], text['top'][i], text['width'][i], text['height'][i]
            cv2.rectangle(img_resize, (x,y), (x+width, y+height), (0,255,0), 2)
            cv2.imshow('OCR-operated',img_resize)
            
    

def showtext():
    content = data
    textbox = tk.Frame(frame,bg = '#FDFFD6')
    textbox.place(relx = 0.2,rely = 0.2,relwidth =0.6,relheight =0.6)
    text_frame = Text(textbox,bg = '#FDFFD6')
    text_frame.insert('1.0',content)
    text_frame.pack()

def save():
    global counter
    global image_resize
    counter+=1
    cv2.imwrite('image_'+str(counter) + '.jpg', my_image)


    


def exit_app():
    root.quit()



root = tk.Tk()

canvas = tk.Canvas(root,height = 800,width = 800,bg = 'green') 
canvas.pack()

frame = tk.Frame(root,bg = 'white')
frame.place(relx = 0.2,rely = 0.1,relwidth =0.6,relheight =0.6)

label=tk.Label(frame,text='TEXT DETECTOR   ',fg='green',bg='white',font=('Arial',20))
label.place(relx=0.28,rely=0.1)


openfile = tk.Button(canvas,text = 'Choose a File',fg = 'blue',padx = 10,pady = 5,command = choose_file )
openfile.place(x = 50 , y = 600)

auto_crop = tk.Button(canvas,text = 'Auto Crop',fg = 'green',padx = 10,pady = 5,command = autocrop)
auto_crop.place(x = 370 ,y = 600)

manual_crop = tk.Button(canvas,text = 'Manual Crop',fg = 'purple',padx = 10,pady = 5,command = mancrop)
manual_crop.place(x = 215 ,y = 600)


OCR_btn = tk.Button(canvas,text = '    OCR   ',fg = 'brown',padx = 10,pady = 5, command = ocr)
OCR_btn.place(x = 500, y = 600)

show_txt_btn = tk.Button(canvas,text = 'Show Text',fg = 'violet',padx = 10,pady = 5, command = showtext)
show_txt_btn.place(x = 640, y = 600)

save_btn = tk.Button(canvas,text = 'Save',fg = 'orange',padx = 10,pady = 5, command = save)
save_btn.place(x = 50, y = 700)

exit_btn = tk.Button(canvas,text = 'Exit',fg = 'red',padx = 10,pady = 5, command = exit_app)
exit_btn.place(x = 700, y = 700)

root.mainloop()