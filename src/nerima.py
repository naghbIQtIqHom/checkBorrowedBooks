# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import chromedriver_binary
import re

class NerimaLibrary:
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

    def login(self):
        driver = self.driver
        driver.get(self.url)
        # driver.find_element_by_xpath(u"//a[contains(text(),'利用者ログイン')]").click()
        driver.find_element_by_partial_link_text(u"貸出・予約状況等の照会").click()
        driver.find_element_by_name("usercardno").click()
        driver.find_element_by_name("usercardno").clear()
        driver.find_element_by_name("usercardno").send_keys(self.user)
        driver.find_element_by_name("userpasswd").clear()
        driver.find_element_by_name("userpasswd").send_keys(self.password)
        driver.find_element_by_name("Login").click()

    def rentlist(self):
        driver = self.driver
        # driver.find_element_by_link_text(u"貸出状況照会").click()
        rentnumber = driver.find_element_by_xpath('//*[@id="contents"]/div[2]/div/ul/li[1]/a/h3/span').text
        pattern = "\s*(?P<number>\d+)"
        result = re.match(pattern, rentnumber)
        if not result:
            return {}
        if int(result.group('number')) < 1:
            return {}

        trs = driver.find_elements_by_xpath('//*[@id="ContentLend"]/form/div[2]/table/tbody/tr')
        trs2 = [tr for tr in trs[1:] if tr.text != '   ']
        booktitles = [tr.find_element_by_xpath('td[3]/a') for tr in trs2]
        bookreturndates = [tr.find_element_by_xpath('td[8]') for tr in trs2]
        
        rents = {}
        for i in range(0, len(booktitles)):
            title = booktitles[i].text
            period = bookreturndates[i].text
            rents[title] = period
            print(title, period)
        return rents
            
    def reserveBooks(self):
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="contents"]/div[2]/div/ul/li[2]/a/h3').click()
        reservenumber = driver.find_element_by_xpath('//*[@id="contents"]/div[2]/div/ul/li[2]/a/h3/span').text
        pattern = "\s*(?P<number>\d+)"
        result = re.match(pattern, reservenumber)
        if not result:
            return {}
        if int(result.group('number')) < 1:
            return {}

        "not implement"
        return reserves
        
    def logout(self):
        driver = self.driver
        driver.execute_script("javascript:OPWUSERLOGOUT(1)")

    def tearDown(self):
        driver = self.driver
        driver.close()
        driver.quit()
