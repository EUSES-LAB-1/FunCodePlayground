# import os
from noaa_sdk import NOAA # NOAA-SDK python
from selenium import webdriver


# Global Variables
n = NOAA()
link = 'https://www.google.com'
pallin_num = 112211
non_pallin_num = 12345

# Test Functions

def check_pallindrome(num):
    num = str(num)
    num_copy = num
    num = num[::-1]
    return num_copy != num

def check_webpage(link: str):
    # Initialize Chrome WebDriver
    driver = webdriver.Chrome()

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


# Using the NOAA-SDK in python. Use the lat and lon to get forecast for a specific location.
def check_weather():
    postal_code = "10001"
    country_code = "US"
    try:
        forecasts = n.get_forecasts(postal_code, country_code)
        print("Test 2 passed")
    except Exception as err:
        print("Test 2 failed")
        print(err)




def main():
    try: # Check the pallindrome function
        if check_pallindrome(pallin_num) == False or check_pallindrome(non_pallin_num) == True:
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

    try: # Check the webpage function
        check_webpage(link)
        print("Test case 3 passed.")
    except Exception as err:
        print("Test case 3 failed.")
        print(err)

if __name__=="__main__":
    main()
