import configparser
from pathlib import Path
from typing import Optional, Union
from flask import Flask


def create_app(config_path: Optional[Union[str, Path]] = None) -> Flask:
    app = Flask(__name__)

    if config_path is None:
        config_path = Path(__file__).resolve().parent / "config.properties"

    config = configparser.ConfigParser()
    loaded = config.read(config_path)
    if not loaded:
        raise FileNotFoundError(f"Config file not found at: {config_path}")

    @app.route("/")
    def hello():
        if config.getboolean("features", "feature_1"):
            message = "Hello, Maria!"
        else:
            message = "Hello, World!"
        return message

    return app


if __name__ == "__main__":
    application = create_app()
    application.run(host="0.0.0.0", port=8050)
