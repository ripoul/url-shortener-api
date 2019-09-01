from google.cloud import firestore
from google.auth.exceptions import DefaultCredentialsError
import os


def get_vars(name):
    try:
        db = firestore.Client()
        doc_ref = db.collection(u"env_vars").document(u"z4o3OFwXqFRGs1BvHfwk")
        doc = doc_ref.get().to_dict()
        return doc[name]
    except DefaultCredentialsError:
        return os.getenv(name)
