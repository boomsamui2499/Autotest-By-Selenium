import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('/chromedriver')  
driver.get("https://tv.line.me/")

driver.maximize_window() #full
print("Fullscreen success")
time.sleep(5)

driver.find_element_by_id("search").send_keys('one piece')
print("Sendkey success")
time.sleep(5)
driver.find_element_by_id("searchButton").click()
print("Search success")
time.sleep(5)
driver.find_element_by_id("search_ranking_toggle_button").click()
li = driver.find_elements_by_tag_name('li')
li[1].click()
print("Selected success")
time.sleep(5)
# driver.find_element_by_link_text("สุภาพบุรุษสุดซอย 2020").click()
# driver.find_element_by_css_selector("a[onclick^='เป็นต่อ2020'").click()

driver.back()
print("Previous Page success")
time.sleep(5)

driver.execute_script("window.history.go(1)")
print("Next Page success")
time.sleep(5)

# driver.refresh() #re page
# driver.close() 


