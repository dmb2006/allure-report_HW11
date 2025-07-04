import json

import allure
from selene import browser, have, by
import pytest
from selene.support.shared.jquery_style import s
from allure_commons.types import AttachmentType, Severity
from page.test_decorator import GitHub


def test_open_github_selene(browser_configuration):
    browser.open("https://github.com")
    s('.header-search-button').click()
    s('#query-builder-test').send_keys('dmb2006/allure-report_HW11').press_enter()
    s(by.css('a[href="/dmb2006/allure-report_HW11"]')).click()
    s('#issues-tab').click()
    s('[class^=TokenTextContainer]').should(have.exact_text('documentation'))

def test_open_github_lambda(browser_configuration):
    with allure.step('Открываем главую страницу GitHub'):
        browser.open("https://github.com")

    with allure.step('Кликаем на поисковую строку'):
        s('.header-search-button').click()

    with allure.step('Ищем репозиторий dmb2006/allure-report_HW11'):
        s('#query-builder-test').send_keys('dmb2006/allure-report_HW11').press_enter()

    with allure.step('Переходим в репозиторий'):
        s(by.css('a[href="/dmb2006/allure-report_HW11"]')).click()

    with allure.step('Переходим на вкладку Issues в репозитории'):
        browser.element('#issues-tab').click()

    with allure.step('Находим Issues с тегом в \'documentation'):
        s('[class^=TokenTextContainer]').should(have.exact_text('documentation'))


def test_open_github_decorator(browser_configuration):
    github = GitHub()

    github.open_github()
    github.find_search_bar()
    github.find_repo('dmb2006/allure-report_HW11')
    github.click_to_repo()
    github.switching_to_tab_issues()
    github.issues_find_documentation()




