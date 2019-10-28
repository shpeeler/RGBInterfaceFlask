import os
import json
import sys
import datetime

class Util(object):

    @staticmethod
    def read_config(path):
        content = None

        try:
            with open(path) as jsonFile:
                content = json.load(jsonFile)

        except IOError:
            print('error while trying to read the config file')
            
        return content

    @staticmethod
    def write_config(path, config):
        """ writes the new config to the given path """

        try:

            with open(path, "w") as config_file:
                json.dump(config, config_file)

        except IOError:
            print('error while trying to write the config file')

    @staticmethod
    def get_directorypath_by_name(path_name):
        """
        returns the modules base directory
        """

        directory = os.path.dirname(os.path.abspath(__file__))
        results = directory.split('\\')
        tail = results[-1].lower()

        while tail != path_name:
            directory = os.path.dirname(os.path.abspath(directory))
            results = directory.split('\\')
            tail = results[-1].lower()

        return directory

    @staticmethod
    def write(dir, message):
        """
        writes exception-messages in the log.txt file located in the modules base directory
        """

        logFile = dir + '/log.txt'

        with open(logFile, "a") as log:
            log.write(str('{0} | {1}\n').format(datetime.datetime.now(), message))