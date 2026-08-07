from playwright.sync_api import Page, expect
import allure

class LoginPage():
    def __init__(self, page: Page): # page: Page является аннотацией типа, указывающей на то, что параметр page должен быть объектом типа Page из Playwright
        self.page = page # сохраняет объект странице в атрибуте экземпляра класса для дальнейшего использования
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login")
        self.error_message = page.locator("#errorAlert")

    URL = 'https://zimaev.github.io/pom/'
    INVALID_CREDENTIALS_MESSAGE = 'Invalid credentials. Please try again.'

    def navigate(self):
        """Открывает страницу логина"""
        with allure.step("Открыть страницу авторизации"):
            self.page.goto(self.URL)

    def login(self, username: str, password: str):
        """Выполняет вход с заданными учетными данными"""
        with allure.step(f"Ввод в форму авторизации логина {username} и пароля {password}"):
            self.username_input.fill(username)
            self.password_input.fill(password)
            self.login_button.click()

    def get_error_message(self):
        """Возвращает текст об ошибке"""
        return self.error_message.inner_text()

    def should_be_on_login_page(self):
        """ Check if there is still login page and url is not changed """
        with allure.step("URL не изменился"):
            expect(self.page).to_have_url(LoginPage.URL)

    def should_be_error_message_on_invalid_credentials(self):
        """ Check if there is correct error message on invalid credentials """
        with allure.step(f"Отображается ошибка: {LoginPage.INVALID_CREDENTIALS_MESSAGE}"):
            expect(self.error_message).to_have_text(LoginPage.INVALID_CREDENTIALS_MESSAGE)