from api_yamdb import settings


class TestSettings:

    def test_settings(self):

        assert not settings.DEBUG, 'Проверьте, что DEBUG в настройках Django выключен'  # nopep8
        assert settings.DATABASES['default']['ENGINE'] == 'django.db.backends.postgresql', 'Проверьте, что используете базу данных PostgreSql'  # nopep8
