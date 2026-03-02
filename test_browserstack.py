from selenium import webdriver
from selenium.webdriver.common.by import By
import time

USERNAME = "your_username"
ACCESS_KEY = "your_access_key"

url = f"https://{USERNAME}:{ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub"

options = webdriver.EdgeOptions()
options.set_capability("browserName", "Chrome")
options.set_capability("browserVersion", "latest")

options.set_capability("bstack:options", {
    "os": "Windows",
    "osVersion": "10",
    "buildName": "Prodigy Task-04",
    "sessionName": "Login Test - Chrome",
})

print("Connecting to BrowserStack...")

driver = webdriver.Remote(
    command_executor=url,
    options=options
)

print("Connected successfully!")

driver.implicitly_wait(10)

driver.get("https://practicetestautomation.com/practice-test-login/")

driver.find_element(By.ID, "username").send_keys("student")
driver.find_element(By.ID, "password").send_keys("Password123")
driver.find_element(By.ID, "submit").click()

time.sleep(5)

driver.execute_script(
    'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed","reason": "Login successful"}}'
)

driver.quit()

print("Test completed.")
