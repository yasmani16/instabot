from selenium import webdriver
import BotEngine
from selenium.webdriver.chrome.options import Options
opts = Options()
opts.add_argument("user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_2 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11A501 Safari/9537.53")


chromedriver_path = '/Users/ross/Programming/Python/Igbot/IgBot/instabot/chromedriver'
webdriver = webdriver.Chrome(chrome_options=opts, executable_path=chromedriver_path)
webdriver.set_window_size(414, 736)
BotEngine.init(webdriver)
BotEngine.update(webdriver)

webdriver.close()