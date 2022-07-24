from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
browser = webdriver.Chrome(options=chrome_options)

browser.get("https://youtu.be/14Cm65o9AR4")

WebDriverWait(browser, 10).until(EC.element_to_be_clickable(
(By.XPATH, "//button[@aria-label='Play']"))).click()

time.sleep(1000000)
