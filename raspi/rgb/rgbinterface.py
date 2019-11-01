import time, os, serial
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
        baudrate = self.config[str(position)]["baudrate"]

        with serial.Serial(addr, baudrate) as ser:
            if ser.isOpen():
                time.sleep(3)
                ser.write(msg)
            else:
                Util.write("serial communication could not be established", MsgType.ERROR)

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

        enc_msg = msg.encode()
        addr = self.config[str(position)]["addr"]
        baudrate = self.config[str(position)]["baudrate"]

        with serial.Serial(addr, baudrate) as ser:
            if ser.isOpen():
                time.sleep(3)
                ser.write(enc_msg)
            else:
                Util.write("serial communication could not be established", MsgType.ERROR)

    def _convert_values_to_msg(self, r, g, b, l):
        """ converts the given values r, g, b, l to a message for serial writing """

        ret_r = self._convert_value_to_string(r, l)
        ret_g = self._convert_value_to_string(g, l)
        ret_b = self._convert_value_to_string(b, l)

        result = '{}{}{}\n'.format(ret_r, ret_g, ret_b)
        enc_result = result.encode()

        return enc_result

    def _convert_value_to_string(self, color, brightness):
        """ converts the given color and brightness to its real value and returns it as a string """

        if color == None:
            color = 0

        if brightness == None:
            brightness = 0

        real_color = int(int(color) * (float(brightness) / 255.0))
        string_color = str(real_color).zfill(3)

        return string_color
