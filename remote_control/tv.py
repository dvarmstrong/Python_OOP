# TV Class 

from mimetypes import init


class TV:
    def __init__(self) -> None:
        self.isOn = False
        self.isMuted = False
        self.channelList =[2,4,5,7,9,11,20,36,44,54,65]
        self.nChannels = len(self.channelList)
        self.channelIndex = 0 
        self.VOLUME_MINIMUM = 0 #constant 
        self.VOLUME_MAXIMUM = 10 #constant 
        self.volume = self.VOLUME_MAXIMUM // #integer divide 

    def power(self):
        self.isOn = not self.isOn #toggle button 

        