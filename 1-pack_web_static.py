#!/usr/bin/python3
""" fabric script to create an archive of our webstatic directory 
of my AirBnB webstatic directory 
"""


from fabric.api import *
import time

def do_pack():
    time_str = time.strftime("%Y%m%d%H%M%S")

    try:
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}.tgz web_static/".format
              (time_str))
        return("versions/web_static_{}".format(time_str))
    except:
        return None
