import allure
from allure_commons.types import Severity


@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.label('Owner', 'mininAV')
@allure.feature('Задачи в репозитории')
@allure.link("https://github.com", name="Testing")
@allure.story('Просмотр задач авторизованным пользователем')
def test_decorators_label():
    pass