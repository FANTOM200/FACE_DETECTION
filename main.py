import cv2
import face_recognition
cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
imgBackground= cv2.imread('Resources/FACE ATTENDENCE (1).png')


while True:
    success, img = cap.read()
    imgBackground[200:200+480,432:432+640]=img
    #cv2.imshow("Webcam ", img)
    cv2.imshow("Face Attendence",imgBackground)
    cv2.waitKey(1)
