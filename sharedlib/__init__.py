"""
Pythonic way for use "shared" folder of packages (utils).

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
"""

from .register import _register


# create virtual package and register it
_register()


__all__ = tuple()
