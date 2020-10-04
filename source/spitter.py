import random as rand
import lyricparser
import chainmarkov

class Spitter:
    def __init__(self, barchain, dirtychain):
       self.barchain = barchain
       self.dirtychain = dirtychain

    def spit(self):
        var = rand.choice(self.barchain.starters)
        bar = ""
        while ((not self.barchain.last(var)) and (not self.barchain.dirty(var))):
            bar = bar + var + " "
            var = self.barchain.get_next(var)

            if self.barchain.dirty(var):
                bar = bar + self.dirty()

        return bar.capitalize()

    def dirty(self):
        var = rand.choice(list(self.dirtychain.chain.keys()))
        bar = ""
        while (not self.dirtychain.last(var)):
            bar = bar + var + " "
            var = self.dirtychain.get_next(var)

        return "(" + bar.capitalize() + ")"
           
        