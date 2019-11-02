import os, json, sys, datetime
from .msgtype import MsgType

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
    def write(message, msgtype, dir_name='flsk'):
        """
        writes exception-messages in the log.txt file located in the modules base directory
        """

        directory = Util.get_directorypath_by_name(dir_name)
        msgtype_string = Util._convert_msgtype(msgtype)

        logFile = directory + '/log.txt'
        with open(logFile, "a") as log:
            log.write(str('{0} | {1}: {2}\n').format(datetime.datetime.now(), msgtype_string, message))

    @staticmethod
    def _convert_msgtype(msgtype):
        switch = {
            0: "INFO",
            1: "ERROR",
            2: "TRACE"
        }

        return switch.get(msgtype)