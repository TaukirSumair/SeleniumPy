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

exppage="Radio Button"
driver.maximize_window()
driver.get("https://demoqa.com/radio-button")

pagename=driver.find_element(By.XPATH,"//h1[text()='Radio Button']").text

if pagename ==exppage:
    print("Please Select Radio Button")
    ifYes=driver.find_element(By.ID,"yesRadio").is_selected()
    print(ifYes)

    if ifYes == False:
        # driver.find_element(By.ID,"yesRadio").click()
        # WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, "yesRadio"))).click()
        element = driver.find_element(By.ID, "yesRadio")
        driver.execute_script("arguments[0].click();", element)
        ifYes=driver.find_element(By.ID,"yesRadio").is_selected()
        print(ifYes)
        acttext=driver.find_element(By.CSS_SELECTOR,"span[class=text-success]").text
        print(acttext)
        assert "Yes" in acttext


        ifenable=driver.find_element(By.ID,'noRadio').is_enabled()
        print(ifenable)
    else:
        print("Alredy Selected")
        
else:
    print("Invalid Page")


driver.quit()