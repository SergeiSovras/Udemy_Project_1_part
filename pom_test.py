from selenium import webdriver
from pages.training_ground_page import TrainingGroundPage
from pages.trial_page import TrialPage

# Test Setup
browser = webdriver.Chrome()

# Test
#Trial Page
trial_page = TrialPage(driver=browser)
trial_page.go()
trial_page.stone_input.input_text("rock")
trial_page.stone_button.click()

input()

#Training_ground page
trng_page = TrainingGroundPage(driver=browser)
trng_page.go()
assert trng_page.button1.text == 'Button1', "Unexpected Result"

input()

browser.quit()
