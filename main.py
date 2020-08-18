import pyrebase
import ToDB
class Storing:
    def __init__(self, x):
        self.cnt = x
        config={
            "apiKey": "AIzaSyCSahwiwsABLqLCTpNQuGgrfcMsX9cc550",
            "authDomain": "guest-only-29465.firebaseapp.com",
            "databaseURL": "https://guest-only-29465.firebaseio.com",
            "projectId": "guest-only-29465",
            "storageBucket": "guest-only-29465.appspot.com",
            "messagingSenderId": "612514515145",
            "appId": "1:612514515145:web:a8cc88d85d73368686a518",
            "measurementId": "G-4J4F3X1YXN"
        }
        fbase = pyrebase.initialize_app(config)
        storage = fbase.storage()
        path_on_cloud = "images/guest_{}.png".format(self.cnt)
        local_path = "opencv_frame_{}.png".format(self.cnt)
        storage.child(path_on_cloud).put(local_path)
        self.url = storage.child(path_on_cloud).get_url(0)
        ob=ToDB.DB()
        ob.getURL(self.url, self.cnt)

