#!/usr/bin/python

try:
  import configparser
  Config = configparser.ConfigParser()
except ImportError:
  import ConfigParser
  Config = ConfigParser.ConfigParser()


Config.read('trailers.conf')


def ConfigSectionMap(section):
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1