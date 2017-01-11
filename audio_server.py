#!/usr/bin/env python
# -*- coding: utf-8 -*-


import socket
#  from pyaudio import PyAudio, paInt16


class Audio():

    """Docstring for Audio. """

    def __init__(self):
        """TODO: to be defined1. """
        #  PyAudio.__init__(self)
        self.chunk = 1024
        #  self.format = paInt16
        #  self.channels = 2
        #  self.rate = 44100
        self.host = 'localhost'
        self.port = 5220
        self.backlog = 5

    #  def start_stream(self):
        #  """TODO: Docstring for start_stream.
        #  :returns: None
#
        #  """
        #  self.stream = self.open(format=self.format,
        #  channels=self.channels,
        #  rate=self.rate,
        #  output=True,
        #  )
#
    def start_socket(self):
        """TODO: Docstring for start_socket.
        :returns: None

        """
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.bind((self.host, self.port))
            print("server is started at {}:{}".format(self.host, self.port))
            self.socket.listen(self.backlog)
            self.client, self.address = self.socket.accept()
        except Exception as e:
            print("\033[31mUnable to connect \n {}\033[39m".format(e))

    def start(self):
        """TODO: Docstring for start.
        :returns: None

        """
        #  self.start_stream()
        self.start_socket()
        while True:
            data = self.client.recv(self.chunk)
            if data:
                #  self.stream.write(data)
                self.client.send('ACK')
        self.client.close()
        self.socket.close()
        #  self.stream.close()
        self.terminate()

if __name__ == '__main__':
    main = Audio()
    main.start()
