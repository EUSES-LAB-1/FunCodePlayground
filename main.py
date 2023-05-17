from selenium.webdriver.chrome.webdriver import WebDriver
from noaa_sdk import NOAA

def check_palindrome(num):
    num_str = str(num)
    return num_str == num_str[::-1]

def check_webpage(link):
    # Initialize Chrome WebDriver
    driver = WebDriver()
    # Navigate to webpage
    driver.get(link)
    
    # Wait for page to load and all elements to become visible
    driver.implicitly_wait(10)
    
    # Get all visible elements on the page
    visible_elements = driver.find_elements_xx("*:not([style*=‘display:none’]):not([style*=‘display: none’])")
    
    # Save visible elements to an HTML file
    with open("visible_elements.html", "w", encoding="utf-8") as file:
        file.write("<html><body>")
        for element in visible_elements:
            file.write(element.get_attribute("outerHTML"))
        file.write("</body></html>")
    
    # Close the WebDriver
    driver.quit()

def get_weather_forecast(lat, lon):
    n = NOAA()
    return n.get_observations_by_lat_lon(lat, lon)

def main():
    link = 'https://www.google.com'
    palindrome_num = 112211
    non_palindrome_num = 12345
    lat = 44.5646
    lon = 123.2620

    try:
        # Check the palindrome function
        if not check_palindrome(palindrome_num) or check_palindrome(non_palindrome_num):
            raise Exception("Palindrome test failed")
        print("Palindrome test passed.")

        # Check the weather function
        forecast = get_weather_forecast(lat, lon)
        print("Weather test passed.")

        # Check the webpage function
        check_webpage(link)
        print("Webpage test passed.")
    except Exception as err:
        print("Test failed:")
        print(err)

if __name__ == "__main__":
    main()