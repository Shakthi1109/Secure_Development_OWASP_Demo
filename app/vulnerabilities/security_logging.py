from flask import Blueprint, request, render_template, redirect, url_for, flash
import logging

logging_bp = Blueprint("logging_monitoring", __name__)

# Setup logging (in real apps this goes in app config)
logger = logging.getLogger("auth_logger")
handler = logging.FileHandler("auth.log")
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.setLevel(logging.INFO)
logger.addHandler(handler)

# Dummy credentials
VALID_USERNAME = "admin"
VALID_PASSWORD = "admin123"

@logging_bp.route("/secure/logging-monitoring", methods=["GET", "POST"])
def secure_logging():
    message = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username == VALID_USERNAME and password == VALID_PASSWORD:
            logger.info(f"Successful login for user: {username}")
            message = "Login successful!"
        else:
            logger.warning(f"Failed login attempt for user: {username}")
            message = "Invalid credentials."
    return render_template("security_logging.html", mode="secure", message=message)


@logging_bp.route("/insecure/logging-monitoring", methods=["GET", "POST"])
def insecure_logging():
    message = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username == VALID_USERNAME and password == VALID_PASSWORD:
            message = "Login successful!"
        else:
            # No logging of failed attempts
            message = "Invalid credentials."
    return render_template("security_logging.html", mode="insecure", message=message)
