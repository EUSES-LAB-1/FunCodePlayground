from selenium import webdriver
from noaa_sdk import NOAA

# Global Variables
n = NOAA()
link = 'https://www.google.com'
pallin_num = 112211
non_pallin_num = 12345

# Test Functions
def check_palindrome(num):
    num = str(num)
    return num == num[::-1]

def check_weather(postal_code, country):
    try:
        forecasts = n.get_forecasts(postal_code, country)
        print("Test case 2 passed.")
        # Process forecast data as needed
    except Exception as err:
        print("Test case 2 failed.")
        print(err)

def check_webpage(link):
    # Initialize Chrome WebDriver
    driver = webdriver.Chrome()
    try:
        # Navigate to webpage
        driver.get(link)
        # Wait for page to load and all elements to become visible
        driver.implicitly_wait(10)
        # Get all visible elements on the page
        visible_elements = driver.find_elements_by_css_selector(
            "*:not([style*='display:none']):not([style*='display: none'])"
        )
        # Save visible elements to an HTML file
        with open("visible_elements.html", "w", encoding="utf-8") as file:
            file.write("<html><body>")
            for element in visible_elements:
                file.write(element.get_attribute("outerHTML"))
            file.write("</body></html>")
        print("Test case 3 passed.")
    except Exception as err:
        print("Test case 3 failed.")
        print(err)
    finally:
        # Close the WebDriver
        driver.quit()

def main():
    try:  # Check the palindrome function
        if not check_palindrome(pallin_num) or check_palindrome(non_pallin_num):
            raise Exception("Palindrome test failed.")
        else:
            print("Test case 1 passed.")
    except Exception as err:
        print("Test case 1 failed.")
        print(err)

    try:  # Check the weather function
        postal_code = "97330"
        country = "US"
        check_weather(postal_code, country)
    except Exception as err:
        print("Test case 2 failed.")
        print(err)

    try:  # Check the webpage function
        check_webpage(link)
    except Exception as err:
        print("Test case 3 failed.")
        print(err)

if __name__ == "__main__":
    main()
