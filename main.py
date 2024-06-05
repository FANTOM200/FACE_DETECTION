import cv2
import os
import face_recognition
import pickle
import numpy as np
import cvzone
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{'databaseURL':"https://faceattendencerealtime-12203-default-rtdb.firebaseio.com/",
                                    'storageBucket':"faceattendencerealtime-12203.appspot.com"})
cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
imgBackground= cv2.imread('Resources/background.png')
folderModePath='Resources/Modes'
modePathList=os.listdir(folderModePath)
imgModeList=[]
for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath,path)))
#Load the encoded files
file=open('EncodeFile.p','rb')
encodelistknownwithIds=pickle.load(file)
file.close()
encodelistknown,Empid=encodelistknownwithIds
#print(Empid)
print("Encode file loaded")
while True:
    success, img = cap.read()
    imgS=cv2.resize(img,(0,0),None,0.25,0.25)
    imgS=cv2.cvtColor(imgS,cv2.COLOR_BGR2RGB) 
    facecurframe=face_recognition.face_locations(imgS)
    encodecurframe=face_recognition.face_encodings(imgS,facecurframe)
    imgBackground[162:162 +480, 55:55 +640]=img
    imgBackground[44:44 + 633,808:808 + 414]=imgModeList[0]
    for encodeface,faceLoc in zip(encodecurframe,facecurframe):
        matches=face_recognition.compare_faces(encodelistknown,encodeface)
        facedist=face_recognition.face_distance(encodelistknown,encodeface)
        print("Matches",matches)
        matchindex=np.argmin(facedist)
        if matches[matchindex]:
           # print("Face detected")
           y1,x2,y2,x1=faceLoc
           y1,x2,y2,x1=y1*4,x2*4,y2*4,x1*4
           bbox=55+x1,162+y1,x2-x1,y2-y1



           imgBackground=cvzone.cornerRect(imgBackground,bbox,rt=0)
        
            

    
    #cv2.imshow("Webcam ", img)
    cv2.imshow("Face Attendence",imgBackground)
    cv2.waitKey(1)






