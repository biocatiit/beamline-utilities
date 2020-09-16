from __future__ import absolute_import, division, print_function, unicode_literals
from builtins import object, range, map
from io import open

import logging
import sys
import time

logger = logging.getLogger(__name__)

import serial
import serial.tools.list_ports as list_ports
import wx

class SerialComm():
    """
    This class impliments a generic serial communication setup. The goal is
    to provide a lightweight wrapper around a pyserial Serial device to make sure
    ports are properly opened and closed whenever used.
    """
    def __init__(self, port=None, baudrate=9600, bytesize=serial.EIGHTBITS,
        parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout=1,
        xonxoff=False, rtscts=False, write_timeout=None, dsrdtr=False,
        inter_byte_timeout=None, exclusive=None):
        """
        Parameters are all of those accepted by a
        `pyserial.Serial <https://pyserial.readthedocs.io/en/latest/pyserial_api.html#serial.Serial>`_
        device, defaults are set to those default values.
        """
        self.ser = None

        logger.info("Attempting to connect to serial device on port %s", port)

        try:
            self.ser = serial.Serial(port, baudrate, bytesize, parity, stopbits, timeout,
                xonxoff, rtscts, write_timeout, dsrdtr, inter_byte_timeout, exclusive)
            logger.info("Connected to serial device on port %s", port)
        except ValueError:
            logger.exception("Failed to connect to serial device on port %s", port)
        except serial.SerialException:
            logger.exception("Failed to connect to serial device on port %s", port)
        finally:
            if self.ser is not None:
                self.ser.close()

    def __repr__(self):
        return self.ser

    def __str__(self):
        return print(self.ser)

    def read(self, size=1):
        """
        This wraps the Serial.read() function for reading in a specified
        number of bytes. It automatically decodes the return value.

        :param size: Number of bytes to read.
        :type size: int

        :returns: The ascii (decoded) value of the ``Serial.read()``
        :rtype: str
        """
        with self.ser as s:
            ret = s.read(size)

        logger.debug("Read %i bytes from serial device on port %s", size, self.ser.port)
        logger.debug("Serial device on port %s returned %s", self.ser.port, ret.decode())

        return ret.decode()

    def read_all(self):
        """
        This wraps the Serial.read() function, and returns all of the
        waiting bytes.

        :returns: The ascii (decoded) value of the ``Serial.read()``
        :rtype: str
        """
        with self.ser as s:
            ret = s.read(s.in_waiting())

        logger.debug("Read all waiting bytes from serial device on port %s", self.ser.port)
        logger.debug("Serial device on port %s returned %s", self.ser.port, ret.decode())

        return ret.decode()

    def write(self, data, get_response=False, term_char='>'):
        """
        This warps the Serial.write() function. It encodes the input
        data if necessary. It can return any expected response from the
        controller.

        :param data: Data to be written to the serial device.
        :type data: str, bytes

        :param term_char: The terminal character expected in a response
        :type term_char: str

        :returns: The requested response, or an empty string
        :rtype: str
        """
        logger.debug("Sending '%s' to serial device on port %s", data, self.ser.port)
        if isinstance(data, str):
            if not data.endswith('\r\n'):
                data += '\r\n'
            data = data.encode()

        out = ''
        try:
            with self.ser as s:
                s.write(data)
                if get_response:
                    out = s.read_until('\n')
                    out.decode('ascii')
        except ValueError:
            logger.exception("Failed to write '%s' to serial device on port %s", data, self.ser.port)

        logger.debug("Recived '%s' after writing to serial device on port %s", out, self.ser.port)

        return out


class SerialFrame(wx.Frame):

    def __init__(self, baudrate=9600, bytesize=serial.EIGHTBITS,
        parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, rtscts=True,
        term_char='>', *args, **kwargs):
        super(SerialFrame, self).__init__(*args, **kwargs)

        self.baudrate = baudrate
        self.bytesize = bytesize
        self.parity = parity
        self.stopbits = stopbits
        self.rtscts=True
        self.term_char = term_char

        self._get_ports()

        self._create_layout()


    def _create_layout(self):
        panel = wx.Panel(self)

        self.com_ctrl = wx.Choice(panel, choices=self.ports, style=wx.CB_SORT)
        self.com_ctrl.Bind(wx.EVT_CHOICE, self._on_portchoice)

        port_sizer = wx.BoxSizer(wx.HORIZONTAL)
        port_sizer.Add(wx.StaticText(panel, label='Select COM Port:'))
        port_sizer.Add(self.com_ctrl, border=5, flag=wx.LEFT)

        self.command =wx.TextCtrl(panel)
        self.send_cmd = wx.Button(panel, label='Send Command')
        self.send_cmd.Bind(wx.EVT_BUTTON, self._send_cmd)
        self.send_cmd.Disable()


        cmd_sizer = wx.BoxSizer(wx.HORIZONTAL)
        cmd_sizer.Add(self.command, 1, flag=wx.EXPAND)
        cmd_sizer.Add(self.send_cmd, border=5, flag=wx.LEFT)

        self.response = wx.TextCtrl(panel, style=wx.TE_READONLY|wx.TE_MULTILINE)

        response_sizer = wx.BoxSizer(wx.VERTICAL)
        response_sizer.Add(wx.StaticText(panel, label='Response:'), flag=wx.EXPAND)
        response_sizer.Add(self.response, 1, flag=wx.EXPAND)


        panel_sizer = wx.BoxSizer(wx.VERTICAL)
        panel_sizer.Add(port_sizer, flag=wx.EXPAND)
        panel_sizer.Add(cmd_sizer, border=20, flag=wx.EXPAND|wx.TOP)
        panel_sizer.Add(response_sizer, 1, border=20, flag=wx.EXPAND|wx.TOP)

        panel.SetSizer(panel_sizer)

        top_sizer = wx.BoxSizer(wx.VERTICAL)
        top_sizer.Add(panel, 1, border=5, flag=wx.EXPAND|wx.ALL)

        self.SetSizer(top_sizer)


    def _get_ports(self):
        """
        Gets a list of active comports.

        .. note:: This doesn't update after the program is opened, so you need
            to start the program after all pumps are connected to the computer.
        """
        port_info = list_ports.comports()
        self.ports = [port.device for port in port_info]

        logger.debug('Found the following comports for the SerialFrame: %s', ' '.join(self.ports))

    def _on_portchoice(self, evt):
        self.serial_device = SerialComm(port=self.com_ctrl.GetStringSelection(),
            baudrate=self.baudrate, bytesize=self.bytesize, parity=self.parity,
            stopbits=self.stopbits, rtscts=self.rtscts)

        self.com_ctrl.Disable()
        self.send_cmd.Enable()

    def _send_cmd(self, evt):
        out = self.serial_device.write(self.command.GetValue(),
            get_response=True, term_char=self.term_char)

        self.response.SetValue(out)


if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    h1 = logging.StreamHandler(sys.stdout)
    h1.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(threadName)s - %(levelname)s - %(message)s')
    h1.setFormatter(formatter)
    logger.addHandler(h1)

    app = wx.App()
    logger.debug('Setting up wx app')
    frame = SerialFrame(baudrate=19200, bytesize=serial.EIGHTBITS,
        parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, rtscts=True,
        term_char='\r\n', parent=None,title='Serial Control')
    frame.Show()
    app.MainLoop()


