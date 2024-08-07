import time, subprocess, requests
from .state import State
from ..util.util import Util
from ..util.msgtype import MsgType

class RGBInterface(object):

    def __init__(self, config):
        self.config = config

    def send_values(self, position, r, g, b, l):
        """ sends the given values to the serial port saved in position """
        
        msg = self._convert_values_to_msg(r, g, b, l)
        addr = self.config[str(position)]["addr"]

        api_endpoint = "http://{}:80/rgb".format(addr).rstrip()

        data = {
            "color": msg
        }

        try:
            response = requests.post(api_endpoint, json=data)
        except requests.ConnectionError as error:
            print("Failed to connect to the ESP8266. Address: '{}' Message: '{}' Error: {}".format(api_endpoint, msg, error))

        print(response)

    def send_state(self, position, state):
        """ sends the state to the port saved in position """

        msg = None
        if(state == State.ON):
            msg = "I"
        else:
            msg = "O"

        if(msg == None):
            Util.write("invalid state: {}".format(state) ,MsgType.ERROR)
            return

        addr = self.config[str(position)]["addr"]
        
        cmd = 'curl {}/State={}'.format(addr, state)
        subprocess.call(cmd)

    def _convert_values_to_msg(self, r, g, b, l):
        """ converts the given values r, g, b, l to a message for serial writing """

        ret_r = self._convert_value_to_string(r, l)
        ret_g = self._convert_value_to_string(g, l)
        ret_b = self._convert_value_to_string(b, l)

        result = '{}{}{}'.format(ret_r, ret_g, ret_b)

        return result

    def _convert_value_to_string(self, color, brightness):
        """ converts the given color and brightness to its real value and returns it as a string """

        if color == None:
            color = 0

        if brightness == None:
            brightness = 0

        real_color = int(int(color) * (float(brightness) / 255.0))
        string_color = str(real_color).zfill(3)

        return string_color
