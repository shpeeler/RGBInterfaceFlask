import os
from .util.util import Util
from .rgb.rgbinterface import RGBInterface
from .sched.action import Action

class RaspiUtil(object):
    """ bundles all raspi utility-objects for central use """

    # constructor
    def __init__(self):
        self.current_dir = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        self.rgbinterface = self._create_RGBInterface()

        self.action_switch = {
            Action.LED_ON : self._change_led_off,
            Action.LED_OFF : self._change_led_on
        }

    # scheduler
    def sched(self, position, time_string, action):

        (eachday, weekday, time) = self._parse_time_string(time_string)

        if(eachday == True):
            pass
            # schedule.every().day.at(time).do(self.action_switch[action](position))
        
        if(weekday != None):
            day = int(weekday)

            if(time == None):
                return

            weekday_switch = {
                # 1: lambda : schedule.every().monday.at(time).do(self.action_switch[action](position)),
                # 2: lambda : schedule.every().tuesday.at(time).do(self.action_switch[action](position)),
                # 3: lambda : schedule.every().wednesday.at(time).do(self.action_switch[action](position)),
                # 4: lambda : schedule.every().thurday.at(time).do(self.action_switch[action](position)),
                # 5: lambda : schedule.every().friday.at(time).do(self.action_switch[action](position)),
                # 6: lambda : schedule.every().saturday.at(time).do(self.action_switch[action](position)),
                # 7: lambda : schedule.every().sunday.at(time).do(self.action_switch[action](position))
            }

            weekday_switch[day]

    def _parse_time_string(self, time_string):
        """
        parses the time string - format: 'eachday-boolean, weekday, time' ex: '012015', each monday at 20:15
        returns: boolean eachday, int weekday 1-7, time in xx:xx format
        """

        eachday = None
        weekday = None
        time = None
        if(len(time_string) == 6):
            eachday = time_string[0]
            weekday = int(time_string[1])
            time = '{}:{}'.format(time_string[2:3], time_string[4:5])

            if (eachday == "0"):
                eachday = False
            elif(eachday == "1"):
                eachday = True 

        return (eachday, weekday, time)

    # module methods
    def _change_led_off(self, position):
        self.rgbinterface.send_state(position, 'O')

    def _change_led_on(self, position):
        self.rgbinterface.send_state(position, 'I')

    # init methods
    def get_rgbinterface(self):
        return self.rgbinterface

    def _create_RGBInterface(self):
        """ creates a new instance of RGBInterface """

        config = Util.read_config(self.current_dir + '/rgb/config.json')
        return RGBInterface(config)