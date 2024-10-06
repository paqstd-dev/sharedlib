# sharedlib

[![PyPI version](https://img.shields.io/pypi/v/sharedlib)](https://pypi.python.org/pypi/sharedlib/)
[![PyPI Supported Python Versions](https://img.shields.io/pypi/pyversions/sharedlib.svg)](https://pypi.python.org/pypi/sharedlib/)

Pythonic way for use "shared" folder of packages in monorepo.
Without dependencies!

## Install package

Install using `pip`:
```bash
pip install sharedlib
```

Install using `uv`:
```bash
uv add sharedlib
```

## Local usage

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

> Shared module should have `__init__.py` file by default. This limitation will be fixed later.  

### An example of a file structure:  
```
service1/
    venv/
    main.py
    requirements.txt
    ...
service2/
    venv/
    main.py
    requirements.txt
    ...
common/
    __init__.py
    ...
pyproject.toml
sharedlib.ini
```

## Docker usage

You can also use Docker to work with a monorepository. To configure the shared module, you need to add the shared folder to the service container. 

```Dockerfile
# you can use any python >= 3.8
FROM python:3.12-slim

# ...before logic
COPY ./service1 /app
COPY ./common /common
COPY sharedlib.ini sharedlib.ini

WORKDIR /app
# ...after logic
```

## Configuration file

The order of configuration search is simple - first look at the pyproject.toml file. Then look at sharedlib.ini file - this file has priority over pyproject.toml because it is an explicit config.   

If both files are configured, sharedlib.ini will overwrite all settings.   

### `sharedlib.ini`

```ini
[sharedlib]
folder_name = custom_shared
import_name = my_shared_pkg
```

> Important: The configuration file must be located in the root of the project. Otherwise imports will not work properly. 

### `pyproject.toml`

```toml
[tool.sharedlib]
folder_name = "custom_shared"
import_name = "my_shared_pkg"
```

## Contributing

If you would like to suggest a new feature, you can create an issue on the GitHub repository for this project. Also you can fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for more information.
