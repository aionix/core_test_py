import time
import logging
from typing import List

#from cssselect import HTMLTranslator
from selenium.common.exceptions import TimeoutException, WebDriverException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.remote.webelement import WebElement
"""
 We import firefox webdriver here just to get a context help menu for pycharm ide.
 It doesn't mean we really have firefox driver here. It could be chrome or any other. They mostly have the same
 methods so any of them will do fine for us.
 """
from selenium.webdriver.firefox.webdriver import WebDriver


class WebDriverWrapper(object):
    """Higher abstraction wrapper for selenium.webdriver"""

    def __init__(self, webdriver):
        """
        @type webdriver: WebDriver
        """
        self.driver = webdriver
        self.driver_wait = WebDriverWait
        self.expected_conditions = EC

    def get_current_url(self):
        return self.driver.current_url

    def find_element_by_name(self, name):
        """
        A simple wrapper for webdriver find_element_by_name method.
        :param name: str
        :return: WebElement
        """
        return self.driver.find_element_by_name(name)

    def find_element_by_class(self, class_name):
        """
        Simple wrapper for webdriver find_element_by_class_name method.

        Args:
            class_name (str): value for class attribute of element to find.

        Returns (WebElement): if located.
        """
        return self.driver.find_element_by_class_name(class_name)

    def find_element_by_css(self, css):
        return self.driver.find_element_by_css_selector(css)

    def find_element_by_xpath(self, xpath):
        return self.driver.find_element_by_xpath(xpath)

    def is_elem_exist_by_css(self, css, wait_time=5):
        try:
            if self.driver_wait(self.driver, wait_time).until(lambda driver: self.driver.find_element_by_css_selector(css)):
                return True
        except TimeoutException:
            return False

    def is_elem_exist_by_xpath(self, xpath, wait_time=5):
        try:
            if self.driver_wait(self.driver, wait_time).until(lambda driver: self.driver.find_element_by_xpath(xpath)):
                return True
        except TimeoutException:
            return False

    def is_elem_exist_by_text(self, text, wait_time=5):
        try:
            if self.find_element_by_text(text, wait_time) is not None:
                return True
        except TimeoutException:
            return False

    def wait_for_element_by_xpath(self, xpath, wait_time=5):
        """
        Args:
            xpath (str): xpath to locate element.
            wait_time (int): time (seconds) to wait for element to appear.

        Returns:
            WebElement: if found.

        Raises:
            TimeoutException: element not found after wait time.
        """
        try:
            """
            :rtype WebElement
            """
            return self.driver_wait(self.driver, wait_time).until(lambda driver: self.driver.find_element_by_xpath(xpath))
        except TimeoutException:
            raise TimeoutException('Unable to find element by xpath %s after waiting for %d seconds' % (xpath, wait_time))

    def wait_for_elements_by_xpath(self, xpath, wait_time=5):
        try:
            """
            :rtype WebElement
            """
            return self.driver_wait(self.driver, wait_time).until(lambda driver: self.driver.find_elements_by_xpath(xpath))
        except TimeoutException:
            raise TimeoutException('Unable to find elements by xpath %s after waiting for %d seconds' % (xpath, wait_time))

    def wait_for_element_by_css(self, css, wait_time=5):
        """
        Args:
            css (str): css to locate element.
            wait_time (int): time (seconds) to wait for element to appear.

        Returns:
            WebElement: if found.

        Raises:
            TimeoutException: element not found after wait time.
        """
        try:
            return self.driver_wait(self.driver, wait_time).until(lambda driver:
                                                                  self.driver.find_element_by_css_selector(css))
        except TimeoutException:
            raise TimeoutException('Unable to find element by css %s after waiting for %d seconds' % (css, wait_time))

    def wait_for_element_clickable_by_xpath(self, xpath, wait_time=5):
        try:
            wait = self.driver_wait(self.driver, wait_time)
            return wait.until(self.expected_conditions.element_to_be_clickable((By.XPATH, xpath)))
        except TimeoutException:
            raise Exception('Element %s not clickable after waiting for %d seconds' % (xpath, wait_time))

    def wait_while_element_visible_by_css(self, css, wait_time=5):
        try:
            wait = self.driver_wait(self.driver, wait_time)
            return wait.until(self.expected_conditions.invisibility_of_element_located((By.CSS_SELECTOR, css)))
        except TimeoutException:
            raise Exception('Element %s still visible after waiting for %d seconds' % (css, wait_time))

    def wait_while_element_visible_by_xpath(self, xpath, wait_time=5):
        try:
            wait = self.driver_wait(self.driver, wait_time)
            return wait.until(self.expected_conditions.invisibility_of_element_located((By.XPATH, xpath)))
        except TimeoutException:
            raise TimeoutException('Element %s still visible after %d seconds' % (xpath, wait_time))

    def find_element_by_text(self, text, wait_time=5):
        """
        Find element by text.
        Works well if  element text is unique on page. If not, better choose another text search method.

        Args:
            text (str): element with this text will be searched.
            wait_time (int): wait time
        Returns:
            WebElement: first found element containing text.
        """
        return self.wait_for_element_by_xpath("//*[contains(text(), '%s')]" % text, wait_time)

    # TODO: I don't like this method name. Need a better word here to describe param for not contains part.
    def find_element_by_text_excepted(self, text, text_excepted):
        """
        Find first element containing text but not text_excepted.

        Args:
            text (str): text to find elements with.
            text_excepted (str): text to exclude elements.

        Returns:
            WebElement: if such element exists.
        """
        return self.wait_for_element_by_xpath("//*[contains(text(), '%s')][not(contains(text(), '%s'))]" % (text, text_excepted))

    def element_has_class(self, element, class_name):
        return class_name in element.get_attribute('class')

    def set_element_attribute(self, selector, attribute, value):
        script = 'document.getElementsByClassName("{}")[0].{} = "{}";'.format(selector, attribute, value)
        try:
            self.driver.execute_script(script)
        except Exception as msg:
            logging.error('Failed to execute script %s. Error: %s', script, msg)
            return False
        return True

    def execute_script(self, script):
        try:
            self.driver.execute_script(script)
        except Exception:
            pass

    def get(self, page_path):
        self.driver.get(page_path)

    def refresh(self):
        self.driver.refresh()

    def maximize_window(self):
        # FIXME selenoid with chrome have low window res due to run in headless mode without window managers
        # need better way
        self.driver.set_window_size(1920, 1080)
        # self.driver.maximize_window() 

    def make_screenshot(self, filename):
        return self.driver.save_screenshot(filename)

    def get_screenshot_as_png(self):
        return self.driver.get_screenshot_as_png()

    def get_full_page_screenshot(self):
        width = self.driver.execute_script("return Math.max(document.body.scrollWidth, document.body.offsetWidth, \
            document.documentElement.clientWidth, document.documentElement.scrollWidth, \
            document.documentElement.offsetWidth);")
        height = self.driver.execute_script("return Math.max(document.body.scrollHeight, document.body.offsetHeight, \
            document.documentElement.clientHeight, document.documentElement.scrollHeight, \
            document.documentElement.offsetHeight);")
        self.driver.set_window_size(width+100, height+100)
        return self.driver.get_screenshot_as_png()

    def get_page_screenshot_fixed_size(self, width, height):
        window_size = self.driver.get_window_size()
        if width > window_size['width'] or height > window_size['height']:
            self.driver.set_window_size(width, height)
        return self.driver.get_screenshot_as_png()

    def get_element_screenshot(self, element, offset=10):
        try:
            size = element.size
        except KeyError:
            logging.error('Current browser is not supporting size prop. Fallback to full page screenshot.')

        if size:
            screenshot = self.get_page_screenshot_fixed_size(size['width'], size['height'])
        else:
            screenshot = self.get_screenshot_as_png()
        try:
            location = element.location_once_scrolled_into_view
        except WebDriverException as error:
            # We should raise if element is not on page.
            if 'Element is not clickable' in str(error):
                raise
            logging.error('Failed to get location: %s. Fallback to full page screenshot.' % error)
            return screenshot
        try:
            from PIL import Image
        except ImportError:
            logging.warning('Pillow library is not installed. Fallback to full page screenshot.')
            return screenshot

        # Crop screenshot image to have element only.
        from io import BytesIO
        image = Image.open(BytesIO(screenshot))
        box = (location['x'] - offset, location['y'] - offset, location['x'] + size['width'] + offset,
               location['y'] + size['height'] + offset)
        region = image.crop(box)
        output = BytesIO()
        region.save(output, format='PNG')
        element_screenshot = output.getvalue()
        output.close()
        return element_screenshot

    def js_has_errors(self):
        """
        Check if there are any js errors in browser console.
        :return (bool): True if there are any.
        """
        # TODO: not finished.
        log = self.driver.get_log('browser')
        for record in log:
            return record.level == 'SEVERE'

    def get_browser_logs(self):
        log = self.driver.get_log('browser')
        return log

    def finish(self):
        """
        Just like quit() but also deletes all browser local data (cookies, local storage)
        :return: None
        """
        self.delete_all_local_variables()
        self.driver.delete_all_cookies()
        self.driver.quit()

    def delete_all_local_variables(self):
        self.execute_script('window.localStorage.clear();')

    def delete_local_variable(self, key):
        self.execute_script('window.localStorage.removeItem("%s");' % key)

    def set_cookies(self, cookies, domain):
        for cookie in cookies:
            try:
                self.set_cookie(cookie.key, cookie.value, domain)
            except Exception as error:
                logging.error('Failed to get set cookies. %s' % error)
                return False
        return True

    def set_cookie(self, name, value, domain=None):
        """
        Set cookie to webdriver.
        :return (Bool): True if success
        """
        cookie = {
            'name': name,
            'value': value,
            'domain': domain,
            # TODO: I don't set expiry because Firefox fails.
            # 'expiry': time.time() + 30 * 24 * 3600
        }
        self.driver.add_cookie(cookie)

    def wait(self, wait_time):
        time.sleep(wait_time)

    def set_local_storage_item(self, key, value):
        self.execute_script("window.localStorage.setItem('%s','%s');" % (key, value))

    def move_mouse(self, element):
        ActionChains(self.driver).move_to_element(element).perform()

    def click_element_as_action(self, element):
        ActionChains(self.driver).click(element).perform()

    def send_keys_as_action(self, element, keys_to_send):
        ActionChains(self.driver).click(element).send_keys(keys_to_send).perform()

    def drag_and_drop(self, draggable, target):
        # TODO: doesn't work.
        # ActionChains(self.driver).move_to_element(draggable).perform()
        # ActionChains(self.driver).double_click(draggable).perform()
        # self.driver.implicitly_wait(2)
        # ActionChains(self.driver).click_and_hold(draggable).perform()
        # self.driver.implicitly_wait(2)
        # ActionChains(self.driver).move_to_element_with_offset(target, -50, -50).perform()
        # self.driver.implicitly_wait(2)
        # ActionChains(self.driver).release().perform()
        # self.driver.implicitly_wait(2)
        # ActionChains(self.driver).release().perform()
        ActionChains(self.driver).drag_and_drop(draggable, target).perform()

    def switch_tab(self, window_handle: int):
        if window_handle < 0 or not isinstance(window_handle, int):
            raise ValueError('Wrong window_handle provided.')
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[window_handle])

    def wait_until_windows_open(self, windows_count, wait_time=5):
        self.driver_wait(self.driver, wait_time).until(lambda d: len(d.window_handles) == windows_count)

    def get_window_handles(self):

        return self.driver.window_handles

    def get_text_by_xpath(self, xpath):
        return self.driver.find_element_by_xpath(xpath).text

    def get_text_by_css(self, css):
        return self.driver.find_element_by_css_selector(css).text

    def is_elem_visible_by_css(self, css, wait_time=5):
        wait = self.driver_wait(self.driver, wait_time)
        wait.until(self.expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, css)))
        wait.until(self.expected_conditions.alert_is_present())
        return True

    def is_element_visible(self, path, wait_time=5):
        xpath = convert_css_to_xpath(path)
        wait = self.driver_wait(self.driver, wait_time)
        try:
            wait.until(self.expected_conditions.visibility_of_element_located((By.XPATH, xpath)))
        except TimeoutException:
            return False
        return True

    def is_element_exist(self, path, wait_time=5):
        try:
            self.wait_for_element(path, wait_time)
        except TimeoutException:
            return False
        return True

    def switch_to_frame(self, index=None):
        if index is None:
            self.driver.switch_to.default_content()
        else:
            self.driver.switch_to.frame(index)
        return True

    def switch_to_frame_by_src(self, iframe_src):
        iframes = self.wait_for_elements('iframe')
        for i in range(0, len(iframes)):
            src = iframes[i].get_attribute('src')
            if iframe_src in src:
                # TODO: Firefox really needs this? Better switch to ids.
                if self.browser == 'firefox':
                    i += 1
                self.switch_to_frame(i)
                return True
        return False

    def wait_for_element(self, path, wait_time=5):
        elements = self.wait_for_elements(path, wait_time)
        return elements[0]

    def wait_for_elements(self, path, wait_time=5) -> List[WebElement]:
        xpath = convert_css_to_xpath(path)
        try:
            return self.wait_for_elements_by_xpath(xpath, wait_time)
        except TimeoutException:
            raise TimeoutException('Failed to find element %s after %s seconds. Xpath: %s.' % (path, wait_time, xpath))

    def wait_while_element_visible(self, path, wait_time=5):
        xpath = convert_css_to_xpath(path)
        try:
            return self.wait_while_element_visible_by_xpath(xpath, wait_time)
        except TimeoutException:
            raise TimeoutException('Failed to find element %s after %s seconds. Xpath: %s.' % (path, wait_time, xpath))

    def select_option(self, selector, value):
        elem = self.wait_for_element(selector)
        select = Select(elem)
        select.select_by_visible_text(value)


def convert_css_to_xpath(css):
    try:
        xpath = HTMLTranslator().css_to_xpath(css, prefix='//')
        logging.info('"%s" converted to xpath "%s"' % (css, xpath))
        return xpath
    except Exception as error:
        raise Exception('Failed to convert "%s" to xpath. %s.' % (css, error))
