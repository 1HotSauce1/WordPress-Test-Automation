from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

def login_function(username, password, driver):
    """Function to login to the wordpress theme
        Writes the username and password and clicks login

    Args:
        username (string): username in login form
        password (string): password in login form
        driver (object): chrome driver
    """
    # Write the username
    user_form = driver.find_element_by_id('user_login')
    user_form.send_keys(username)

    # Write the password
    pass_form = driver.find_element_by_id('user_pass')
    pass_form.send_keys(password)

    # Click login
    login_button = driver.find_element_by_id('wp-submit')
    login_button.click()


def open_container(driver):
    """Function to open the container customization panel.
        Click on layout, then click on container.

    Args:
        driver (object): chrome driver
    """
    # Click layout button
    layout = driver.find_element_by_xpath('//*[@id="accordion-panel-neve_layout"]/h3')
    layout.click()

    # Click container button
    container = driver.find_element_by_xpath('//*[@id="accordion-section-neve_container"]/h3')
    container.click()


def test_container_width(driver):
    """Function to test the container width.

    Args:
        driver (object): chrome driver
    """
    # List that contains the width values that the theme is going to be tested with
    values = [x for x in range(-1,2002)]

    # Finds the width input form
    value_input = driver.find_element_by_id('inspector-input-control-20')

    # Write the values in the form
    for value in values:
        # The first 2 calls are used for deleting the form text
        # so the program can write all the values 1 by 1
        value_input.send_keys(Keys.CONTROL + 'a')
        value_input.send_keys(Keys.DELETE)
        value_input.send_keys(value)





