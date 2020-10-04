import lyricparser
import chainmarkov
import spitter
import random as rand

bars, dirty = lyricparser.parse('./data/sample.txt')

for bar in bars:
    print(bar)

print(" -- ")
for bar in dirty:
    print(bar)

'''
chain = chainmarkov.BarsChain(bars)
dirtychain = chainmarkov.DirtyChain(dirty)
spitter = spitter.Spitter(chain, dirtychain)

while(True):
    print(spitter.spit(), end="")
    a = input()
'''
