from appium.webdriver.webdriver import WebDriver
from appium.webdriver.common.appiumby import AppiumBy
import time

voucher_text = "Diskon 2% s/d Rp500RB"

def run(driver: WebDriver):
    global voucher_text
    start = time.perf_counter()

    btns = driver.find_elements(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Voucher")')
    (btns[0] if btns else driver.find_element(AppiumBy.XPATH, "//*[@text='Voucher']")).click()

    voucher_candidates = driver.find_elements(AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{voucher_text}")')
    if voucher_candidates:
        voucher_candidates[0].click()
        print(f"[✓] Voucher '{voucher_text}' berhasil dipilih tanpa scroll.")
    else:
        try:
            driver.swipe(500, 1500, 500, 500, 25)
            voucher_candidates = driver.find_elements(AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{voucher_text}")')
            if voucher_candidates:
                voucher_candidates[0].click()
                print(f"[✓] Voucher '{voucher_text}' berhasil dipilih setelah 1x scroll ke bawah.")
            else:
                print(f"[!] Voucher '{voucher_text}' tidak ditemukan setelah 1x scroll.")
        except Exception as e:
            print(f"[!] Voucher '{voucher_text}' tidak ditemukan: {e}")
            pass

    try:
        size = driver.get_window_size()
        driver.tap([(size['width'] // 2, int(size['height'] * 0.975))])
    except Exception:
        pass

    print(f"⏱️ Total: {time.perf_counter() - start:.2f} s")
