from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from flask import Flask, request, abort
from bs4 import BeautifulSoup
import requests
import time

class GoogleTranslater():
	def __init__(self):
		self.driver = webdriver.PhantomJS("bin/phantomjs")
		self.driver.get("https://translate.google.com.tw/?hl=zh-TW&tab=TT#zh-CN/en/")
	def sendText(self, text):
		self.source = self.driver.find_element_by_id("source")
		self.source.clear()
		self.source.send_keys(text)
	def getText(self):
		self.wait = WebDriverWait(self.driver, 10)
		return self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//span[@id='result_box']/span[1]")))[0].text
	def __del__(self):
		self.driver.close()
