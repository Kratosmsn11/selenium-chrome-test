# src/main.py
import time

from src.selenium.browser_manager import BrowserManager

def main():
    # Set up the browser manager and run a Selenium task
    browser_manager = BrowserManager()
    browser_manager.start_driver()

    browser_manager.get_website()
    time.sleep(5)

    browser_manager.close_driver()


if __name__ == "__main__":
    main()
