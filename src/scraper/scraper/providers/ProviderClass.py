from selenium import webdriver
from selenium.webdriver.common.by import By

# def throw_err_info (self, value):
#     if value is not None or 
class ProviderClass():
    def __init__ (self, settings):
        #define algo-spec attributes
        self.webdriver = webdriver.Firefox()
        self.name = settings['name']
        self.url = settings['url']
        self.selectors  = settings['selectors']
    
    def search_for_args(self, args):
        self.webdriver.get(self.url)
        elm = self.webdriver.find_element(By.CSS_SELECTOR,self.selectors['search_box_selc'])
        elm.send_keys(args)
        btn = self.webdriver.find_element(By.CSS_SELECTOR,self.selectors['search_btn_selc'])
        btn.click()
        # self.webdriver.context()
        return self.webdriver.current_url
    def some_otherthings(self):
        pass
