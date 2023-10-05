#!/usr/bin/python3
""" using fabric and create a tar file .tgz
"""
from datetime import datetime
from fabric.api import *
import os


def do_pack():
    """ function that create a directory and a .tgz archive
    """
    try:
        if not os.path.exists("versions"):
            local("mkdir versions")
        date = datetime.now()
        date = date.strftime("%Y%m%d%H%M%S")
        name = "versions/web_static_" + date + '.tgz'
        local('tar -cvzf {} web_static'.format(name))
        return (name)
    except:
        return (None)
