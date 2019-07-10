import unittest

from selenium import webdriver
from time import sleep
import time

class Login:
    def __init__(self,driver):
        self.driver = driver

    def activity_builder_login(self):
        sleep(1)
        self.driver.get("http://192.168.109.200:22001/isc_sso/login?service=http://192.168.108.175/web/")
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="username"]').send_keys('gwsc14')
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys('PH2019.com')
        self.driver.find_element_by_xpath('//*[@id="submi"]').click()

    def shenhe_login(self):
        sleep(1)
        self.driver.get("http://192.168.109.200:22001/isc_sso/login?service=http://192.168.108.175/admin_web/#/login")
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="username"]').send_keys('scywsh3')
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys('PH2020.com')
        self.driver.find_element_by_xpath('//*[@id="submi"]').click()
    def activity_participant_login(self):
        sleep(1)
        self.driver.get("http://192.168.109.200:22001/isc_sso/login?service=http://192.168.108.175/web/")
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="username"]').send_keys('gwsc15')
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys('PH2020..com')
        self.driver.find_element_by_xpath('//*[@id="submi"]').click()

