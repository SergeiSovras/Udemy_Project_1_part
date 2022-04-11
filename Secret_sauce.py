from selenium import webdriver
from lxml import etree


browser = webdriver.Chrome()
browser.get("https://techstepacademy.com/trial-of-the-stones")
divs = browser.find_elements_by_xpath("//div/span/..")
tree = etree.HTML(browser.page_source)
tree.findall(".//div/span/..")
merchant_divs = tree.findall(".//div/span/..")
merchant_divs
first_merchant = merchant_divs[0]
first_merchant
first_merchant.find("./span/b")
first_merchant.find("./span/b").text
