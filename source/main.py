import lyricparser
import chainmarkov
import spitter
import random as rand

bars, dirty = lyricparser.parse('./data/sample.txt')
chain = chainmarkov.BarsChain(bars)
spitter = spitter.Spitter(chain, None)

while(True):
    print(spitter.spit())
    a = input()
