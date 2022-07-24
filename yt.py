from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
import time
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(options=chrome_options)
start_url = "https://www.youtube.com/watch?v=MR-MPwaN7Ns?autoplay=1"
driver.get(start_url)
