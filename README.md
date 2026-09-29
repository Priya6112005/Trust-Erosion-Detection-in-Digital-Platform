Trust Erosion Detection System

An AI-powered backend that detects early warning signs of **customer trust erosion** during an online shopping session — before the customer actually leaves the platform — and automatically alerts the platform manager with the likely cause and a recommended action.

 📌 Overview

Ecommerce platforms often lose customers silently. A manager rarely finds out *why* a customer abandoned checkout, hesitated too long, or seemed frustrated — until it's too late, and the same underlying issue often repeats across many different customers.

This system continuously analyzes live customer session data, calculates a **Trust Score**, identifies the specific reason trust is eroding, and sends the platform manager an actionable email alert — so they can intervene quickly and fix recurring problems before more customers are lost.


 🔄 System Workflow

Customer Session Data
        ↓
FastAPI Analysis (Sentiment + Behavior + Interaction)
        ↓
Trust Score Calculation
        ↓
Risk Reason Detection
        ↓
Personalization Engine (customer problem + recommended action)
        ↓
n8n Webhook
        ↓
Gmail Alert
        ↓
Manager receives an actionable email


 ✨ Key Features

- Real-time analysis of customer sessions across three dimensions: sentiment, behavior, and interaction
- Weighted Trust Score calculation with four risk levels: **LOW / MEDIUM / HIGH / CRITICAL**
- Automatic detection of specific risk reasons (checkout abandonment, high hesitation, repeated policy checks, negative sentiment)
- Rule-based personalization engine that translates each reason into a plain-language explanation and a concrete recommended action for the manager
- Automated email alerts via an n8n workflow, triggered only when a session crosses the risk threshold
- Lightweight, beginner-friendly FastAPI backend with interactive Swagger UI for testing


 📊 Dataset / Input Data

This system does not require a pre-collected historical dataset — it operates on **live session data** submitted per customer interaction. Each request represents a single customer session.

### Main Fields & Signals Used

| Field | Type | Description |
|---|---|---|
| `text` | string | Customer's message/feedback text, used for sentiment analysis |
| `abandonment` | int (0/1) | Whether the customer abandoned checkout |
| `policy_checks` | int | Number of times the customer viewed return/refund/policy pages |
| `hesitation_time` | int (seconds) | Time spent hesitating during checkout |
| `messages_count` | int | Number of messages/interactions during the session |
| `dispute_flag` | int (0/1) | Whether a dispute was raised during the session |

### What the Data Should Contain

For accurate detection, each session payload should reflect genuine behavioral signals — for example, real elapsed hesitation time (not estimated), an accurate count of policy page visits, and the customer's actual message text where available. Missing or synthetic values will still be processed, but may reduce the accuracy of the resulting Trust Score.

---
🧩 Overall Pipeline

1. **Ingestion** — Session data is sent to the `/analyze-session` FastAPI endpoint
2. **Sentiment Analysis** — `sentiment.py` scores the customer's text
3. **Behavior Analysis** — `behavior.py` scores checkout abandonment, policy checks, and hesitation time
4. **Interaction Analysis** — `interaction.py` scores message volume and dispute flags
5. **Trust Score Calculation** — `trust_score.py` combines the three scores using a weighted formula:
   
   final_trust_score = sentiment_score × 0.3 + behavior_score × 0.4 + interaction_score × 0.3
   
6. **Risk Reason Detection** — `main.py` checks thresholds and compiles a list of specific reasons
7. **Personalization** — `personalization.py` maps the primary reason to a `customer_problem` explanation and a `recommended_action`
8. **Alerting** — If `final_trust_score` falls below the threshold, the data is sent to an n8n webhook, which formats and sends a Gmail alert to the platform manager

🤖 Model / Scoring Approach Used

This project currently uses a **rule-based scoring and personalization approach** rather than a trained machine learning model:
- Sentiment, behavior, and interaction scores are computed using deterministic logic
- Risk reasons and recommended actions are matched via a fixed rules dictionary (`PERSONALIZATION_RULES`)

*(Planned enhancement: replacing the rule-based personalization engine with an AI/LLM-based approach for more nuanced explanations.)*



📈 Performance Metrics & Testing Tool

- **Testing Tool:** FastAPI's built-in **Swagger UI** (`/docs`) was used for manual endpoint testing and validating responses during development
- **Manual Test Scenarios:**
  - High-risk session (multiple negative signals) → confirmed CRITICAL risk level and correct alert email delivery
  - Medium-risk/borderline session → confirmed threshold behavior around the risk cutoff
  - Low-risk/positive session → confirmed no alert email is sent (system correctly stays silent for healthy sessions)
- **End-to-end delivery verified:** FastAPI → n8n webhook (`200 OK`) → Gmail alert received with correct Trust Score, Risk Level, Customer Problem, and Recommended Action

*(Formal accuracy/precision metrics are not applicable, as this is currently a rule-based system rather than a trained classifier.)*



🛠️ Tech Stack

- **Python** — core backend language
- **FastAPI** — REST API framework for session analysis and scoring
- **Uvicorn** — ASGI server to run the FastAPI app
- **n8n** — workflow automation connecting the backend to email delivery
- **Gmail (via n8n)** — automated manager alert delivery
- **python-dotenv** — environment variable management for secrets


💻 Installation

### Prerequisites
- Python 3.10+
- pip
- An n8n account/workflow with a configured Webhook + Gmail node

Clone the repository

git clone https://github.com/xxx/project_name.git
cd Trust-Erosion-Detection-in-Digital-Platform


Windows

python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt


Linux / macOS

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt


Set up environment variables
Create a `.env` file in the project root:

WEBHOOK_URL=your_n8n_webhook_url_here

▶️ How to Run Locally

1. Activate your virtual environment (see above)
2. Start the FastAPI server:
   
   uvicorn main:app --reload
   
3. Open Swagger UI in your browser:
   
   http://127.0.0.1:8000/docs
   
4. Use the /analyze-session endpoint to send a test customer session payload and view the analysis result
5. If the trust score falls below the alert threshold, check the connected n8n workflow and the manager's inbox for the alert email


🎯 Project Objective

The objective of this project is to give ecommerce platform managers **real-time, actionable visibility** into why customers are losing trust and disengaging — before they leave for good. By automatically detecting behavioral and sentiment-based warning signs and translating them into a clear explanation and recommended action, this system aims to help businesses intervene proactively and fix recurring platform issues, ultimately reducing customer churn caused by preventable, repeated problems.

