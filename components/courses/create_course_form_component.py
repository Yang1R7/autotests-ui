import allure

from components.base_component import BaseComponent
from playwright.sync_api import Page, expect

from elements.input import Input
from elements.textarea import Textarea


class CreateCourseFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title_input = Input(page, "create-course-form-title-input", "Title input")

        self.estimated_time_input = Input(
            page,
            "create-course-form-estimated-time-input",
            "Estimated time input"
        )

        self.description_textarea = Textarea(
            page,
            "create-course-form-description-input",
            "Description"
        )

        self.max_score_input = Input(page, "create-course-form-max-score-input", "Max score")
        self.min_score_input = Input(page, "create-course-form-min-score-input", "Min score")

    @allure.step('Fill create course form')
    def fill(
            self,
            title: str,
            estimated_time: str,
            description: str,
            max_score: str,
            min_score: str
    ):
        self.title_input.fill(title)
        self.estimated_time_input.fill(estimated_time)
        self.description_textarea.fill(description)
        self.max_score_input.fill(max_score)
        self.min_score_input.fill(min_score)

    @allure.step('Check visible create course form')
    def check_visible(
            self,
            title: str = None,
            estimated_time: str = None,
            description: str = None,
            max_score: str = None,
            min_score: str = None
    ):
        self.title_input.check_visible()
        if title:
            self.title_input.check_have_text(title)

        self.estimated_time_input.check_visible()
        if estimated_time:
            self.estimated_time_input.check_have_value(estimated_time)

        self.description_textarea.check_visible()
        if description:
            self.description_textarea.check_have_value(description)

        self.max_score_input.check_visible()
        if max_score:
            self.max_score_input.check_have_value(max_score)

        self.min_score_input.check_visible()
        if min_score:
            self.min_score_input.check_have_value(max_score)
