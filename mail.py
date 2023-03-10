from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Replace with your own Gmail account details
username = "your_username@gmail.com"
password = "your_password"

# Start a new browser session
driver = webdriver.Chrome()

# Navigate to the Gmail login page
driver.get("https://www.gmail.com")

# Enter the username and password and click the login button
driver.find_element_by_id("identifierId").send_keys(username)
driver.find_element_by_id("identifierNext").click()

driver.implicitly_wait(10)

driver.find_element_by_name("password").send_keys(password)
driver.find_element_by_id("passwordNext").click()

driver.implicitly_wait(10)

# Navigate to the inbox
driver.get("https://mail.google.com/mail/u/0/#inbox")

# Find the email you want to read and click on it
email_subject = "Subject of the email you want to read"
email_element = driver.find_element_by_xpath(f"//span[@class='bog']/span[text()='{email_subject}']")
email_element.click()

# Get the contents of the email
email_body_element = driver.find_element_by_xpath("//div[@class='a3s aiL ']")
email_body = email_body_element.text

# Print the contents of the email
print(email_body)

# Close the browser
driver.quit()
