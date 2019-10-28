from colors import Colors
import pigpio

class RGBController(object):
    """ holds methods for working with a single rgb stripe set """

    # constructor
    def __init__(self, position, config):
        self.position = position
        self.config = config
        self.switch =   {
                            Colors.Red : self._change_red,
                            Colors.Green : self._change_green, 
                            Colors.Blue : self._change_blue
                        }
        self.pi = pigpio.pi()

    # public methods
    def change_color(self, color, value, lightness):
        """ changes the values of a specific color """

        if(not self.pi.connected):
            return

        self.switch[color](value, lightness)
    
    def toggle_state(self, state):
        """ changes the state to either on or off depending on current state"""
        self.pi = pigpio.pi()

        # if(state == 0):
        #     if(not self.p.connected):
        #         return

        
        # if(state == 1):
        #     if(self.pi.connected):
        #         return


    def get_pins(self):
        """ returns the controllers pins in the order r, g, b """

        r = self.config['pin_pot_r']
        g = self.config['pin_pot_g']
        b = self.config['pin_pot_b']

        return (r, g, b)

    # private methods
    def _change_red(self, value, brightness):
        """ changes the stripes r ration and brightness """
        
        pin = int(self.config['pin_r'])

        if(value >= 0 and value <= 255): 
            real_value = int(int(value) * (float(brightness) / 255.0))
            self.pi.set_PWM_dutycycle(pin, real_value)

    def _change_green(self, value, brightness):
        """ changes the stripes g ration and brightness """

        pin = int(self.config['pin_g'])

        if(value >= 0 and value <= 255):
            real_value = int(int(value) * (float(brightness) / 255.0))
            self.pi.set_PWM_dutycycle(pin, real_value)
        
    def _change_blue(self, value, brightness):
        """ changes the stripes b ration and brightness """

        pin = int(self.config['pin_b'])

        if(value >= 0 and value <= 255):
            real_value = int(int(value) * (float(brightness) / 255.0))
            self.pi.set_PWM_dutycycle(pin, real_value) 