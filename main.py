import cv2 as cv
import sys
import numpy as np
from matplotlib import pyplot as plt

def camara():
    cap = cv.VideoCapture(0, cv.CAP_V4L2)
    ret, frame = cap.read()
    cv.imwrite("teste.jpeg",frame)
    cap.release()
    
def color_range():
    aux = []
    name = []
    color = []
    f = open('Red.txt', 'r')
    n = f.readline()
    n = np.uint8(n)
    aux.append(n)
    n = f.readline()
    n = np.uint8(n)
    aux.append(n)
    n = f.readline()
    n = np.uint8(n)
    aux.append(n)
    n = f.readline()
    n = np.uint8(n)
    aux.append(n)
    n = f.readline()
    n = np.uint8(n)
    aux.append(n)
    n = f.readline()
    n = np.uint8(n)
    aux.append(n)
    f = open('Green.txt', 'r')
    n = f.readline()
    n = np.uint8(n)
    aux.append(n)
    n = f.readline()
    n = np.uint8(n)
    aux.append(n)
    n = f.readline()
    n = np.uint8(n)
    aux.append(n)
    n = f.readline()
    n = np.uint8(n)
    aux.append(n)
    n = f.readline()
    n = np.uint8(n)
    aux.append(n)
    n = f.readline()
    n = np.uint8(n)
    aux.append(n)
    f = open('Yellow.txt', 'r')
    n = f.readline()
    n = np.uint8(n)
    aux.append(n)
    n = f.readline()
    n = np.uint8(n)
    aux.append(n)
    n = f.readline()
    n = np.uint8(n)
    aux.append(n)
    n = f.readline()
    n = np.uint8(n)
    aux.append(n)
    n = f.readline()
    n = np.uint8(n)
    aux.append(n)
    n = f.readline()
    n = np.uint8(n)
    aux.append(n)
    
    f.close()

    color = [[aux[0], aux[1], aux[2]], [aux[3], aux[4], aux[5]],
             [aux[6], aux[7], aux[8]], [aux[9], aux[10], aux[11]],
             [aux[12], aux[13], aux[14]], [aux[15], aux[16], aux[17]]]#,
             #[aux[18], aux[19], aux[20]], [aux[21], aux[22], aux[23]]#,
             #[aux[24], aux[25], aux[26]], [aux[27], aux[28], aux[29]],
             #[aux[30], aux[31], aux[32]], [aux[33], aux[34], aux[35]],
             #[aux[36], aux[37], aux[38]], [aux[39], aux[40], aux[41]],
             #[aux[42], aux[43], aux[44]], [aux[45], aux[46], aux[47]]]

    name = ['Red','Green','Yellow']
    #name = ['Red','Green','Blue','Yellow','Brown','Orange','Violet','Black']
    return color,name
#colortable
def filterblur(image): #filtro blur

    blur = cv.blur(image, (5, 5))
    blur = cv.bilateralFilter(blur, 9, 75, 75)
     
    return blur

def MostrarImage(img,imagename):    #Mostra a imagem
    newimage = cv.resize(img,None, fx=1,fy=1) 
    cv.imshow(imagename,newimage)

def mask_funct(hsvFrame,l,u):
    lower = np.array(l,np.uint8)
    upper = np.array(u,np.uint8)
    mask = cv.inRange(hsvFrame,lower,upper)
    return mask
def masks(hsvFrame):
    color,array_mask = color_range()

    for k in range(int(len(array_mask))):
        array_mask[k] = mask_funct(hsvFrame,color[2*k],color[2*k+1])
    return array_mask


def countrs(arraymask,image):
    array,name = color_range()
    ar = 1500 

    for k in range(len(name)):
        contours, hierarchy = cv.findContours(arraymasks[k], cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        for pic, contour in enumerate(contours):
            area = cv.contourArea(contour)
            if (area > ar):
                x, y, w, h = cv.boundingRect(contour)
                cv.drawContours(image, contours, -1, (0, 255, 0), 5)
                image = cv.putText(image, name[k], (x, y), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1, cv.LINE_AA)
                print(area)
    return  image

#main
while(1):
    camara()
    name = 'teste.jpeg'
    image = cv.imread(name,5)
    imagecountrs = cv.imread(name)

    imagefilter = filterblur(image)
    hsvFrame = cv.cvtColor(imagefilter,cv.COLOR_BGR2HSV)
    arraymasks = masks(hsvFrame)

    image = countrs(arraymasks,imagecountrs)

    
    MostrarImage(image,"original")

    k = cv.waitKey(5)
    if k ==27:
        break
cap.release()
cv.destroyAllWindows()