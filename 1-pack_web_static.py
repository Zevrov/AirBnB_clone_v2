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
                os.mkdir("versions")
        time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        packed = 'versions/web_static_' + time + '.tgz'
        fabric.api.local("tar -cvzf {} web_static".format(packed))
        return packed
    except:
        return None
