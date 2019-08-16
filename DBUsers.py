import datetime, TimeHelper
from DBHandler import *
import Constants

#delete user by username
def delete_user(username):
  mydb = DBhandler.get_mydb()
  cursor = mydb.cursor()
  sql = "DELETE FROM FollowedUsers Where username = '{0}'".format(username)
  cursor.execute(sql)
  mydb.commit()

#add new user
def add_user(username):
  mydb = DBhandler.get_mydb()
  cursor = mydb.cursor()
  now = datetime.datetime.now().date()
  sql = "INSERT INTO FollowedUsers (Username,Dated_added) VALUES {}{}".format(username, now)
  cursor.execute(sql)
  mydb.commit()

#check if any user qualifies to be unfollowed
def check_unfollow_list():
  mydb = DBhandler.get_mydb()
  cursor = mydb.cursor()
  sql = "SELECT * FROM FollowedUsers"
  cursor.execute(sql)
  results = cursor.fetchall()
  users_to_unfollow = []
  for r in results:
    d = TimeHelper.days_since_date(r[1])
    if d > Constants.DAYS_TO_UNFOLLOW:
      users_to_unfollow.append(r[0])
  return users_to_unfollow

#get all followed users
def get_followed_users():
  users =[]
  mydb = DBhandler.get_mydb()
  cursor = mydb.cursor()
  sql = "SELECT * FROM FollowedUsers"
  cursor.execute(sql)
  results = cursor.fetchall()
  for r in results:
    users.append(r[0])
  
  return users