from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time
import json
CONFIG = json.load(open("config.json",'r',encoding="utf-8"))

#建立連線
caps = {}
caps['deviceName']= '127.0.0.1:62001'
caps['platformName']= 'Android'
caps['platformVersion']= '5.1.1'
caps['appPackage']= 'com.blockchainvault'
caps['appActivity']= 'com.pinetwork.MainActivity'
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',caps)
driver.implicitly_wait(5)
#用電話登入
el3 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View[4]/android.view.View/android.widget.TextView")
el3.click()
time.sleep(5)
#點選國碼
el4 = driver.find_element_by_id("android:id/text1")
el4.click()
driver.implicitly_wait(10)

#拖拉下拉式選單
source = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[1]')
target = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[10]')
TouchAction(driver).long_press(source).move_to(target).release().perform()
driver.implicitly_wait(10)
source = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[2]')
target = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[10]')
TouchAction(driver).long_press(source).move_to(target).release().perform()
driver.implicitly_wait(10)
driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[1]').click()
time.sleep(5)
#輸入手機號
el6 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.widget.ScrollView/android.view.View/android.view.View[3]/android.widget.EditText")
el6.send_keys(CONFIG["data"]["cellphone"])
time.sleep(5)
#送出
el7 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.widget.ScrollView/android.view.View/android.view.View[3]/android.view.View/android.view.View/android.widget.TextView")
el7.click()
driver.implicitly_wait(30)
#輸入密碼
e18 = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText')

password = CONFIG["data"]["password"]
e18.send_keys(password)



driver.implicitly_wait(5)
#送出
el9 =  driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[4]/android.widget.Button")
el9.click()
driver.implicitly_wait(5)
# time.sleep(10)

try:
    # 點擊挖幣
    e20 = driver.find_element_by_xpath(
        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[3]/android.view.View[3]/android.view.View[3]')
    e20.click()


except:
    #remind me later
    e21 = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.webkit.WebView/android.webkit.WebView/android.view.View/android.app.Dialog/android.view.View/android.view.View/android.view.View[4]')
    e21.click()

    #點擊挖幣
    e20 = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[3]/android.view.View[3]/android.view.View[3]')
    e20.click()

