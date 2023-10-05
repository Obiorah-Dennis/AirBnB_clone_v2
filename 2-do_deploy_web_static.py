#!/usr/bin/python3
""" using fabric and create a tar file .tgz
"""
from datetime import datetime
from fabric.api import *
import os
import shlex

env.hosts = ['35.227.82.74', '35.231.166.249']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """ send and run commands in a server
    """
    if not os.path.exists(archive_path):
        return (False)
    try:
        # getting just name with .tgz
        name_ext = archive_path.replace('/', ' ')
        name_ext = shlex.split(name_ext)
        name_ext = name_ext[-1]
        # gettin just name without extension
        name = name_ext.replace('.', ' ')
        name = shlex.split(name)
        name = name[0]
        # varible of directory
        dir = "/data/web_static/releases/"
        # instructions
        put(archive_path, "/tmp/")
        run("mkdir -p {}{}/".format(dir, name))
        run("tar -xzf /tmp/{} -C {}{}/".format(name_ext, dir, name))
        run("rm /tmp/{}".format(name_ext))
        run("mv {}{}/web_static/* {}{}/".format(dir, name, dir, name))
        run("rm -rf {}{}/web_static".format(dir, name))
        run("rm -rf /data/web_static/current")
        run("ln -s {}{}/ /data/web_static/current".format(dir, name))
        print("New version deployed!")
        return (True)
    except:
        return (False)
