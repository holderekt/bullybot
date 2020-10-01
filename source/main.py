import lyricparser
import chainmarkov
import random as rand

bars, dirty = lyricparser.parse('./data/message.txt')
chain = chainmarkov.Chain(bars)

while True:
    var = rand.choice(list(chain.chain.keys()))
    stop = True
    while stop:
        print(var, end=' ')
        if(not chain.is_last(var)):
            var = chain.get_next(var)
        else:
            if((chain.neighbor_size(var) > 0) and (rand.random() >= 85)):
                var = chain.get_next(var)  
            else:
                a = input()
                stop = False
