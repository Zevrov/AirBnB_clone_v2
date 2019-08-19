#!/usr/bin/python3
"""module pack up in tar format"""

import os
import os.path
import datetime
import fabric.api


def do_pack():
    """compress + bundle local sweb files"""
    try:
        if os.path.isdir("versions") is False:
                fabric.apilocal("mkdir versions")
        time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        file = "versions/web_static_{}.tgz".format(time)
        fabric.api.local("tar -cvzf {} web_static".format(file_name))
        return file
    except:
        return None
