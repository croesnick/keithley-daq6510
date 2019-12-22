import pytest
from pyvisa import ResourceManager
import tests.fixtures

try:
    import importlib.resources as pkg_resources
except ImportError:
    import importlib_resources as pkg_resources


@pytest.fixture(scope='session')
def resource_manager():
    with pkg_resources.path(tests.fixtures.__name__, 'devices.yml') as devices_fixture_path:
        rm = ResourceManager(f'{devices_fixture_path}@sim')
        yield rm
        rm.close()
