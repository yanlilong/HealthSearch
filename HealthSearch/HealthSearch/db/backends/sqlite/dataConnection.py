__author__ = 'l94wang'
import sqlite3
from sqlite3 import Error
import os


def init_connection(db_file):
  print 'open a database connection'
  try:
    conn = sqlite3.connect(':memory:')
    conn = sqlite3.connect(db_file)
    # return conn
  except Error as e:
    print (e)
  return conn


def removeDatabase(path):
  try:
    if os.path.isfile(path):
      os.remove(path)
  except IOError, msg:
    print("sql script remove error", msg)


def execute_querywithparm(self, sql_command, paramters):
  print 'execute a sql query'

  try:
    self.cursor = self.conn.cursor()

    for row in self.cursor.execute(sql_command, paramters):
      print row
    self.conn.commit()
  except Error as self.e:
    print(self.e)


def execute_query(self, sql_command):
  result_tuple = ((),)
  try:
    self.cursor = self.conn.cursor()
    for row in self.cursor.execute(sql_command):
      print result_tuple.__add__(row)

  except Error as self.e:
    print(self.e)
  return result_tuple


def execute_query(self, sql_command):
  print 'execute a sql query'

  try:
    self.cursor = self.conn.cursor()

    for row in self.cursor.execute(sql_command):
      print row
    self.conn.commit()
  except Error as self.e:
    print(self.e)


def close_conection(cursor, conn):
  print 'close a database connection'
  try:
    if cursor:
      cursor.close()
    if conn:
      conn.close()

  except Error as e:
    print (e)
