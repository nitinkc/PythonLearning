from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Set up WebDriver
chrome_options = Options()
# chrome_options.add_argument("--headless")

# Set up WebDriver with headless Chrome
driver = webdriver.Chrome(options=chrome_options)

# Open a website
driver.get("https://www.google.com")

# Find an element by ID
search_box = driver.find_element(By.NAME, "q")

# Type something into the search box
search_box.send_keys("Hello, world!")

# Submit the form
search_box.submit()

# Wait for the results page to load
try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "rso")))
    print("Search results page loaded successfully!")
except:
    print("Timeout: Search results page did not load")

# Close the browser
driver.quit()
