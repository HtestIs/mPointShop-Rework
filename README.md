# mPointShop-Rework 🚀
![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-Framework-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-Automation-43B02A?style=for-the-badge&logo=selenium&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-API-FF6F00?style=for-the-badge)
![Allure](https://img.shields.io/badge/Allure-Reports-8A2BE2?style=for-the-badge)

A QA automation framework combining **UI testing** and **API testing** using modern Python tools.

Built as a **job-ready portfolio project** to demonstrate real-world automation practices:

* Page Object Model (UI)
* API abstraction layer
* Data-driven testing
* Environment-based configuration

---

## ✨ Features

* UI automation with **Selenium + Page Object Model**
* API testing with **Requests + structured endpoints**
* Test separation: `UI (e2e)` vs `API`
* Reusable fixtures for driver, API, and data
* Environment handling via `.env`
* Parametrized test cases (data-driven)
* Allure report integration

---

## 🧱 Project Structure

```text
mPointShop-Rework/
├── api/                         # API layer
│   ├── client.py                # Base API client
│   ├── endpoints/               # Endpoint classes (StoreAPI, AuthAPI)
│   └── api_assertions/          # Reusable API assertions
│       ├── menu_assertions.py
│       └── store_assertions.py
│
├── assets/                      # Static assets (images, uploads)
│   └── icon_auto.png
│
├── config/                      # Environment & config
│   ├── env_config.py
│   └── paths.py
│
├── data/                        # Test data & payload builders
│   ├── builders.py
│   ├── data_generator.py
│   ├── fake_location.py
│   ├── store_data.py
│   └── test_data.py
│
├── drivers/                     # WebDriver setup
│   ├── browser_options.py
│   └── driver_manager.py
│
├── fixtures/                    # Pytest fixtures
│   ├── api_fixture.py
│   └── driver_fixture.py
│
├── pages/                       # Page Object Model (UI)
│   ├── base_page.py
│   ├── login_page.py
│   ├── store_manage_page.py
│   └── voucher_scan_page.py
│
├── tests/
│   ├── api/
│   │   ├── auth/                # Auth API tests
│   │   │   ├── test_login_contract_api.py
│   │   │   ├── test_login_negative_api.py
│   │   │   └── test_login_positive_api.py
│   │   │
│   │   ├── menu/                # Menu-related API tests
│   │   │   └── test_menu_api.py
│   │   │
│   │   └── store/               # Store-related API tests 
│   │       └── test_stores_api.py
│   │
│   └── e2e/                     # UI (end-to-end tests)
│       ├── test_login.py
│       ├── test_store_location.py
│       ├── test_store_registration.py
│       ├── test_store_search.py
│       ├── test_store_security.py
│       └── test_voucher_scan.py
│
├── utils/                       # Utilities
│   ├── data_helpers.py
│   └── logger.py
│
├── reports/
├── allure-results/
├── allure-report/
│
├── .env
├── .env.example
├── .gitignore
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## 🧪 Test Coverage

### UI (E2E)
- Login
- Store search
- Store registration
- Store location validation
- Store security validation

### API
#### Auth
- Login API

#### Store List
- Get store list with valid pagination
- Unauthorized access
- Invalid token
- Invalid page / pageSize values
- pageSize edge cases
- Exceed max page
- Missing or unexpected params
- Wrong HTTP method on list endpoint

#### Store Create
- Create store with valid payload
- Create store with no payload
- Create store validation and business-error scenarios (ongoing)
---

## ⚙️ Setup

### 1. Clone repo

```bash
git clone https://github.com/HtestIs/mPointShop-Rework.git
cd mPointShop-Rework
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment

Create `.env` from `.env.example`:

```env
DEV_WEB_BASE_URL=your_web_url
DEV_API_BASE_URL=your_api_url

DEV_PARTNER_USERNAME=your_partner_username
DEV_PARTNER_PASSWORD=your_partner_password

DEV_MERCHANT_USERNAME=your_merchant_username
DEV_MERCHANT_PASSWORD=your_merchant_password
```

---

## ▶️ Running Tests

### Run all tests

```bash
pytest
```

### Run UI tests only

```bash
pytest tests/e2e
```

### Run API tests only

```bash
pytest tests/api
```

### Run by marker

```bash
pytest -m api
pytest -m search
pytest -m registration
pytest -m security
```

---

## 📊 Reporting (Allure)

```bash
pytest --alluredir=allure-results
allure serve allure-results
```

---

## 🧠 Design Principles

* Separate **UI layer** and **API layer**
* Keep tests **clean and readable**
* Move logic into **pages / endpoints / fixtures**
* Prefer **data-driven tests over duplication**
* Fail fast with clear assertions

---

## 🚀 Future Improvements

* Token reuse across API tests
* API + UI hybrid testing (skip UI login)
* CI/CD integration (GitHub Actions)
* Better test data management
* Expanded API coverage

---

## 🔒 Notes

* Sensitive data is NOT committed
* Use `.env.example` as reference
* Replace credentials before running tests

---

## 👨‍💻 Author

A QA Automation project focused on building practical skills in UI and API testing.