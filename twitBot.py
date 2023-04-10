from selenium import webdriver

class twitBot(webdriver.Chrome):

    def __init__(self) -> None:
        webdriver.Chrome.__init__(self)
    
    def collectTweetWeb(self):
        pass

    def collectTweetCSV(self):
        pass