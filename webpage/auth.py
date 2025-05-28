from flask import redirect, url_for, flash, session
from functools import wraps

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            flash("you need to log in first")
            return redirect(url_for('login_get'))
        return f(*args, **kwargs)
    return decorated_function