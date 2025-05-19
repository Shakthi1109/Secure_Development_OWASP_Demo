from flask import Blueprint, render_template, request

design_bp = Blueprint("design", __name__)

# Secure demo: input validation with whitelist
@design_bp.route("/secure/insecure-design", methods=["GET", "POST"])
def secure_design():
    message = ""
    if request.method == "POST":
        color = request.form.get("color", "").lower()
        allowed_colors = ["red", "blue", "green"]
        if color in allowed_colors:
            message = f"Secure: You chose a safe color: {color}"
        else:
            message = "Secure: Invalid color, rejected input."
    return render_template("insecure_design.html", mode="secure", message=message)

# Insecure demo: no input validation, reflect input directly
@design_bp.route("/insecure/insecure-design", methods=["GET", "POST"])
def insecure_design():
    message = ""
    if request.method == "POST":
        color = request.form.get("color", "")
        message = f"Insecure: You chose color: {color}"
    return render_template("insecure_design.html", mode="insecure", message=message)
