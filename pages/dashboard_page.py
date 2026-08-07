import allure
from playwright.sync_api import Page, expect


class DashboardPage():
    def __init__(self, page: Page):
        self.page = page
        self.profile = page.locator("#usernameDisplay")
        self.logout = page.locator("#logout")

    def should_be_welcome_message(self, message):
        with allure.step(f"Отображается приветственное сообщение: {message}"):
            expect(self.profile).to_have_text(message)