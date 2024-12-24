from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import time

class Flipcart_main:
    def cart(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.flipkart.com")
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)

        search = "//input[@placeholder='Search for Products, Brands and More']"
        wait.until(EC.element_to_be_clickable((By.XPATH, search))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, search))).send_keys("hand bag")
        wait.until(EC.element_to_be_clickable((By.XPATH, search))).send_keys(Keys.ENTER)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div[normalize-space()='Price -- High to Low']"))).click()

        time.sleep(3)


        results = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='DOjaWF gdgoEp']//div//a[@class='+tlBoD']//div[@class='hl05eU']")))
        results[0].click()
        time.sleep(2)

        parant_window = driver.current_window_handle
        all_handles = driver.window_handles

        time.sleep(3)

        for handle in all_handles:
            if handle != parant_window:
                driver.switch_to.window(handle)

                element = driver.find_element(By.XPATH, "//img[@class='xTaogf _3iTqAS']")
                driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
                time.sleep(1)
                wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Add to cart']"))).click()
                time.sleep(3)
                driver.back()
                time.sleep(1)
                driver.back()
                time.sleep(1)

                break

        # come to parant handled
        driver.refresh()
        cart_count = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ZuSA--']")))
        print(f"The cart contain {cart_count.text} item/items.")
        number_of_items = int(cart_count.text)
        assert number_of_items == 1
        time.sleep(3)

helo = Flipcart_main()
helo.cart()



