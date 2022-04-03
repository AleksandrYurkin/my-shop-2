########################################################
# Регистрация аккаунта
########################################################
from selenium import webdriver
driver = webdriver.Chrome('/home/alex/Downloads/chromedriver')
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")
register = driver.find_element_by_link_text("My Account")
register.click()
email = driver.find_element_by_id("reg_email")
email.send_keys("Pupkin@mail.ru")
password = driver.find_element_by_id("reg_password")
password.send_keys("Qw$!R12&")
REGISTER = driver.find_element_by_css_selector("[value='Register']")
REGISTER.click()

# driver.quit()

########################################################
# Логин в систему
########################################################
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
#
# LOGOUT = driver.find_element_by_link_text("Logout")

# driver.quit()
