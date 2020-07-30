##
import random
statist = 0
tomatis = 2.7
statistlist = []
for x in range(1000):
    for x in range(0,100):
        numbers = []
        for x in range(100):
            numbers.append(random.randint(0,(9**999)))
        
        numbers = list(set(numbers)) 
        random.shuffle(numbers)
            
        first_part = numbers[0:(int(((len(numbers))/tomatis)))]
        second_part = numbers[(int(((len(numbers))/tomatis))):]
        if max(first_part) == max(numbers):
            statist = statist+1
            
    statistlist.append(statist)
    statist = 0
    
print(statistlist)
print(sum(statistlist)/len(statistlist))

