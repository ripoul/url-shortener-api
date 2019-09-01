from google.cloud import firestore
from google.auth.exceptions import DefaultCredentialsError
import os

def get_vars(name):
    try:
        db = firestore.Client()
        env_vars = db.collection(u'env_vars').document(u'z4o3OFwXqFRGs1BvHfwk')
        return env_vars[name]
    except DefaultCredentialsError:
        return os.getenv(name)