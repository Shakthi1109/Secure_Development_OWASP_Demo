from flask import Blueprint, render_template, request, redirect, url_for, session

identification_auth_bp = Blueprint("identification_auth", __name__)


# Insecure Route
@identification_auth_bp.route("/insecure/identification-authentication", methods=["GET", "POST"])
def insecure_identification():
    error = ""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["admin123"]
        # Insecure: hardcoded credentials
        if username == "admin" and password == "password":
            return redirect(url_for("identification_auth.insecure_welcome"))
        else:
            error = "Invalid credentials"
    return render_template("identification_authentication.html", mode="insecure", error=error)


# Secure Route
@identification_auth_bp.route("/secure/identification-authentication", methods=["GET", "POST"])
def secure_identification():
    error = ""
    valid_users = {"admin": "StrongPass123"}
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if valid_users.get(username) == password:
            session["user"] = username
            return redirect(url_for("identification_auth.secure_welcome"))
        else:
            error = "Invalid credentials"
    return render_template("identification_authentication.html", mode="secure", error=error)

@identification_auth_bp.route("/insecure/welcome")
def insecure_welcome():
    return render_template("welcome.html", mode="insecure")

@identification_auth_bp.route("/secure/welcome")
def secure_welcome():
    if "user" not in session:
        return redirect(url_for("identification_auth.secure_identification"))
    return render_template("welcome.html", mode="secure")

@identification_auth_bp.route("/secure/logout")
def secure_logout():
    session.pop("user", None)
    return redirect(url_for("identification_auth.secure_identification"))

@identification_auth_bp.route("/insecure/logout")
def insecure_logout():
    return redirect(url_for("identification_auth.insecure_identification"))
