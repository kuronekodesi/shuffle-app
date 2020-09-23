import asyncio
import time
from walkoff_app_sdk.app_base import AppBase

class Blog(AppBase):
    __version__ = "1.0.0"
    app_name = "log"  # this needs to match "name" in api.yaml

    def __init__(self, redis, logger, console_logger=None):

        super().__init__(redis, logger, console_logger)

    async def sendBlog(self, title, context):
        try:
            from selenium import webdriver
            from selenium.webdriver.common.keys import Keys
        except:
            mystr = "no selenium"
            return mystr
        path = '/logs.txt'
        logs = 'This is logs!'
        file = open(path, 'w')
        file.write(logs)
        option = webdriver.ChromeOptions()
        # option.add_argument('--user-data-dir=/Users/apple/Library/Application Support/Google/Chrome/Default')
        option.add_argument('--headless')
        option.add_argument('--no-sandbox')
        option.add_argument('--disable-gpu')
        option.add_argument('--disable-dev-shm-usage')
        browser = webdriver.Chrome(chrome_options=option)
        # browser=webdriver.Chrome()

        browser.get("http://10.245.142.98:83/wp-login.php")
        # browser.execute_script("document.body.style.zoom='0.5'")#缩放0.5
        browser.set_window_size(1920, 1080)
        browser.maximize_window()
        time.sleep(1)
        browser.find_element_by_name('log').send_keys('kuroneko')
        browser.find_element_by_name('pwd').send_keys('wangxiao')
        browser.find_element_by_name('wp-submit').click()
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/ul/li[3]/a/div[3]').click()
        time.sleep(1)
        browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/ul/li[3]/ul/li[3]/a').click()
        time.sleep(1)
        browser.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div/div/div[1]/div[1]/div[1]/input').send_keys(title)
        time.sleep(1)
        browser.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div/div/div[1]/div[2]/div/div[1]/div[2]/button[2]').click()
        time.sleep(1)
        browser.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div/div/div[1]/div[2]/div/div[2]/textarea').send_keys(
            context)
        time.sleep(1)
        browser.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/form/div/div/div[2]/div/div[1]/div/div/div[2]/div[2]/input[2]').click()
        time.sleep(1)
        # browser.find_element_by_name("password").send_keys("macro123")
        # browser.find_element_by_name("password").send_keys(Keys.ENTER)
        time.sleep(2)

        return "OK!!"


if __name__ == "__main__":
    asyncio.run(Blog.run(), debug=True)
