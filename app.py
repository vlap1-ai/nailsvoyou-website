from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
import os

app = Flask(__name__)

# =========================
# SECRET KEY
# =========================
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-key")

# =========================
# EMAIL CONFIG
# =========================
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = os.environ.get("MAIL_USERNAME")
app.config["MAIL_PASSWORD"] = os.environ.get("MAIL_PASSWORD")
app.config["MAIL_DEFAULT_SENDER"] = os.environ.get("MAIL_USERNAME")

mail = Mail(app)

# =========================
# HOME
# =========================
@app.route("/")
def home():
    return render_template("index.html")

# =========================
# BOOKING
# =========================
@app.route("/book", methods=["POST"])
def book():
    try:
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        appointment_date = request.form.get("appointment_date")
        appointment_time = request.form.get("appointment_time")
        service = request.form.get("service", "")
        notes = request.form.get("notes", "")

        OWNER_EMAIL = os.environ.get("MAIL_USERNAME")

        # ================= ADMIN EMAIL =================
        try:
            admin_msg = Message(
                subject="💅 New Booking NailsVoYou",
                recipients=[OWNER_EMAIL]
            )

            admin_msg.body = f"""
New Booking 💅

Name: {first_name} {last_name}
Email: {email}
Phone: {phone}
Date: {appointment_date}
Time: {appointment_time}
Service: {service}
Notes: {notes}
"""

            mail.send(admin_msg)

        except Exception as e:
            print("ADMIN EMAIL ERROR:", e)

        # ================= CUSTOMER EMAIL =================
        try:
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

            mail.send(customer_msg)

        except Exception as e:
            print("CUSTOMER EMAIL ERROR:", e)

        flash("Booking received successfully!", "success")
        return redirect(url_for("home"))

    except Exception as e:
        flash(str(e), "error")
        return redirect(url_for("home"))

# =========================
# RUN
# =========================
if __name__ == "__main__":
    app.run(debug=True)