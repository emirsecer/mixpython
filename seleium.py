from selenium import webdriver
import time
driver=webdriver.Edge()
url="http://github.com"
driver.get(url)
driver.maximize_window()
driver.save_screenshot("selenium_python_ile_çekildi")
time.sleep(2)
print("driver.title")
time.sleep(2)
url="http://www.github.com/sadikturan"
driver.get(url)
time.sleep(2)
driver.back()
driver.close
