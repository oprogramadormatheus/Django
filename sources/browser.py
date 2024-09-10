from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# --headless
def create_chrome_browser(*options):
    browser_options = webdriver.ChromeOptions()

    if options is not None:
        for option in options:
            browser_options.add_argument(option)

    browser_service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=browser_service, options=browser_options)
    return browser

if __name__ == '__main__':
    browser = create_chrome_browser('--headless')
    browser.get("https://google.com")
