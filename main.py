from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android.uiautomator2.base import UiAutomator2Options

options = UiAutomator2Options()
options.platform_name = "Android"
options.automation_name = "UiAutomator2"
options.device_name = "Android"
options.app_package = "com.shopee.id"
options.app_activity = "com.shopee.id/com.shopee.app.ui.home.HomeActivity_"
options.no_reset = True
options.auto_grant_permissions = True
options.language = "en"
options.locale = "US"

caps = options.to_capabilities()
driver = webdriver.Remote(command_executor="http://localhost:4723", options=options) # type: ignore

el = driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Saya"]')
el.click()

driver.quit()
