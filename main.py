import os
from selenium.webdriver.chrome.webdriver import WebDriver
from noaa_sdk import noaa # NOAA-SDK python

# Global Variables
n = noaa.NOAA()
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

def is_pallindrome(num):
    input_num = str(num)
    reversed_num = input_num[::-1]

    return input_num == reversed_num

def check_webpage(link: str) -> None:
    # Initialize Chrome WebDriver
    driver: WebDriver = WebDriver()
    # Navigate to webpage
    driver.get(link)
    
    # Wait for page to load and all elements to become visible
    driver.implicitly_wait(10)
    # Get all visible elements on the page
    # visible_elements = driver.find_elements_by_css_selector("*:not([style*=‘display:none’]):not([style*=‘display: none’])")
    visible_elements = driver.find_elements(by="CSS_SELECTOR", value="*:not([style*='display:none']):not([style*='display: none'])")
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
    try:
        forecasts = n.get_forecasts(lat, lon)
        # forecasts = n.get_forecasts(coordinates=(lat, lon))
        print("Test 2 passed")
    except Exception as err:
        print("Test 2 failed")
        print(err)



def test_palindrome():
    if is_pallindrome(pallin_num) and not is_pallindrome(non_pallin_num):
        print("Test case 1 passed.")
    else:
        raise Exception("Test case 1 failed. Please correct the palindrome function.")

def test_weather():
    check_weather()
    print("Test case 2 passed.")

def test_webpage():
    check_webpage(link)
    print("Test case 3 passed.")

def main():
    try:
        test_palindrome()
    except Exception as err:
        print(err)

    try:
        test_weather()
    except Exception as err:
        print(err)

    try:
        test_webpage()
    except Exception as err:
        print(err)

if __name__=="__main__":
    main()
