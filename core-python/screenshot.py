from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.lvivek.com/')
driver.save_screenshot('vivek.png')
driver.quit()