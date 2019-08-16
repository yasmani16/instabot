import tags
import os

tag = tags.tags
mylist = list(dict.fromkeys(tag))
def removedp():
  """
  Removes dupes from Tags
  """
  f = open("tags.py","w") 
  f.write("tags = [ ")
  for i in mylist:
    f.write('"' + i + '",\n')

  f.truncate()
  f.truncate()
  f.write("]")
  f.close() 