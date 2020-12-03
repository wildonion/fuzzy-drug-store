




from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import numpy as np
from db import init
from fuzzer import Antecedent, ControlSystem, Rule, ControlSystemSimulation



scaler = MinMaxScaler()
db = init()
# q = "INSERT INTO stocks VALUES (?, ?, ?, ?)" # v = ['2006-01-05', 'BUY', 'RHAT', 100,35.14]
q = "CREATE TABLE IF NOT EXISTS current_drugs (date text, trans text, symbol text, qty real, price real)"
db.query(q,[])



# References : https://pythonhosted.org/scikit-fuzzy/auto_examples/plot_tipping_problem_newapi.html


# ================================================
# DEFINING ANTECEDENTS, CONSEQUENTS AND FUZZY SETS
# ================================================

X = Antecedent(range=np.arange(0, 100, 1), name="current drugs")
X.low = np.arange(0, 35, 1) # fuzzy set low
X.medium = np.arange(30, 50, 1) # fuzzy set medium
X.high = np.arange(45, 100, 1) # fuzzy set high
X.view() # plot the X antecedent


Y = Antecedent(range=np.arange(0, 100, 1), name="drug sales over the past month") 
Y.very_few = np.arange(0, 20, 1) # fuzzy set very few
Y.few = np.arange(15, 35, 1) # fuzzy set few
Y.medium = np.arange(30, 50, 1) # fuzzy set medium
Y.many = np.arange(45, 65, 1) # fuzzy set many
Y.a_lot = np.arange(60, 100, 1) # fuzzy set a lot
# Y.view() # plot the Y antecedent


Z = Antecedent(range=np.arange(0, 100, 1), name="drug sales over the past year")
Z.very_few = np.arange(0, 20, 1) # fuzzy set very few
Z.few = np.arange(15, 35, 1) # fuzzy set few
Z.medium = np.arange(30, 50, 1) # fuzzy set medium
Z.many = np.arange(45, 65, 1) # fuzzy set many
Z.a_lot = np.arange(60, 100, 1) # fuzzy set a lot
# Z.view() # plot the Z antecedent















