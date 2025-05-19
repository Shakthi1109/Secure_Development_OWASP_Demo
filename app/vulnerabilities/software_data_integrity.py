import json
from flask import Blueprint, render_template, request, flash

software_data_bp = Blueprint("software_data", __name__)

# Insecure route: deserializes untrusted JSON
@software_data_bp.route("/insecure/software-data-integrity", methods=["GET", "POST"])
def insecure_software_data():
    result = None
    if request.method == "POST":
        try:
            user_input = request.form["data"]
            # Insecure: blindly deserializing untrusted input
            obj = json.loads(user_input)
            result = f"Deserialized name: {obj.get('name', 'N/A')}"
        except Exception as e:
            result = f"Error: {str(e)}"
    return render_template("software_data_integrity.html", mode="insecure", result=result)

# Secure route: validates structure before deserializing
@software_data_bp.route("/secure/software-data-integrity", methods=["GET", "POST"])
def secure_software_data():
    result = None
    if request.method == "POST":
        try:
            user_input = request.form["data"]
            # Secure: validates input format
            if not user_input.strip().startswith("{") or "name" not in user_input:
                raise ValueError("Invalid format.")
            obj = json.loads(user_input)
            result = f"Deserialized name: {obj.get('name', 'N/A')}"
        except Exception as e:
            result = f"Error: {str(e)}"
    return render_template("software_data_integrity.html", mode="secure", result=result)
