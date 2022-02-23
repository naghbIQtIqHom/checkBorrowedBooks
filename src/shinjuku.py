# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import chromedriver_binary
import re

class ShinjukuLibrary:
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
        driver.find_element_by_partial_link_text(u"利用照会").click()
        driver.switch_to.window(driver.window_handles[-1])
        driver.find_element_by_id("userno").click()
        driver.find_element_by_id("userno").clear()
        driver.find_element_by_id("userno").send_keys(self.user)
        driver.find_element_by_id("passwd").click()
        driver.find_element_by_id("passwd").clear()
        driver.find_element_by_id("passwd").send_keys(self.password)
        driver.find_element_by_xpath('//*[@id="page_content"]/form/div/div[2]/div/button[1]').click()
        # driver.find_element_by_link_text(u"ログインする").click()

    def rentlist(self):
        driver = self.driver
        
        infotables = driver.find_elements_by_xpath('//*[@id="M_LENDLIST"]/div/div[2]/table/tbody/tr')
        rents = {}
        for infotable in infotables:
            title = infotable.find_element_by_xpath("td[2]").text
            period = infotable.find_element_by_xpath("td[3]").text
            rents[title] = period
            print(title, period)
        return rents
            
    def reserveBooks(self):
        driver = self.driver

        infotables = driver.find_elements_by_xpath('//*[@id="M_RESERVELIST"]/div/div[2]/table/tbody/tr')
        rents = {}
        for infotable in infotables:
            title = infotable.find_element_by_xpath("td[2]").text
            period = infotable.find_element_by_xpath("td[3]").text
            rents[title] = period
            print(title, period)
        return rents
        
    def logout(self):
        driver = self.driver
        driver.find_element_by_link_text(u"ログアウト").click()

    def tearDown(self):
        driver = self.driver
        driver.close()
        driver.quit()

