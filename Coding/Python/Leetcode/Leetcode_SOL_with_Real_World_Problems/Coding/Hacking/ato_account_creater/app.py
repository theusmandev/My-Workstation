# import pandas as pd
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# import time
# import random

# # Excel file load
# try:
#     df = pd.read_excel("users.xlsx")
# except FileNotFoundError:
#     print("Error: users.xlsx not found. Please check the file path.")
#     exit(1)

# # ChromeDriver setup with webdriver-manager
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# # Website URL
# registration_url = "https://example.com/register"  # Replace with actual URL

# try:
#     for index, row in df.iterrows():
#         driver.get(registration_url)
#         try:
#             # Wait for form elements to be present
#             phone_field = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.NAME, "phone"))
#             )
#             password_field = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.NAME, "password"))
#             )
#             referral_field = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.NAME, "referral"))
#             )
#             submit_button = WebDriverWait(driver, 10).until(
#                 EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
#             )

#             # Fill form
#             phone_field.send_keys(str(row['Phone']))
#             password_field.send_keys(str(row['Password']))
#             referral_field.send_keys(str(row['Referral']))

#             # Submit form
#             submit_button.click()
#             time.sleep(random.uniform(2, 5))  # Random delay for submission

#             print(f"Successfully submitted for index {index}")

#         except Exception as e:
#             print(f"Error at index {index}: {e}")
#             continue

# finally:
#     driver.quit()







# import pandas as pd
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# import time
# import random

# # Excel file load
# try:
#     df = pd.read_excel("users.xlsx")
# except FileNotFoundError:
#     print("Error: users.xlsx not found. Please check the file path.")
#     exit(1)

# # ChromeDriver setup with webdriver-manager
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# # Website URL
# registration_url = "https://binoworld.top/pages/reset/reset"

# try:
#     for index, row in df.iterrows():
#         driver.get(registration_url)
#         try:
#             # Wait for form elements to be present
#             # Update selectors based on actual HTML (inspect the page)
#             phone_field = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter your Number']"))
#             )
#             password_field = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter password']"))
#             )
#             confirm_password_field = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter confirm password']"))
#             )
#             referral_field = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter your invitation code']"))
#             )
#             submit_button = WebDriverWait(driver, 10).until(
#                 EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Continue')]"))
#             )

#             # Fill form
#             phone_field.send_keys(str(row['Phone']))
#             password_field.send_keys(str(row['Password']))
#             confirm_password_field.send_keys(str(row['Password']))  # Same as password
#             referral_field.send_keys(str(row['Referral']))

#             # Submit form
#             submit_button.click()
#             time.sleep(random.uniform(2, 5))  # Random delay for submission

#             print(f"Successfully submitted for index {index}")

#         except Exception as e:
#             print(f"Error at index {index}: {e}")
#             continue

# finally:
#     driver.quit()








# import pandas as pd
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# import time
# import random

# # Excel file load
# try:
#     df = pd.read_excel("users.xlsx")
# except FileNotFoundError:
#     print("Error: users.xlsx not found. Please check the file path.")
#     exit(1)

# # ChromeDriver setup with options
# options = webdriver.ChromeOptions()
# options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36")
# options.add_argument("--disable-gpu")
# options.add_argument("--no-sandbox")
# # Uncomment below line to run in headless mode for testing
# # options.add_argument("--headless")

# driver = None
# try:
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

#     # Website URL
#     registration_url = "https://binoworld.top/pages/reset/reset"

#     for index, row in df.iterrows():
#         try:
#             driver.get(registration_url)
#             # Wait for page to load
#             WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

#             # Wait for form elements to be present
#             phone_field = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter your Number']"))
#             )
#             password_field = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter password']"))
#             )
#             confirm_password_field = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter confirm password']"))
#             )
#             referral_field = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter your invitation code']"))
#             )
#             submit_button = WebDriverWait(driver, 10).until(
#                 EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Continue')]"))
#             )

#             # Fill form
#             phone_field.send_keys(str(row['Phone']))
#             password_field.send_keys(str(row['Password']))
#             confirm_password_field.send_keys(str(row['Password']))  # Same as password
#             referral_field.send_keys(str(row['Referral']))

#             # Submit form
#             submit_button.click()
#             time.sleep(random.uniform(2, 5))  # Random delay for submission

#             print(f"Successfully submitted for index {index}")

#         except Exception as e:
#             print(f"Error at index {index}: {e}")
#             continue

# finally:
#     if driver:
#         driver.quit()



# import pandas as pd
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# import time
# import random
# import logging
# import sys

# # Logging setup
# logging.basicConfig(filename='selenium.log', level=logging.DEBUG,
#                     format='%(asctime)s - %(levelname)s - %(message)s')

# # Excel file load
# try:
#     df = pd.read_excel("users.xlsx")
#     logging.debug("Excel file loaded successfully with rows: %d", len(df))
# except FileNotFoundError:
#     logging.error("Error: users.xlsx not found. Please check the file path.")
#     print("Error: users.xlsx not found. Please check the file path.")
#     exit(1)

# # ChromeDriver setup with options
# options = webdriver.ChromeOptions()
# options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36")
# options.add_argument("--disable-gpu")
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev-shm-usage")  # For Windows/Linux stability
# options.add_argument("--remote-debugging-port=9222")  # For debugging
# # options.add_argument("--headless")  # Uncomment for headless mode

# driver = None
# try:
#     logging.debug("Attempting to initialize ChromeDriver...")
#     service = Service(ChromeDriverManager().install())
#     service.log_path = "chromedriver.log"  # ChromeDriver specific logs
#     service.service_args = ["--verbose"]
#     driver = webdriver.Chrome(service=service, options=options)
#     logging.info("ChromeDriver initialized successfully.")
#     driver.set_page_load_timeout(30)  # Set timeout for page load

#     # Website URL
#     registration_url = "https://binoworld.top/pages/reset/reset"

#     for index, row in df.iterrows():
#         try:
#             logging.debug(f"Processing index {index}, Phone: {row['Phone']}")
#             driver.get(registration_url)
#             logging.debug("Page URL accessed.")
#             # Wait for page to load
#             WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

#             # Wait for form elements to be present (using name attributes)
#             phone_field = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.NAME, "phone"))
#             )
#             password_field = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.NAME, "password"))
#             )
#             confirm_password_field = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.NAME, "confirm_password"))
#             )
#             referral_field = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.NAME, "ref_by"))
#             )
#             submit_button = WebDriverWait(driver, 10).until(
#                 EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Continue')]"))
#             )

#             # Fill form
#             phone_field.send_keys(str(row['Phone']))
#             logging.debug(f"Entered phone: {row['Phone']}")
#             password_field.send_keys(str(row['Password']))
#             logging.debug("Entered password")
#             confirm_password_field.send_keys(str(row['Password']))  # Same as password
#             logging.debug("Entered confirm password")
#             referral_field.send_keys(str(row['Referral']))
#             logging.debug(f"Entered referral: {row['Referral']}")

#             # Submit form
#             submit_button.click()
#             logging.debug("Form submitted")
#             time.sleep(random.uniform(2, 5))  # Random delay for submission

#             print(f"Successfully submitted for index {index}")
#             logging.info(f"Successfully submitted for index {index}")

#         except Exception as e:
#             logging.error(f"Error at index {index}: {str(e)}", exc_info=True)
#             print(f"Error at index {index}: {e}")
#             continue

# finally:
#     if driver:
#         driver.quit()
#         logging.info("Driver quit successfully.")






import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
import logging
import sys
from datetime import datetime

# Logging setup
logging.basicConfig(filename='selenium.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Excel file load
try:
    df = pd.read_excel("users.xlsx")
    logging.debug("Excel file loaded successfully with rows: %d", len(df))
except FileNotFoundError:
    logging.error("Error: users.xlsx not found. Please check the file path.")
    print("Error: users.xlsx not found. Please check the file path.")
    exit(1)

# ChromeDriver setup with options
options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")  # For Windows/Linux stability
options.add_argument("--remote-debugging-port=9222")  # For debugging
options.add_argument("--disable-extensions")  # Disable extensions
options.add_argument("--ignore-certificate-errors")  # Ignore SSL issues
# options.add_argument("--headless")  # Uncomment for headless mode

driver = None
try:
    logging.debug("Attempting to initialize ChromeDriver...")
    service = Service(ChromeDriverManager().install())
    service.log_path = "chromedriver.log"  # ChromeDriver specific logs
    service.service_args = ["--verbose"]
    driver = webdriver.Chrome(service=service, options=options)
    logging.info("ChromeDriver initialized successfully.")
    driver.set_page_load_timeout(60)  # Increased timeout for page load

    # Website URL
    registration_url = "https://binoworld.top/pages/reset/reset"

    for index, row in df.iterrows():
        try:
            logging.debug(f"Processing index {index}, Phone: {row['Phone']}")
            driver.get(registration_url)
            logging.debug("Page URL accessed.")
            # Wait for page to load
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

            # Take screenshot for debugging
            screenshot_path = f"screenshot_index_{index}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            driver.save_screenshot(screenshot_path)
            logging.debug(f"Screenshot saved at: {screenshot_path}")

            # Wait for form elements to be present (using name attributes)
            phone_field = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.NAME, "phone"))
            )
            password_field = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.NAME, "password"))
            )
            confirm_password_field = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.NAME, "confirm_password"))
            )
            referral_field = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.NAME, "ref_by"))
            )
            submit_button = WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Continue')]"))
            )

            # Fill form
            phone_field.send_keys(str(row['Phone']))
            logging.debug(f"Entered phone: {row['Phone']}")
            password_field.send_keys(str(row['Password']))
            logging.debug("Entered password")
            confirm_password_field.send_keys(str(row['Password']))  # Same as password
            logging.debug("Entered confirm password")
            referral_field.send_keys(str(row['Referral']))
            logging.debug(f"Entered referral: {row['Referral']}")

            # Submit form
            submit_button.click()
            logging.debug("Form submitted")
            time.sleep(random.uniform(2, 5))  # Random delay for submission

            print(f"Successfully submitted for index {index}")
            logging.info(f"Successfully submitted for index {index}")

        except Exception as e:
            logging.error(f"Error at index {index}: {str(e)}", exc_info=True)
            print(f"Error at index {index}: {e}")
            # Take screenshot on error
            error_screenshot_path = f"error_screenshot_index_{index}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            driver.save_screenshot(error_screenshot_path)
            logging.debug(f"Error screenshot saved at: {error_screenshot_path}")
            continue

finally:
    if driver:
        driver.quit()
        logging.info("Driver quit successfully.")