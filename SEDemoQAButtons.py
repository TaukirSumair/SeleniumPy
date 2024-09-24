from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#ToPerformDoubleClick
from selenium.webdriver.common.action_chains import ActionChains


chrome_option=Options()
chrome_option.add_experimental_option("detach",True)
service=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service,options=chrome_option)

driver.get("https://demoqa.com/buttons")
exppage="Button"
pagename=driver.find_element(By.XPATH,"//h1[text()='Buttons']").text
if pagename ==exppage:

    print("Click on Buttons")
# ActionChains(driver) creates a new action chain.
# .double_click(element) specifies that you want to double-click on the located element.
# .perform() executes the action chain

    # Locate the element to double-click
    elementfordoubleclick=driver.find_element(By.ID,"doubleClickBtn")
    # Initialize ActionChains object
    actions=ActionChains(driver)
    # Perform double-click on the element
    actions.double_click(elementfordoubleclick).perform()

    doubleclicktext=driver.find_element(By.ID,"doubleClickMessage").text
    assert "You have done a double click" in doubleclicktext
    print("Successfully Double Clicked")

    rightclick=driver.find_element(By.ID,"rightClickBtn")
    actions.context_click(rightclick).perform()
    rightclicktext=driver.find_element(By.ID,"rightClickMessage").text
    assert "You have done a right click" in rightclicktext
    print("Successfully Right Clicked")

    dynamicclick=driver.find_element(By.XPATH,"//button[text()='Click Me']")
    actions.click(dynamicclick).perform()
    dynamicclickmessage=driver.find_element(By.ID,"dynamicClickMessage").text
    assert "You have done a dynamic click" == dynamicclickmessage
    print("Successfully Clicked")

else :
    print("Invalid Buttons")

driver.quit()

