from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options



# def throw_err_info (self, value):
#     if value is not None or 
options = Options()
options.add_argument("-profile")
options.add_argument("/home/abdessamadz/snap/firefox/common/.mozilla/firefox/g3l9pxya.bot_user")
options.set_preference('detach', True)

class ProviderClass():
    def __init__ (self, settings):
        #define algo-spec attributes
        self.webdriver = webdriver.Firefox(options=options)
        self.name = settings['name']
        self.url = settings['url']
        self.selectors  = settings['selectors']
    
    def search_for_args(self, args):
        self.webdriver.get(self.url)
        elm = self.webdriver.find_element(By.CSS_SELECTOR, self.selectors['search_box_selc'])
        elm.send_keys(args)
        btn = self.webdriver.find_element(By.CSS_SELECTOR, self.selectors['search_btn_selc'])
        btn.click()
        # self.webdriver.context()
        return self.webdriver.current_url
    def some_otherthings(self):
        pass
