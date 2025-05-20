from flask import Blueprint, render_template, request, redirect, url_for, session

access_bp = Blueprint('access', __name__)

# Simulate session for this simple demo
# (We’ll store role in Flask session)

@access_bp.route("/secure/broken-access", methods=["GET", "POST"])
def secure_broken_access():
    message=""
    if request.method == "POST":
        username = request.form.get("username")
        if username == "admin":
            session["role"] = "admin"
            message = f"Welcome, Admin! Access Granted to {session.get('role')}!"
        else:
            session["role"] = "user"
            message = f"Access Denied!"
    return render_template("broken_access_login.html", mode="secure", message=message)

@access_bp.route("/secure/admin")
def secure_admin_page():
    message=""
    if session.get("role") != "admin":
        message = f"Welcome, Admin! Login success!"
    return render_template("broken_access_login.html", mode="secure", message=message)

@access_bp.route("/insecure/broken-access", methods=["GET", "POST"])
def insecure_broken_access():
    message=""
    if request.method == "POST":
        username = request.form.get("username")
        # Insecure: anyone can access /admin just by POSTing anything
        session["user"] = username
        message = f"Access Granted to {session.get('user', 'Unknown')}! (Insecure)"
    return render_template("broken_access_login.html", mode="insecure", message=message)
    
    

# @access_bp.route("/insecure/admin")
# def insecure_admin_page():
#     # No role check!
#     return f"Access Granted to {session.get('user', 'Unknown')}! (Insecure)"
