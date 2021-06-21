import cv2
import sys
import numpy as np


def nothing(x):
    pass


def writetxt(filename, hMin, sMin, vMin, hMax, sMax, vMax):

    # convert values to string
    str_hMin = str(hMin)
    str_sMin = str(sMin)
    str_vMin = str(vMin)
    str_hMax = str(hMax)
    str_sMax = str(sMax)
    str_vMax = str(vMax)

    file = open(filename, 'w')
    file.write(str_hMin)
    file.write("\n")
    file.write(str_sMin)
    file.write("\n")
    file.write(str_vMin)
    file.write("\n")
    file.write(str_hMax)
    file.write("\n")
    file.write(str_sMax)
    file.write("\n")
    file.write(str_vMax)
    file.close()


# Create a window
cv2.namedWindow('image')

# create trackbars for color change
cv2.createTrackbar('HMin', 'image', 0, 179, nothing) # Hue is from 0-179 for Opencv
cv2.createTrackbar('SMin', 'image', 0, 255, nothing)
cv2.createTrackbar('VMin', 'image', 0, 255, nothing)
cv2.createTrackbar('HMax', 'image', 0, 179, nothing)
cv2.createTrackbar('SMax', 'image', 0, 255, nothing)
cv2.createTrackbar('VMax', 'image', 0, 255, nothing)

# Set default value for MAX HSV trackbars.
cv2.setTrackbarPos('HMax', 'image', 179)
cv2.setTrackbarPos('SMax', 'image', 255)
cv2.setTrackbarPos('VMax', 'image', 255)

# Initialize to check if HSV min/max value changes
hMin = sMin = vMin = hMax = sMax = vMax = 0
phMin = psMin = pvMin = phMax = psMax = pvMax = 0


cap = cv2.VideoCapture(0, cv2.CAP_V4L2)
ret, frame = cap.read()
cv2.imwrite("teste.jpeg",frame)
cap.release()

img = frame
output = frame
waitTime = 33

while(1):

    # get current positions of all trackbars
    hMin = cv2.getTrackbarPos('HMin', 'image')
    sMin = cv2.getTrackbarPos('SMin', 'image')
    vMin = cv2.getTrackbarPos('VMin', 'image')

    hMax = cv2.getTrackbarPos('HMax', 'image')
    sMax = cv2.getTrackbarPos('SMax', 'image')
    vMax = cv2.getTrackbarPos('VMax', 'image')

    # Set minimum and max HSV values to display
    lower = np.array([hMin, sMin, vMin])
    upper = np.array([hMax, sMax, vMax])

    # Create HSV Image and threshold into a range.
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower, upper)
    output = cv2.bitwise_and(img, img, mask=mask)

    # Print if there is a change in HSV value
    if( (phMin != hMin) | (psMin != sMin) | (pvMin != vMin) | (phMax != hMax) | (psMax != sMax) | (pvMax != vMax) ):
        print("(hMin = %d, sMin = %d, vMin = %d), (hMax = %d, sMax = %d, vMax = %d)" % (hMin, sMin, vMin, hMax, sMax, vMax))
        phMin = hMin
        psMin = sMin
        pvMin = vMin
        phMax = hMax
        psMax = sMax
        pvMax = vMax


    # Display output image
    cv2.imshow('image', output)

    # Wait longer to prevent freeze for videos.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    if cv2.waitKey(1) & 0xFF == ord('s'):
        zinput = str(input("Nome da cor a guardar: "))
        nameform = []
        nameform.append(zinput)
        nameform.append('.txt')
        filename = ''.join(nameform)
        writetxt(filename, hMin, sMin, vMin, hMax, sMax, vMax)

cv2.destroyAllWindows()