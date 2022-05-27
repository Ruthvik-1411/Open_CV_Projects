''' Python code for face tracking application
 using pan/tilt mechanism.
 By Ruthvik @nagasairuthvik1919@gmail.com
 '''

import cv2
import serial
import time

print('---- Starting Process ----')
# Setting up serial communication
ard = serial.Serial('COM5', 9600)
time.sleep(2)
print('Process Started')
# Importing haar cascade classifier
haar = cv2.CascadeClassifier('../Open cv/haarcascades/haarcascade_frontalface_default.xml')
text = 'ADMIN'
color = (0, 255, 255)

# Function to draw bounding box on the image around the face


def mark_face_v2(img, x, y, w, h):
    factor = round((1.0*h)/(9*22), 1)
    xx = int(x+(w/2))
    yy = int(y+(h/2))
    cv2.circle(img, (xx, yy), 1, color, -1)
    for each in range(0, 10, 2):
        cv2.line(img, (x+(each*(round(w/9))), y), ((x+((each+1)*(round(w/9)))), y), color, 4)
        cv2.line(img, (x+(each*(round(w/9))), y+h), ((x+((each+1)*(round(w/9)))), y+h), color, 4)
        cv2.line(img, (x, y+(each*round(h/9))), (x, y+((each+1)*(round(h/9)))), color, 4)
        cv2.line(img, (x+w, y+(each*round(h/9))), (x+w, y+((each+1)*(round(h/9)))), color, 4)
    cv2.rectangle(img, (x+round((2*w/9)), y+h+round((0.2*h/9))), (x+w-round((2*w/9)), y+h+round((1.5*h/9))), color, -1)
    cv2.putText(img, text, (x+round((2.3*w/9)), y+h+round((1.2*h/9))), cv2.FONT_HERSHEY_COMPLEX, color=(0, 0, 0), fontScale=factor, thickness=2)
# Selecting video capturing device
cap = cv2.VideoCapture(0)

'''This part of the code reads the video
and applies haar cascade to detect faces.
After detecting the faces it marks them
and sends the coordinates of center of the face to arduino.
The data is sent serially in the form X230Y230
where 230,230 are coordinates. The process is terminated by hitting esc key.
'''
while True:
    ret, frame = cap.read()

    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = haar.detectMultiScale(gray_img, 1.4)
    for (x, y, w, h) in faces:
        mark_face_v2(frame, x, y, w, h)
        xx = int(x+(w/2))
        yy = int(y+(h/2))
        print('Face: {},{}'.format(xx, yy))
        data = str("X{0:d}Y{1:d}".format(xx, yy))
        ard.write(data.encode())

    cv2.imshow('Video Stream', frame)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
print('----Ending Process----')
time.sleep(2)
print('Process Ended')
