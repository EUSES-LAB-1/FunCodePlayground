import os
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from noaa_sdk import NOAA # NOAA-SDK python

# Global Variables
n = NOAA()
link = 'https://www.google.com'
pallin_num = 112211
non_pallin_num = 12345

# Test Functions
# def check_dir(path):
    # # Create directory to save the file
    # path: str = os.getcwd()
    # parent_path: str = os.path.abspath(os.path.join(path, os.pardir))
    # out_dir_path: str = os.path.join(parent_path, "HTML_output")
    # os.makedirs(out_dir_path)

def check_pallindrome(num):
    # num = str(num)
    num_copy = str(num)
    num = str(num)[::-1]
    if num_copy != num:
        return False
    return True

def check_webpage(link: str) -> None:
    # Initialize Chrome WebDriver
    driver: WebDriver = WebDriver()
    # Navigate to webpage
    driver.get(link)
    
    # Wait for page to load and all elements to become visible
    driver.implicitly_wait(10)

    # Get all visible elements on the page
    visible_elements = driver.find_elements(By.CSS_SELECTOR,'*:not([style*=‘display:none’]):not([style*=‘display: none’])')
    
    # Save visible elements to an HTML file
    with open("visible_elements.html", "w", encoding="utf-8") as file:
        file.write("<html><body>")
        for element in visible_elements:
            file.write(element.get_attribute("outerHTML"))
        file.write("</body></html>")
    # Close the WebDriver
    driver.quit()


# Using the NOAA-SDK in python. Use the lat and lon to get forecast for a specific location.
def check_weather():
    lat = 40.7314
    lon = -73.8656
    forecasts = n.get_forecasts('11374', 'US')



def main():
    try: # Check the pallindrome function
        if check_pallindrome(pallin_num) == False or check_pallindrome(non_pallin_num) == True:
            raise Exception
        else:
            print("Test 1 passed.")
    except Exception as err:
        print("Test 1 failed. Please correct the check_pallindrome function.")
        print(err)

    try: # Check the weather function
        check_weather()
        print("Test 2 passed.")
    except Exception as err:
        print("Test 2 failed. Please correct the check_weather function.")
        print(err)

    try: # Check the webpage function
        check_webpage(link)
        print("Test 3 passed.")
    except Exception as err:
        print("Test 3 failed. Please correct the check_webpage function.")
        print(err)

if __name__=="__main__":
    main()
