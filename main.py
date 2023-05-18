import os
from selenium.webdriver.chrome.webdriver import WebDriver
from noaa_sdk import NOAA # NOAA-SDK python

# Test Functions
# def check_dir(path):
    # # Create directory to save the file
    # path: str = os.getcwd()
    # parent_path: str = os.path.abspath(os.path.join(path, os.pardir))
    # out_dir_path: str = os.path.join(parent_path, "HTML_output")
    # os.makedirs(out_dir_path)

def check_pallindrome(num):
    s = str(num)
    return s == s[::-1]

def check_webpage(link: str) -> None:
    
    # Initialize Chrome WebDriver
    driver: WebDriver = WebDriver()
    # Navigate to webpage
    driver.get(link)
    
    # Wait for page to load and all elements to become visible
    driver.implicitly_wait(10)
    # Get all visible elements on the page
    visible_elements = filter(lambda x: x.is_displayed(), driver.find_elements('css selector', '*'))
    # Save visible elements to an HTML file
    with open("visible_elements.html", "w", encoding="utf-8") as file:
        file.write("<html><body>")
        for element in visible_elements:
            file.write(element.get_attribute("outerHTML"))
        file.write("</body></html>")
    # Close the WebDriver
    driver.quit()


# Using the NOAA-SDK in python. Use the lat and lon to get forecast for a specific location.
def check_weather(lat: float, lon: float):
    n = NOAA()
    return n.points_forecast(lat, lon)


def test(f, success_msg, err_msg, *params):
    try:
        f(*params)
    except Exception as err:
        print(err_msg, err, sep='\n')
    print(success_msg)


def main():
    pallin_num = 112211
    non_pallin_num = 12345
    lat = 40.7314
    lon = -73.8656
    link = 'https://www.google.com'

    def test_palindrome():
        if not check_pallindrome(pallin_num) or check_pallindrome(non_pallin_num):
            raise Exception
        
    test(test_palindrome, "Test case 1 passed.", "Test case 1 failed. Please correct the pallindrome function")

    test(check_weather, "Test case 2 passed.", "Test case 2 failed. Please correct the check_weather function", lat, lon)

    test(check_webpage, "Test case 3 passed.", "Test case 3 failed. Please correc the check_webpage function", link)

if __name__=="__main__":
    main()
