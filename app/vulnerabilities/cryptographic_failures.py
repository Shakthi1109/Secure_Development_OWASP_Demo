from flask import Blueprint, render_template, request
import hashlib

crypto_bp = Blueprint("crypto", __name__)

# Secure demo: Password hashed with SHA-256 + salt
@crypto_bp.route("/secure/cryptographic-failures", methods=["GET", "POST"])
def secure_crypto():
    message = ""
    if request.method == "POST":
        password = request.form.get("password")
        salt = "somesecurestaticSalt"  # Example static salt
        hashed = hashlib.sha256((password + salt).encode()).hexdigest()
        message = f"Secure hash (SHA256 + salt): {hashed}"
    return render_template("crypto_demo.html", mode="secure", message=message)

# Insecure demo: Plain text password storage
@crypto_bp.route("/insecure/cryptographic-failures", methods=["GET", "POST"])
def insecure_crypto():
    message = ""
    if request.method == "POST":
        password = request.form.get("password")
        message = f"Insecure: Stored password in plain text: {password}"
    return render_template("crypto_demo.html", mode="insecure", message=message)
