#!/usr/bin/python3
"""destribute an archive to a web server"""

from fabric.api import *
import os
import os.path
import datetime
env.hosts = ['34.73.58.99', '34.74.6.218']


def do_deploy(archive_path):
    """deploy an archive from the archive_path"""
    if os.path.exists(archive_path) is False:
        return False

    file_name = os.path.splitext(os.path.split(archive_path)[1])[0]
    target = '/data/web_static/releases/' + file_name
    try:
        path = put(archive_path, '/tmp/' + file_name)
        path = path[0]
        run('sudo mkdir -p ' + target)
        run('sudo tar -xzf /tmp/' + file_name + ' -C ' + target + '/')
        run('sudo rm /tmp/' + path)
        run('sudo mv ' + target + '/web_static/* ' + target + '/')
        run('sudo rm -rf ' + target + '/web_static')
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s ' + target + '/ /data/web_static/current')
        print('deploy success')
        return True
    except:
        return False
