from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

# =========================
# EMAIL CONFIG
# =========================
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = "phuma1959@gmail.com"
app.config["MAIL_PASSWORD"] = "pbeykweppdwklzdq"

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

    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    email = request.form["email"]
    phone = request.form["phone"]
    appointment_date = request.form["appointment_date"]
    appointment_time = request.form["appointment_time"]
    service = request.form["service"]
    notes = request.form["notes"]

    # =========================
    # EMAIL TO OWNER (YOU)
    # =========================
    owner_msg = Message(
        subject="💅 New NailsVoYou Booking",
        sender=app.config["MAIL_USERNAME"],
        recipients=[app.config["MAIL_USERNAME"]]
    )

    owner_msg.body = f"""
NEW BOOKING RECEIVED

Name: {first_name} {last_name}
Email: {email}
Phone: {phone}
Date: {appointment_date}
Time: {appointment_time}
Service: {service}
Notes: {notes}
"""

    mail.send(owner_msg)


    # =========================
    # EMAIL TO CUSTOMER
    # =========================
    customer_msg = Message(
        subject="💅 Your NailsVoYou Appointment Confirmation",
        sender=app.config["MAIL_USERNAME"],
        recipients=[email]
    )

    customer_msg.html = f"""
    <div style="font-family:Arial; padding:20px;">
        <h2>💅 NailsVoYou</h2>

        <p>Hi {first_name},</p>

        <p>We received your appointment request.</p>

        <hr>

        <p><b>Date:</b> {appointment_date}</p>
        <p><b>Time:</b> {appointment_time}</p>
        <p><b>Service:</b> {service}</p>

        <hr>

        <p>📍 3405 Talbot Rd S, Renton WA</p>

        <p>We will contact you soon to confirm.</p>

        <p>Thank you 💅</p>
    </div>
    """

    mail.send(customer_msg)

    # =========================
    # SUCCESS PAGE
    # =========================
    return f"""
    <html>
    <body style="font-family:Arial; text-align:center; padding:50px;">
        <h1>🎉 Appointment Submitted!</h1>
        <p>Thank you {first_name} {last_name}</p>
        <p>We sent confirmation to your email.</p>
        <a href="/">Go Back</a>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)