from prismatic import user_tracker as p_tracker

class Window:
    device = None

    def __init__(self):
        pass

    def initialize(self, **kargs):
        self.tracker = p_tracker.UserTracker()

        if not self.tracker.initialize(**kargs):
            raise StandardError, "User tracker failed to initialize."


