#!/usr/bin/python3
""" using fabric and create a tar file .tgz
"""
from datetime import datetime
from fabric.api import *
import os
import shlex

env.hosts = ['35.227.82.74', '35.231.166.249']
env.user = 'ubuntu'


def do_clean(number=0):
    if os.path.exists('versions'):
        if int(number) == 0:
            variable = 2
        else:
            variable = int(number) + 1
        command = 'tail -n +{}| xargs rm -rf'.format(variable)
        local('cd versions ; ls -t|{}'.format(command))
        dir = '/data/web_static/releases'
        run('cd {}; ls -t| grep web_static|{}'.format(dir, command))
