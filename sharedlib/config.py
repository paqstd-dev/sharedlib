import os
import configparser
import tomllib
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class _config:
    folder_name: str = "shared"
    import_name: str = "_shared"


_CONFIG_SECTION = "sharedlib"
_CONFIG_FILENAME = f"{_CONFIG_SECTION}.ini"
_PYPROJECT_FILENAME = "pyproject.toml"


def _get_config() -> tuple[_config, str]:
    """
    Searches for the config file recursively, moving one level up.
    """
    current_dir = os.path.dirname(__file__)

    while True:
        # Search for pyproject.toml
        pyproject_file_path = os.path.join(current_dir, _PYPROJECT_FILENAME)
        file_content = None

        if os.path.exists(pyproject_file_path):
            with open(pyproject_file_path, "rb") as f:
                pyproject_data = tomllib.load(f)
            if _CONFIG_SECTION in pyproject_data:
                file_content = pyproject_data[f"tool.{_CONFIG_SECTION}"]

        # Search for _CONFIG_FILENAME
        ini_file_path = os.path.join(current_dir, _CONFIG_FILENAME)
        if os.path.exists(ini_file_path):
            config = configparser.ConfigParser()
            config.read(ini_file_path)

            if not config.has_section(_CONFIG_SECTION):
                raise KeyError(
                    f'"[{_CONFIG_SECTION}]" section is required in file `{_CONFIG_FILENAME}`!'
                )
            file_content = config[_CONFIG_SECTION]

        if file_content is not None:
            try:
                return _config(**file_content), current_dir
            except Exception:
                raise KeyError("Unexpected key found!")

        parent_dir = os.path.dirname(current_dir)
        if parent_dir == current_dir:
            # Reached the root directory, file not found
            raise FileNotFoundError(
                f"Neither {_PYPROJECT_FILENAME} nor {_CONFIG_FILENAME} file found"
            )
        current_dir = parent_dir


__all__ = ["_get_config"]
