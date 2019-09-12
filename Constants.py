import json
from tags import tags
from logger import logs
INST_USER= INST_PASS= USER= PASS= HOST= DATABASE= POST_COMMENTS = ''
LIKES_LIMIT=DAYS_TO_UNFOLLOW=CHECK_FOLLOWERS_=0
HASHTAGS = ""

def init():
  global INST_USER, INST_PASS, USER, PASS,HOST,DATABASE,LIKES_LIMIT, DAYS_TO_UNFOLLOW, DAYS_TO_UNFOLLOW, CHECK_FOLLOWERS, HASHTAGS
  # Read Files
  data = None
  with open('settings.json', 'r') as myfile:
    data= myfile.read()
  obj = json.loads(data)
  INST_USER=obj['igcredDappered']['username']
  INST_PASS=obj['igcredDappered']['password']
  USER = obj['db']['user']
  HOST = obj['db']['host']
  PASS = obj['db']['pass']
  DATABASE = obj['db']['database']
  LIKES_LIMIT = obj['config']['likes_over']
  CHECK_FOLLOWERS = obj['config']['check_followers']
  HASHTAGS = ["followforfollowback"]
  DAYS_TO_UNFOLLOW = obj['config']['days_to_unfollow']
