import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{'databaseURL':"https://faceattendencerealtime-12203-default-rtdb.firebaseio.com/"})
ref =db.reference("Emp")

data={
    "1":
    {
      "NAME":"MODI",
      "DEPT":"CSE",
      "EMPID":"1",
      "ATTENDENCE":10,
      "LEAVE-LEFT":15
    },
     "2":
    {
      "NAME":"RATAN TATA",
      "DEPT":"MECH",
      "EMPID":"2",
      "ATTENDENCE":12,
      "LEAVE-LEFT":15
    },
     "3":
    {
      "NAME":"ELON",
      "DEPT":"CSE",
      "EMPID":"3",
      "ATTENDENCE":15,
      "LEAVE-LEFT":15
    },
     "4":
    {
      "NAME":"DHRUV",
      "DEPT":"CSE",
      "EMPID":"4",
      "ATTENDENCE":14,
      "LEAVE-LEFT":15
    }

    
}
for key,value in data.items():
    ref.child(key).set(value)