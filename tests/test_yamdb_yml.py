import os

from django.conf import settings


class TestWorkflow:

    def test_workflow(self):
        try:
            with open(f'{os.path.join(settings.BASE_DIR, "yamdb_workflow.yaml")}', 'r') as f:  # noqa: E501
                yamdb = f.read()
        except FileNotFoundError:
            assert False, 'Проверьте, что добавили файл yamdb_workflow.yaml в корневой каталог для проверки'  # noqa: E501

        assert 'on: [push]' in yamdb, 'Проверьте, что добавили действие при пуше в файл yamdb_workflow.yaml'  # noqa: E501
        assert 'pytest' in yamdb, 'Проверьте, что добавили pytest в файл yamdb_workflow.yaml'  # noqa: E501
        assert 'appleboy/ssh-action' in yamdb, 'Проверьте, что добавили деплой в файл yamdb_workflow.yaml'  # noqa: E501
        assert 'appleboy/telegram-action' in yamdb, 'Проверьте, что добавили доставку отправку telegram сообщения в файл yamdb_workflow.yaml'  # noqa: E501
