

# class TestAddGroup(unittest.TestCase):
#     def setUp(self):
#         self.app = Application()

# def test_open_smth(app2):
#         app2.driver.get("https://www.google.com/")
#         app2.driver.find_element_by_id("lst-ib").send_keys("selenium")
#         app2.driver.find_element_by_css_selector("input[name='btnK']").click()
#         sleep(2)

def test_use_helper(app):
    app.session.open_home_page()
    app.session.login(username="admin", password="secret")




