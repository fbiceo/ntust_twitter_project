# -*- coding: utf-8 -*-
"""
Created on Wed Nov 01 13:43:41 2015

@author: user
"""
import random
import networkx as nx 
D=nx.DiGraph()

f = open('log/step2_user_user.tsv')

for l in f:
    col = l.strip().split("\t")    
    if(int(col[2]) > 0 ):
        D.add_weighted_edges_from([(col[0],col[1],float(col[2]))])

pk = nx.pagerank(D)


f = open('log/pagerank.tsv', 'w+')
for l in nx.pagerank(D):       
    f.writelines(l+"\t"+str(pk[l])+"\r\n")
