import lyricparser
import chainmarkov
import spitter
import random as rand

bars, dirty = lyricparser.parse('./data/sample.txt')
chain = chainmarkov.BarsChain(bars)
spitter = spitter.Spitter(chain, None)


for d in dirty:
    print(d)

chain = chainmarkov.DirtyChain(dirty)

while True:
    var = rand.choice(list(chain.chain.keys()))
    bar = ""
    while not chain.last(var):
        bar = bar + var + " "
        var = chain.get_next(var)
    print(bar)
    a = input()

        
