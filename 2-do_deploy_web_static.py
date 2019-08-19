#!/usr/bin/python3
"""destribute an archive to a web server"""

import fabric.api
import os
import os.path
import datetime
fabric.api.env.hosts = ['34.73.58.99', '34.74.6.218']


def do_deploy(archive_path):
    """deploy an archive from the archive_path"""
    if os.path.exists(archive_path) is False:
        return False

path = archive_path.split('/')[1]
target = '/data/web_static/releases/' + path

    try:
        fabric.api.put(archive_path, "/tmp/")
        fabric.api.run('sudo mkdir -p ' + target + '/')
        fabric.api.run('sudo tar -xzf /tmp/' + path + ' -C ' + target + '/')
        fabric.api.run('sudo rm /tmp/' + path)
        fabric.api.run('sudo mv ' + target + '/web_static/* ' + target + '/')
        fabric.api.run('sudo rm -rf ' + target + '/web_static')
        fabric.api.run('sudo rm -rf /data/web_static/current')
        fabric.api.run('sudo ln -s ' + target + ' /data/web_static/current')
        print('deploy success')
        return True
    except:
        return False
