import time

from playwright.sync_api import sync_playwright, expect
import pytest


@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(registration_page, dashboard_page):
    registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    registration_page.fill_registration_form(email="user.name@gmail.com", username="username", password="password")
    registration_page.click_registration_button()

    dashboard_page.check_dashboard_title()
