import unittest
from time import sleep
from appium import webdriver
import desired_capabilities


class TestAddContacts(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        desired_caps = desired_capabilities.get_desired_capabilities()
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def test_add_contacts(self):
        self.driver.implicitly_wait(5000)
        el = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[3]")
        el.click()
        la = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View[1]/android.view.View[3]/android.view.View/android.widget.EditText")
        la.send_keys(5513559665)
      """   textfields[2].send_keys("someone@appium.io")
        self.assertEqual('Appium User', textfields[0].text)
        self.assertEqual('someone@appium.io', textfields[2].text)
        self.driver.find_element_by_accessibility_id("Save").click() """
        try:
            self.driver.find_element_by_id('android:id/button1').click()
        except:
            pass
        self.driver.find_element_by_android_uiautomator('new UiSelector().clickable(true)').click()
        self.driver.press_keycode(3)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
