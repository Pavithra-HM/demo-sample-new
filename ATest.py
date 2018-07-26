import time
from selenium.webdriver import Chrome, ActionChains

driver=Chrome((r"C:\Users\Admin\AppData\Local\Programs\Python\Python36-32\chromedriver_win32\chromedriver.exe"))
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("https://www.flipkart.com/")
time.sleep(5)
#Step1
element=driver.find_element_by_xpath("//span[text()='Electronics']")
#Step2
act=ActionChains(driver)
#Step3
act.move_to_element(element).perform()


