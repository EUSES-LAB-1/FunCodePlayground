import os
from selenium import webdriver
from noaa_sdk import NOAA # NOAA-SDK python

# Global Variables
n = NOAA()
link = 'https://www.google.com'
palin_num = 112211
non_palin_num = 12345

# Test Functions
# def check_dir(path):
    # # Create directory to save the file
    # path: str = os.getcwd()
    # parent_path: str = os.path.abspath(os.path.join(path, os.pardir))
    # out_dir_path: str = os.path.join(parent_path, "HTML_output")

# Check that a number is a palindrome.
def check_palindrome(num):
    num = str(num)
    num_copy = num[::-1]
    for i in num:
        if num_copy != num:
            return False
        return True

# Using the Selenium WebDriver, save all elements from a webpage to an HTML file.
def check_webpage(link: str) -> None:
    driver: webdriver.Chrome()
    driver.get(link)


    driver.implicitly_wait(10)
    visible_elements = driver.find_elements_by_css_selector("*:not([style*=‘display:none’]):not([style*=‘display: none’])")
    # Save visible elements to an HTML file
    with open("visible_elements.html", "w", encoding="utf-8") as file:
        file.write("<html><body>")
        for element in visible_elements:
            file.write(element.get_attribute("outerHTML"))
        file.write("</body></html>")

    driver.quit()


# Using the NOAA-SDK, use the latitute and longitude to get the forecast for a specific location.
def check_weather():
    lat = 40.7314
    lon = -73.8656
    try:
        forecasts = n.get_forecasts_by_lat_lon(lat, lon)
        print("Test 2 passed")
    except Exception as err:
        print("Test 2 failed")
        print(err)



def main():
    try: # Check the palindrome function
        if not check_palindrome(palin_num) or check_palindrome(non_palin_num):
            raise Exception
        else:
            print("Test 1 passed.")
    except Exception as err:
        print("Test case 1 failed. Please correct the palindrome function")
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
