from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://lms.umt.edu.pk")
time.sleep(5)
driver.find_element_by_id("username").send_keys("***********")
time.sleep(5)
driver.find_element_by_id("password").send_keys("********")
time.sleep(5)
driver.find_element_by_id("loginbtn").click()
time.sleep(5)
course1 = driver.find_element_by_css_selector("#nav-drawer > nav > ul > li:nth-child(6) > a ").text
time.sleep(5)
course2 = driver.find_element_by_css_selector("#nav-drawer > nav > ul > li:nth-child(7) > a ").text
time.sleep(5)
course3 = driver.find_element_by_css_selector("#nav-drawer > nav > ul > li:nth-child(8) > a ").text
time.sleep(5)
course4 = driver.find_element_by_css_selector("#nav-drawer > nav > ul > li:nth-child(9) > a ").text
time.sleep(5)
print(course1)
print(course2)
print(course3)
print(course4)
driver.close()