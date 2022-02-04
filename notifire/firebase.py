import firebase_admin
import time
from datetime import timedelta
from uuid import uuid4

from firebase_admin import firestore, initialize_app
from firebase_admin import credentials

# Use the application default credentials
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
  'projectId': "cen4010group10-3b7e9",
})

db = firestore.client()

__all__ = ['send_to_firebase', 'update_firebase_snapshot']

initialize_app()

def send_to_firebase(raw_notification):
    db = firestore.client()
    start = time.time()
    db.collection('notifications').document(str(uuid4())).create(raw_notification)
    end = time.time()
    spend_time = timedelta(seconds=end - start)
    return spend_time


def update_firebase_snapshot(snapshot_id):
    start = time.time()
    db = firestore.client()
    db.collection('notifications').document(snapshot_id).update(
        {'is_read': True}
    )
    end = time.time()
    spend_time = timedelta(seconds=end - start)
    return spend_time