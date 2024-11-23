import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException,TimeoutException
import time
from selenium.webdriver.common.action_chains import ActionChains
import os

def test_markirovka(driver_setup):
    driver, udid = driver_setup
    wait = WebDriverWait(driver, 15)
    add_receipt_items = wait.until(
        EC.presence_of_element_located((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/button_add_receipt_item')))
    add_receipt_items.click()
    time.sleep(1)
    menu_search = wait.until(
        EC.presence_of_element_located((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/menu_item_search')))
    menu_search.click()

    search_input1 = wait.until(EC.presence_of_element_located((AppiumBy.ID, 'android:id/search_src_text')))
    search_input1.clear()
    search_input1.send_keys("Маркировка")
    select_item = wait.until(EC.presence_of_element_located((AppiumBy.XPATH,"//androidx.recyclerview.widget.RecyclerView[@resource-id='com.bifit.cashdesk.mobile:id/recycler']/android.view.ViewGroup[2]")))
    select_item.click()
    time.sleep(1)

    mark = "0000004621065422dBtACAAPidGVz"
    input_command = f'adb shell input text "{mark}"'

    # Отправляем команду
    os.system(input_command)

    # Нажимаем Enter после передачи строки
    os.system("adb shell input keyevent 66")

    search_input2 = wait.until(EC.visibility_of_element_located((AppiumBy.ID, 'android:id/search_src_text')))
    search_input2.clear()
    search_input2.send_keys("Маркировка")
    select_item = wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(5)')))
    select_item.click()

    mark = "04601653035829H;dV)bFACVUdGVz"
    input_command = f'adb shell input text "{mark}"'

    # Отправляем команду
    os.system(input_command)

    # Нажимаем Enter после передачи строки
    os.system("adb shell input keyevent 66")
    done = wait.until(EC.presence_of_element_located((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/fab_done')))
    done.click()
    time.sleep(1)

    total = wait.until(EC.visibility_of_element_located((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/button_continue')))
    total.click()
    time.sleep(2)
    next_button = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Далее")')))
    next_button.click()
    without_change = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, ("//android.widget.Button[@text='Без сдачи']"))))
    without_change.click()
    sno = wait.until(EC.presence_of_element_located((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/text_input_tax_system')))
    sno.click()
    sno_select = wait.until(EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.ListView/android.widget.LinearLayout[1]')))
    sno_select.click()
    button_pay = driver.find_element(AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/button_pay')
    button_pay.click()

