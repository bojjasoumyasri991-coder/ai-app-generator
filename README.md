# AI App Generator 🚀

## Overview
This project converts natural language prompts into structured application configurations including:

- UI Schema (pages, components)
- API Schema (endpoints, methods)
- Database Schema (tables, relations)
- Authentication (roles, permissions)
- Business Logic (rules, constraints)

---

## 🧠 Architecture

The system follows a **multi-stage pipeline design**:

1. Prompt Parsing  
2. Feature Extraction  
3. Schema Generation  
4. Validation & Repair  

---

## ⚙️ Pipeline Design

### 1. Parser
Extracts intent from user input:
- Detects login, roles, payments, analytics

### 2. Generator
Builds:
- UI pages
- API endpoints
- Database tables

### 3. Validator (IMPORTANT)
Ensures system completeness:
- Adds missing user table if login exists
- Adds roles if admin detected
- Adds subscription logic if payments exist

👉 This ensures **reliability even for incomplete prompts**

---

## 🔐 Features Supported

- Login & Authentication
- Role-based Access (Admin/User)
- Contacts / CRM modules
- Payment & Premium Plans
- Admin Analytics

---

## 💻 How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
