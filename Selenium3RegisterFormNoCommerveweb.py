from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

chrome_option=Options()
chrome_option.add_experimental_option("detach",True)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service,options=chrome_option)

driver.get("https://demo.nopcommerce.com/register")

actual_text=driver.find_element(By.XPATH,"//h1[text()='Register']").text
exp_text="Register"

if actual_text==exp_text:
    print("User Can Fill The Form")

    val=driver.find_element(By.ID,"gender-male").is_selected()

    if val == False:
        driver.find_element(By.ID,"gender-male").click()
    else:
        print("Gender alredy Selected")

    driver.find_element(By.NAME,'FirstName').send_keys("Sam")
    driver.find_element(By.CSS_SELECTOR,'input[name="LastName"]').send_keys("Kumar")
    
    dropdownday=driver.find_element(By.NAME,"DateOfBirthDay")
    selectday=Select(dropdownday)
    selectday.select_by_index(1)

    selectmonth=Select(driver.find_element(By.NAME,"DateOfBirthMonth"))
    selectmonth.select_by_value("4")

    selectyear=Select(driver.find_element(By.NAME,"DateOfBirthYear"))
    selectyear.select_by_visible_text("2010")

    driver.find_element(By.CSS_SELECTOR,'input[type="email"]').send_keys("Sam@gmail.com")

    checkselected=driver.find_element(By.ID,'Newsletter').is_selected()

    if checkselected == True:
        print("Checkbox alredy Selected")
    else:
        driver.find_element(By.ID,'Newsletter').click()

    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.NAME,"Password"))).send_keys("123123")
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.NAME,"ConfirmPassword"))).send_keys("123123")

    # driver.find_element(By.CLASS_NAME,'button-1 register-next-step-button').is_enabled()
    regbutton=driver.find_element(By.CLASS_NAME, 'register-next-step-button') # n Selenium, you need to pass a class name without any spaces
    regbutton.is_enabled()
    regbutton.click()
    print("Form Submitted Successfully")

    driver.quit()


else:
    print("Page is Different")
    driver.quit()



