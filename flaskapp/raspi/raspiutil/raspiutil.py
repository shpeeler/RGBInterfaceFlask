import io
import json
import os
from .mail.mailsender import MailSender
from .rgb.rgbcontroller import RGBController
from .util.util import Util

class RaspiUtil(object):
    """ bundles all raspi utility-objects for central use """

    # constructor
    def __init__(self):
        self.current_dir = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        self.raspi_util_config = Util.read_config(self.current_dir + '/config.json')

    # MailSender methods
    def create_mailsender(self):
        """ creates a MailSender object | returns: MailSender """

        config = Util.read_config(self.current_dir + self.raspi_util_config['msConfigPath'])
        return MailSender(config['user'], config['pw'], config['toAddr'], config['toCc'])


    # RGBController methods
    def create_rgbcontroller(self, position):
        """ creates a RGBController object | returns: Dict<position, RGBController> """

        fullconfig = Util.read_config(self.current_dir + self.raspi_util_config['rgbConfigPath'])
        config = fullconfig[str(position)]

        return RGBController(position, config)