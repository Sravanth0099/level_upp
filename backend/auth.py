import bcrypt
from db import users_collection

# Check if username and password match
def authenticate_user(username, password):
    user = users_collection.find_one({"username": username})
    if user:
        # Passwords are hashed, so check with bcrypt
        if bcrypt.checkpw(password.encode('utf-8'), user['password']):
            return True
    return False
