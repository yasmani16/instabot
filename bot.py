from Selenium import webdriver
import os
import time
import json
import random
import logging
from datetime import date
import removedupes


##setting up Logger##
currenttime = date.today()
LOG_FORMAT ="%(levelname)s %(asctime)s - %(message)s"
logname = "{}.log".format(currenttime)
subdir = "logging"
logfile = os.path.join(subdir, logname)
logging.basicConfig(
    filename= logfile, 
    level = logging.DEBUG,
    format = LOG_FORMAT
    )

logger=logging.getLogger()
class InstagramBot:
    logger.info("InstagramBot has started")
    def __init__(self, username, password):

        """
        Initializes am instance of the InstagramBot class.
        Calls the login method to authenticate a user with IG


        Args:
            username:str: The instagram username for a user
            password:str: The instagram password for a user

        Attributes:
            driver:Selenium.webdriver.Chrome: The Chromedriver that is used to automate browser actions

        """
        self.username = username
        self.password = password

        self.driver = webdriver.Chrome("/Users/ross/Programming/Python/Igbot/IGREDBot/chromedriver")

        self.base_url ='https://www.instagram.com/'

        self.login()
    def time_delay(self, delay):
        """
        Function to randomize the time sleep between actions. Takes in a variable named delay. Delay should equal SS =0-5 seconds,S for 1-60 seconds, M for 1 minute to 60, and H for one hour to 3 hours

        args:
        delay:str: SS S M H 
        """
        if delay == 'SS':
            num = random.randrange(0,5)
            logger.info("Time delay {}".format(num))
            time.sleep(num)
        if delay == 'S':
            num = random.randrange(1,60)
            logger.info("Time delay {}".format(num))
            time.sleep(num)
        if delay == 'M':
            num = random.randrange(60,3600,39)
            logger.info("Time delay {}".format(num))
            time.sleep(num)
        if delay == 'H':
            num = random.randrange(3600,10800,3000)
            logger.info("Time delay {}".format(num))
            time.sleep(num)

    def login(self):
        """
        This function logs in to IG with Selenium
        """
        logger.info("Logging into IG")
        self.driver.get('{}accounts/login/'.format(self.base_url))
        self.time_delay('SS')
        emailInput = self.driver.find_elements_by_css_selector('form input')[0]
        passwordInput = self.driver.find_elements_by_css_selector('form input')[1]
        emailInput.send_keys(self.username)
        logger.info("Writing Username")
        self.time_delay('SS')
        passwordInput.send_keys(self.password)
        logger.info("Writing password")
        self.time_delay('SS')
        login_btn = self.driver.find_elements_by_css_selector('button')[1]
        login_btn.click()
        logger.info("Clicking log in button")
        self.time_delay('SS')


    def nav_user(self, user):
        """
        Navigate to a User
        
        Arg:
            user:str: User to be being navigated to.
        """
        logger.info("Navigating to User '{}'".format(user))
        self.driver.get('{}{}'.format(self.base_url, user))

    def follow_user(self, user):

        """
        Follow a User
        
        Arg:
            user:str: User to be followed
        """
        logger.info("Following User '{}'".format(user))
        self.nav_user(user)
        self.time_delay('S')
        followButton= self.driver.find_elements_by_xpath("//button[contains(text(), 'Follow')]")[0]
        self.time_delay('SS')
        followButton.click()
        logger.info("Follow action complete")

    def unfollow_user(self, user):

        """
        Unfollow a User
        
        Arg:
            user:str: User to be unfollow
        """
        logger.info("UnFollowing User '{}'".format(user))
        self.nav_user(user)
        self.time_delay('S')
        unfollowButton= self.driver.find_elements_by_xpath("//button[contains(text(), 'Following')]")[0]
        self.time_delay('SS')
        unfollowButton.click()
        self.time_delay('SS')
        unfollowbut = self.driver.find_elements_by_xpath("//button[contains(text(), 'Unfollow')]")[0]
        self.time_delay('SS')
        unfollowbut.click()
        logger.info("Unfollow action complete")
    def updatetags(self):
        
        removedupes.removedp()


if __name__ == '__main__':
    def loadAccount(cred,json_file = "settings.json",json_key ="igcredDappered"):
        with open(json_file) as f:
            data = json.load(f)

            user_values = data[json_key]
            username = user_values['username'],
            password = user_values['password'],
            if cred == "username":
                uname= ''.join(username) 
                return uname
            elif cred== "password":
                pword= ''.join(password)
                return pword
            return uname +","+pword 
    ig_bot = InstagramBot(loadAccount(cred="username"), loadAccount(cred="password"))
    ig_bot.time_delay('SS')
    ig_bot.follow_user('j_d_won')
