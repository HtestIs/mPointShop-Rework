# mPointShop Rework

![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-Automation-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-UI_Testing-43B02A?style=for-the-badge&logo=selenium&logoColor=white)
![Allure](https://img.shields.io/badge/Allure-Reporting-8A2BE2?style=for-the-badge)

Automation framework for the **mPointShop ecosystem**, covering **UI**, **API**, **mobile**, and **cross-system hybrid** validation across `mPointShop`, `mExchange`, `mShopAdmin`, and `mPointApp`.

---

## ✨ Highlights

- `pytest` + `selenium` + `allure` test stack
- Page Object Model for UI automation
- Shared base classes, drivers, and helpers in `core/`
- Shared fixture plugins for cross-system API setup
- Environment-based execution using `.env` and `--env`
- HTML and Allure reporting built in

---

## 🧱 Systems Covered

| System | Scope | Coverage | Notes |
|---|---|---|---|
| `mPointShop` | Merchant / partner product | API + E2E | Main system under active coverage |
| `mExchange` | Voucher exchange integration | API + E2E | Reuses shared voucher sync helpers |
| `mShopAdmin` | Admin / AAP portal | E2E in progress | ⚠️ Login can be unstable because some environments show **captcha** |
| `mPointApp` | Mobile app | Appium-ready scaffold | Placeholder structure ready for future device automation |

---

## 📁 Project Structure

```text
mPointShop_rework/
├─ core/
│  ├─ base/                      # shared BasePage / API client layers
│  ├─ drivers/                   # browser driver manager
│  └─ utils/                     # token helpers, data helpers, shared flows
├─ config/                       # env config loading and shared settings
├─ data/                         # factories and static test data
│  ├─ store_data.py
│  └─ voucher_data.py
├─ fixtures/
│  ├─ driver_fixture.py          # shared Selenium driver fixture
│  ├─ shared_api_fixtures.py     # shared login/API fixtures
│  └─ shared_voucher_fixtures.py # shared voucher fixtures
├─ mPointShop/
│  ├─ api/
│  │  ├─ api_assertions/
│  │  ├─ endpoints/
│  │  ├─ flows/
│  │  └─ helpers/
│  ├─ pages/
│  │  ├─ components/
│  │  ├─ login_page.py
│  │  ├─ menu_page.py
│  │  ├─ store_manage_page.py
│  │  └─ voucher_partner_page.py
│  ├─ tests/
│  │  ├─ api/
│  │  └─ e2e/
│  └─ conftest.py
├─ mExchange/
│  ├─ api/
│  │  ├─ endpoints/
│  │  ├─ flows/
│  │  └─ helpers/
│  ├─ pages/
│  │  ├─ login_page.py
│  │  └─ menu_page.py
│  ├─ tests/
│  │  ├─ api/
│  │  └─ e2e/
│  └─ conftest.py
├─ mShopAdmin/
│  ├─ pages/
│  │  ├─ basepage.py
│  │  ├─ dashboard_page.py
│  │  ├─ login_page.py
│  │  └─ voucher_list_page.py
│  ├─ tests/
│  │  ├─ api/
│  │  └─ e2e/
│  └─ conftest.py
├─ mPointApp/
│  ├─ pages/
│  │  ├─ base_screen.py
│  │  └─ login_screen.py
│  ├─ tests/
│  │  └─ e2e/
│  └─ conftest.py
├─ reports/                      # pytest-html output
├─ allure-results/               # raw Allure results
├─ allure-report/                # generated Allure report
├─ conftest.py                   # root pytest options + shared plugins
├─ pytest.ini                    # markers and runner settings
├─ requirements.txt
└─ README.md
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

Copy `.env.example` to `.env` and fill in the required values for:

- `mPointShop` web URL, API URL, partner/merchant credentials
- `mExchange` web URL, API URL, exchange credentials
- `mShopAdmin` / AAP URL and admin credentials

---

## 📱 mPointApp / Mobile Scaffold

The mobile area is a **starter Appium scaffold** for future app automation.

### Included

- `mPointApp/conftest.py` with an Appium-ready `mobile_driver` fixture
- `mPointApp/pages/base_screen.py` for shared mobile screen actions
- `mPointApp/pages/login_screen.py` as a starter login page object
- `mPointApp/tests/e2e/test_app_smoke.py` as a placeholder smoke test

> The project uses `Appium-Python-Client`, so install dependencies from `requirements.txt` before running mobile tests.

Update the placeholder locators in `mPointApp/pages/login_screen.py` to match the real app under test.

---

## ▶️ Running Tests

### Run all tests

```powershell
pytest
```

### Run by system

```powershell
pytest mPointShop/tests
pytest mExchange/tests
pytest mShopAdmin/tests
pytest mPointApp/tests
```

### Run by marker

```powershell
pytest -m mpointshop
pytest -m mexchange
pytest -m mshopadmin
pytest -m mpointapp
pytest -m api
pytest -m e2e
pytest -m smoke
pytest -m ongoing
pytest -m defect
```

### Run with environment and browser options

```powershell
pytest --env=dev --browser=chrome
```

> If `CI=true` is set, browser sessions run in headless mode automatically.

---

## 🏷️ Pytest Markers

Common markers defined in `pytest.ini` include:

- `mpointshop`
- `mexchange`
- `mshopadmin`
- `mpointapp`
- `api`
- `e2e`
- `smoke`
- `slow`
- `registration`
- `search`
- `security`
- `ongoing`
- `defect`

---

## 📊 Reports

### HTML report

```text
reports/report.html
```

### Allure report

```powershell
pytest --alluredir=allure-results
allure serve allure-results
```

On failures, the framework can attach:

- screenshots
- page source
- current URL
- browser logs (when available)

---

## ⚠️ Known Notes / Limitations

- `mShopAdmin` may show a **captcha** on the login page in some environments.
- Because of that, AAP login-related E2E tests can be **blocked or unstable** until a test-safe bypass or captcha-free QA environment is available.
- Cross-system voucher helpers are shared through `core/utils/shared_voucher_flows.py`.

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
