import pyaudio


def play(data):
    obj = pyaudio.PyAudio()
    stream = obj.open(format=pyaudio.paInt16,
                      channels=2,
                      output=True,
                      rate=16000)
    stream.write(data)
