from selenium.common.exceptions import NoSuchElementException
import XLUtilis
from selenium import webdriver
import os

driver = webdriver.Chrome(executable_path="drivers/chromedriver")
current_path = os.getcwd()
file_path = current_path + "/Datadriven.xlsx"

rows= XLUtilis.getRowCount(file_path, 'Sheet1')
# Add a for loop to read row by row from the excel sheet.
for r in range(2, rows+1):
    # Open the Facebook url.
    driver.get('https://www.facebook.com/')
    # Read the email address from the excel sheet.
    email = XLUtilis.readData(file_path, "Sheet1",r,1)
    # Read the password from the excel sheet.
    password = XLUtilis.readData(file_path, "Sheet1",r,2)
    # Read the expected message from the excel sheet.
    expected_message = XLUtilis.readData(file_path, "Sheet1",r,3)
    other_expected_message = XLUtilis.readData(file_path, "Sheet1",r,4)

    # Try to login.
    driver.find_element_by_name('email').send_keys(email or "")
    driver.find_element_by_name('pass').send_keys(password or "")
    driver.find_element_by_id('u_0_b').click()

    # Try to find the class name for the error message (the first format)
    try:
        error_message = driver.find_element_by_class_name("_3-95")

        if error_message.text == expected_message:
            XLUtilis.writeData(file_path, 'Sheet1', r, 5, 'test passed')
        else:
            XLUtilis.writeData(file_path, 'Sheet1', r, 5, 'test failed')
            XLUtilis.writeData(file_path, 'Sheet1', r, 6, error_message.text)

    # If there is no error message, check for the logged in case.
    except NoSuchElementException:
        # Try to find the class name for the error message (the second format)
        try:
            error_message = driver.find_element_by_class_name("_53ij")

            if error_message.text == other_expected_message:
                XLUtilis.writeData(file_path, 'Sheet1', r, 5, 'test passed')
            else:
                XLUtilis.writeData(file_path, 'Sheet1', r, 5, 'test failed')
                XLUtilis.writeData(file_path, 'Sheet1', r, 6, error_message.text)

        # If there is no error message, check for the logged in case.
        except NoSuchElementException:
            try:
                loged_in_message = driver.find_element_by_class_name("_59fb")
                XLUtilis.writeData(file_path, 'Sheet1', r, 5, 'test passed')
                XLUtilis.writeData(file_path, 'Sheet1', r, 6, 'Logged In Successfully')

            # If element is not found then there 's another error
            except NoSuchElementException:
                XLUtilis.writeData(file_path, 'Sheet1', r, 5, 'test failed')
            
driver.close()
