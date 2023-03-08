from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Enter your Twitter login credentials
username = "your_username"
password = "your_password"

# Set up the Selenium driver
driver = webdriver.Chrome()

# Navigate to Twitter's login page
driver.get("https://twitter.com/login")

# Wait for the login page to load
time.sleep(2)

# Enter login credentials and click the login button
username_input = driver.find_element_by_xpath('//input[@name="session[username_or_email]"]')
username_input.send_keys(username)
password_input = driver.find_element_by_xpath('//input[@name="session[password]"]')
password_input.send_keys(password)
password_input.send_keys(Keys.RETURN)

# Wait for the home page to load
time.sleep(2)

# Navigate to the trends page
driver.get("https://twitter.com/explore/tabs/trending")

# Wait for the trends page to load
time.sleep(2)

# Find the latest trend hashtags and print them out
hashtags = driver.find_elements_by_xpath('//span[@class="r-18u37iz"]/span')
for hashtag in hashtags:
    print(hashtag.text)

# Navigate to the compose tweet page
driver.get("https://twitter.com/compose/tweet")

# Wait for the compose tweet page to load
time.sleep(2)

# Enter the tweet message and click the tweet button
tweet_input = driver.find_element_by_xpath('//div[@data-testid="tweetTextarea_0"]/div/div/div')
tweet_input.send_keys("Hello world, this is my tweet!")
tweet_button = driver.find_element_by_xpath('//div[@data-testid="tweetButtonInline"]/div/span')
tweet_button.click()

# Wait for the tweet to be sent
time.sleep(2)

# Close the browser
driver.quit()