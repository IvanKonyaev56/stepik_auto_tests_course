# from selenium import webdriver

# driver = webdriver.Chrome("C:/Program Files/Google/Chrome/Application/chrome.exe")
# driver.get("https://www.python.org")

# driver.close()


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com")
driver.close()