from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome options for normal and incognito mode
chrome_option_normal = Options()
chrome_option_incognito = Options()

# Detach option for normal browser to keep it open after script ends
chrome_option_normal.add_experimental_option("detach", True)
# Add incognito mode for the second browser
chrome_option_incognito.add_argument("--incognito")

# Create separate services for each WebDriver instance
service_normal = Service(ChromeDriverManager().install())
service_incognito = Service(ChromeDriverManager().install())

# Normal browser instance
driver_normal = webdriver.Chrome(service=service_normal, options=chrome_option_normal)

# Navigate to the page in normal mode
driver_normal.get("https://www.google.in")

# Fetch the title from the normal browser
title = driver_normal.title
print(f"Title from normal browser: {title}")

# Quit the normal browser (if it's no longer needed)
driver_normal.quit()

# Incognito browser instance
driver_incognito = webdriver.Chrome(service=service_incognito, options=chrome_option_incognito)

# Use the title in the incognito browser to perform a search
driver_incognito.get("https://www.google.com")

# Wait for the search box to be visible and search for the title
search_box = WebDriverWait(driver_incognito, 10).until(
    EC.presence_of_element_located((By.NAME, "q"))
)
search_box.send_keys(title)
search_box.submit()

# Close the incognito browser after the search is done
# driver_incognito.quit()
