from functools import wraps
from flask import session, redirect, url_for

# rôles
roles = {
    "admin": ["dashboard", "settings"],
    "user": ["dashboard"]
}

# Vérif des perms
def role_required(role):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            username = session.get('username')
            if username and role in roles.get(username, []):
                return func(*args, **kwargs)
            return "Accès refusé", 403
        return wrapper
    return decorator

# Road protégée par rôle
@app.route('/settings')
@role_required('admin')
def settings():
    return "Page des paramètres réservée aux administrateurs."
