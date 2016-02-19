#!/usr/bin/env python
# Copyright (c) 2015 Abhishek Dujari  http://www.webmastersupport.com/
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish, dis-
# tribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the fol-
# lowing conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABIL-
# ITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
# SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

import platform
import os
import sys
import logging
import logging.config
from config.config import Config
import simplejson as json

__version__ = '0.1.0'
Version = __version__  # for backwaed compatibility


UserAgent = 'Nene/%s Python/%s %s/%s' % (
    __version__,
    platform.python_version(),
    platform.system(),
    platform.release()
)
EXISTING_ENDPOINTS_FILE = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    'nene', 'endpoints.json')


def load_endpoint_json(path):
    """
    Loads a given JSON file & returns it.
    :param path: The path to the JSON file
    :type path: string
    :returns: The loaded data
    """
    with open(path, 'r') as endpoints_file:
        return json.load(endpoints_file)

endpoints = load_endpoint_json(EXISTING_ENDPOINTS_FILE)

config = Config()
token = config.get('Client','Token')
secret = config.get('Client','Secret')
access_token = config.get('Client','Access-Token')
service_hostname = config.get('Client','Hostname')