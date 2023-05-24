import os
from selenium import webdriver
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

def check_pallindrome(num: int) -> bool:
    num = str(num)
    return num == num[::-1]

def check_webpage(link: str) -> None:
    # Initialize Chrome WebDriver
    driver = webdriver.Chrome()
    # Navigate to webpage
    driver.get(link)

    # Wait for page to load and all elements to become visible
    driver.implicitly_wait(10)
    # Get all visible elements on the page
    selector = "*:not([style*=‘display:none’]):not([style*=‘display: none’])"
    visible_elements = driver.find_elements_by_css_selector(selector)
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
    forecasts = n.get_forecasts(lat, lon, 'c')



def main():
    try: # Check the pallindrome function
        if check_pallindrome(pallin_num) == False or check_pallindrome(non_pallin_num) == True:
            raise Exception
        print("Test 1 passed.")
    except Exception as err:
        print("Test case 1 failed.")
        print(err)

    try: # Check the weather function
        check_weather()
        print("Test case 2 passed")
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
