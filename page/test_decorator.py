import allure
from selene import browser, have, be, by
from selene.support.shared.jquery_style import s
import json
from allure_commons.types import AttachmentType


class GitHub:
    @allure.step('Открываем главую страницу GitHub')
    def open_github(self):
        browser.open("https://github.com")

    @allure.step('Кликаем на поисковую строку')
    def find_search_bar(self):
        s('.header-search-button').click()

    @allure.step('Ищем репозиторий {repo}')
    def find_repo( self, repo):
        s('#query-builder-test').should(be.visible)
        s('#query-builder-test').send_keys(f'{repo}').press_enter()

    @allure.step('Переходим в репозиторий')
    def click_to_repo(self):
        s(by.css(f'a[href="/dmb2006/allure-report_HW11"]')).click()

        # "/dmb2006/allure-report_HW11"
    @allure.step('Переходим на вкладку Issues в репозитории')
    def switching_to_tab_issues(self):
        browser.element('#issues-tab').click()

    @allure.step('Находим Issues с тегом в \'documentation')
    def issues_find_documentation(self):
        s('[class^=TokenTextContainer]').should(have.exact_text('documentation'))

