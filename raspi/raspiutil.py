import os, schedule, time
from .util.util import Util
from .rgb.rgbinterface import RGBInterface
from .sched.action import Action
from .sched.day import Day
from .sched.place import Place
from .sched.task import Task

class RaspiUtil(object):
    """ bundles all raspi utility-objects for central use """

    # constructor
    def __init__(self):
        self.current_dir = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        self.rgbinterface = self._create_RGBInterface()
        self.tasks = list()

        self.action_switch = {
            Action.LED_ON : self._change_led_off,
            Action.LED_OFF : self._change_led_on
        }

        schedule.run_all()

    def sched(self, action, time, days, places):
        
        if(action == None or time == None):
            return

        for place in places:
            for day in days:
                 self.add_job(action, time, place, day)

    # scheduling methods
    def add_job(self, action, time, place, day):
        """
        adds a new scheduled task/job
        """
        if(time == None):
            return

        weekday_switch = {
            Day.MONDAY : schedule.every().monday.at(str(time)).do(self.action_switch[action], place),
            Day.TUESDAY : schedule.every().tuesday.at(str(time)).do(self.action_switch[action], place),
            Day.WEDNESDAY : schedule.every().wednesday.at(str(time)).do(self.action_switch[action], place),
            Day.THURSDAY : schedule.every().thursday.at(str(time)).do(self.action_switch[action], place),
            Day.FRIDAY : schedule.every().friday.at(str(time)).do(self.action_switch[action], place),
            Day.SATURDAY : schedule.every().saturday.at(str(time)).do(self.action_switch[action], place),
            Day.SUNDAY : schedule.every().sunday.at(str(time)).do(self.action_switch[action], place)
        }

        job = weekday_switch[day]
        
        print(job)

        if job != None:
            self.tasks.append(Task(len(self.tasks) + 1, job, day, time, action, place))

    def remove_job(self, identifier):
        """
        removes a scheduled task/job based on given identifier
        """
        
        for task in self.tasks:
            if task.Identifier == identifier:
                schedule.cancel_job(task.Job)
                self.tasks.remove(task)

    def _parse_time_string(self, time_string):
        """
        parses the time string - format: 'eachday-boolean, weekday, time' ex: '012015', each monday at 20:15
        returns: boolean eachday, int weekday 1-7, time in xx:xx format
        """

        eachday = None
        weekday = None
        time = None
        if(len(time_string) == 6):
            eachday = bool(time_string[0] == "1")
            weekday = int(time_string[1])
            time = '{}:{}'.format(time_string[2:3], time_string[4:5])

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