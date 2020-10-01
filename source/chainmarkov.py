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

    def get_count(self, word):
        return self.wordcount[word]
    
    def get_frequency(self, word):
        return self.wordcount[word] / self.total

    def is_last(self):
        return self.last

    def get_value(self):
        return self.value

    def neighbor_size(self):
        return len(self.words)

    def update_frequency(self):
        self.words = [w for w in self.wordcount]
        self.distribution = [ 0 for _ in range(len(self.words))]
        for index in range(len(self.words)):
            self.distribution[index] = self.get_frequency(self.words[index])
        
    def next_state(self):
        return rand.choices(population=self.words, weights=self.distribution)[0]
        

class Chain:
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

    def update(self):
        for element in self.chain:
            self.chain[element].update_frequency()

    def get_next(self, value):
        return self.chain[value].next_state()

    def neighbor_size(self, value):
        return self.chain[value].neighbor_size()
