import pytest


@pytest.fixture(autouse=True)
def send_data():
    print("[AUTOUSE] Отправляем данные в сервис аналитике")


@pytest.fixture(scope="session")
def settings():
    print("[SESSION] Инициализируем настройки тестов ")


@pytest.fixture(scope="class")
def user():
    print("[CLASS] Создаем данные пользователя один раз на тестовый класс")


@pytest.fixture(scope="function")
def browser():
    print("[FUNCTIONAL] Открываем браузер на каждый автотетс")


class TestUserFlow:
    def test_user_login(self, settings, user, browser):
        pass

    def test_user_create_course(self, settings, user, browser):
        pass


class TestAccountFlow:
    def test_user_account(self, settings, user, browser):
        pass
