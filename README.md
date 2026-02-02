# QA Selenium Automation Project

This project is a **UI test automation framework** built with **Python, Selenium, and PyTest**.  
It demonstrates professional QA automation practices such as reusable setup, Page Object Model (POM), and robust UI assertions.

The goal of this project is to showcase skills relevant to **Software QA Engineer / QA Automation Engineer** roles.

---

## Tech Stack

- Python 3.13+
- Selenium WebDriver
- PyTest
- webdriver-manager
- Chrome browser

---

## Project Structure

qa-selenium-smoke-test/
├── pages/ # Page Object Model (POM)
│   └── homepage.py
│
├── tests/# Test cases
│   ├── conftest.py # PyTest fixtures (browser setup)
│   └── test_homepage.py
│
├── screenshots/
├── requirements.txt # Dependencies
└── README.md # Documentation
---

## What This Project Tests

- Homepage loads successfully
- Page title is correct
- Main heading text is visible and correct
- Important links are present
- Navigation works as expected

---

## Key QA Concepts Demonstrated

- UI automation using Selenium
- PyTest test execution
- Page Object Model (POM)
- Reusable fixtures
- Explicit waits for stability
- Clean and maintainable test structure
- Headless-ready browser execution (CI/CD friendly)

---

## How to Run the Tests

### 1. Install dependencies
```bash
python -m pip install -r requirements.txt

Run tests: python -m pytest tests -v