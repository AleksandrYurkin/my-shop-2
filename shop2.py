##########################################
# Проверка цены в корзине
##########################################
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
driver = webdriver.Chrome('/home/alex/Downloads/chromedriver')
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")

# Переходим в Магазин
shop = driver.find_element_by_link_text("Shop")
shop.click()

# Добавляем в Корзину Книгу
add_basket_btn = driver.find_element_by_css_selector("[href='/shop/?add-to-cart=181']")
add_basket_btn.click()
time.sleep(10)
# time.sleep(60)

# Что на экране: Количество и Стоимость
count = driver.find_element_by_css_selector("[class='cartcontents']")
count_get_text = count.text
assert count_get_text == "1 Item"

price = driver.find_element_by_css_selector("[class='amount']")
price_get_text = price.text
assert price_get_text == "₹280.00"

print("В корзине", count_get_text)
print("Стоимость", price_get_text)

# Переходим в Корзину
driver.get("http://practice.automationtesting.in/basket/")

# Проверка в Корзине
Subtotal = WebDriverWait(driver, 20).until(
EC.element_to_be_clickable((By.CSS_SELECTOR,
"[data-title='Subtotal']")))
Subtotal.click()
Subtotal_get_text = Subtotal.text

Total = WebDriverWait(driver, 20).until(
EC.element_to_be_clickable((By.CSS_SELECTOR,
"[data-title='Total']")))
Total.click()
Total_get_text = Total.text

print("Subtotal", Subtotal_get_text)
print("Total", Total_get_text)

driver.quit()
