from time import sleep
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

exppage="Browser Windows"
driver.get("https://demoqa.com/browser-windows")

pagename=driver.find_element(By.XPATH,"//h1[text()='Browser Windows']").text
if pagename ==exppage:
    print("Click on Browser Windows")

    # ================To Handle Tabs=================

    driver.find_element(By.ID,"tabButton").click()
    window_handles=driver.window_handles
    print("Tabs",window_handles)
    driver.switch_to.window(window_handles[1])
    sampletext=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"sampleHeading"))).text
    print(sampletext)
    assert "This is a sample page" == sampletext
    driver.switch_to.window(window_handles[0])

    # ================To Handle Window=================
    
    # Store the main window handle (the original window)
    mainWindow=driver.current_window_handle
    print("MainWindow "+mainWindow)
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"messageWindowButton"))).click()
    new_window = None
    driverHandles=driver.window_handles
    print("Driver Handles",driverHandles)
    for handle in driverHandles:
        if handle !=mainWindow:
            new_window = handle
            break
    print("New Window ",new_window)
    driver.switch_to.window(new_window)
    message = driver.find_element(By.TAG_NAME, "body").text
    print(message)


else :
    print("Invalid Page")

driver.quit()