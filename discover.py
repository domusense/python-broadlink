#!/usr/bin/python

import broadlink;

class discover():
 def __init__(self, timeout):
  self.devices = broadlink.discover(timeout)
  print("__init__")
