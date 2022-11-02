from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
import unittest




class NewVisitorTest(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        self.browser.implicitly_wait(3)  # wait 3 secs

    def tearDown(self) -> None:
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # get TO-DO list web
        self.browser.get("http://localhost:8000")

        # check TO-DO in web title
        self.assertIn("TO-DO",self.browser.title)
        self.fail("Finish the test!")

# user is invited to a TO-DO list

# add a new TO-DO item "buy a dress"

# when user press ENTER, web reload and show the TO-DO list
# 1. "buy a dress" -> a TO-DO item

# web show another text box to add a new TO-DO item
# user add "open the online-store"

# web reload, TO-DO list show two items

# web generate a unique url to get the data
# web shows some text to explain the url function

# User go to the url and get the TO-DO list
if __name__ == "__main__":
    unittest.main(warnings="ignore")
