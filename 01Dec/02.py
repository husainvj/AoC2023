import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re


# Using readlines()
file = open('01Dec/input.txt', 'r')
Lines = file.readlines()

num_dict={"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6","seven":"7","eight":"8","nine":"9","ten":"10"}

for i in range(len(Lines)):
    matched={}
    
    for k in num_dict.keys():
        x=re.search(k,Lines[i])
        if x:
            matched.update({x.start():x.group()})

    z=dict(sorted(matched.items()))
    z

    for v in z.values():
        Lines[i] = Lines[i].replace(v, num_dict[v])

#print(Lines)





integers = []
count = 0
for line in Lines:
    x = "".join(re.findall("\d+", line))[0]
    y = "".join(re.findall("\d+", line))[-1]
    str = x+y

    integers.append(int(str))
    count += 1
#print(integers)
print("sum of integers is : ", sum(integers))




"""    
for i in range(len(Lines)):
    if "teen" in Lines[i]:
        for k , v in teen_dict.items():
            Lines[i] = Lines[i].replace(k, v)   
    else:
        for k , v in num_dict.items():
            Lines[i] = Lines[i].replace(k, v)
"""
