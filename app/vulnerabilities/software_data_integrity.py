import json
from flask import Blueprint, render_template, request

software_data_bp = Blueprint("software_data", __name__)

# Insecure route: deserializes untrusted JSON
@software_data_bp.route("/insecure/software-data-integrity", methods=["GET", "POST"])
def insecure_software_data():
    result = None
    if request.method == "POST":
        user_input = request.form["data"]
        try:
            # 🚨 Insecure: eval executes arbitrary Python code!
            obj = eval(user_input)
            result = f"Deserialized name: {obj.get('name', 'N/A')}"
        except Exception as e:
            result = f"Error: {str(e)}"
    return render_template("software_data_integrity.html", mode="insecure", result=result)


# Secure route: validates structure before deserializing
@software_data_bp.route("/secure/software-data-integrity", methods=["GET", "POST"])
def secure_software_data():
    result = None
    if request.method == "POST":
        user_input = request.form["data"]
        try:
            obj = json.loads(user_input)
            result = f"Securely parsed data: {obj.get('name', 'N/A')}"
        except Exception as e:
            result = f"Error: {str(e)}"
    return render_template("software_data_integrity.html", mode="secure", result=result)
