import pytest
from utils.driver_factory import DriverFactory


@pytest.fixture()
def setup(request):
    driver = DriverFactory.get_driver("firefox")
    driver.implicitly_wait(10)
    request.cls.driver = driver
    driver.maximize_window()
    yield
    driver.quit()
