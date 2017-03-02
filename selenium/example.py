import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException

from pyvirtualdisplay import Display
from selenium import webdriver

class VotingApp(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.display = Display(visible=1, size=(1024, 768))


    def test_vote_in_voteapp(self):
        driver = self.driver
        driver.get("http://172.23.0.3")
        button = driver.find_element_by_id('a')
        button.click()
        driver.get("http://172.23.0.2")
        votes = driver.find_element_by_name('cats_results')
        assert not '100.0%' is votes.text

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
