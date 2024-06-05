import cv2
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{'databaseURL':"https://faceattendencerealtime-12203-default-rtdb.firebaseio.com/",
                                    'storageBucket':"faceattendencerealtime-12203.appspot.com"})
ref =db.reference("Emp")

folderpath='images'
imgpathlist=os.listdir(folderpath)
Empid=[]
imagelist=[]
for path in imgpathlist:
        imagelist.append(cv2.imread(os.path.join(folderpath,path)))
        Empid.append(os.path.splitext(path)[0])
        filename=f'{folderpath}/{path}'
        bucket=storage.bucket()
        blob=bucket.blob(filename)
        blob.upload_from_filename(filename)
        #print(path)
#print(len(imagelist))
print(Empid)
def findEncodings(imagelist):
        encodelist=[]
        for img in imagelist:
                img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB) 
                encode=face_recognition.face_encodings(img)[0]
                encodelist.append(encode)
        return encodelist
print("Encoding Started...")
encodelistknown=findEncodings(imagelist)
print(encodelistknown)
encodelistknownwithIds=[encodelistknown,Empid]
print("Encoding Complete")
file=open("EncodeFile.p",'wb')
pickle.dump(encodelistknownwithIds, file)
file.close()
print("file saved")