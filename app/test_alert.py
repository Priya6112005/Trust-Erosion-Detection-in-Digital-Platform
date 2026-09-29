import requests
import random
from webhook_alert import generate_alert

url = "http://localhost:5678/webhook-test/trust"

user_id = str(random.randint(100, 999))
trust_score = round(random.uniform(0.1, 0.9), 2)

reasons = []

if trust_score < 0.4:
    reasons.append("User hesitating during checkout")

if trust_score < 0.5:
    reasons.append("Negative sentiment detected")

if trust_score < 0.6:
    reasons.append("Multiple policy checks")

if trust_score < 0.4:
    risk_level = "HIGH"
elif trust_score < 0.7:
    risk_level = "MEDIUM"
else:
    risk_level = "LOW"

alert_message = generate_alert(trust_score, reasons)

data = {
    "user_id": user_id,
    "trust_score": trust_score,
    "risk_level": risk_level,
    "alert_message": alert_message
}

response = requests.post(url, json=data)
print(response.text)