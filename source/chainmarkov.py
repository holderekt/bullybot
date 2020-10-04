# -----------------------------------------------------------
# Markov Chain Model
# -----------------------------------------------------------

import random as rand

class State:
    def __init__(self, value, last):
        self.value = value
        self.last = last
        self.wordcount = {}
        self.total = 0
        self.words = []
        self.distribution = []

    def update_count(self, word):
        if word in self.wordcount:
            self.wordcount[word] = self.wordcount[word] + 1
        else:
            self.wordcount[word] = 1
        self.total = self.total + 1

    def add_word(self, word, value):
        self.wordcount[word] = value
        self.total = self.total + value

    def get_count(self, word):
        return self.wordcount[word]
    
    def get_frequency(self, word):
        return self.wordcount[word] / self.total

    def is_last(self):
        return self.last

    def get_value(self):
        return self.value

    def neighbor_size(self):
        return len(self.wordcount)

    def update_frequency(self):
        self.words = [w for w in self.wordcount]
        self.distribution = [ 0 for _ in range(len(self.words))]
        for index in range(len(self.words)):
            self.distribution[index] = self.get_frequency(self.words[index])
        
    def next_state(self):
        return rand.choices(population=self.words, weights=self.distribution)[0]
        

class Chain(object):
    def __init__(self, bars):
        self.chain = {}
        self._calculate_frequency(bars)
        self.update()
    
    def _calculate_frequency(self, bars):
        for bar in bars:
            for index in range(len(bar) - 1):
                if(not (bar[index] in self.chain)):
                    self.chain[bar[index]] = State(bar[index], False)
                self.chain[bar[index]].update_count(bar[index + 1])

            if bar[-1] in self.chain:
                self.chain[bar[-1]].last = True
            else:
                self.chain[bar[-1]] = State(bar[-1], True)

    def is_last(self, value):
        return self.chain[value].is_last()

    def add_word(self, word, value, weight):
        self.chain[word].add_word(value, weight)

    def update(self):
        for element in self.chain:
            self.chain[element].update_frequency()

    def get_next(self, value):
        return self.chain[value].next_state()

    def neighbor(self, word):
        return self.chain[word].words, self.chain[word].distribution

    def neighbor_size(self, value):
        return self.chain[value].neighbor_size()


class BarsChain(Chain):
    def __init__(self, bars):
        self.chain = {}
        self.LAST_STATE = "__FINAL__"
        self.LAST_WEIGHT = 0.4
        self.DIRTY_STATE = "__DIRTY__"
        self.DIRTY_WEIGHT = 0.5
        self.starters = []

        super()._calculate_frequency(bars) 
        self.update_last()
        super().update()

    def update_last(self):
        for word in self.chain:
            if self.neighbor_size(word) >= 1 and (not self.is_last(word)):
                self.starters.append(word)

            if self.chain[word].is_last():
                super().add_word(word, self.LAST_STATE, self.LAST_WEIGHT)
                super().add_word(word, self.DIRTY_STATE, self.DIRTY_WEIGHT)

    def last(self, value):
        return value == self.LAST_STATE

    def dirty(self, value):
        return value == self.DIRTY_STATE


class DirtyChain(Chain):
    def __init__(self, dirty):
        self.chain = {}
        self.LAST_STATE = "__FINAL__"
        self.LAST_WEIGHT = 0.2
        super()._calculate_frequency(dirty)
        self.update_last()
        super().update()

    def update_last(self):
        for word in self.chain:
            if self.chain[word].is_last():
                super().add_word(word, self.LAST_STATE, self.LAST_WEIGHT)

    def last(self, value):
        return value == self.LAST_STATE


class ErgordicChain(Chain):
    def __init__(self, bars):
        self.chain = {}
        self.RANDOM_STATE = "__RANDOM__"
        self.RANDOM_WEIGHT = 1
        super()._calculate_frequency(bars)
        self.update_last()
        super().update()

    def update_last(self):
        for word in self.chain:
            super().add_word(word, self.RANDOM_STATE, self.RANDOM_WEIGHT)

    def get_next(self, value):
        var =  super().get_next(value) 
        if var == self.RANDOM_STATE:
            var = rand.choice(list(self.chain.keys()))
        return var
