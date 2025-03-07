from flask import Flask, render_template, request
import re

app = Flask(__name__)

def check_password_strength(password):
    # Define criteria
    has_upper = bool(re.search(r"[A-Z]", password))
    has_lower = bool(re.search(r"[a-z]", password))
    has_digit = bool(re.search(r"\d", password))
    has_special = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    has_length = len(password) >= 8

    score = sum([has_upper, has_lower, has_digit, has_special, has_length])

    # Provide feedback
    if score == 5:
        return "Strong Password ✅", "green"
    elif score >= 3:
        return "Moderate Password ⚠️", "orange"
    else:
        return "Weak Password ❌ - Try adding special characters!", "red"

@app.route("/", methods=["GET", "POST"])
def home():
    feedback = ""
    color = "black"
    if request.method == "POST":
        password = request.form["password"]
        feedback, color = check_password_strength(password)
    return render_template("index.html", feedback=feedback, color=color)

if __name__ == "__main__":
    app.run(debug=True)
