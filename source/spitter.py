import random as rand
import lyricparser
import chainmarkov

class Spitter:
    def __init__(self, barchain, dirtychain):
       self.barchain = barchain
       self.dirtychani = dirtychain

    def spit(self):
        var = rand.choice(list(self.barchain.chain.keys()))
        bar = ""

        while ((not self.barchain.last(var)) and (not self.barchain.dirty(var))):
            bar = bar + var + " "
            var = self.barchain.get_next(var)

            if self.barchain.dirty(var):
                bar = bar + "( SPORCA )"

        return bar
           
           
        