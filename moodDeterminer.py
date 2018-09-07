from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from flask import Flask, request, abort
from bs4 import BeautifulSoup
import requests
import time

class MoodDeterminer():
	def __init__(self):
		self.driver = webdriver.PhantomJS("bin/phantomjs")
		self.driver.get("https://azure.microsoft.com/zh-tw/services/cognitive-services/text-analytics/")
	def sendText(self, text):
		self.source = self.driver.find_element_by_id("text-analytics-demo")
		self.source.clear()
		self.source.send_keys(text)
		self.driver.find_element_by_css_selector(".button.button-primary.full-row-width-button").click()
		time.sleep(2)
	def getText(self):
		self.wait = WebDriverWait(self.driver, 10)
		return self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='absolutely-centered']")))[0].text
	def __del__(self):
		self.driver.close()
