import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

class DB:
    cred = credentials.Certificate('guest-only-29465-firebase-adminsdk-ie677-df4e47c6e5.json')
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    url = ""
    cnt = 0
    data = {}
    doc_ref = db.collection('Guest').document('0')
    def getURL(self, u, ctr):
        self.url = u
        self.cnt = ctr
        self.doc_ref.set({
                "url": self.url,
                "permission": 0
            })
