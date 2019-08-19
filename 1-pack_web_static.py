#!/usr/bin/python3
"""module pack up in tar format"""

import os
import os path
import datetime
import fabric.api


def do_pack():
    """compress + bundle local sweb files"""
    if isdir("versions") is False:
            local("mkdir versions")
    time =  datetime.now().strftime("%Y%m%d%H%M%S")
    file = "versions/web_static_{}.tgz".format(time)
    fabric.api.local('tar -cvzf ' + file + ' web_static')
    return target
