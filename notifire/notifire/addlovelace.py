import datetime
import threading
from time import sleep

from google.cloud import 


def quickstart_add_data_one():
    db = firestore.Client()
    # [START firestore_setup_dataset_pt1]
    doc_ref = db.collection(u'users').document(u'alovelace')
    doc_ref.set({
        u'first': u'Ada',
        u'last': u'Lovelace',
        u'born': 1815
    })
    # [END firestore_setup_dataset_pt1]

    # example of collecting data using python