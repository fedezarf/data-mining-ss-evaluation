# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 20:00 2016

@author: Federico Zarfati

"""

import pandas as pd
import sys 
import numpy as np
import os
import pylab
import csv
from docutils.utils.punctuation_chars import delimiters
from fileinput import close

os.getcwd()

values = None

def avg_p_at_k(output, ground):
    """Save computed p@k in a Report.csv file

    The function takes two argument: queries and ground truth.
    For every p@k (1,3,5,10) the function compute the p@k
    calculating the intersection between the query's results set and
    the set of relevant documents. It divides the result of the intersection
    by the minimum between k and the length of the ground set.
    Every result is added to the previous and then divided by the number of queries.
    """
    global values
    counter = 0
    total=0
    
    for k in [1,3,5,10]: # For each k
        
        for query in ground.keys(): # For each query in groundtruth
            total += len(set(output[query][:k]) & set(ground[query]))*1.0/min(k,len(ground[query]))
            print(k)
            print(set(output[query][:k]))
            counter +=1   # Query counter
        
        # Total of the k divided by the number of the queries
        values.append((total*1.0)/counter)
       
        # Reset the counters
        total = 0
        counter = 0
    
    # Save the data
    with open("Report.csv", "a") as fp:
        
        wr = csv.writer(fp, dialect='excel')
        
        wr.writerow(values)
    
def main():
    global values
    values = []
    
    #Read the file from the main arguments
    queries = pd.read_csv(sys.argv[1], sep="\t")
    ground  = pd.read_csv(sys.argv[2], sep="\t" )
    
    #Groupd the tsv file for query_id
    out = queries.groupby('Query_ID')
    tru = ground.groupby('Query_id')
    
    #Create dictionaries with query_id as keys
    out_dic = {k: g["Doc_ID"].tolist() for k,g in out}
    tru_dic = {k: g["Relevant_Doc_id"].tolist() for k,g in tru}
    
    #Compute the Average P@k
    avg_p_at_k(out_dic,tru_dic)
    

if __name__=="__main__":
    main()