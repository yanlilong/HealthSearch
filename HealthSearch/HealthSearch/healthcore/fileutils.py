__author__ = 'l94wang'
import os


#delete file
def removeDatabase(path):
  try:
    if os.path.isfile(path):
      os.remove(path)
  except IOError, msg:
    print("delete"+path+"error", msg)
