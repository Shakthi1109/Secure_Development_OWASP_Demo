from flask import Blueprint, render_template, request

design_bp = Blueprint("design", __name__)

# Dangerous: account deletion with no auth check or confirmation
@design_bp.route("/insecure/insecure-design", methods=["GET", "POST"])
def insecure_design():
    message = ""
    if request.method == "POST":
        username = request.form.get("username", "")
        message = f"Account for user '{username}' has been deleted. (Insecure)"
        # Insecure logic: no authentication, no ownership check, no confirmation
    return render_template("insecure_design.html", mode="insecure", message=message)


# Secure: requires auth and confirmation to delete account
@design_bp.route("/secure/insecure-design", methods=["GET", "POST"])
def secure_design():
    message = ""
    if request.method == "POST":
        username = request.form.get("username", "")
        confirm = request.form.get("confirm", "")
        comfirmation="I CONFIRM TO DELETE ACCOUNT"
        # Simulate current user is 'alice'
        current_user = "user123"
        if username != current_user:
            message = "Please enter your correct username"
        elif confirm != comfirmation:
            message = "Secure: Please confirm deletion by typing <" + comfirmation + ">."
        else:
            message = f"Account '{username}' has been safely deleted (secure)."
    return render_template("insecure_design.html", mode="secure", message=message)

