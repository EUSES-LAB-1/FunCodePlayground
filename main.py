import os
from selenium.webdriver.chrome.webdriver import WebDriver
from noaa_sdk import NOAA # NOAA-SDK python
from noaa_sdk import noaa
# Global Variables
n = NOAA()
link = 'https://www.google.com'
pallindrome_num = 112211
non_pallindrome_num = 12345

# Test Functions
# def check_dir(path):
    # # Create directory to save the file
    # path: str = os.getcwd()
    # parent_path: str = os.path.abspath(os.path.join(path, os.pardir))
    # out_dir_path: str = os.path.join(parent_path, "HTML_output")
    # os.makedirs(out_dir_path)

# Changed to 'reversed_num' and fixed the =! to ==
def check_pallindrome(num):
    num = str(num)
    reversed_num = num[::-1]
    if num == reversed_num:
        return True
    return False

# Did not alter
def check_webpage(link: str) -> None:
    # Initialize Chrome WebDriver
    driver: WebDriver = WebDriver()
    # Navigate to webpage
    driver.get(link)
    
    # Wait for page to load and all elements to become visible
    driver.implicitly_wait(10)
    # Get all visible elements on the page
    visible_elements = driver.find_elements_by_css_selector("*:not([style*=‘display:none’]):not([style*=‘display: none’])")
    # Save visible elements to an HTML file
    with open("visible_elements.html", "w", encoding="utf-8") as file:
        file.write("<html><body>")
        for element in visible_elements:
            file.write(element.get_attribute("outerHTML"))
        file.write("</body></html>")
    # Close the WebDriver
    driver.quit()

# Attempted to fix, did not succeed; only changed line 53
# Using the NOAA-SDK in python. Use the lat and lon to get forecast for a specific location.
def check_weather():
    lat = 40.7314
    lon = -73.8656
    try:
        forecasts = noaa.NOAA().get_forecasts(lat, lon)
        print("Test 2 passed")
    except Exception as err:
        print("Test 2 failed")
        print(err)


# Added raise Exception() to try 1, altered pallin_num to pallindrome_num
def main():
    try: # Check the pallindrome function
        if check_pallindrome(pallindrome_num) and not check_pallindrome(non_pallindrome_num):
            print("Test 1 passed.")
        else:
            raise Exception("Test case 1 failed. Please correct the palindrome function")
    except Exception as err:
        print("Test case 1 failed. Please correct the pallindrome function")
        print(err)
    try: # Check the weather function
        check_weather()
    except Exception as err:
        print("Test case 2 failed.")
        print(err)
    try: # Check the webpage function
        check_webpage(link)
        print("Test case 3 passed.")
    except Exception as err:
        print("Test case 3 failed.")
        print(err)
        

if __name__=="__main__":
    main()
