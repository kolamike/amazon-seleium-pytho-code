import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.fixture()
def test_login():
    global driver
    driver_service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=driver_service)
    options=Options()
    driver.implicitly_wait(10)
    driver.maximize_window()
def test_setup(test_login):
    driver.get("https://amazon.com")
    goto = driver.find_element(By.ID, "nav-hamburger-menu")
    goto.click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//div[normalize-space()='Arts & Crafts']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[normalize-space()='Beading & Jewelry Making']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "// span[contains(text(), 'Engraving Machines & Tools')]").click()
    time.sleep(2)
    elemen = driver.find_element(By.CLASS_NAME, "a-dropdown-prompt")
    elemen.click()
    time.sleep(2)
    driver.find_element(By.ID, "s-result-sort-select_2").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//img[@alt='Laser Engraving Machine，EM-Smart 25W Fiber Laser Engraver, Foldable Laser Engraving Machine Deep Engraving Machine, LightB...']").click()
    time.sleep(5)
def test_price(test_login):
    item_price = driver.find_element(By.XPATH, "//span[@class='a-price aok-align-center']//span[@class='a-price-whole']")
    if item_price > 4000:
        print("fail")
    else:
        print("pass")
    driver.get_screenshot_as_file("C:\\Program Files\\error.png")
    driver.save_screenshot(".\\test2.png")