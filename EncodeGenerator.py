import cv2
import face_recognition
import pickle
import os

folderpath='images'
imgpathlist=os.listdir(folderpath)
Empid=[]
imagelist=[]
for path in imgpathlist:
        imagelist.append(cv2.imread(os.path.join(folderpath,path)))
        Empid.append(os.path.splitext(path)[0])
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