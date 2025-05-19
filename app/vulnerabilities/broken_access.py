from flask import Blueprint, render_template, request, redirect, url_for, session

access_bp = Blueprint('access', __name__)

# Simulate session for this simple demo
# (We’ll store role in Flask session)

@access_bp.route("/secure/broken-access", methods=["GET", "POST"])
def secure_broken_access():
    if request.method == "POST":
        username = request.form.get("username")
        if username == "admin":
            session["role"] = "admin"
        else:
            session["role"] = "user"
        return redirect(url_for("access.secure_admin_page"))
    return render_template("broken_access_login.html", mode="secure")

@access_bp.route("/secure/admin")
def secure_admin_page():
    if session.get("role") != "admin":
        return "Access Denied. Admins only!"
    return "Welcome, Admin! This is a protected page."

@access_bp.route("/insecure/broken-access", methods=["GET", "POST"])
def insecure_broken_access():
    if request.method == "POST":
        username = request.form.get("username")
        # Insecure: anyone can access /admin just by POSTing anything
        session["user"] = username
        return redirect(url_for("access.insecure_admin_page"))
    return render_template("broken_access_login.html", mode="insecure")

@access_bp.route("/insecure/admin")
def insecure_admin_page():
    # No role check!
    return f"Access Granted to {session.get('user', 'Unknown')}! (Insecure)"
