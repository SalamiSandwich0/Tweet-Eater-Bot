from selenium import webdriver

class twitBot(webdriver.Chrome):

    def __init__(self, driver:str):
        super(twitBot, self).__init__(executable_path=driver)
        #self.browser = webdriver.Chrome('./chrome-win/chrome.exe')

    def collectTweetWeb(self):
        pass

    def collectTweetCSV(self):
        pass
