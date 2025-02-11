import pytest
import allure
from pages.main_page import MainPage

BASE_URL = "https://effective-mobile.ru"


@allure.feature("Главная страница")
class TestNavigation:
    @pytest.mark.parametrize("link_name, expected_path", [
        ("О нас", "/#about"),
        ("Услуги", "/#moreinfo"),
        ("Проекты", "/#cases"),
        ("Отзывы", "/#Reviews"),
        ("Контакты", "/#contacts"),
    ])
    @allure.story("Проверка навигации")
    def test_navigation(self, page, link_name, expected_path):  # Фикстура page из conftest.py
        main_page = MainPage(page)

        with allure.step("Открыть главную страницу"):
            main_page.navigate_to(BASE_URL)

        with allure.step(f"Кликнуть на ссылку '{link_name}'"):
            main_page.click_nav_link(link_name)

        with allure.step(f"Проверить URL страницы"):
            main_page.check_current_url(f"{BASE_URL}{expected_path}")