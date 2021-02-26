from selenium import webdriver
from utils import *

PATH = 'C:\Program Files (x86)\chromedriver.exe' # Path to chrome driver
USERNAME = 'adming' # wordpress username
PASSWORD = 'admin' # wordpress password
driver = webdriver.Chrome(PATH)

if __name__ == '__main__':
  # Loading my localhost server that contains the neve theme
  driver.get('http://localhost/dragos/wp-admin/customize.php?theme=neve&return=http%3A%2F%2Flocalhost%2Fdragos%2Fwp-admin%2Fthemes.php')

  # Login to the theme
  login_function(USERNAME, PASSWORD, driver)

  # Open the container panel
  open_container(driver)

  # Test container width
  test_container_width(driver)  
