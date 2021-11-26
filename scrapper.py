import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from random import randint
from proxy import Proxy
import time
import json


class Scrapper:
    browser = None
    pages = 100
    firefoxCapabilities = webdriver.DesiredCapabilities.FIREFOX
    Proxy = Proxy()
    randomProxy = Proxy.getRandomProxy()
    Options = Options()
    config = None

    def __init__(self) -> None:
        self.firefoxCapabilities['marionette'] = True

        # Load Config
        self.loadConfig()

        # Setting Proxy
        if self.config["use_proxy"] == True:
            # Get random proxy and setting proxy
            proxy = self.randomProxy["ip"]+":"+self.randomProxy["port"]
            self.firefoxCapabilities['proxy'] = {
                "proxyType": "MANUAL",
                "httpProxy": proxy,
                "sslProxy": proxy
            }

            # Set Headless
            if self.config["headless"] == True:
                self.Options.headless = True

            self.browser = webdriver.Firefox(
                executable_path='./geckodriver.exe', capabilities=self.firefoxCapabilities, options=self.Options)
        else:
            self.browser = webdriver.Firefox(
                executable_path='./geckodriver.exe')

    def loadConfig(self):
        with open("./config.json") as file:
            self.config = json.load(file)

    def searchGoogleByKeyword(self, keyword, URI):
        results = []
        for page in range(1, self.pages):
            try:
                self.browser.get(
                    "https://google.com/search?q=" +
                    keyword + '&start=' + str((page-1)*10)
                )
                search = self.browser.find_elements_by_css_selector(
                    "div.yuRUbf > a")
                for link in search:
                    if link.get_attribute('href') == URI:
                        self.browser.find_element_by_xpath(
                            '//a[@href="'+URI+'"]').click()
                        self.randomScrollUpToDown(
                            1, randint(20, 40), 5, 10, randint(5, 10))
                time.sleep(1)
                self.randomScrollUpToDown(10, 40)
                time.sleep(5)
                self.browser.quit()
                if self.config["interval"] != "Default":
                    INTERVAL = self.config["interval"]
                else:
                    INTERVAL = random.randint(3000, 6000)
                print("\033[93m"+"Bot akan berjalan lagi setelah " +
                      INTERVAL+" detik"+"\033[0m")
            except Exception as e:
                if self.config["use_proxy"] == True:
                    print(
                        "\033[93m"+"Sepertinya proxy anda ("+self.randomProxy["ip"]+":"+self.randomProxy["port"]+") bermasalah ...."+"\033[0m")
                print(e)
                try:
                    print("Close browser")
                    self.browser.quit()
                except Exception as e:
                    print(e)
                exit()

    def randomScrollUpToDown(self, fromNum, to, start=1, stop=5, SCROLL_PAUSE_TIME=0.5):
        for foo in range(fromNum, to):
            self.scrollUpToDown(randint(start, stop))
            time.sleep(SCROLL_PAUSE_TIME)

    def scrollUpToDown(self, time):
        body = self.browser.find_element_by_css_selector('body')
        body.click()
        for foo in range(1, time):
            body.send_keys(Keys.ARROW_DOWN)
