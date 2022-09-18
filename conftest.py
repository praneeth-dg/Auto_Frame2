import pytest

@pytest.fixture(scope="class")
def test_setup(request):
    global driver
    from selenium import webdriver
    driver = webdriver.Chrome("E:/Selenium/AutomationFramework/drivers/chromedriver.exe")
    driver.implicitly_wait(7)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    print("Test Completed")