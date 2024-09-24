import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_option=Options()
chrome_option.add_experimental_option("detach",True)
service=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service,options=chrome_option)

driver.get("https://demoqa.com/links")

exppage="Links"
pagename=driver.find_element(By.XPATH,"//h1[text()='Links']").text
if pagename ==exppage:
    print("Click on Links")

    driver.find_element(By.LINK_TEXT,"Home").click()
    # Get the window handles of the current open tabs
    window_handles=driver.window_handles
    print(window_handles)
    # Switch to the new tab (the second handle)
    driver.switch_to.window(window_handles[1])

    # Perform actions in the new tab
    print(driver.title)
    driver.find_element(By.CSS_SELECTOR,'img[class="banner-image"]').click()
    print(window_handles)

    # Get the window handles of the current open tabs
    newindow_handle=driver.window_handles
    print(newindow_handle)
    # Switch to the new tab (the Third handle)
    driver.switch_to.window(newindow_handle[2])
    # Perform actions in the new tab
    driver.find_element(By.XPATH,"//a[text()='Go To Registration ']").click()
    print("Registration page Open")

    #switch back to the original tab
    driver.switch_to.window(newindow_handle[0])

    # Perform actions in the original tab
    driver.find_element(By.PARTIAL_LINK_TEXT,"eated").click()
    response=WebDriverWait(driver,15).until(EC.presence_of_element_located((By.ID,"linkResponse"))).text
    print(response)
    assert "Link has responded with staus 201 and status text Created" == response

else:
    print("Invalid Page")




