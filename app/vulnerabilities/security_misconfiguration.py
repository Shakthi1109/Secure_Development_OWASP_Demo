from flask import Blueprint, render_template, request, abort

misconfig_bp = Blueprint("misconfig", __name__)

# Secure demo: Proper error handling without exposing sensitive info
@misconfig_bp.route("/secure/security-misconfiguration", methods=["GET", "POST"])
def secure_misconfig():
    message = ""
    if request.method == "POST":
        param = request.form.get("param", "")
        if param == "allowed":
            message = "Secure: Access granted."
        else:
            # Properly abort with 403, no detailed error leaked
            abort(403)
    return render_template("security_misconfiguration.html", mode="secure", message=message)

# Insecure demo: Exposes detailed error messages
@misconfig_bp.route("/insecure/security-misconfiguration", methods=["GET", "POST"])
def insecure_misconfig():
    message = ""
    if request.method == "POST":
        param = request.form.get("param", "")
        if param == "allowed":
            message = "Insecure: Access granted."
        else:
            # Insecure: Display detailed error to user (simulating debug mode leak)
            message = f"Insecure: Access denied. Debug info: param='{param}' not allowed."
    return render_template("security_misconfiguration.html", mode="insecure", message=message)
