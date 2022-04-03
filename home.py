########################################################
# Добавление комментария
########################################################
from selenium import webdriver
driver = webdriver.Chrome('/home/alex/Downloads/chromedriver')
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")
driver.execute_script("window.scrollBy(0, 600);")
Ruby = driver.find_element_by_css_selector("[data-product_id='160']")
Ruby.click()
REVIEWS = driver.find_element_by_css_selector("[href='#tab-reviews']")
REVIEWS.click()
star5 = driver.find_element_by_css_selector("[class='star-5']")
star5.click()
comment = driver.find_element_by_id("comment")
comment.send_keys("Nice book!")
author = driver.find_element_by_id("author")
author.send_keys("Pupkin")
email = driver.find_element_by_id("email")
email.send_keys("Pupkin@mail.ru")
submit_btn = driver.find_element_by_id("submit")
submit_btn.click()

driver.quit()
