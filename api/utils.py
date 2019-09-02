from google.cloud import firestore
import os


def get_vars(name):
    if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/'):
        db = firestore.Client()
        doc_ref = db.collection(u"env_vars").document(u"z4o3OFwXqFRGs1BvHfwk")
        doc = doc_ref.get().to_dict()
        return doc[name]
    else:
        return os.getenv(name)
