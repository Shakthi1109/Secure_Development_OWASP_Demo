# 🔐 OWASP Top 10 Vulnerabilities Demo App

This is a Flask-based web application that demonstrates **secure vs. insecure implementations** of the **OWASP Top 10 vulnerabilities**. It helps learners, developers, and interviewers understand and visualize security flaws through hands-on examples.

![Screenshot (38)](https://github.com/user-attachments/assets/cf3eb662-1c4a-4d26-bbad-8b84096bb197)

![Screenshot (37)](https://github.com/user-attachments/assets/c4deabe1-325a-4241-a1b2-a4a9efd200af)

![Screenshot (36)](https://github.com/user-attachments/assets/1839689e-4a37-40d0-a051-e3fecbd71b0f)

![Screenshot (39)](https://github.com/user-attachments/assets/4cd6b83b-d585-4ca4-8ce3-c1a4f6affc0c)

---

## 📌 Features

- 🧪 Secure and insecure routes for each vulnerability
- 📚 Simple UI with hints and vulnerability descriptions
- 🌐 Frontend: HTML, CSS, JavaScript (Vanilla/jQuery)
- 🔙 Backend: Python Flask
- 📁 Modular blueprint-based structure

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/owasp-top10-demo.git
cd owasp-top10-demo
```

2. Create a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```
3. Install Required Packages
```bash
pip install -r requirements.txt
```
4. Run the Flask App
```bash
flask --app app run
```
Now open your browser and go to:
http://127.0.0.1:5000

🛡️ Vulnerabilities Demonstrated
A01: Broken Access Control
A02: Cryptographic Failures
A03: Injection (SQL/XSS)
A04: Insecure Design
A05: Security Misconfiguration
A06: Vulnerable & Outdated Components
A07: Identification & Authentication Failures
and more ...


Each page includes:

✅ Secure Implementation

❌ Insecure Implementation

💡 Hint + Description

🙋 Why This Project?
This app was created to showcase hands-on secure coding knowledge and demonstrate practical understanding of the OWASP Top 10 — useful for interviews and educational purposes.

✅ Requirements
Python 3.7+

Flask

🧠 Credits
Created with ❣️ by Shakthivel Murugavel
Inspired by OWASP Top 10 official website


