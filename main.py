from flask import Flask, render_template
from app.vulnerabilities.injection import injection_bp

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(injection_bp)

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
