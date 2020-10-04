import random as rand
import lyricparser
import chainmarkov

class Spitter:
    def __init__(self, barchain, dirtychain, titlechain):
       self.barchain = barchain
       self.dirtychain = dirtychain
       self.titlechain = titlechain
       self.MIN_TITLE = 2
       self.MAX_TITLE = 6
    
    def title(self):
        lng = rand.randrange(self.MIN_TITLE, self.MAX_TITLE)
        var = rand.choice(list(self.titlechain.chain.keys()))
        bar = ""
        for index in range(lng):
           bar = bar + var + " "
           var = self.titlechain.get_next(var)
        return bar

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
           
        