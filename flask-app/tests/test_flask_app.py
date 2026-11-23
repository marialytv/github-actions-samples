import pytest
from app import create_app

def write_config(tmp_path, content: str):
    cfg_file = tmp_path / "config.properties"
    cfg_file.write_text(content.strip(), encoding="utf-8")
    return cfg_file

def test_shows_personalised_message_when_enabled(tmp_path):
    cfg_file = write_config(
        tmp_path,
        """
        [features]
        feature_1 = true
        """,
    )
    app = create_app(config_path=cfg_file)
    client = app.test_client()

    response = client.get("/")

    assert response.get_data(as_text=True) == "Hello, Maria!"


def test_shows_standard_message_when_disabled(tmp_path):
    cfg_file = write_config(
        tmp_path,
        """
        [features]
        feature_1 = false
        """,
    )
    app = create_app(config_path=cfg_file)
    client = app.test_client()

    response = client.get("/")

    assert response.get_data(as_text=True) == "Hello, World!"


def test_raises_error_when_config_missing(tmp_path):
    missing_file = tmp_path / "does_not_exist.properties"

    with pytest.raises(FileNotFoundError):
        create_app(config_path=missing_file)