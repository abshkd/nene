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

# This is a lazy module to start making some requests. It needs to be cleaned up and made into Request class.

import nene
import requests
import os
import simplejson as json
import urlparse
import pytz
from base64 import b64encode
from os import urandom
import hmac
import hashlib
from akamai.edgegrid import EdgeGridAuth

#migrate to edgedrid fork

class Request:

    def __init__(self,access_token,token,secret,service_hostname):
        self.access_token = access_token
        self.token = token
        self.secret = secret
        self.service_hostname = service_hostname

    def contruct_auth_headers(self):
        nonce = self.__generate_nonce()
        timestamp = self.__timestamp()
        header_keys = [('client-token', self.token),('access-token', self.access_token),('timestamp',timestamp), ('nonce' , nonce)]
        auth_header = "EG1-HMAC-SHA256 " + ';'.join([ "%s=%s" % h for h in header_keys]) + ';'
        return auth_header

    def connect_purge(self):
        url = 'https://'+nene.service_hostname + '.' +  nene.endpoints['ccu']['queues']
        params  = urlparse.urlparse(url)

    def __generate_nonce(self):
        return lambda length: filter(lambda s: s.isalpha(), b64encode(urandom(length * 2)))[:length]

    def __timestamp(self):
        return pytz.datetime.datetime.utcnow().strftime('%Y%m%dT%H%M%S%z')

    def base64_hmac_sha256(data, key):
        return b64encode(
            hmac.new(key.encode('utf8'), data.encode('utf8'), hashlib.sha256).digest()
                ).decode('utf8')

    def content_hash(self, data):
         return b64encode(hashlib.sha256(data.encode('utf8')).digest()).decode('utf8')

    def __sign_key(self,timestamp):
        return  self.base64_hmac_sha256(timestamp,self.secret)
