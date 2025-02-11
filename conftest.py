import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        # Запуск с графическим интерфейсом для отладки
        browser = p.chromium.launch(
            headless=False,
            args=[
                "--no-sandbox",
                "--start-maximized"
            ],
            timeout=60000
        )
        yield browser
        browser.close()

@pytest.fixture
def context(browser):
    context = browser.new_context(no_viewport=True)  # Полноэкранный режим
    yield context
    context.close()

@pytest.fixture
def page(context):
    page = context.new_page()
    yield page
    page.close()