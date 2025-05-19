from flask import Blueprint, request, render_template
import requests

ssrf_bp = Blueprint("ssrf", __name__)

# Insecure SSRF: accepts any user-provided URL
@ssrf_bp.route("/insecure/ssrf", methods=["GET", "POST"])
def insecure_ssrf():
    result = ""
    if request.method == "POST":
        url = request.form.get("url")
        try:
            response = requests.get(url)
            result = response.text[:500]  # show only first 500 characters
        except Exception as e:
            result = f"Error: {str(e)}"
    return render_template("server_side_request_forgery.html", mode="insecure", result=result)

# Secure SSRF: allows only whitelisted URLs
@ssrf_bp.route("/secure/ssrf", methods=["GET", "POST"])
def secure_ssrf():
    result = ""
    allowed_domains = ["https://api.github.com", "https://httpbin.org/get"]
    if request.method == "POST":
        url = request.form.get("url")
        if url in allowed_domains:
            try:
                response = requests.get(url)
                result = response.text[:500]
            except Exception as e:
                result = f"Error: {str(e)}"
        else:
            result = "Blocked: This URL is not allowed."
    return render_template("server_side_request_forgery.html", mode="secure", result=result)
