from random import randint


class Cashier:
    def __init__(self, position, mintime, maxtime):
        self.position = position
        self.mintime = mintime
        self.maxtime = maxtime
        self.countdown = 0
        self.busy = False

    def process_transaction(self, customer):
        self.countdown = randint(self.mintime, self.maxtime) + (self.position // randint(customer.minspeed, customer.maxspeed))
        self.busy = True
