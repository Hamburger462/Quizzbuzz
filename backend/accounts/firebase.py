import firebase_admin
from firebase_admin import credentials
import os

_firebase_app = None


def initialize_firebase():
    global _firebase_app

    if _firebase_app:
        return _firebase_app

    if firebase_admin._apps:
        _firebase_app = firebase_admin.get_app()
        return _firebase_app

    path = os.getenv("FIREBASE_SECRET_KEY")

    if not path:
        raise RuntimeError("Missing Firebase service account path")

    cred = credentials.Certificate(path)

    _firebase_app = firebase_admin.initialize_app(cred)

    return _firebase_app