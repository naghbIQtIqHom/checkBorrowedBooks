# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
import chromedriver_binary

class SuginamiLibrary:
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
        driver.find_element_by_xpath(u"//img[@alt='利用者ログイン']").click()
        driver.switch_to.window(driver.window_handles[1])
        driver.find_element_by_id("usrcardnumber").clear()
        driver.find_element_by_id("usrcardnumber").send_keys(self.user)
        driver.find_element_by_id("password").click()
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(self.password)
        driver.execute_script("javascript:login();return false;")

    def rentlist(self):
        driver = self.driver
        driver.find_element_by_id("myUsrLend").click()

        rentnumber = driver.find_element_by_xpath('//*[@id="stat-lent"]/span[@class="value"]').text
        if int(rentnumber) < 1:
            return {}
        
        infotables = driver.find_elements_by_xpath('//*[@id="body"]/form/div/div[1]/table/tbody/tr')
        rents = {}
        for infotable in infotables:
            title = infotable.find_element_by_xpath("td[1]/a/strong").text
            period = infotable.find_element_by_xpath("td[5]").text
            rents[title] = period
            print(title, period)
        return rents
            
    def reserveBooks(self):
        driver = self.driver

        reservenumber = driver.find_element_by_xpath('//*[@id="stat-resv"]/span[@class="value"]').text
        if int(reservenumber) < 1:
            return {}

        driver.execute_script("javascript:toUsrRsv(1)") # 予約状況照会

        infotables = driver.find_elements_by_xpath('//*[@id="ItemDetaTable"]/tbody/tr')
        reserves = {}
        for infotable in infotables:
            title = infotable.find_element_by_xpath("td[@id='ItemDeta0105b']/strong/a").text
            status = infotable.find_element_by_xpath("td[@id='ItemDeta0105i']").text
            reserves[title] = status
        return reserves
        
    def logout(self):
        driver = self.driver
        driver.find_element_by_link_text(u"ログアウト").click()
        Alert(driver).accept()

    def tearDown(self):
        driver = self.driver
        driver.close()
        driver.quit()
