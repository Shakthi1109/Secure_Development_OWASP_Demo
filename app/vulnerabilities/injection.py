from flask import Blueprint, render_template, request

injection_bp = Blueprint('injection', __name__)

@injection_bp.route("/secure/injection", methods=["GET", "POST"])
def secure_injection():
    message = ""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == "admin" and password == "admin123":
            message = "Access Granted!"
        else:
            message = "Invalid credentials (secure)"
    return render_template("injection.html", vuln="Injection", mode="secure", message=message)

@injection_bp.route("/insecure/injection", methods=["GET", "POST"])
def insecure_injection():
    message = ""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        # Fake SQL injection vulnerability simulation
        if "'" in username or "--" in username:
            message = "SQL Injection Successful! Login bypassed!"
        else:
            message = "Invalid credentials (insecure)"
    return render_template("injection.html", vuln="Injection", mode="insecure", message=message)
