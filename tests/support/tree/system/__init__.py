from fabric.api import task
import six
if six.PY3:
    from . import debian
else:
    from . import debian


@task
def install_package():
    pass
