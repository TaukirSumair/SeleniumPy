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

exppage="Practice Form"
driver.get("https://demoqa.com/automation-practice-form")
# driver.maximize_window()

pagename=driver.find_element(By.XPATH,"//h1[text()='Practice Form']").text
if pagename ==exppage:
    print("Please Fill the Form")

    formName=driver.find_element(By.XPATH,"//h5[text()='Student Registration Form']").text
    assert "Student Registration Form" == formName

    driver.find_element(By.ID,"firstName").send_keys("Sam")
    driver.find_element(By.ID,"lastName").send_keys("Kumar")
    driver.find_element(By.ID,"userEmail").send_keys("Sam@gmail.com")

    if not driver.find_element(By.ID,"gender-radio-1").is_selected():
        driver.execute_script("arguments[0].click();", driver.find_element(By.ID,"gender-radio-1"))

    driver.find_element(By.ID,"userNumber").send_keys("1234567888")

    if not driver.find_element(By.ID,"hobbies-checkbox-1").is_selected():
       driver.execute_script("arguments[0].click();",driver.find_element(By.ID,"hobbies-checkbox-1"))

    if not driver.find_element(By.ID,"hobbies-checkbox-2").is_selected():
       driver.execute_script("arguments[0].click();",driver.find_element(By.ID,"hobbies-checkbox-2"))

    if not driver.find_element(By.ID,"hobbies-checkbox-3").is_selected():
       driver.execute_script("arguments[0].click();",driver.find_element(By.ID,"hobbies-checkbox-3"))

    driver.find_element(By.ID,"currentAddress").send_keys("Test")
   


    state_dropdown = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//div[@id="state"]'))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", state_dropdown)


    state_dropdown.click()

    ncr_option = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'NCR')]"))
    )
    ncr_option.click()


    city_dropdown = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '(//div[@class=" css-1hwfws3"])[2]'))
    )
    city_dropdown.click()

    ncr_option = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Delhi')]"))
    )
    ncr_option.click()

    driver.find_element(By.ID,"submit").click()

    closebtn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "closeLargeModal"))
    )
    closebtn.click()

    # table = driver.find_element(By.CLASS_NAME, 'table-dark')
    # print(table)

    # rows = table.find_elements(By.TAG_NAME, "tr")
    # print(rows)
    # for row in rows:
    # # Get all columns for each row
    #     cols = row.find_elements(By.TAG_NAME, "td")
    #     print(cols)
    
    # # Check if there are two columns and the first column matches "Student Email"
    #     if len(cols) == 2 and cols[0].text == "Student Email":
    #     # Validate the email
    #        email = cols[1].text
    #     if email == "Sam@gmail.com":
    #         print("Email validation passed!")
    #     else:
    #           print("Email validation failed!")
    #     break


    print("Form Submitted Succesfully")

else :
    print("Invalid Page")

# driver.quit()