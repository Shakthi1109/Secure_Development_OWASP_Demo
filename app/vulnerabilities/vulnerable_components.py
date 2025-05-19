from flask import Blueprint, render_template

components_bp = Blueprint("components", __name__)

@components_bp.route("/secure/vulnerable-components")
def secure_components():
    return render_template("vulnerable_components.html", mode="secure")

@components_bp.route("/insecure/vulnerable-components")
def insecure_components():
    return render_template("vulnerable_components.html", mode="insecure")
