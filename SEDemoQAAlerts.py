from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_option = Options()
chrome_option.add_experimental_option("detach",True)
service=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service,options=chrome_option)

exppage="Alerts"
driver.get("https://demoqa.com/alerts")

pagename=driver.find_element(By.XPATH,"//h1[text()='Alerts']").text
if pagename ==exppage:
    print("Click on Checkbox")
    # Click Button to see alert
    driver.find_element(By.ID,"alertButton").click()
    WebDriverWait(driver,10).until(EC.alert_is_present())
    alert=driver.switch_to.alert
    print(alert.text)
    alert.accept()
    print("alert Acceted")

    # On button click, alert will appear after 5 seconds

    driver.find_element(By.ID,"timerAlertButton").click()
    time.sleep(7) 
    WebDriverWait(driver,10).until(EC.alert_is_present())
    timealert=driver.switch_to.alert
    print(timealert.text)
    timealert.accept()
    print("Time alert Acceted")

    # On button click, confirm box will appear

    driver.find_element(By.ID,"confirmButton").click()
    WebDriverWait(driver,10).until(EC.alert_is_present())
    confirmAlert=driver.switch_to.alert
    print(confirmAlert.text)
    confirmAlert.accept() #dismiss()  #accept()
    confirmMessage=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"confirmResult"))).text
    print(confirmMessage)

    assert "You selected Ok" == confirmMessage or "You selected Cancel"== confirmMessage , "Neither result matches the expected result"
    print("confirm box Acceted")

    # On button click, prompt box will appear

    clickPromtbutton=driver.find_element(By.ID,"promtButton")
    driver.execute_script("arguments[0].click()",clickPromtbutton)
    WebDriverWait(driver,10).until(EC.alert_is_present())
    promtboxAlert=driver.switch_to.alert
    print(promtboxAlert.text)
    time.sleep(3)
    promtboxAlert.send_keys("Testing")
    promtboxAlert.accept()
    promtMessage=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"promptResult"))).text
    print(promtMessage)
    assert "You entered Testing" == promtMessage
    print("Promt added Successfully")

else :
    print("Invalid Page")

driver.quit()