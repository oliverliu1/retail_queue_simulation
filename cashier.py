from random import randint

class Cashier(object):

    def __init__(self, position, mintime, maxtime):
        self.position = position
        self.mintime = mintime
        self.maxtime = maxtime
        self.countdown = 0
        self.busy = False

    def process_transaction(self):
        self.countdown = randint(mintime, maxtime)
        self.busy = True
