# sharedlib

[![PyPI version](https://img.shields.io/pypi/v/sharedlib)](https://pypi.python.org/pypi/sharedlib/)
[![PyPI Supported Python Versions](https://img.shields.io/pypi/pyversions/sharedlib.svg)](https://pypi.python.org/pypi/sharedlib/)

Pythonic way for use "shared" folder of packages (utils).

## Install package

Install using `pip`:
```bash
pip install sharedlib
```

Install using `uv`:
```bash
uv add sharedlib
```

## Usage

First, we need to import “sharedlib” into the file where we will use the shared packages: 

```py
import sharedlib
```

Then import a “shared” package with the same name as specified in the config settings:

```py
import my_shared_pkg
from my_shared_pkg import a, b, c
from my_shared_pkg.a.b.c import d
```

And it's working! Python registers a package with the specified name and you can use that in your files. 

A complete example: 

```py
# file: service1/routes/admin.py
import sharedlib

# file: service2/models/user.py
import sharedlib

# original folder: custom_shared/
import my_shared_pkg

# original folders: custom_shared/a, custom_shared/b, custom_shared/c
from my_shared_pkg import a, b, c

# original folder: custom_shared/a/b/c, file: d.py
from my_shared_pkg.a.b.c import d

print(a, b, c, d)
```

## Configuration file

### `sharedlib.ini`

To work with “sharedlib” it is necessary to specify the file `sharedlib.ini` in the root of the project (repository):

```ini
[sharedlib]
folder_name = custom_shared
import_name = my_shared_pkg
```

If the file is not found, an exception will be raised. 

> Important: The configuration file must be located in the root of the project. Otherwise imports will not work properly. 

### `pyproject.toml`

You can also use `pyproject.toml` for customization:

```toml
[tool.sharedlib]
folder_name = "custom_shared"
import_name = "my_shared_pkg"
```

## Contributing

If you would like to suggest a new feature, you can create an issue on the GitHub repository for this project. Also you can fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for more information.
