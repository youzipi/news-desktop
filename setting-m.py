# -*- coding: utf-8 -*-
import ConfigParser
import os 

config = ConfigParser.SafeConfigParser()
config.read("setting.ini")
sections = config.sections()
host = config.get("mysql","host")
print host
port = int(config.get("mysql","port"))
print port
print type(port)
database = config.get("mysql","database")
print database
print type(database)
username = config.get("mysql","username")
print username
print type(username)

password = config.get("mysql","password")
print password
print type(password)
dirpath = config.get("imgpath","dirpath")
print dirpath
dirpath=unicode(dirpath,"utf8")
print os.path.exists(dirpath)
print type(dirpath)