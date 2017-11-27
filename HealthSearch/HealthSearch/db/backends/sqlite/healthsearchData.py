__author__ = 'l94wang'
import sqlite3
import os
import dataConnection
import HealthSearch.base.const as constant


# remove a file
def removeFile(path):
  try:
    if os.path.isfile(path):
      os.remove(path)
  except IOError, msg:
    print(constant.FILE_STRING + path + constant.REMOVE_ERRO, msg)


# read line by line of sql file
def readSQL(sqlFile, conn, cursor):
  sqlCommands = sqlFile.split(';')
  for command in sqlCommands:
    try:
      cursor.execute(command)
    except sqlite3.OperationalError, msg:
      print(constant.SKIP_SQL_FILE, msg)


removeFile(constant.DATABASE_NAME)
# open,read healthsearch sql file
healthdata = open(constant.HEALTH_SEARCH_SQL, 'r')
sqlFile = healthdata.read();
healthdata.close();

conn = dataConnection.init_connection(constant.DATABASE_NAME)
cursor = conn.cursor()
readSQL(sqlFile, conn, cursor)

dataConnection.close_conection(cursor, conn)



