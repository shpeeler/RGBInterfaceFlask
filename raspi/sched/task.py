class Task(object):

    def __init__(self, identifier, job, day, time, action, position):
        self.id = identifier
        self.job = job
        self.day = day
        self.time = time
        self.action = action
        self.position = position