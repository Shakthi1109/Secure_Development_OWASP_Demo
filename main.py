from flask import Flask, render_template, session
from app.vulnerabilities.injection import injection_bp
from app.vulnerabilities.broken_access import access_bp
from app.vulnerabilities.cryptographic_failures import crypto_bp
from app.vulnerabilities.insecure_design import design_bp
from app.vulnerabilities.security_misconfiguration import misconfig_bp
from app.vulnerabilities.vulnerable_components import components_bp
from app.vulnerabilities.identification_authentication import identification_auth_bp
from app.vulnerabilities.software_data_integrity import software_data_bp


app = Flask(__name__)
app.secret_key = "supersecretkey"


# Register Blueprints
app.register_blueprint(injection_bp)
app.register_blueprint(access_bp)
app.register_blueprint(crypto_bp)
app.register_blueprint(design_bp)
app.register_blueprint(misconfig_bp)
app.register_blueprint(components_bp)
app.register_blueprint(identification_auth_bp)
app.register_blueprint(software_data_bp)



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/mode/<mode>")
def mode_page(mode):
    if mode not in ["secure", "insecure"]:
        return render_template("index.html", error="Invalid mode selected.")
    return render_template("menu.html", mode=mode)

if __name__ == "__main__":
    app.run(debug=True)



@app.errorhandler(403)
def forbidden_error(e):
    return render_template("403.html"), 403
