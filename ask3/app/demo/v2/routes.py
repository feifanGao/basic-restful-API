# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.weather import Weather


routes = [
    dict(resource=Weather, urls=['/weather'], endpoint='weather'),
]