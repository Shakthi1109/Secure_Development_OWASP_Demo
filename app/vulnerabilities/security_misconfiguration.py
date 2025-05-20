import traceback
from flask import Blueprint, render_template, request

misconfig_bp = Blueprint("misconfig", __name__)

@misconfig_bp.route("/insecure/security-misconfiguration", methods=["GET", "POST"])
def insecure_misconfig():
    message = ""
    if request.method == "POST":
        try:
            value = int(request.form.get("number"))
            result = 100 / value
            message = f"Insecure: Result is {result}"
        except Exception:
            # Simulate debug mode by displaying the traceback in the UI
            error_trace = traceback.format_exc()
            message = f"Insecure: An error occurred:<br><pre>{error_trace}</pre>"
    return render_template("security_misconfiguration.html", mode="insecure", message=message)

@misconfig_bp.route("/secure/security-misconfiguration", methods=["GET", "POST"])
def secure_misconfig():
    message = ""
    if request.method == "POST":
        try:
            value = int(request.form.get("number"))
            result = 100 / value
            message = f"Secure: Result is {result}"
        except Exception:
            message = "Secure: Something went wrong. Please contact support."
    return render_template("security_misconfiguration.html", mode="secure", message=message)
