import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email_alert(score):
    sender_email = "apriyadharshini101@gmail.com"
    receiver_email = "roshiniramanujam2327@gmail.com"
    app_password = "nkkx axhz xhrc fdii"


    subject = "⚠️ Trust Erosion Alert"
    body = f"""
    Alert!

    Trust score has significantly dropped.

    Current Trust Score: {score}

    Immediate action required.
    """

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, app_password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
    server.quit()
