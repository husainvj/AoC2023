import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re


Lines = [line.replace('\n', '') for line in open('04Dec/input.txt', 'r')]
Lines


cards={}
for i in range(len(Lines)):
    cards.update({i:[re.findall(r'\d+', Lines[i][9:40]), re.findall(r'\d+', Lines[i][41:])]})


count=[]
for j in range(len(cards)):
    y=0
    for i in cards[j][0]:    
        #x=re.search(i, cards[j][1])
        if i in cards[j][1]:   
            y+=1
            #print(x.group())  
    #print(y)
    if y!=0:
        count.append(2**(y-1))
    else:
        count.append(0)     


print("answer to part 1 is: " + str(sum(count)))
