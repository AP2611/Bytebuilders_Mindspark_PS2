from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

def user_approval(caption):
    """
    Displays caption and asks for approval.
    Returns:
        approved (bool)
    """
    print("\nGenerated Caption:\n", caption)
    approval = input("Do you approve posting this caption? (y/n): ").lower()
    return approval == "y"

def post_to_instagram(image_path, caption):
    """
    Uses Selenium to post image + caption to Instagram.
    """
    driver = webdriver.Chrome()  # Ensure chromedriver is installed & in PATH
    driver.get("https://www.instagram.com/")

    print("Log in to Instagram manually within 30 seconds...")
    time.sleep(30)

    driver.get("https://www.instagram.com/create/select/")
    time.sleep(5)

    upload_input = driver.find_element(By.XPATH, "//input[@accept='image/jpeg,image/png']")
    upload_input.send_keys(os.path.abspath(image_path))

    time.sleep(5)

    caption_box = driver.find_element(By.TAG_NAME, "textarea")
    caption_box.send_keys(caption)

    post_button = driver.find_element(By.XPATH, "//button[contains(text(),'Share')]")
    post_button.click()

    print("Post uploaded successfully!")
    time.sleep(5)
    driver.quit()
