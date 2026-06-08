from flask import Flask, render_template, request

app = Flask(__name__)

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

    print("\n========== NEW APPOINTMENT ==========")
    print("Name:", first_name, last_name)
    print("Email:", email)
    print("Phone:", phone)
    print("Date:", appointment_date)
    print("Time:", appointment_time)
    print("Service:", service)
    print("Notes:", notes)
    print("=====================================\n")

    return f"""
<!DOCTYPE html>
<html>

<head>

<title>Appointment Submitted</title>

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

<p>Thank you {first_name} {last_name}</p>

<p>We have received your appointment request.</p>

<p>📅 {appointment_date}</p>

<p>⏰ {appointment_time}</p>

<p>📞 {phone}</p>

<p>📧 {email}</p>

<p>NailsVoYou will contact you shortly.</p>

<a href="/">Return Home</a>

</div>

</body>

</html>
"""

if __name__ == "__main__":
    app.run()

