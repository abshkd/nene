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

import os
from ConfigParser import SafeConfigParser as ConfigParser
import re
# try windows/usnix locations
UserConfigPath = os.path.join(os.path.expanduser('~'),'.nene')
NeneConfigLocations = [UserConfigPath]

if 'NENE_CONFIG' in os.environ:
    NeneConfigLocations = [os.path.expanduser(os.environ['NENE_CONFIG'])]


#To overload ConfigParser

class Config(ConfigParser):

    def __init__(self,path=None,fp=None,do_load=True):
        ConfigParser.__init__(self, {'debug' : 0})

        if do_load:
            if path:
                self.load_from_path(path)
            elif fp:
                self.readfp(fp)
            else:
                self.read(NeneConfigLocations)

    def load_from_path(self, path):
        file = open(path)
        for line in file.readlines():
            match = re.match("^#import[\s\t]*([^\s^\t]*)[\s\t]*$", line)
            if match:
                extended_file = match.group(1)
                (dir, file) = os.path.split(path)
                self.load_from_path(os.path.join(dir, extended_file))
        self.read(path)

    def get(self, section, name, default=None):
        try:
            val = ConfigParser.get(self, section, name)
        except:
            val = default
        return val