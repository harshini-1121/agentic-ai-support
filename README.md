# Agentic AI Support System

An **Agentic AI-based customer support system** designed for e-commerce platforms to automatically handle user queries such as order tracking, refunds, and FAQs using an orchestrator and specialized agents.

---

## Problem Statement

E-commerce platforms receive **10,000+ customer queries daily**, leading to:

*  Long response times (~6 hours)
*  Poor customer satisfaction
*  Overloaded support teams

---

## Solution

We built an **Agentic AI system** where:

* An **Orchestrator** classifies user queries
* Routes them to specialized **agents**
* Applies **guardrails** for safety
* Logs all actions for **monitoring**
* Provides a **simple chat UI** for interaction

---

## System Architecture

```
User Query
   ↓
Orchestrator (Intent Classification)
   ↓
-----------------------------------
| Order | Refund | FAQ | Escalation |
-----------------------------------
   ↓
Guardrails → Response → Logs
```

---

## Features
*  Order Tracking Agent
*  Refund Agent with Guardrails
*  FAQ Agent
*  Orchestrator (Intent Routing)
*  Guardrails (Safety + Limits)
*  Monitoring & Logging
*  Frontend Chat UI

---

## Tech Stack

* **Backend:** FastAPI
* **Frontend:** HTML, CSS, JavaScript
* **Language:** Python
* **Architecture:** Agentic AI System

---

## Project Structure

```
agentic-ai-support/
│
├── main.py
├── orchestrator.py
├── llm_classifier.py
├── guardrails.py
├── monitor.py
│
├── agents/
│   ├── order_agent.py
│   ├── refund_agent.py
│   ├── faq_agent.py
│
├── frontend/
│   └── index.html
│
├── .env
├── requirements.txt
└── README.md
```

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/agentic-ai-support.git
cd agentic-ai-support
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate it:

**Windows:**

```bash
venv\Scripts\activate
```

**Mac/Linux:**

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

##  Running the Backend

```bash
uvicorn main:app --reload
```

Open in browser:

 http://127.0.0.1:8000/docs

Use the `/query` endpoint to test.

---

##  Running the Frontend

1. Go to the `frontend` folder
2. Open `index.html` in your browser

Enter queries like:
* "Where is my order?"
* "I want refund"

---

##  Example API Request

```json
{
  "user_query": "Where is my order?"
}
```

---

##  Guardrails Implemented

* Refund limit enforcement
* Sensitive data protection
* Escalation for high-risk actions
* Loop prevention

---

## Monitoring

System logs:

* Query received
* Intent detected
* Agent used
* Guardrail triggers

Logs stored in:

```
system.log
```

---

## LLM Design Note

The system is designed to use **LLM-based classification**.
Due to API quota limitations, a **semantic fallback classifier** is used to ensure:

* Reliability
* Zero downtime
* Consistent performance

---

##  Key Concepts

* Agentic AI
* Orchestrator Pattern
* Guardrails
* Monitoring & Observability

---

##  Future Improvements

* Integrate real LLM (Grok / GPT / Gemini)
* Add vector database for FAQ
* Improve UI/UX
* Add authentication

---

## Author

Harshini T N

---

## Conclusion

This project demonstrates a **scalable and reliable Agentic AI system** capable of improving customer support efficiency while ensuring safety and robustness.
