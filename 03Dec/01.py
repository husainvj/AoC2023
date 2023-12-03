import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re


Lines = [line.replace('\n', '.') for line in open('03Dec/input.txt', 'r')]
Lines.append('.'*len(Lines[0]))
Lines

num_all={}
for i in range(len(Lines)):
    num_all.update({i:re.findall(r'\d+', Lines[i])})


def is_not(input_string):
    return not (input_string.isnumeric() or input_string == '.')


chosen_numbers=[]
chosen={}
add_num=0
for i in range(len(Lines)-1):
    chosen_numbers=[] 
    for j in num_all[i]:       
        #print("68", m.start())
        s=re.search(j, Lines[i]).start() 
        e=re.search(j, Lines[i]).end()-1    
        if is_not(Lines[i+1][s+1]):
            chosen_numbers.append(int(j))
            #chosen.update({i:num_all[i][j]})
            add_num += int(j)
        elif is_not(Lines[i+1][s]):
            chosen_numbers.append(int(j))
            #chosen.update({i:num_all[i][j]})
            add_num += int(j)
        elif is_not(Lines[i+1][s-1]):
            chosen_numbers.append(int(j))
            #chosen.update({i:num_all[i][j]})
            add_num += int(j)
        elif is_not(Lines[i][s-1]):
            chosen_numbers.append(int(j))
            #chosen.update({i:num_all[i][j]})
            add_num += int(j)
        elif is_not(Lines[i-1][s-1]):
            chosen_numbers.append(int(j))
            #chosen.update({i:num_all[i][j]})
            add_num += int(j)
        elif is_not(Lines[i-1][s]):
            chosen_numbers.append(int(j))
            #chosen.update({i:num_all[i][j]})
            add_num += int(j)
        elif is_not(Lines[i-1][s+1]):
            chosen_numbers.append(int(j))
            #chosen.update({i:num_all[i][j]})
            add_num += int(j)
        elif is_not(Lines[i-1][e]):
            chosen_numbers.append(int(j))
            #chosen.update({i:num_all[i][j]})
            add_num += int(j)
        elif is_not(Lines[i-1][e+1]):
            chosen_numbers.append(int(j))
            #chosen.update({i:num_all[i][j]})
            add_num += int(j)
        elif is_not(Lines[i][e+1]):
            chosen_numbers.append(int(j))
            #chosen.update({i:num_all[i][j]})
            add_num += int(j)
        elif is_not(Lines[i+1][e+1]):
            chosen_numbers.append(int(j))
            #chosen.update({i:num_all[i][j]})
            add_num += int(j)
        elif is_not(Lines[i+1][e]):
            chosen_numbers.append(int(j))
            #chosen.update({i:num_all[i][j]})
            add_num += int(j)  
                  
         
    chosen.update({i:chosen_numbers})  

print("directly added sum:", add_num)
print(chosen)
flat_list = [item for sublist in list(chosen.values()) for item in sublist]
print("dict added sum:", sum(flat_list))