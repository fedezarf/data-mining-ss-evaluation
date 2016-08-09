# -*- coding: utf-8 -*-
"""
Created on Thu Apr  16 10:52:00 2016

@author: Federico Zarfati
"""

import pandas as pd
import matplotlib.pyplot as plt

report=pd.read_csv('Report.csv', header=None, names=[1,3,5,10])

documents=("Cranfield","Time")
stemmers=(" --downcase", "EnglishStemmer" ,"EnglishStemmerStopwords" )
scorers=("CountScorer" ,"TfIdfScorer", "BM25Scorer" )


cran= report[:9]
time= report[9:]
leg=[]
for i in stemmers:
    for j in scorers:
        leg.append(i+' '+j)

tableau20 = [(31, 119, 180), (174, 199, 232), (255, 127, 14), (255, 187, 120),    
             (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150),    
             (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),    
             (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),    
             (188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229)]    
  
# Scale the RGB values to the [0, 1] range, which is the format matplotlib accepts.    
for i in range(len(tableau20)):    
    r, g, b = tableau20[i]    
    tableau20[i] = (r / 255., g / 255., b / 255.) 
plt.gca().set_color_cycle(tableau20)


plt.subplot(2, 1, 1)
plt.plot(cran.T)
plt.title('Performance of Stemmer-Scorer Combinations on Cranfield Dataset ')
plt.ylabel('Precision @ K')
plt.xlabel('k')
plt.xticks([1,3,5,10])
plt.legend( tuple(leg),fontsize='xx-small', framealpha=0.5, shadow=True, title="Legend", fancybox=True,loc='upper center', ncol=5)
plt.gcf().set_size_inches(20,20)


plt.subplot(2, 1, 2)

plt.plot(time.T)
plt.title('Performance of Stemmer-Scorer Combinations on Time Dataset ')
plt.ylabel('Precision @ K')
plt.xlabel('k')
plt.xticks([1,3,5,10])
plt.gcf().set_size_inches(20,20)
plt.legend( tuple(leg),fontsize='xx-small', framealpha=0.5, shadow=True, title="Legend", fancybox=True,loc='upper center', ncol=5)



plt.show()



