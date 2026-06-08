from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

# =========================
# EMAIL CONFIG
# =========================
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USE_SSL"] = False

# 🔥 YOUR GMAIL (ADMIN)
app.config["MAIL_USERNAME"] = "phuma1959@gmail.com"
app.config["MAIL_PASSWORD"] = "pbeykweppdwklzdq"  # App Password

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

    try:
        # =========================
        # EMAIL TO ADMIN
        # =========================
        admin_msg = Message(
            subject="💅 NEW BOOKING - NailsVoYou",
            sender=app.config["MAIL_USERNAME"],
            recipients=[app.config["MAIL_USERNAME"]]
        )

        admin_msg.body = f"""
💅 NEW BOOKING RECEIVED

━━━━━━━━━━━━━━━━━━
👤 CUSTOMER INFO
━━━━━━━━━━━━━━━━━━
Name: {first_name} {last_name}
Email: {email}
Phone: {phone}

━━━━━━━━━━━━━━━━━━
📅 APPOINTMENT
━━━━━━━━━━━━━━━━━━
Date: {appointment_date}
Time: {appointment_time}
Service: {service}
Notes: {notes}

━━━━━━━━━━━━━━━━━━
Status: NEW REQUEST
"""

        mail.send(admin_msg)

        # =========================
        # EMAIL TO CUSTOMER
        # =========================
        customer_msg = Message(
            subject="💅 Appointment Confirmed - NailsVoYou",
            sender=app.config["MAIL_USERNAME"],
            recipients=[email]
        )

        customer_msg.body = f"""
Hi {first_name} ✨

Thank you for booking with NailsVoYou 💅

━━━━━━━━━━━━━━━━━━
📅 YOUR APPOINTMENT
━━━━━━━━━━━━━━━━━━
Date: {appointment_date}
Time: {appointment_time}
Service: {service}

We will contact you shortly to confirm details.

💖 NailsVoYou Team
"""

        mail.send(customer_msg)

    except Exception as e:
        print("EMAIL ERROR:", e)
        return "Error sending email"

    # =========================
    # SUCCESS PAGE (DECORATED)
    # =========================
    return f"""
<!DOCTYPE html>
<html>
<head>
<title>Appointment Confirmed</title>

<style>

body {{
    margin:0;
    height:100vh;
    display:flex;
    justify-content:center;
    align-items:center;
    font-family:Arial;
    background:linear-gradient(135deg,#ffe4f0,#fff);
}}

.card {{
    background:white;
    padding:50px;
    border-radius:25px;
    text-align:center;
    max-width:500px;
    box-shadow:0 20px 60px rgba(0,0,0,0.15);
    animation:pop .4s ease;
}}

@keyframes pop {{
    from {{ transform:scale(0.8); opacity:0; }}
    to {{ transform:scale(1); opacity:1; }}
}}

h1 {{
    color:#ff4f9a;
}}

p {{
    color:#444;
    margin:10px 0;
}}

a {{
    display:inline-block;
    margin-top:20px;
    padding:12px 25px;
    background:#ff4f9a;
    color:white;
    text-decoration:none;
    border-radius:12px;
}}

a:hover {{
    background:#ff2f86;
}}

</style>

</head>

<body>

<div class="card">

<h1>🎉 Appointment Confirmed</h1>

<p>Thank you <b>{first_name} {last_name}</b></p>

<p>📅 {appointment_date} at {appointment_time}</p>

<p>💌 Check your email: {email}</p>

<a href="/">Back Home</a>

</div>

</body>
</html>
"""


# =========================
# RUN APP
# =========================
if __name__ == "__main__":
    app.run(debug=True)