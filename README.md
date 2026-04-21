# Agentic AI Support System

An intelligent customer support system built using an Agentic AI architecture and LLM-based intent classification for e-commerce platforms.

---

## Problem

E-commerce platforms handle high volumes of customer queries, which leads to:

* Slow response times
* Poor customer satisfaction
* Overloaded support teams

---

## Solution

This project implements an AI-driven system that:

* Uses a large language model (Hugging Face) to classify user queries
* Routes queries to specialized agents
* Applies guardrails for safety
* Logs system behavior for monitoring
* Provides a simple chat-based user interface

---

## Design Thinking Approach

The system is designed using Design Thinking principles:

* Empathize: Identify customer frustration and support overload
* Define: Need for fast, scalable support
* Ideate: Multi-agent AI system with LLM classification
* Prototype: FastAPI backend with chat interface
* Test: Validated through API calls and logs

---

## Architecture

```
User → Frontend UI → FastAPI Backend  
     → Orchestrator  
     → Hugging Face LLM (Zero-shot Classification)  
     → Agent (Order / Refund / FAQ)  
     → Guardrails  
     → Response  
     → Logs (system.log)
```

---

## Features

* Order Tracking Agent
* Refund Processing Agent
* FAQ Agent
* LLM-based Intent Classification
* Guardrails for safety
* Monitoring and logging
* Chat-based frontend interface

---

## Tech Stack

* Backend: FastAPI
* LLM: Hugging Face (BART MNLI – zero-shot classification)
* Frontend: HTML, CSS, JavaScript
* Language: Python

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

Activate:

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Backend

```bash
uvicorn main:app --reload
```

Open:
http://127.0.0.1:8000/docs

---

## Running the Frontend

Open:

```
frontend/index.html
```

---

## Environment Variables

Create a `.env` file:

```
HF_API_KEY=your_huggingface_token
```

---

## Example API Request

```json
{
  "user_query": "Where is my order?"
}
```

---

## Guardrails

* Refund limit enforcement
* Safe response handling
* Escalation for high-risk queries

---

## Monitoring

The system logs:

* User queries
* Intent classification
* Agent routing
* Errors

Logs are stored in:

```
system.log
```

---

## Key Concepts

* Agentic AI
* Orchestrator pattern
* LLM integration
* Guardrails
* Observability

---

## Future Improvements

* Database integration
* Improved UI/UX
* Authentication system
* Multi-language support

---

## References

* https://fastapi.tiangolo.com/
* https://huggingface.co/
* https://docs.python.org/

---

## Author

Harshini T N

---

## Conclusion

This project demonstrates a scalable AI-driven support system using LLM-based classification and agent-based architecture to improve customer support efficiency.
