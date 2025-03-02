# Firestore JSON Uploader

## Overview
This Python script uploads JSON files to a Firestore collection using the Firebase Admin SDK. It is designed for users who need to batch-upload structured data into Firestore.

## Features
- Reads JSON files and uploads them to Firestore.
- Uses Firebase Admin SDK for authentication.
- Supports customizable Firestore collection and document structure.
- Skips missing files and logs progress.

## Prerequisites
- Python 3.x installed on your system.
- Firebase Admin SDK installed.
- A valid `serviceAccountKey.json` file for Firebase authentication.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/firestore-json-uploader.git
   cd firestore-json-uploader
   ```
2. Install dependencies:
   ```bash
   pip install firebase-admin
   ```
3. Place your Firebase service account key in the project directory and update the script:
   ```python
   cred = credentials.Certificate("path/to/your/serviceAccountKey.json")
   ```
4. Modify the Firestore collection reference as needed:
   ```python
   collection_ref = db.collection("your_collection").document("your_document").collection("your_subcollection")
   ```

## Usage
1. Add your JSON files (e.g., `document1.json`, `document2.json`, etc.) in the project directory.
2. Run the script:
   ```bash
   python upload_to_firestore.py
   ```
3. The script will upload data and display progress logs.

## Notes
- Ensure your Firebase project is properly configured with Firestore.
- JSON files should have a structure compatible with Firestore.
