import os
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from noaa_sdk import NOAA # NOAA-SDK python

# Global Variables

def check_pallindrome(num):
    num = str(num)
    num_copy = num
    num = num[::-1]
    num_copy = ""
    for char in reversed(num):
        num_copy += char
    if num_copy != num:
        return True
    return False
        return False
    return True


def check_webpage(link: str) -> None:
    # Initialize Chrome WebDriver
    driver: WebDriver = WebDriver()
    # Navigate to webpage
    driver.get(link)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = WebDriver(options=chrome_options)

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
        forecasts = n.get_forecasts(coordinates=(lat, lon))
        forecasts = n.get_forecasts(lat=lat,lon= lon)
        print("Test 2 passed")
    except Exception as err:
        print("Test 2 failed")


def main():
    try: # Check the pallindrome function
        if check_pallindrome(pallin_num) == False or check_pallindrome(non_pallin_num) == True:
        if check_pallindrome(pallin_num):
            raise Exception
        else:
            print("Test 1 passed.")
    except Exception as err:
        print("Test case 1 failed. Please correct the pallindrome function")
        print(err)

    try: # Check the weather function
        check_weather()
    except Exception as err:
        print("Test case 2 failed.")
        print(err)
    check_weather()


    try: # Check the webpage function
        check_webpage(link)
