# mPointShop Rework

![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-Automation-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-UI_Testing-43B02A?style=for-the-badge&logo=selenium&logoColor=white)
![Allure](https://img.shields.io/badge/Allure-Reporting-8A2BE2?style=for-the-badge)

Python test automation framework for **mPointShop**, **mExchange**, and **mShopAdmin**.
It supports **UI**, **API**, and **cross-system hybrid** validation using `pytest`, `selenium`, and reusable client/fixture layers.

---

## ✨ Highlights

- Page Object Model for UI automation
- Shared Selenium base layer in `core/`
- API client + endpoint abstraction for backend checks
- Environment-driven execution with `.env` and `--env`
- Built-in HTML and Allure reporting
- Known failing cases can be tagged with `@pytest.mark.defect`

---

## 🧱 Systems Covered

| System | Purpose | Current focus |
|---|---|---|
| `mPointShop` | Main merchant/partner flows | UI + API + E2E |
| `mExchange` | Exchange-side integration flows | API + E2E |
| `mShopAdmin` | Admin system | early structure / extension point |

---

## 📁 Project Structure

```text
mPointShop_rework/
├─ core/                 # shared base classes, drivers, utilities
├─ config/               # environment config loading
├─ fixtures/             # shared pytest fixtures
├─ data/                 # test data factories and helpers
├─ mPointShop/           # app-specific pages, API, tests
├─ mExchange/            # app-specific pages, API, tests
├─ mShopAdmin/           # third system pages, API, tests
├─ reports/              # pytest-html output
├─ allure-results/       # raw Allure results
├─ allure-report/        # generated Allure report
├─ conftest.py           # global pytest config/options
├─ pytest.ini            # markers and runner settings
└─ requirements.txt
```

---

## ⚙️ Setup

### 1. Create and activate a virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2. Install dependencies

```powershell
pip install -r requirements.txt
```

### 3. Configure environment variables

Copy `.env.example` to `.env`, then fill in your real values.

#### Core `mPointShop` values

```env
DEV_WEB_BASE_URL=
DEV_API_BASE_URL=
DEV_PARTNER_USERNAME=
DEV_PARTNER_PASSWORD=
DEV_MERCHANT_USERNAME=
DEV_MERCHANT_PASSWORD=
DEV_DUP_USERNAME=

PROD_WEB_BASE_URL=
PROD_API_BASE_URL=
PROD_PARTNER_USERNAME=
PROD_PARTNER_PASSWORD=
PROD_MERCHANT_USERNAME=
PROD_MERCHANT_PASSWORD=
PROD_DUP_USERNAME=
```

#### `mExchange` values

```env
DEV_MEXCHANGE_WEB_URL=
DEV_MEXCHANGE_API_URL=
DEV_MEXCHANGE_USERNAME=
DEV_MEXCHANGE_PASSWORD=

PROD_MEXCHANGE_WEB_URL=
PROD_MEXCHANGE_API_URL=
PROD_MEXCHANGE_USERNAME=
PROD_MEXCHANGE_PASSWORD=
```

#### `mShopAdmin` / AAP values

```env
DEV_AAP_BASE_URL=
DEV_AAP_USERNAME=
DEV_AAP_PASSWORD=

PROD_AAP_BASE_URL=
PROD_AAP_USERNAME=
PROD_AAP_PASSWORD=
```

---

## ▶️ Running Tests

### Run the full suite

```powershell
pytest
```

### Run by system

```powershell
pytest mPointShop/tests
pytest mExchange/tests
pytest mShopAdmin/tests
```

### Run by feature area

```powershell
pytest mPointShop/tests/e2e/auth
pytest mPointShop/tests/e2e/store
pytest mPointShop/tests/e2e/voucher
pytest mExchange/tests/api
pytest mExchange/tests/e2e
```

### Run by marker

```powershell
pytest -m smoke
pytest -m api
pytest -m e2e
pytest -m regression
pytest -m ongoing
pytest -m defect
```

### Run with environment and browser options

```powershell
pytest --env=dev --browser=chrome
```

> If `CI=true` is set, the browser driver runs headless automatically.

---

## 🏷️ Available Pytest Markers

Defined in `pytest.ini`:

- `smoke`
- `regression`
- `slow`
- `search`
- `registration`
- `security`
- `e2e`
- `api`
- `ongoing`
- `defect`
- `fixthisdumdum`

---

## 📊 Reports

### HTML report

Generated automatically at:

```text
reports/report.html
```

### Allure report

```powershell
pytest --alluredir=allure-results
allure serve allure-results
```

On failures, the framework attaches:
- screenshot
- page source
- current URL
- browser logs (when available)

---

## 🧠 Framework Notes

- Keep shared logic in `core/`
- Keep system-specific behavior inside each product folder
- Prefer fixtures and data factories over repeated setup code
- Use API setup + UI verification for faster hybrid coverage
- Mark unstable known issues with `@pytest.mark.defect`

---

## 📸 Report Preview

### Overview
<p align="center">
  <img src="./assets/readme/overview.png" alt="Allure overview screenshot" width="900" />
</p>

### Behaviors
<p align="center">
  <img src="./assets/readme/behavior.png" alt="Allure behaviors screenshot" width="900" />
</p>

### Packages
<p align="center">
  <img src="./assets/readme/packages.png" alt="Allure packages screenshot" width="900" />
</p>

Screenshots are stored in `assets/readme/`.
