import requests
from app.personalization import get_personalization
from fastapi import FastAPI
from app.models import SessionData
from app.sentiment import analyze_sentiment
from app.behavior import analyze_behavior
from app.interaction import analyze_interaction
from app.trust_score import compute_trust_score
from app.webhook_alert import generate_alert
from dotenv import load_dotenv
import os

load_dotenv()


app = FastAPI()

THRESHOLD = 50

WEBHOOK_URL = os.getenv("WEBHOOK_URL")

@app.post("/analyze-session")
def analyze_session(data: SessionData):

    
    sentiment_score = analyze_sentiment(data.text)

   
    behavior_score = analyze_behavior(
        data.abandonment,
        data.policy_checks,
        data.hesitation_time
    )

   
    interaction_score = analyze_interaction(
        data.messages_count,
        data.dispute_flag
    )

   
    final_trust_score = compute_trust_score(
        sentiment_score,
        behavior_score,
        interaction_score
    )

    
    reasons = []

    if data.hesitation_time > 80:
        reasons.append("High hesitation time during checkout")

    if data.policy_checks > 3:
        reasons.append("Multiple policy verification attempts")

    if sentiment_score < 50:
        reasons.append("Negative sentiment detected")

    if data.abandonment == 1:
        reasons.append("Checkout abandonment detected")

    if final_trust_score < 40:
        risk_level = "CRITICAL"

    elif final_trust_score < 60:
        risk_level = "HIGH"

    elif final_trust_score < 80:
        risk_level = "MEDIUM"

    else:
        risk_level = "LOW"

    personalization = get_personalization(reasons)

   
    alert_message = None
    webhook_status = None

    if final_trust_score < THRESHOLD:

      
        alert_message = generate_alert(
            final_trust_score,
            reasons
        )

        
        webhook_data = {
    "trust_score": final_trust_score,
    "risk_level": risk_level,
    "risk_reasons": reasons,
    "alert_message": alert_message,
    "customer_problem": personalization["customer_problem"],
    "recommended_action": personalization["recommended_action"]
}

   
        try:
            response = requests.post(
                WEBHOOK_URL,
                json=webhook_data,
                timeout=10
            )

            webhook_status = response.status_code

            print("N8N Status:", response.status_code)
            print("N8N Response:", response.text)

        except Exception as e:
            print("N8N ERROR:", e)
            webhook_status = "Failed"


        return {
        "sentiment_score": sentiment_score,
        "behavior_score": behavior_score,
        "interaction_score": interaction_score,
        "final_trust_score": final_trust_score,
        "risk_level": risk_level,
        "risk_reasons": reasons,
        "personalization": personalization,
        "alert_message": alert_message,
        "webhook_status": webhook_status
    }


@app.get("/")
def home():
    return {
        "message": "Trust Erosion Detection Backend is running successfully"
    }
