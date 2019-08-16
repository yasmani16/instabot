import time
import datetime
import DBUsers, Constants
import traceback
import random
from logger import logs


logger = logs()


def time_delay(delay):
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

def login(webdriver):
    #Open the instagram login page
    webdriver.get('https://www.instagram.com/accounts/login/')
    time_delay('SS')
    #Find username and password field and add input
    emailInput = webdriver.find_elements_by_css_selector('form input')[0]
    passwordInput = webdriver.find_elements_by_css_selector('form input')[1]
    emailInput.send_keys(Constants.INST_USER)
    logger.info("Writing Username")
    time_delay('SS')
    passwordInput.send_keys(Constants.INST_PASS)
    logger.info("Writing password")
    time_delay('SS')
    login_btn = webdriver.find_elements_by_css_selector('button')[2]
    # login_btn = webdriver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div/div/div/form/div[6]/button')
    print(login_btn.text)
    login_btn.click()
    logger.info("Clicking log in button")
    time_delay('SS')

def follow_people(webdriver):
    logger.info("Starting follow people function")
    #all the followed user
    prev_user_list = DBUsers.get_followed_users()
    logger.info("Grabed Users from DB")
    #a list to store newly followed users
    new_followed = []
    #counters
    followed = 0
    likes = 0
    time.sleep(5)
    #Iterate theough all the hashtags from the constants
    for hashtag in Constants.HASHTAGS:
        logger.info("Looking for hasgtags to follow")
        #Visit the hashtag
        webdriver.get('https://www.instagram.com/explore/tags/' + hashtag+ '/')
        logger.info("Looking up tag {}".format(hashtag))
        time_delay('SS')

        #Get the first post thumbnail and click on it
        first_thumbnail = webdriver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div')

        first_thumbnail.click()
        time.sleep(random.randint(2,5))

        likebut = webdriver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/section[2]/div/div/a')
        
        likebut.click()

        

        #get all the usernames in page
        allusernames = webdriver.find_elements_by_xpath("//a[@href]")
        for a in allusernames:
            print(a.get_attribute("href"))
        time.sleep(30)
        try:
            #iterate over the first 200 posts in the hashtag
            for x in range(1,20):
                t_start = datetime.datetime.now()
                #Get the poster's username
                username = webdriver.find_element_by_xpath('//*[@id="f30743eb9448574"]/div/a').text
                logger.info("Located Username {}".format(username))
                likes_over_limit = False
                try:
                    #get number of likes and compare it to the maximum number of likes to ignore post
                    likes = int(webdriver.find_element_by_xpath(
                        '/html/body/div[3]/div[2]/div/article/div[2]/section[2]/div/div/button/span').text)
                    logger.info("Username {} has {} likes".format(username, likes))
                    if likes > Constants.LIKES_LIMIT:
                        print("likes over {0}".format(Constants.LIKES_LIMIT))
                        likes_over_limit = True


                    print("Detected: {0}".format(username))
                    #If username isn't stored in the database and the likes are in the acceptable range
                    if username not in prev_user_list and not likes_over_limit:
                        #Don't press the button if the text doesn't say follow
                        logger.info("User is not Followed and is eligible to be followed")
                        if webdriver.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').text == 'Follow':
                            #Use DBUsers to add the new user to the database
                            DBUsers.add_user(username)
                            logger.info("{} has been added to added to DB")
                            #Click follow
                            webdriver.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').click()
                            followed += 1
                            logger.info("Followed {0}, #{1}".format(username, followed))
                            print("Followed: {0}, #{1}".format(username, followed))
                            new_followed.append(username)


                        # Liking the picture
                        button_like = webdriver.find_element_by_xpath(
                            '/html/body/div[3]/div[2]/div/article/div[2]/section[1]/span[1]/button')

                        button_like.click()
                        likes += 1
                        logger.info("Liked {0}'s post, #{1}".format(username, likes))
                        print("Liked {0}'s post, #{1}".format(username, likes))
                        time.sleep(random.randint(5, 18))


                    # Next picture
                    webdriver.find_element_by_link_text('Next').click()
                    webdriver.find_elements_by_xpath("//a[contains(text(), 'Next')]")[0].click()
                    webdriver.find_element_by_class('coreSpriteRightPaginationArrow').click()
                    webdriver.find_elements_by_css_selector('body > div._2dDPU.vCf6V > div.EfHg9 > div > div > a').click()
                    print()
                    time.sleep(random.randint(20, 30))
                    
                except:
                    traceback.print_exc()
                    logger.Error(traceback.print_exc)
                    continue
                t_end = datetime.datetime.now()

                #calculate elapsed time
                t_elapsed = t_end - t_start
                logger.info("This post took {0} seconds".format(t_elapsed.total_seconds()))
                print("This post took {0} seconds".format(t_elapsed.total_seconds()))


        except:
            traceback.print_exc()
            continue

        #add new list to old list
        for n in range(0, len(new_followed)):
            prev_user_list.append(new_followed[n])
        print('Liked {} photos.'.format(likes))
        logger.info('Liked {} photos.'.format(likes))
        logger.info('Followed {} new people.'.format(followed))
        print('Followed {} new people.'.format(followed))

def getNewUsers(webdriver):
    logger.info("Starting follow people function")
    #all the followed user
    prev_user_list = DBUsers.get_followed_users()
    logger.info("Grabed Users from DB")
    #a list to store newly followed users
    new_followed = []
    #counters
    followed = 0
    likes = 0
    time.sleep(5)
    hashtag = Constants.HASHTAGS
    logger.info("Looking for hasgtags to follow")
    #Visit the hashtag
    logger.info("Looking up tag {}".format(hashtag))
    time_delay('SS')
    for x in range(1,20):
        webdriver.get('https://www.instagram.com/explore/tags/' + hashtag+ '/')
        thumbnail = webdriver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[{}]/a/div'.format(x))

        thumbnail.click()
        time.sleep(random.randint(1,3))
        

def unfollow_people(webdriver, people):
    #if only one user, append in a list
    logger.info("Unfollow people has started")
    if not isinstance(people, (list,)):
        p = people
        people = []
        people.append(p)

    for user in people:
        try:
            webdriver.get('https://www.instagram.com/' + user + '/')
            time_delay('SS')
            unfollow_xpath = '//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/span/span[1]/button'

            unfollow_confirm_xpath = '/html/body/div[3]/div/div/div[3]/button[1]'

            if webdriver.find_element_by_xpath(unfollow_xpath).text == "Following":
                time.sleep(random.randint(4, 15))
                webdriver.find_element_by_xpath(unfollow_xpath).click()
                time_delay('SS')
                webdriver.find_element_by_xpath(unfollow_confirm_xpath).click()
                time.sleep(4)
            DBUsers.delete_user(user)

        except Exception:
            traceback.print_exc()