# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 23:28:06 2019

@author: trung
"""
import numpy as np
import pandas as pd
from os.path import abspath, dirname
#%%
parent_dir=dirname(dirname(abspath(__file__)))
with open(parent_dir+"\data\Problem 99\p099_base_exp.txt", "r") as fin:
    lines=[line.strip("\n").split(",") for line in fin.readlines()]
    A=np.array(lines,dtype=float)
df=pd.DataFrame(A)
df.columns=["Base","Exp"]
#%%
for _ in range(1):
    df=df.loc[(df["Base"]>df["Base"].mean()) | (df["Exp"]>df["Exp"].mean())]
print(df)