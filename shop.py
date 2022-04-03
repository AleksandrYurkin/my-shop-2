########################################№#
# Отображение страницы товара
#########################################№
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
# HTML5_Forms = driver.find_element_by_css_selector("[title='Mastering HTML5 Forms']")
# HTML5_Forms.click()

##########################################
# Количество товаров в категории
##########################################
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
HTML = driver.find_element_by_link_text("HTML")
HTML.click()
element = driver.find_element_by_xpath("//*[@id='woocommerce_product_categories-2']/ul/li[2]/span")
element_text_get = element.text
print(element_text_get)


# driver.quit()