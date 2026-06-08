from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

# =========================
# Gmail Settings
# =========================

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = "phuma1959@gmail.com"
app.config["MAIL_PASSWORD"] = "pbeykweppdwklzdq"

mail = Mail(app)

# =========================
# Home Page
# =========================

@app.route("/")
def home():
    return render_template("index.html")


# =========================
# Booking Form
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

    msg = Message(
        subject="💅 New NailsVoYou Appointment",
        sender="phuma1959@gmail.com",
        recipients=["phuma1959@gmail.com"]
    )

    # Text fallback

    msg.body = f"""
NEW APPOINTMENT

Name: {first_name} {last_name}

Email: {email}

Phone: {phone}

Date: {appointment_date}

Time: {appointment_time}

Service: {service}

Notes: {notes}
"""

    # HTML Email

    msg.html = f"""
    <div style="
    max-width:650px;
    margin:auto;
    background:#fff7fa;
    padding:30px;
    border-radius:20px;
    font-family:Arial,sans-serif;
    ">

        <div style="text-align:center;">

            <h1 style="
            color:#ff5fa2;
            margin-bottom:10px;
            ">
                💅 NailsVoYou
            </h1>

            <p style="
            color:#777;
            ">
                New Appointment Request
            </p>

        </div>

        <div style="
        background:white;
        padding:25px;
        border-radius:15px;
        margin-top:20px;
        ">

            <p><strong>Name:</strong> {first_name} {last_name}</p>

            <p><strong>Email:</strong> {email}</p>

            <p><strong>Phone:</strong> {phone}</p>

            <p><strong>Date:</strong> {appointment_date}</p>

            <p><strong>Time:</strong> {appointment_time}</p>

            <p><strong>Service:</strong> {service}</p>

            <p><strong>Notes:</strong> {notes}</p>

        </div>

        <p style="
        text-align:center;
        margin-top:20px;
        color:#888;
        ">
            NailsVoYou • Renton, Washington
        </p>

    </div>
    """

    mail.send(msg)

    return f"""
<!DOCTYPE html>
<html>

<head>

<title>Appointment Confirmed</title>

<style>

body {{
    font-family:Arial,sans-serif;
    background:#fff1f7;
    display:flex;
    justify-content:center;
    align-items:center;
    height:100vh;
}}

.card {{
    background:white;
    padding:40px;
    border-radius:20px;
    text-align:center;
    max-width:600px;
    box-shadow:0 10px 30px rgba(0,0,0,.15);
}}

h1 {{
    color:#ff6ea9;
}}

p {{
    margin:15px 0;
}}

a {{
    display:inline-block;
    margin-top:20px;
    padding:15px 25px;
    background:#ff6ea9;
    color:white;
    text-decoration:none;
    border-radius:10px;
}}

</style>

</head>

<body>

<div class="card">

<h1>🎉 Appointment Submitted!</h1>

<p>
Thank you {first_name} {last_name}
</p>

<p>
We have received your appointment request.
</p>

<p>
📅 {appointment_date}
</p>

<p>
⏰ {appointment_time}
</p>

<p>
📞 {phone}
</p>

<p>
📧 {email}
</p>

<p>
NailsVoYou will contact you shortly.
</p>

<a href="/">
Return Home
</a>

</div>

</body>

</html>
"""


if __name__ == "__main__":
    app.run(debug=True)

