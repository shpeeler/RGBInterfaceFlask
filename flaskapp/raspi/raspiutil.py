import os
from .util.util import Util
from .rgb.rgbinterface import RGBInterface

class RaspiUtil(object):
    """ bundles all raspi utility-objects for central use """

    # constructor
    def __init__(self):
        self.current_dir = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

    def create_RGBInterface(self):
        """ creates a new instance of RGBInterface """

        config = Util.read_config(self.current_dir + '/rgb/config.json')
        return RGBInterface(config)