import pytest
import allure
from pages.main_page import MainPage


@allure.epic("Главная страница")
@allure.feature("Навигация по разделам")
class TestMainPageNavigation:
    SECTIONS = ["about", "services", "contacts", "projects"]

    @pytest.mark.smoke
    @pytest.mark.parametrize("section", SECTIONS)
    def test_section_navigation(self, page, section):
        main_page = MainPage(page)

        with allure.step("1. Открыть главную страницу"):
            main_page.open()
            allure.attach(
                page.screenshot(),
                name="main_page_loaded",
                attachment_type=allure.attachment_type.PNG
            )

        with allure.step(f"2. Кликнуть на раздел '{section}'"):
            main_page.navigate_to_section(section)

        with allure.step("3. Проверить URL и видимость раздела"):
            expected_url = f"{main_page.base_url}/#{section}"
            assert main_page.current_url == expected_url

            allure.attach(
                page.screenshot(),
                name=f"section_{section}_opened",
                attachment_type=allure.attachment_type.PNG
            )