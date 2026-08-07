from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
import pytest
import allure

@allure.feature("Авторизация")
@allure.story("Авторизации недействительные учетные данные")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Авторизация с недействительными учетными данными")
def test_login_failure(login_page):
    login_page.navigate()
    login_page.login("invalid_user", "invalid_password")
    login_page.should_be_on_login_page()
    login_page.should_be_error_message_on_invalid_credentials()

@allure.feature("Login")
@allure.story("Login with valid credentials")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Авторизация с корректными учетными данными")
@pytest.mark.parametrize("username, password", [
    ("user", "user"),
    ("admin", "admin")
])
def test_login_success(login_page, dashboard_page, username, password):

    login_page.navigate()
    login_page.login(username, password)

    dashboard_page.should_be_welcome_message("Welcome admin")