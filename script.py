from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from faker import Faker


def search_random_words():

    fake = Faker()


    driver = webdriver.Edge()

    try:

        driver.get("https://www.bing.com")
        time.sleep(2)

        for _ in range(40):
            random_word = fake.word()


            ActionChains(driver).key_down(Keys.CONTROL).send_keys('t').key_up(Keys.CONTROL).perform()
            time.sleep(1)


            driver.switch_to.window(driver.window_handles[-1])


            driver.get("https://www.bing.com")
            time.sleep(5)
            search_box = driver.find_element("name", "q")
            search_box.send_keys(random_word)
            search_box.send_keys(Keys.RETURN)

            time.sleep(2)

    finally:

        driver.quit()


if __name__ == "__main__":
    search_random_words()
