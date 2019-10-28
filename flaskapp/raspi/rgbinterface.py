import time, os
from raspiutil.raspiutil import RaspiUtil
from raspiutil.util.util import Util
from raspiutil.rgb.colors import Colors

class RGBInterface(object):

    def __init__(self):
        self.current_dir = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        self.config = Util.read_config(self.current_dir + '/config.json')

        self.raspiutil = RaspiUtil()
        self.controllers = []
        self.create_controller(0)
        self.init_controller(0)

    def create_controller(self, position):
        """ creates a controller and adds it to the controller dictionary """

        rgbcontroller = self.raspiutil.create_rgbcontroller(position)
        self.controllers.insert(int(position), rgbcontroller)

    def update_colors(self, r, g, b, l, p):
        """ loops through the interfaces task """

        self.controllers[int(p)].change_color(Colors.Blue, int(b), int(l))
        self.controllers[int(p)].change_color(Colors.Red, int(r), int(l))
        self.controllers[int(p)].change_color(Colors.Green, int(g), int(l))

    def toggle_state(self, position, state):
        """ changes a rgb controllers state """

        self.controllers[int(position)].toggle_state(state)

    def init_controller(self, position):
        """ initializes a rgb controller with the most recent config settings """

        rgbl = self.config['RGBInterface'][str(position)]
        
        r = int(rgbl['r'])
        g = int(rgbl['g'])
        b = int(rgbl['b'])
        l = int(rgbl['lightness'])

        self.controllers[position].change_color(Colors.Blue, b, l)
        self.controllers[position].change_color(Colors.Red, r, l)
        self.controllers[position].change_color(Colors.Green, g, l)
