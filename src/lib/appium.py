import os
import time
from datetime import datetime, timedelta
from typing import Callable as function

from dotenv import load_dotenv

from appium import webdriver
from appium.options.android.uiautomator2.base import UiAutomator2Options

load_dotenv()

class Appium:
    timeout: int = 30

    def __init__(self):
        self.options = UiAutomator2Options()
        self.set_options()

    def start(self, running_flow: function, allowed_time: str = ""):
        """
        Starts the Appium server and runs the specified flow at the allowed time.
        Args:
            running_flow (function): The function to run after the specified time.
            allowed_time (str): The time in HH:MM or HH:MM:SS format when the automation should run.
        """

        driver = webdriver.Remote(
            command_executor=os.getenv("APPIUM_SERVER_URL", "http://localhost:4723"),
            options=self.options
        )

        if not allowed_time:
            allowed_time = input("At what time do you want to run the script? (e.g. 20:15:30) PM WIB: ")

        try:
            time_parts = list(map(int, allowed_time.strip().split(":")))
            if len(time_parts) == 2:
                hour, minute = time_parts
                second = 0
            elif len(time_parts) == 3:
                hour, minute, second = time_parts
            else:
                raise ValueError
        except ValueError:
            print(f"Invalid time format: {allowed_time}, should be HH:MM or HH:MM:SS")
            return

        while True:
            now_utc = datetime.utcnow()
            now_wib = now_utc + timedelta(hours=7)
            current_hour_wib = now_wib.hour
            current_minute_wib = now_wib.minute
            current_second_wib = now_wib.second

            if (current_hour_wib, current_minute_wib, current_second_wib) == (hour, minute, second):
                break
            else:
                print(f"Current WIB time {current_hour_wib:02d}:{current_minute_wib:02d}:{current_second_wib:02d} is not {hour:02d}:{minute:02d}:{second:02d}. Waiting...")
                time.sleep(0.2)

        running_flow(driver)
        driver.quit()

    def set_options(self):
        """
        Sets the Appium options based on environment variables or defaults.
        """

        self.options.platform_name = os.getenv("ANDROID_PLATFORM_NAME") or "Android"
        self.options.automation_name = os.getenv("ANDROID_AUTOMATION_NAME") or "UiAutomator2"
        self.options.device_name = os.getenv("ANDROID_DEVICE_NAME") or "Android"
        self.options.app_package = os.getenv("ANDROID_APP_PACKAGE") or "com.shopee.id"
        self.options.app_activity = os.getenv("ANDROID_APP_ACTIVITY") or "com.shopee.id/com.shopee.app.ui.home.HomeActivity_"
        self.options.no_reset = (os.getenv("ANDROID_NO_RESET") or "True") == "True"
        self.options.auto_grant_permissions = (os.getenv("ANDROID_AUTO_GRANT_PERMISSIONS") or "True") == "True"
        self.options.language = os.getenv("ANDROID_LANGUAGE") or "en"
        self.options.locale = os.getenv("ANDROID_LOCALE") or "US"
