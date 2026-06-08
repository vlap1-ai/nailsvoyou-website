from flask import Flask, render_template, request
from flask_mail import Mail, Message
import os

app = Flask(__name__)

# =========================
# EMAIL CONFIG (SAFE WAY)
# =========================
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True

app.config["phuma1959@gmail.com"] = os.getenv("MAIL_USERNAME")
app.config["pbeykweppdwklzdq"] = os.getenv("MAIL_PASSWORD")

mail = Mail(app)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/book", methods=["POST"])
def book():

    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    email = request.form["email"]
    phone = request.form["phone"]
    appointment_date = request.form["appointment_date"]
    appointment_time = request.form["appointment_time"]
    service = request.form["service"]
    notes = request.form["notes"]

    # =========================
    # EMAIL TO YOU (ADMIN)
    # =========================
    admin_msg = Message(
        subject="💅 New Booking NailsVoYou",
        sender=app.config["MAIL_USERNAME"],
        recipients=[app.config["MAIL_USERNAME"]]
    )

    admin_msg.body = f"""
NEW BOOKING

Name: {first_name} {last_name}
Email: {email}
Phone: {phone}
Date: {appointment_date}
Time: {appointment_time}
Service: {service}
Notes: {notes}
"""

    mail.send(admin_msg)

    # =========================
    # EMAIL TO CUSTOMER
    # =========================
    customer_msg = Message(
        subject="💅 Appointment Confirmed",
        sender=app.config["MAIL_USERNAME"],
        recipients=[email]
    )

    customer_msg.body = f"""
Hi {first_name},

We received your appointment 💅

Date: {appointment_date}
Time: {appointment_time}
Service: {service}

We will contact you soon.
"""

    mail.send(customer_msg)

    return f"""
    <h1>Appointment Submitted 🎉</h1>
    <p>Check your email for confirmation</p>
    """


if __name__ == "__main__":
    app.run()