import socket
#  from pyaudio import PyAudio, paInt16


class Audio():

    """Docstring for Audio. """

    def __init__(self):
        """TODO: to be defined1. """
        #  PyAudio.__init__(self)
        self.chunk = 1024
        #  self.format = paInt16
        #  self.channels = 1
        #  self.rate = 44100
        self.host = 'localhost'
        self.port = 5220

    #  def start_stream(self):
    #      """TODO: Docstring for start_stream.
    #      :returns: TODO
    #
    #      """
    #      self.stream = self.open(format=self.format,
    #                              channels=self.channels,
    #                              rate=self.rate,
    #                              input=True,
    #                              frames_per_buffer=self.chunk)
    #
    def start_socket(self):
        """TODO: Docstring for start_socket.
        :returns: TODO

        """
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.socket.connect((self.host, self.port))
        except Exception as e:
            print("Unable to connect \n {}".format(e))

    def start(self):
        """TODO: Docstring for start.
        :returns: TODO

        """
        #  self.start_stream()
        self.start_socket()
        self.socket.send("hello world")
        self.socket.recv(self.chunk)
        self.socket.close()
        #  self.stream.close()
        self.terminate()

if __name__ == '__main__':
    main = Audio()
    main.start()
