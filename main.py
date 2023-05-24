from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from noaa_sdk import NOAA # NOAA-SDK python

# Global Variables
n = NOAA()
link = 'https://www.google.com'
pallin_num = 112211
non_pallin_num = 12345

def check_palindrome(num):
    num = str(num)
    num_copy = num
    num = num[::-1]
    if num_copy == num:
        return True
    return False

def check_webpage(link: str) -> None:
    # Initialize Chrome WebDriver
    driver: WebDriver = WebDriver()
    # Navigate to webpage
    driver.get(link)

    # Wait for page to load and all elements to become visible
    driver.implicitly_wait(10)
    # Get all visible elements on the page
    visible_elements = driver.find_elements(By.CSS_SELECTOR, ":not([style*='display:none']):not([style*='display: none'])")
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
    forecasts = n.get_forecasts(lat, lon)


def main():
    try: # Check the pallindrome function
        if check_palindrome(pallin_num) == False or check_palindrome(non_pallin_num) == True:
            raise ValueError("Palindrome check failed")
        else:
            print("Test 1 passed.")
    except ValueError as err:
        print("Test case 1 failed. Please correct the palindrome function.")
        print(err)

    try: # Check the weather function
        check_weather()
        print("Test case 2 passed.")
    except Exception as err:
        print("Test case 2 failed. Please correct the check_weather function")
        print(err)

    try: # Check the webpage function
        check_webpage(link)
        print("Test case 3 passed.")
    except Exception as err:
        print("Test case 3 failed. Please correct the check_webpage function")
        print(err)

if __name__=="__main__":
    main()
