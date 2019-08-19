#!/usr/bin/python3
"""destribute an archive to a web server"""

import fabric.api
import os
import os.path
import datetime
fabric.api.env.hosts = ['34.73.58.99', '35.231.152.200']


def do_deploy(archive_path):
    """deploy an archive from the archive_path"""
    if os.path.exists(archive_path) is False:
        return False

    try:
        file_name = os.path.splitext(os.path.split(archive_path)[1])[0]
        target = '/data/web_static/releases/' + file_name
        path = fabric.api.put(archive_path, '/tmp/' + file_name)
        path = path[0]
        fabric.api.run('mkdir -p ' + target)
        fabric.api.run('tar -xzf ' + path + ' -C ' + target)
        fabric.api.run('rm ' + path)
        fabric.api.run('mv ' + target + '/web_static/* ' + target + '/')
        fabric.api.run('rm -rf ' + target + '/web_static')
        fabric.api.run('rm -rf /data/web_static/current')
        fabric.api.run('ln -s ' + target + '/ /data/web_static/current')
        print('deploy success')
        return True
    except:
        return False
