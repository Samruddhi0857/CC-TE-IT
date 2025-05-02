from flask import Flask, request, jsonify, send_from_directory
import firebase_admin
from firebase_admin import auth, credentials, firestore  # Import Firestore

app = Flask(__name__, static_url_path='', static_folder='static')

# Initialize Firebase Admin SDK
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred)

# Initialize Firestore
firestore_client = firestore.client()

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/verifyToken', methods=['POST'])
def verify_token():
    try:
        id_token = request.json.get('idToken')
        decoded_token = auth.verify_id_token(id_token)
        uid = decoded_token['uid']
        email = decoded_token['email']

        # Save to Firestore
        user_ref = firestore_client.collection('users').document(uid)
        user_ref.set({
            'email': email
        })

        return jsonify({"status": "success"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400
