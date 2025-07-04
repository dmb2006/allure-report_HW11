import json
import allure
from allure_commons.types import AttachmentType


def test_attachment():
    allure.attach('Проверка на наличие issues в repo', name='Text', attachment_type=AttachmentType.TEXT)
    allure.attach('<h1>Проверка на наличие issues в repo</h1>', name='HTML', attachment_type=AttachmentType.HTML)
    allure.attach(json.dumps({'first': 'issues', 'second': 1}), name='Json', attachment_type=AttachmentType.JSON)