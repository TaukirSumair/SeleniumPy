from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service , options=chrome_options )

driver.get("https://demo.nopcommerce.com/register")
print(driver.title)

driver.find_element(By.NAME,"q").is_displayed()
WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'button[type="submit"]'))).is_enabled()

WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"gender-female"))).is_enabled()
WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"gender-female"))).click()
ab = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"gender-female"))).is_selected()
print(ab)
print("=======================")
WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"gender-male"))).is_enabled()
WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"gender-male"))).click()
ba = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"gender-male"))).is_selected()
ab = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"gender-female"))).is_selected()

print(ba)
print(ab)

driver.quit()