# ##########################################
# # Сортирвка товаров
# ##########################################
# import time
# from selenium.webdriver.support.select import Select
# from selenium import webdriver
# driver = webdriver.Chrome('/home/alex/Downloads/chromedriver')
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get("http://practice.automationtesting.in/")
# register = driver.find_element_by_link_text("My Account")
# register.click()
# username_email = driver.find_element_by_id("username")
# username_email.send_keys("Pupkin@mail.ru")
# login_password = driver.find_element_by_id("password")
# login_password.send_keys("Qw$!R12&")
# LOGIN = driver.find_element_by_css_selector("[value='Login']")
# LOGIN.click()
# shop = driver.find_element_by_link_text("Shop")
# shop.click()
#
# element = driver.find_element_by_css_selector("[name='orderby']")
# select = Select(element)
# print(element)
# time.sleep(5)
#
# select.select_by_index(5)
# print(element)
# time.sleep(5)


##########################################
# Отображение, скидка товара
##########################################
# import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
driver = webdriver.Chrome('/home/alex/Downloads/chromedriver')
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")
register = driver.find_element_by_link_text("My Account")
register.click()
username_email = driver.find_element_by_id("username")
username_email.send_keys("Pupkin@mail.ru")
login_password = driver.find_element_by_id("password")
login_password.send_keys("Qw$!R12&")
LOGIN = driver.find_element_by_css_selector("[value='Login']")
LOGIN.click()
shop = driver.find_element_by_link_text("Shop")
shop.click()

price = driver.find_element_by_css_selector(
"#content > ul > li.post-169.product.type-product.status-publish.product_cat-android.product_tag-android.has-post-title.no-post-date.has-post-category.has-post-tag.has-post-comment.has-post-author.first.instock.sale.downloadable.taxable.shipping-taxable.purchasable.product-type-simple > a.woocommerce-LoopProduct-link > span.price")
price_get_text = price.text
assert "600" in price_get_text
assert "450" in price_get_text
print(price_get_text)
price.click()

img = driver.find_element_by_css_selector("#product-169 > div.images > a > img")
img.click()

img_IMG = WebDriverWait(driver, 20).until(
EC.element_to_be_clickable((By.CSS_SELECTOR,
"[class='pp_close']")))
img_IMG.click()



