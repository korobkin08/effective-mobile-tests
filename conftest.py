import pytest
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'

load_dotenv()

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            args=[
                "--no-sandbox",
                "--disable-dev-shm-usage",
                "--disable-gpu"
            ]
        )
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    context = browser.new_context(
        viewport={"width": 1920, "height": 1080},
        locale="ru-RU",
        timezone_id="Europe/Moscow"
    )
    page = context.new_page()
    yield page
    context.close()