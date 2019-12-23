from selenium import webdriver

driver = webdriver.Chrome(executable_path="drivers/chromedriver")

driver.get('https://www.facebook.com/')


driver.find_element_by_name('firstname').send_keys('shaimaa')
driver.find_element_by_name('lastname').send_keys('mesha')
driver.find_element_by_name('reg_email__').send_keys('shaimaatest1991@gmail.com')
driver.find_element_by_name('reg_passwd__').send_keys('P@ssw0rdsha@123')
driver.find_element_by_name('reg_email_confirmation__').send_keys('shaimaatest1991@gmail.com')
driver.find_element_by_name('birthday_day').send_keys('1')
driver.find_element_by_name('birthday_month').send_keys('Oct')
driver.find_element_by_name('birthday_year').send_keys('1991')
driver.find_element_by_id('u_0_9').click()
driver.find_element_by_name('websubmit').click()

if driver.find_element_by_id('facebook'):
    print('sign up successful')
else:
    print('Sign Up failed')

driver.close()











