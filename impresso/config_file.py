import os

from pydantic import BaseModel, ValidationError
import yaml

from impresso.util.token import get_jwt_status


class ImpressoPyConfigContent(BaseModel):
    """Content of the configuration file."""

    token: str | None = None


class ImpressoPyConfig:
    """File backed configuration of the library."""

    def __init__(self, config_file="~/.impresso_py.yml") -> None:
        self._config_file = config_file
        self._config = ImpressoPyConfigContent()

        filepath = os.path.expanduser(self._config_file)
        if os.path.exists(filepath):
            with open(filepath, "r", encoding="utf-8") as f:
                try:
                    config = yaml.safe_load(f)
                    self._config = ImpressoPyConfigContent.model_validate(config)
                except yaml.YAMLError as exc:
                    print("Error loading config file:", exc)
                except ValidationError as exc:
                    print("Error validating config file:", exc)

    def get_token(self) -> str | None:
        """Return the token for the given username."""
        token = self._config.token
        token_status, _ = get_jwt_status(token)
        if token_status == "valid":
            return token

        return None

    def set_token(self, token: str) -> None:
        """Set the token for the given username."""
        self._config.token = token
        self._write_config()

    def _write_config(self) -> None:
        """Write the configuration to the file."""
        filepath = os.path.expanduser(self._config_file)
        with open(filepath, "w", encoding="utf-8") as f:
            yaml.dump(self._config.model_dump(exclude_none=True), f)
