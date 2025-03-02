import firebase_admin
from firebase_admin import credentials, firestore
import json
import os

# Initialize Firebase Admin SDK
cred = credentials.Certificate("path/to/your/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

# Get Firestore database
db = firestore.client()

# Define document names (Modify this list as needed)
document_names = [
    "document1",
    "document2",
    "document3",
    "document4"
]

# Firestore collection reference (Modify for your Firestore setup)
collection_ref = db.collection("your_collection").document("your_document").collection("your_subcollection")

# Upload data to Firestore
for doc_name in document_names:
    file_path = f"{doc_name}.json"
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            data = json.load(file)
            collection_ref.document(doc_name).set(data)
            print(f"Uploaded {doc_name}.json to Firestore")
    else:
        print(f"Warning: {doc_name}.json not found, skipping upload.")

print("Data upload process completed!")
