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
# Register a new user
def register_user(first_name, last_name, dob, email, username, password):
    hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    user_data = {
        "first_name": first_name,
        "last_name": last_name,
        "dob": dob,
        "email": email,
        "username": username,
        "password": hashed_pw
    }
    users_collection.insert_one(user_data)
