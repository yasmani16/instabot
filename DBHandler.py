import mysql.connector
import Constants

class DBhandler:
  def __init__(self):
    DBhandler.HOST = Constants.HOST
    DBhandler.USER = Constants.USER
    DBhandler.DBNAME = Constants.DATABASE
    DBhandler.PASSWORD = Constants.PASS
  HOST= Constants.HOST
  USER= Constants.USER
  DBNAME= Constants.DATABASE
  PASSWORD = Constants.PASS

  @staticmethod
  def get_mydb():
    if DBhandler.DBNAME == '':
      Constants.init()
    db =DBhandler()
    mydb = db.connect()
    return mydb
  def connect(self):
    mydb = mysql.connector.connect(
      host=DBhandler.HOST,
      user=DBhandler.USER,
      passwd=DBhandler.PASSWORD,
      database=DBhandler.DBNAME
    )
    return mydb