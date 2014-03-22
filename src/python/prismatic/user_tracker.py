from primesense import openni2 as openni
from primesense import nite2 as nite

class UserTracker:
    def __init__(self):
        pass

    def initialize(self, openni2_path = None, nite2_path=None):
        openni.initialize(openni2_path)
        nite.initialize(nite2_path)

    def device(self):
        self.device = self.device or nite.Device.open_any()
        return self.Device

    def __exit__():
        nite.unload()
        openni.unload()




