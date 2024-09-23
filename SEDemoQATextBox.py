from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrome_option=Options()
chrome_option.add_experimental_option("detach",True)

service = Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service,options=chrome_option)

driver.get("https://demoqa.com/")

name="Sam"
mail="Sam@gmail.com"
curradd="Mumbai"
peradd = "America"
expFormName="Text Box"

driver.find_element(By.XPATH,"//h5[text()='Elements']").click()
driver.find_element(By.XPATH,"//span[text()='Text Box']").click()

formName=driver.find_element(By.CSS_SELECTOR,'h1[class="text-center"]').text
print(formName)

if formName == expFormName:
    print("Please Fill Form")
    driver.find_element(By.ID,"userName").send_keys(name)
    driver.find_element(By.CSS_SELECTOR,'input[type="email"]').send_keys(mail)
    driver.find_element(By.ID,"currentAddress").send_keys(curradd)
    driver.find_element(By.ID,"permanentAddress").send_keys(peradd)
    btn=driver.find_element(By.ID,"submit")
    btn.is_enabled()
    btn.click()
    #Assertion
    outpt=driver.find_element(By.ID,"output").text
    print(outpt)
    assert f"Name:{name}" in outpt
    assert f"Email:{mail}" in outpt
    assert f"Current Address :{curradd}" in outpt
    assert f"Permananet Address :{peradd}" in outpt
    print("Form Submit & Assert Successfully")
else :
    print("Invalid Form")

driver.quit()








