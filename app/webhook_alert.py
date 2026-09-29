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