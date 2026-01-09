users = {
    "admin": "admin123",     # Security issue: hardcoded password
    "guest": "guest"
}

def get_user(username):
    if username in users:
        return users[username]
    else:
        return None


def authenticate(username, password):
    if users.get(username) == password:
        return True
    return False
