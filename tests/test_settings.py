import pytest
from pydantic import ValidationError

from settings import Settings

# load_dotenv()


def test_settings_load_properly():
    settings = Settings()

    assert isinstance(settings.API_KEY, str)
    assert isinstance(settings.ENVIRONMENT, str)
    assert isinstance(settings.APP_NAME, str)


@pytest.mark.parametrize("env_name", ["dev", "prod", "test"])
def test_settings_accepts_env(env_name: str):
    settings = Settings(ENVIRONMENT=env_name)

    assert settings.ENVIRONMENT == env_name


def test_settings_invalid_env():
    with pytest.raises(ValidationError):
        Settings(ENVIRONMENT="invalid-env")
