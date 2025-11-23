import allure
from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from components.navigation.sidebar_list_item_component import SideBarListComponent
import re


class SidebarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.logout_list_item = SideBarListComponent(page, "logout")
        self.courses_list_item = SideBarListComponent(page, "courses")
        self.dashboard_list_item = SideBarListComponent(page, "dashboard")

    @allure.step('Check visible sidebar')
    def check_visible(self):
        self.logout_list_item.check_visible("Logout")
        self.courses_list_item.check_visible("Courses")
        self.dashboard_list_item.check_visible("Dashboard")

    @allure.step('Click logout on sidebar')
    def click_logout(self):
        self.logout_list_item.navigate_url(re.compile(r".*/#/auth/login"))

    @allure.step('Click courses on sidebar')
    def click_courses(self):
        self.logout_list_item.navigate_url(re.compile(r".*/#/courses"))

    @allure.step('Click dashboard on sidebar')
    def click_dashboard(self):
        self.logout_list_item.navigate_url(re.compile(r".*/#/dashboard"))
