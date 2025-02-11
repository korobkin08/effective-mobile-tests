from playwright.sync_api import Page, expect


class MainPage:
    def __init__(self, page: Page):
        self.page = page
        self.nav_links = {
            "О нас": page.get_by_role("link", name="О нас"),
            "Услуги": page.get_by_role("link", name="Услуги"),
            "Проекты": page.get_by_role("link", name="Проекты"),
            "Отзывы": page.get_by_role("link", name="Отзывы"),
            "Контакты": page.get_by_role("link", name="Контакты"),

        }

    def navigate_to(self, url: str):
        self.page.goto(url)

    def click_nav_link(self, link_name: str):
        self.nav_links[link_name].click()

    def check_current_url(self, expected_url: str):
        expect(self.page).to_have_url(expected_url)