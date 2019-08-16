import AccountAgent, DBUsers
import Constants
import datetime
from logger import logs


logger = logs()

def init(webdriver):
  Constants.init()
  logger.info("Initializing Constants")
  logger.info("Starting login")
  AccountAgent.login(webdriver)
  

def update(webdriver):
      #Get start of time to calculate elapsed time later
    start = datetime.datetime.now()
    #Before the loop, check if should unfollow anyone
    _check_follow_list(webdriver)
    while True:
        #Start following operation
        AccountAgent.follow_people(webdriver)
        #Get the time at the end
        end = datetime.datetime.now()
        #How much time has passed?
        elapsed = end - start
        #If greater than our constant to check on
        #followers, check on followers
        if elapsed.total_seconds() >= Constants.CHECK_FOLLOWERS:
            #reset the start variable to now
            start = datetime.datetime.now()
            #check on followers
            _check_follow_list(webdriver)


def _check_follow_list(webdriver):
    print("Checking for users to unfollow")
    #get the unfollow list
    users = DBUsers.check_unfollow_list()
    logger.info("Found {} users to unfollow".format(len(users)))
    print("Found {} users to unfollow".format(len(users)))
    #if there's anyone in the list, start unfollowing operation
    if len(users) > 0:
        logger.info("Starting Unfollow people function")
        AccountAgent.unfollow_people(webdriver, users)
        logger.info("Unfollow people function has completed")
    else:
      print(" No users found next step")
      logger.info("No User found")
      pass
