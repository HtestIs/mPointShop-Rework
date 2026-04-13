# mPointShop Rework

Test automation framework for the mPointShop ecosystem, covering API, web E2E, and mobile-app E2E flows.

## Scope

- mPointShop
- mExchange
- mShopAdmin
- mPointApp

## Stack

- Python 3.12
- Pytest
- Selenium
- Appium (mPointApp)
- Allure + pytest-html reports

## Quick Setup

1. Create and activate venv

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies

```powershell
pip install -r requirements.txt
```

3. Configure environment variables in `.env`

## Default Test Policy

By default, test runs now exclude these markers:

- `defect`
- `oopsie`
- `mpointapp`

This is enforced in `pytest.ini` with:

```ini
-m "not defect and not oopsie and not mpointapp"
```

So running plain `pytest` will skip defect/oopsie/mobile-app tests automatically.

## Running Tests

Run default suite (with excluded markers above):

```powershell
pytest
```

Run only stable web/API E2E for a system:

```powershell
pytest mPointShop/tests
pytest mExchange/tests
pytest mShopAdmin/tests
```

Run excluded groups intentionally (override default with `-m`):

```powershell
pytest -m "mpointapp"
pytest -m "defect"
pytest -m "oopsie"
pytest -m "defect or oopsie"
```

Run with env/browser options:

```powershell
pytest --env=dev --browser=chrome
```

## Marker Catalog

- `smoke`
- `regression`
- `slow`
- `search`
- `registration`
- `security`
- `e2e`
- `api`
- `mpointshop`
- `mexchange`
- `mshopadmin`
- `mpointapp`
- `ongoing`
- `defect`
- `oopsie`
- `fixthisdumdum`

## Reports

HTML report:

- `reports/report.html`

Allure report:

```powershell
pytest --alluredir=allure-results
allure serve allure-results
```

## Notes

- mShopAdmin login can be unstable in environments that enable captcha.
- mPointApp suites are organized in `mPointApp/tests/e2e/register` and `mPointApp/tests/e2e/login`.
- CI limitation: a reliable setup for Appium and Android virtual devices/emulators in CI has not been finalized yet.
