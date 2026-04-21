# mPointShop Rework

![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-Automation-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-UI_Testing-43B02A?style=for-the-badge&logo=selenium&logoColor=white)
![Allure](https://img.shields.io/badge/Allure-Reporting-8A2BE2?style=for-the-badge)

Automation framework for the **mPointShop ecosystem**, covering UI, API, mobile and cross-system flows across `mPointShop`, `mExchange`, `mShopAdmin` and `mPointApp`.

Quick links
- pytest configuration: `pytest.ini`
- test entrypoints: `mPointShop/tests`, `mExchange/tests`, `mShopAdmin/tests`, `mPointApp/tests`

---

## Requirements

- Python 3.10+ (3.12 badge used in repo)
- Git (to clone)
- Windows: PowerShell recommended for provided examples
- Optional: Allure CLI if you want to serve the Allure report locally

Install project dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

---

## Configure environment

1. Copy `.env.example` to `.env` and fill required values. Typical keys used by tests / fixtures:

- `mpointshop_web_url`, `mpointshop_api_url`, `mpointshop_username`, `mpointshop_password`
- `mexchange_web_url`, `mexchange_api_url`, `mexchange_username`, `mexchange_password`
- `mshopadmin_web_url`, `mshopadmin_username`, `mshopadmin_password`
- `app_username`, `app_password`

2. The test runner accepts `--env` to select environment config (see `config/env_config.py`) and `CI=true` can be used to force headless browser sessions in CI.

---

## Running tests

- Run all tests (note: `pytest.ini` sets useful default options including HTML and Allure output):

```powershell
pytest
```

- Run tests by marker (recommended):

```powershell
pytest -m mpointshop
pytest -m mexchange
pytest -m mshopadmin
pytest -m mpointapp
pytest -m api
pytest -m e2e
```

- Run tests with environment/browser options:

```powershell
pytest --env=dev --browser=chrome --headless
```

- Run a single test file or folder:

```powershell
pytest mPointShop/tests/e2e/auth/test_login.py -q
```

---

## Pytest markers & conventions

Markers are defined in `pytest.ini` (strict markers enabled). Common markers:

- System-level: `mpointshop`, `mexchange`, `mshopadmin`, `mpointapp`
- Test type: `api`, `e2e`, `smoke`, `regression`, `slow`
- Status: `defect`, `ongoing`, `oopsie`, `fixthisdumdum`

The UI `driver` fixture uses markers (via `request.node.get_closest_marker(...)`) to determine which base URL fixture to use (e.g. `mexchange_base_url`). Keep test markers consistent so fixtures can pick the correct configuration.

---

## Reports

- HTML report: `reports/report.html` (pytest-html)

- Allure results (preferred for rich reporting):

```powershell
pytest --alluredir=allure-results
# Serve (if Allure CLI installed)
allure serve allure-results
# Or generate a static report
allure generate allure-results -o allure-report --clean
allure open allure-report
```

On failures, the framework attaches screenshots, page source, current URL and browser logs (when available) to Allure results.

---

## Mobile (mPointApp)

The `mPointApp` folder contains a starter Appium scaffold. Before running mobile tests:

- Ensure Appium / device/emulator is available
- Update locators in `mPointApp/pages/login_screen.py`
- Run mobile tests with the same `pytest` CLI; mobile fixtures provide a `mobile_driver` fixture scoped per test/session

---

## Troubleshooting / Notes

- `mShopAdmin` login may display a captcha in some environments — those E2E tests can be flaky until a captcha-free test environment is available.
- Do not commit secrets into repository. Use `.env` and CI secret storage.
- Add any new custom markers to `pytest.ini` (project uses `--strict-markers`).

---

## Contributing

1. Create a branch
2. Run tests locally for the area you changed (use markers)
3. Open a PR describing the change and how to run affected tests

---

If you'd like, I can also:
- generate a shorter "Quickstart" README for newcomers
- add a PowerShell script that wraps common pytest commands

