from flask import Flask, render_template, request
from flask_mail import Mail, Message
import os

app = Flask(__name__)

# =========================
# EMAIL CONFIG
# =========================
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = os.getenv("MAIL_USERNAME")
app.config["MAIL_PASSWORD"] = os.getenv("MAIL_PASSWORD")
app.config["MAIL_DEFAULT_SENDER"] = os.getenv("MAIL_USERNAME")

mail = Mail(app)

# =========================
# ROUTES
# =========================
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/book", methods=["POST"])
def book():
    try:
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        phone = request.form["phone"]
        appointment_date = request.form["appointment_date"]
        appointment_time = request.form["appointment_time"]
        service = request.form["service"]
        notes = request.form["notes"]

        # ADMIN EMAIL
        admin_msg = Message(
            subject="New Booking NailsVoYou",
            recipients=[app.config["MAIL_USERNAME"]],
        )

        admin_msg.body = f"""
New booking:
{first_name} {last_name}
{email}
{phone}
{appointment_date} {appointment_time}
{service}
{notes}
"""

        mail.send(admin_msg)

        # CUSTOMER EMAIL
        customer_msg = Message(
            subject="Appointment Confirmed",
            recipients=[email],
        )

        customer_msg.body = f"""
Hi {first_name},
Your appointment is confirmed:
{appointment_date} at {appointment_time}
"""

        mail.send(customer_msg)

        return "<h1>Appointment Submitted 🎉</h1>"

    except Exception as e:
        return f"ERROR: {str(e)}"


if __name__ == "__main__":
    app.run(debug=True)