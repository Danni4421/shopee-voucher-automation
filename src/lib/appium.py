import os
import time
from datetime import datetime
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
        self.driver = webdriver.Remote(
            command_executor=os.getenv("APPIUM_SERVER_URL", "http://localhost:4723"),
            options=self.options
        )

    def start(self, running_flow: function):
        allowed_hours = input("What time do you want to run the script? (e.g. 8, 9, 10) PM WIB: ")
        if allowed_hours:
            allowed_hours = [int(h.strip()) for h in allowed_hours.split(",") if h.strip().isdigit()]
            while True:
                now_utc = datetime.utcnow()
                now_wib = now_utc.replace(hour=(now_utc.hour + 7) % 24)
                current_hour_wib = now_wib.hour
                if current_hour_wib in allowed_hours:
                    break

                print(f"Current WIB hour {current_hour_wib} is not in the allowed hours {allowed_hours}. Waiting for the next hour...")
                time.sleep(60)

        running_flow(self.driver)
        self.driver.quit()

    def set_options(self):
        self.options.platform_name = os.getenv("ANDROID_PLATFORM_NAME") or "Android"
        self.options.automation_name = os.getenv("ANDROID_AUTOMATION_NAME") or "UiAutomator2"
        self.options.device_name = os.getenv("ANDROID_DEVICE_NAME") or "Android"
        self.options.app_package = os.getenv("ANDROID_APP_PACKAGE") or "com.shopee.id"
        self.options.app_activity = os.getenv("ANDROID_APP_ACTIVITY") or "com.shopee.id/com.shopee.app.ui.home.HomeActivity_"
        self.options.no_reset = (os.getenv("ANDROID_NO_RESET") or "True") == "True"
        self.options.auto_grant_permissions = (os.getenv("ANDROID_AUTO_GRANT_PERMISSIONS") or "True") == "True"
        self.options.language = os.getenv("ANDROID_LANGUAGE") or "en"
        self.options.locale = os.getenv("ANDROID_LOCALE") or "US"
