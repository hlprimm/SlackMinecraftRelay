"""
Just send the animation packet every 5min
"""
__author__ = "Nick Gamberini, Morgan Creekmroe"
__copyright__ = "Copyright 2015, The SpockBot Project"
__license__ = "MIT"

AFK_TIME = 5

class AntiAFKPlugin:
    def __init__(self, ploader, settings):
        self.net = ploader.requires('Net')
        self.timers = ploader.requires('Timers')
        self.physics = ploader.requires('Physics')
        self.timers.reg_event_timer(AFK_TIME, self.avoid_afk)

    def avoid_afk(self):
        self.physics.jump()
        self.net.push_packet('PLAY>Animation', '')
