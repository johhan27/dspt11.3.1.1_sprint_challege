import random


class Product():

    def __init__(
            self, name, price=10,
            weight=20, flammability=0.5):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = random.randint(1000000, 9999999)

        self.stealability_ratio = self.price/self.weight
        self.explode_index = self.flammability * self.weight

    def stealability(self):

        if self.stealability_ratio < 0.5:
            return "Not so stealable"
        elif 0.5 <= self.stealability_ratio < 1:
            return "Kinda stealable"
        else:
            return "Very stealable"


    def explode(self):

        if self.explode_index < 10:
            return "...fizzle"
        elif 10 <= self.explode_index < 50:
            return "...boom!"
        else:
            return "...BABOOM!!"


class BoxingGlove(Product):

    def __init__(self, name, weight=10):
        super(BoxingGlove, self).__init__(
            name=name,
            weight=weight
        )

    def explode(self):
        return "...it's a glove"

    def punch(self):
        if self.weight < 5:
            return "That tickles"
        elif 5 <= self.weight < 15:
            return "Hey that hurt!"
        else:
            return "OUCH!"

        