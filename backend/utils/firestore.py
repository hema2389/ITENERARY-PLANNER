import firebase_admin
from firebase_admin import credentials, firestore
import os

db = None
cred_path = os.getenv("FIREBASE_ADMIN_SDK_CREDENTIALS")

if cred_path:
    cred = credentials.Certificate(cred_path)
    if not firebase_admin._apps:
        firebase_admin.initialize_app(cred)
    db = firestore.client()
else:
    print("WARNING: FIREBASE_ADMIN_SDK_CREDENTIALS not set. Firestore database not initialized.")

def add_document(collection: str, data: dict):
    """Adds a new document to the specified collection."""
    doc_ref = db.collection(collection).document()
    doc_ref.set(data)
    return doc_ref.id

def get_document(collection: str, document_id: str):
    """Retrieves a document from the specified collection."""
    doc_ref = db.collection(collection).document(document_id)
    doc = doc_ref.get()
    if doc.exists:
        return doc.to_dict()
    return None

def update_document(collection: str, document_id: str, data: dict):
    """Updates an existing document in the specified collection."""
    doc_ref = db.collection(collection).document(document_id)
    doc_ref.update(data)

def delete_document(collection: str, document_id: str):
    """Deletes a document from the specified collection."""
    db.collection(collection).document(document_id).delete()
