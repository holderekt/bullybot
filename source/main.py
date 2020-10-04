import lyricparser
import chainmarkov
import spitter
import random as rand

bars, dirty = lyricparser.parse('./data/lyrics.txt')
titles = lyricparser.parsetitle('./data/title.txt')

barchain = chainmarkov.BarsChain(bars)
dirtychain = chainmarkov.DirtyChain(dirty)
titlechain = chainmarkov.ErgordicChain(titles)

spitter = spitter.Spitter(barchain, dirtychain, titlechain)

print(spitter.title())
print(" ")

while(True):
    print(spitter.spit(), end="")
    a = input()