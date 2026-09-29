import requests

WEBHOOK_URL = "https://dharshpri.app.n8n.cloud/webhook-test/828ceb6e-6e22-4a24-8bc7-37c3e78391da"


def generate_alert(trust_score, reasons):

    message = f"""
🚨 TRUST EROSION ALERT

Trust Score: {trust_score}
Status: EROSION STAGE

Detected Risk Signals:
"""

    for r in reasons:
        message += f"\n• {r}"

    message += "\n\nRecommended Action:\nTake immediate action"

    return message


def send_webhook_alert(trust_score, risk_level, reasons):

    alert_message = generate_alert(trust_score, reasons)

    data = {
        "trust_score": trust_score,
        "risk_level": risk_level,
        "risk_reasons": reasons,
        "alert_message": alert_message
    }

    response = requests.post(
        WEBHOOK_URL,
        json=data
    )

    return response.status_code