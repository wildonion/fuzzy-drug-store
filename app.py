



import matplotlib.pyplot as plt
import numpy as np
from db import init


db = init()
# q = "INSERT INTO stocks VALUES (?, ?, ?, ?)" # v = ['2006-01-05', 'BUY', 'RHAT', 100,35.14]
q = "CREATE TABLE IF NOT EXISTS current_drugs (date text, trans text, symbol text, qty real, price real)"
db.query(q,[])




# ================================================
# DEFINING ANTECEDENTS, CONSEQUENTS AND FUZZY SETS
# ================================================

# https://pythonhosted.org/scikit-fuzzy/auto_examples/plot_tipping_problem_newapi.html

X = {"low": np.arange(0, 36, 1), "medium": np.arange(30, 51, 1), "high": np.arange(45, 101, 1)} # current drugs
Y = {"very_few": np.arange(0, 21, 1), "few": np.arange(15, 36, 1), "medium": np.arange(30, 51, 1), 
     "many": np.arange(45, 66, 1), "a_lot": np.arange(60, 101, 1)} # drug sales over the past month
Z = {"very_few": np.arange(0, 21, 1), "few": np.arange(15, 36, 1), "medium": np.arange(30, 51, 1), 
     "many": np.arange(45, 66, 1), "a_lot": np.arange(60, 101, 1)} # drug sales over the past years






