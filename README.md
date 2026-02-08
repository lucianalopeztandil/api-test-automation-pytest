# API Test Automation Framework

This repository contains an API test automation framework built with **Python**, **pytest**, and **requests**, designed with clean structure, reusable components, and clear reporting using **Allure**.

The framework demonstrates how to manage test data lifecycle, avoid hardcoded values, and provide fast, readable feedback suitable for CI pipelines.

---

## 🧪 Tech Stack
- Python
- Pytest
- Requests
- Allure Reporting

---

## 🔁 Test Data Lifecycle
Test data is handled using **pytest fixtures**:
- A book is created before test execution
- The generated `bookId` is reused across tests
- The book is deleted after validation

This approach ensures:
- Clean test execution
- No duplicated data
- Reusable and maintainable tests

---

## ▶️ How to Run Tests

1. Create and activate a virtual environment
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. pytest -q --alluredir=allure-results

```bash
pip install -r requirements.txt
