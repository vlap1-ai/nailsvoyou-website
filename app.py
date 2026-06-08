from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

# ======================
# GMAIL CONFIG
# ======================
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True

# 🔥 PUT THẲNG GMAIL + APP PASSWORD
app.config["MAIL_USERNAME"] = os.getenv("MAIL_USERNAME")
app.config["MAIL_PASSWORD"] = os.getenv("MAIL_PASSWORD")

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
    date = request.form["appointment_date"]
    time = request.form["appointment_time"]
    service = request.form["service"]

    # ===== EMAIL TO YOU =====
    admin = Message(
        "New Booking",
        sender=app.config["MAIL_USERNAME"],
        recipients=[app.config["MAIL_USERNAME"]]
    )

    admin.body = f"""
Name: {first_name} {last_name}
Email: {email}
Phone: {phone}
Date: {date}
Time: {time}
Service: {service}
"""

    mail.send(admin)

    # ===== EMAIL TO CUSTOMER =====
    customer = Message(
        "Appointment Confirmed 💅",
        sender=app.config["MAIL_USERNAME"],
        recipients=[email]
    )

    customer.body = f"""
Hi {first_name},

Your appointment is confirmed 💅

Date: {date}
Time: {time}
Service: {service}

Thank you!
"""

    mail.send(customer)

    return f"""
    <h1>Appointment Submitted 🎉</h1>
    <p>Check email: {email}</p>
    """


if __name__ == "__main__":
    app.run(debug=True)