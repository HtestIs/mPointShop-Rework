# mPointShop Rework 🚀

![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-Framework-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-Automation-43B02A?style=for-the-badge&logo=selenium&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-API-FF6F00?style=for-the-badge)
![Allure](https://img.shields.io/badge/Allure-Reports-8A2BE2?style=for-the-badge)

A QA automation project built to practice and improve structured **UI**, **API**, and **hybrid** testing using Python tools on the `mPointShop` system, with room to expand into `mExchange` later.

---

## ✨ Highlights

- **UI automation** with Selenium using the **Page Object Model (POM)**
- **API testing** with Requests and reusable endpoint/client layers
- **Hybrid test flows** using API setup + UI verification
- **Data-driven tests** with reusable fixtures and test data modules
- **Environment-based configuration** via `.env`
- **Allure reporting** for test evidence and debugging artifacts

---

## 🧰 Tech Stack

| Area | Tools |
|---|---|
| Language | Python 3.12 |
| Test runner | `pytest` |
| UI automation | `selenium` |
| API testing | `requests` |
| Reporting | `allure-pytest`, `pytest-html` |
| Test utilities | `Faker`, `pytest-xdist`, `pytest-repeat` |

---

## 📁 Project Structure

```text
mPointShop_rework/
├─ api/
│  ├─ mPointShop/
│  │  ├─ api_assertions/
│  │  ├─ endpoints/
│  │  ├─ helpers/
│  │  └─ client.py
│  └─ mExchange/
├─ pages/
│  ├─ mPointShop/
│  │  ├─ base_page.py
│  │  ├─ login_page.py
│  │  ├─ menu_page.py
│  │  ├─ store_manage_page.py
│  │  ├─ voucher_partner_page.py
│  │  ├─ voucher_scan_page.py
│  │  └─ warehouse_page.py
│  └─ mExchange/
├─ tests/
│  ├─ mPointShop/
│  │  ├─ api/
│  │  │  ├─ auth/
│  │  │  ├─ menu/
│  │  │  └─ stores/
│  │  └─ e2e/
│  │     ├─ auth/
│  │     ├─ store/
│  │     ├─ voucher/
│  │     └─ conftest.py
│  └─ mExchange/
├─ data/
├─ fixtures/
├─ config/
├─ reports/
├─ allure-results/
├─ allure-report/
├─ conftest.py
├─ pytest.ini
└─ requirements.txt
```

---

## 🧪 Current Coverage

### E2E (`tests/mPointShop/e2e`)
- **Auth**: login scenarios
- **Store**: registration, search, location behavior, security flows
- **Voucher**: voucher creation/sync and voucher scan flows

### API (`tests/mPointShop/api`)
- **Auth** endpoints
- **Menu** endpoints
- **Store** endpoints and assertions

### Hybrid scenarios
- API used for fast setup
- UI used for user-facing verification
- Example: create/sync voucher by API, then validate behavior in UI

---

## ⚙️ Setup

### 1) Create and activate a virtual environment

**Windows PowerShell**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2) Install dependencies

```bash
pip install -r requirements.txt
```

### 3) Configure environment variables

Create a `.env` file from `.env.example` and fill in your real values:

```env
DEV_WEB_BASE_URL=...
DEV_API_BASE_URL=...
DEV_PARTNER_USERNAME=...
DEV_PARTNER_PASSWORD=...
DEV_MERCHANT_USERNAME=...
DEV_MERCHANT_PASSWORD=...
DEV_DUP_USERNAME=...

PROD_WEB_BASE_URL=...
PROD_API_BASE_URL=...
PROD_PARTNER_USERNAME=...
PROD_PARTNER_PASSWORD=...
PROD_MERCHANT_USERNAME=...
PROD_MERCHANT_PASSWORD=...
PROD_DUP_USERNAME=...
```

> The active environments are defined in `config/env_config.py`.

---

## ▶️ Running Tests

### Run everything

```bash
pytest
```

### Run only E2E tests

```bash
pytest tests/mPointShop/e2e
```

### Run only API tests

```bash
pytest tests/mPointShop/api
```

### Run by feature group

```bash
pytest tests/mPointShop/e2e/auth
pytest tests/mPointShop/e2e/store
pytest tests/mPointShop/e2e/voucher
```

### Run with markers

```bash
pytest -m api
pytest -m e2e
pytest -m search
pytest -m registration
pytest -m security
```

### Run with options

```bash
pytest --env=dev --browser=chrome
```

Available options from `conftest.py`:
- `--env` → environment key such as `dev` or `prod`
- `--browser` → browser name, default is `chrome`

---

## 📊 Reporting

### Allure

```bash
pytest --alluredir=allure-results
allure serve allure-results
```

On failures, the framework attaches useful evidence such as:
- screenshots
- page source
- current URL
- browser logs when available

---

## 🧠 Framework Design Notes

- Keep **tests readable**, with logic pushed into `pages/`, `api/`, and fixtures
- Prefer **reusable helpers and assertions** over duplicated code
- Use **data-driven** patterns for validation-heavy scenarios
- Separate coverage by **system** (`mPointShop`, `mExchange`) and by **test type** (`api`, `e2e`)

---

## 🔒 Notes

- Do not commit real credentials or sensitive URLs
- Use `.env.example` as the source template
- `mExchange` folders are already scaffolded for future expansion
