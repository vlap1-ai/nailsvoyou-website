from flask import Flask, render_template, request, redirect, url_for
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
# HOME PAGE
# =========================
@app.route("/")
def home():
    return render_template("index.html")


# =========================
# BOOKING ROUTE
# =========================
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

        # =====================
        # EMAIL TO OWNER
        # =====================
        admin_msg = Message(
            subject="💅 New Booking NailsVoYou",
            recipients=[app.config["MAIL_USERNAME"]],
        )

        admin_msg.body = f"""
New Booking:

Name: {first_name} {last_name}
Email: {email}
Phone: {phone}
Date: {appointment_date}
Time: {appointment_time}
Service: {service}
Notes: {notes}
"""

        mail.send(admin_msg)

        # =====================
        # EMAIL TO CUSTOMER
        # =====================
        customer_msg = Message(
            subject="💅 Appointment Confirmed",
            recipients=[email],
        )

        customer_msg.body = f"""
Hi {first_name},

Your appointment is confirmed 💅

Date: {appointment_date}
Time: {appointment_time}
Service: {service}

We will contact you soon.
"""

        mail.send(customer_msg)

        # SUCCESS REDIRECT (IMPORTANT)
        return redirect(url_for("home"))

    except Exception as e:
        return f"ERROR: {str(e)}"


if __name__ == "__main__":
    app.run()