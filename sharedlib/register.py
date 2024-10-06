import sys
import os
import importlib.util
from .config import _get_config


def _register():
    """
    Register a virtual module with "config.import_name" name.
    """
    config, path = _get_config()

    # Calculate the relative path to the shared folder
    module_path = os.path.join(path, config.folder_name, "__init__.py")
    if not os.path.exists(module_path):
        raise ModuleNotFoundError(f"Module {config.folder_name} not found!")

    spec = importlib.util.spec_from_file_location(config.import_name, module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    sys.modules[config.import_name] = module


__all__ = ["_register"]
