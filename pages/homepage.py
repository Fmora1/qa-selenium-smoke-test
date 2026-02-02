from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    URL = "https://example.com"

    HEADING = (By.TAG_NAME, "h1")
    MORE_INFO_LINK = (By.CSS_SELECTOR, "a[href]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def load(self):
        self.driver.get(self.URL)
        self.wait.until(EC.presence_of_element_located(self.HEADING))

    def get_title(self):
        return self.driver.title

    def get_heading_text(self):
        return self.driver.find_element(*self.HEADING).text

    def more_info_link_is_visible(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.visibility_of_element_located(self.MORE_INFO_LINK))

    def click_more_info(self):
        wait = WebDriverWait(self.driver, 10)
        link = wait.until(EC.element_to_be_clickable(self.MORE_INFO_LINK))
        link.click()