import os
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
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
    num = str(num)
    num_copy = ""
    for char in reversed(num):
        num_copy += char
    if num_copy != num:
        return False
    return True


def check_webpage(link: str) -> None:
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = WebDriver(options=chrome_options)
    
    try:
        driver.get(link)
        driver.implicitly_wait(10)
        visible_elements = driver.find_elements(by.CSS_SELECTOR, "*:not([style*='display:none']):not([style*='display: none'])")
        
        with open("visible_elements.html", "w", encoding="utf-8") as file:
            file.write("<html><body>")
            for element in visible_elements:
                file.write(element.get_attribute("outerHTML"))
            file.write("</body></html>")
            
    finally:
        driver.quit()


# Using the NOAA-SDK in python. Use the lat and lon to get forecast for a specific location.
def check_weather():
    lat = 40.7314
    lon = -73.8656
    
    try:
        forecasts = n.get_forecasts(lat=lat,lon= lon)
        print("Test 2 passed")
    except Exception as err:
        print("Test 2 failed")
        print(err)



def main():
    try: # Check the pallindrome function
        if check_pallindrome(pallin_num):
            raise Exception
        else:
            print("Test 1 passed.")
    except Exception as err:
        print("Test case 1 failed. Please correct the pallindrome function")
        print(err)

    check_weather()


    try: # Check the webpage function
        check_webpage(link)
        print("Test case 3 passed.")
    except Exception as err:
        print("Test case 3 failed.")
        print(err)

if __name__=="__main__":
    main()
