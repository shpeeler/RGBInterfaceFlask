import os, subprocess, time
from daemon import runner

class Scheduler(object):

    def __init__(self):
        pass

    def run(self):

        try:
            while True:
                pass

        except Exception, e:
            raise
    
scheduler = Scheduler()
daemon_runner = runner.DaemonRunner(scheduler)
daemon_runner.do_action()
    