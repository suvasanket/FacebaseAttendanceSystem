import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://studentsattendance-7cd66-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')
data = {
    "21DIS139":
        {
            "name": "Suva Sanket Rout",
            "dept": "ist",
            "starting_year": 2021,
            "total_attendance": 7,
            "sec": "B",
            "year": 3,
            "last_attendance_time": "2024-02-11 00:54:34"
        },
    "21DIS210":
        {
            "name": "Elon Musk",
            "dept": "ist",
            "starting_year": 2021,
            "total_attendance": 12,
            "sec": "B",
            "year": 3,
            "last_attendance_time": "2024-01-11 00:54:34"
        },
}

for key, value in data.items():
    ref.child(key).set(value)