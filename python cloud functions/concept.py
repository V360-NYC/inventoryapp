import firebase_admin
from firebase_admin import credentials, firestore, storage
import time
import datetime

cred = credentials.Certificate("C:\\Users\\OMKAR\google\\credentials\\kp-assist-4b13d9b7e9e5.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

collection_ref = db.collection('fileMeta/V65Xdo4EENQmDopi4GkCFiWh3oz2/masterFiles').order_by('created_at', direction=firestore.Query.DESCENDING).limit(1)


# for i in range(10):
#    print(time.time_ns())

print(datetime.datetime.strftime('%Y-%m-%dT%H:%M:%s.%sz'),'2021-06-26T04:29:31.079Z')