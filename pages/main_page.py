from playwright.sync_api import Page, expect


class MainPage:
    def __init__(self, page: Page):
        self.page = page
        self.base_url = "https://effective-mobile.ru"

        # Локаторы в формате {section: (link_selector, target_selector)}
        self.sections = {
            "about": ("a[href='#about']", "section#about"),
            "services": ("a[href='#services']", "section#services"),
            "contacts": ("a[href='#contacts']", "section#contacts"),
            "projects": ("a[href='#projects']", "section#projects")
        }

    def open(self) -> None:
        self.page.goto(self.base_url)
        self.page.wait_for_load_state("networkidle")

    def navigate_to_section(self, section_name: str) -> None:
        link_selector, target_selector = self.sections[section_name]

        with self.page.expect_navigation():
            self.page.click(link_selector)

        expect(self.page.locator(target_selector)).to_be_visible()

    @property
    def current_url(self) -> str:
        return self.page.url