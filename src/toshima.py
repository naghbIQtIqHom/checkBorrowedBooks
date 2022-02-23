# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import chromedriver_binary
import re

class ToshimaLibrary:
    def __init__(self, url, user, password):
        self.url = url
        self.user = user
        self.password = password
        
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
        self.driver = self.driver

    def login(self):
        driver = self.driver
        driver.get(self.url)
        driver.find_element_by_partial_link_text(u"ログイン").click()
        driver.find_element_by_id("textUserId").click()
        driver.find_element_by_id("textUserId").clear()
        driver.find_element_by_id("textUserId").send_keys(self.user)
        driver.find_element_by_id("textPassword").clear()
        driver.find_element_by_id("textPassword").send_keys(self.password)
        driver.find_element_by_id("buttonLogin").click()

    def rentlist(self):
        driver = self.driver
        #driver.find_elements_by_link_text(u"マイページ")[0].click()
        #driver.find_element_by_link_text(u"マイページ").click()
        driver.find_element_by_link_text(u"利用者メニュー").click()
        rentnumber = driver.find_element_by_xpath('//*[@id="honbun"]/div/div/div/div/section[1]/section[1]/dl/dt').text
        pattern = "\s*(?P<number>\d+)件"
        result = re.match(pattern, rentnumber)
        if not result:
            return {}
        if int(result.group('number')) < 1:
            return {}

        driver.find_element_by_partial_link_text(u"貸出状況照会へ").click()
        infotables = driver.find_elements_by_xpath('//*[@id="result"]/section[@class="infotable"]')
        rents = {}
        for infotable in infotables:
            title = infotable.find_element_by_xpath("h3/a/span[1]").text
            period = infotable.find_element_by_xpath("div/div[2]/dl[4]/dd").text
            rents[title] = period
            print(title, period)
        return rents
            
    def reserveBooks(self):
        driver = self.driver
        driver.find_element_by_link_text(u"利用者メニュー").click()
        reservenumber = driver.find_element_by_xpath('//*[@id="honbun"]/div/div/div/div/section[1]/section[2]/dl/dt').text
        pattern = "\s*(?P<number>\d+)件"
        result = re.match(pattern, reservenumber)
        if not result:
            return {}
        if int(result.group('number')) < 1:
            return {}

        driver.find_element_by_partial_link_text(u"予約状況照会へ").click()
        
        infotables = driver.find_elements_by_xpath('//*[@id="first"]/section/div[4]/section[@class="infotable"]')
        reserves = {}
        for infotable in infotables:
            title = infotable.find_element_by_xpath("h3/a/span[1]").text
            status = infotable.find_element_by_xpath("div/div[2]/dl[3]/dd").text
            reserves[title] = status
        return reserves
        
    def logout(self):
        driver = self.driver
        driver.find_element_by_link_text(u"ログアウト").click()

    def tearDown(self):
        driver = self.driver
        driver.close()
        driver.quit()
