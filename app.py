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
MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

app.config["MAIL_USERNAME"] = MAIL_USERNAME
app.config["MAIL_PASSWORD"] = MAIL_PASSWORD
app.config["MAIL_DEFAULT_SENDER"] = MAIL_USERNAME

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

        # =========================
        # EMAIL TO OWNER (ADMIN)
        # =========================
        admin_msg = Message(
            subject="💅 New Booking NailsVoYou",
            recipients=[app.config["MAIL_USERNAME"]]
        )

        admin_msg.body = f"""
NEW BOOKING 💅

Name: {first_name} {last_name}
Email: {email}
Phone: {phone}
Date: {appointment_date}
Time: {appointment_time}
Service: {service}
Notes: {notes}
"""

        try:
            mail.send(admin_msg)
        except Exception as e:
            print("ADMIN EMAIL ERROR:", e)

        # =========================
        # EMAIL TO CUSTOMER
        # =========================
        customer_msg = Message(
            subject="💅 Appointment Confirmed",
            recipients=[email]
        )

        customer_msg.body = f"""
Hi {first_name},

Your appointment is confirmed 💅

Date: {appointment_date}
Time: {appointment_time}
Service: {service}

We will contact you soon.
"""

        try:
            mail.send(customer_msg)
        except Exception as e:
            print("CUSTOMER EMAIL ERROR:", e)

        return redirect(url_for("home"))

    except Exception as e:
        return f"ERROR: {str(e)}"


# =========================
# RUN APP
# =========================
if __name__ == "__main__":
    app.run()