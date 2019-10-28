import os
import datetime
import RPi.GPIO as GPIO
from raspiutil.raspiutil import RaspiUtil
from raspiutil.util.util import Util

# TODO: get the sensor working

class MovementSensor(object):

    def __init__(self):
        self.current_dir = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        config = Util.read_config(self.current_dir + '/config.json')
        
        self.raspiutil = RaspiUtil()
        self.mailsender = self.raspiutil.create_mailsender()
        
        self.pin = config[0]['MovementSensor'][0]['PIN_SENSOR']
        # GPIO.setmode(GPIO.BOARD)
        # GPIO.setup(self.pin, GPIO.IN)

    def go(self):
        """ loops through the sensors task """

        while True:

            success = self.mailsender.send_mail('movement detected', 'Time: {0} '.format(datetime.datetime.now()))

            if(success == False):
                Util.write(self.current_dir, 'error while trying to send a notification e-mail')

    def take_photo(self):
        # TODO: impl camera 
        pass

