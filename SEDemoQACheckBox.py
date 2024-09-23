from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_option = Options()
chrome_option.add_experimental_option("detach",True)
service=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service,options=chrome_option)

exppage="Check Box"
driver.get("https://demoqa.com/checkbox")

pagename=driver.find_element(By.XPATH,"//h1[text()='Check Box']").text
if pagename ==exppage:
    print("Click on Checkbox")

    exp=driver.find_element(By.CSS_SELECTOR,'svg[class~="rct-icon-expand-all"]')
    exp.click()
    driver.find_element(By.CSS_SELECTOR,'button[title="Collapse all"]').click()
    exp.click()

    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CLASS_NAME,"rct-checkbox"))).click()
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'label[for="tree-node-react"]'))).click()
else :
    print("Invalid Checkbox")

driver.quit()