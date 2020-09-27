import os

from django.conf import settings


class TestRequirements:

    def test_requirements(self):
        try:
            with open(f'{os.path.join(settings.BASE_DIR, "requirements.txt")}', 'r') as f:  # nopep8
                requirements = f.read()
        except FileNotFoundError:
            assert False, 'Проверьте, что добавили файл requirements.txt'

        assert 'gunicorn' in requirements, 'Проверьте, что добавили gunicorn в файл requirements.txt'  # nopep8
        assert 'django' in requirements, 'Проверьте, что добавили django в файл requirements.txt'  # nopep8
        assert 'pytest-django' in requirements, 'Проверьте,pytest-django в файл requirements.txt'  # nopep8
