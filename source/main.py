import source.lyricparser
import source.markov
import random as rand




        




bars, dirty = lyricparser.parse('./data/message.txt')
chain = Chain(bars)

while True:
    print(chain.get_next("le"))
    a = input()
    




'''
while True:
    var = rand.choice(list(chain.chain.keys()))
    stop = True
    while stop:
        print(var, end=' ')
        if(not chain.is_last(var)):
            elements = [element for element in chain.get_word_counts(var)]
            coumulative_percentage = [0 for _ in range(len(elements))]
            coumulative_percentage[0] = chain.get_frequency(var, elements[0])
         
            for index in range(1, len(elements)):
                coumulative_percentage[index] = coumulative_percentage[index - 1] + chain.get_frequency(var, elements[index])

            x = rand.random()
            chosen_var = 0

            for index in range(len(elements)):
                if x <= coumulative_percentage[index]:
                    chosen_var = elements[index]

            var = chosen_var
        else:
            if((len(chain.get_word_counts(var)) > 0) and (rand.random() >= 85)):
      
                    elements = [element for element in chain.get_word_counts(var)]
                    coumulative_percentage = [0 for _ in range(len(elements))]
                    coumulative_percentage[0] = chain.get_frequency(var, elements[0])
                
                    for index in range(1, len(elements)):
                        coumulative_percentage[index] = coumulative_percentage[index - 1] + chain.get_frequency(var, elements[index])

                    x = rand.random()
                    chosen_var = 0

                    for index in range(len(elements)):
                        if x <= coumulative_percentage[index]:
                            chosen_var = elements[index]

                    var = chosen_var        
            else:
                a = input()
                stop = False
'''


            
            


