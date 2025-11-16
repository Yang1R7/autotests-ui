import pytest
from playwright.sync_api import Page

from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage


@pytest.fixture(scope="function")
def login_page(chromium_page) -> LoginPage:
    return LoginPage(page=chromium_page)


@pytest.fixture(scope="function")
def dashboard_page(chromium_page) -> DashboardPage:
    return DashboardPage(page=chromium_page)

@pytest.fixture(scope="function")
def dashboard_page_with_state(chromium_page_with_state) -> DashboardPage:
    return DashboardPage(page=chromium_page_with_state)


@pytest.fixture(scope="function")
def registration_page(chromium_page) -> RegistrationPage:
    return RegistrationPage(page=chromium_page)


@pytest.fixture(scope="function")
def courses_list_page(chromium_page_with_state) -> CoursesListPage:
    return CoursesListPage(page=chromium_page_with_state)


@pytest.fixture(scope="function")
def create_course_page(chromium_page_with_state) -> CreateCoursePage:
    return CreateCoursePage(page=chromium_page_with_state)
