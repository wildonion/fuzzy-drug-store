




from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import numpy as np
from db import init
from fuzzer import Antecedent, ControlSystem, Rule, ControlSystemSimulation

'''

References : https://pythonhosted.org/scikit-fuzzy/auto_examples/plot_tipping_problem_newapi.html

TODO : specify the number of inputs and outputs
TODO : fetch from db

'''

scaler = MinMaxScaler()
db = init()

# q = "INSERT INTO stocks VALUES (?, ?, ?, ?)" # v = ['2006-01-05', 'BUY', 'RHAT', 100,35.14]
q = "CREATE TABLE IF NOT EXISTS medicines (date text, trans text, symbol text, qty real, price real)"
db.query(q,[])



X = Antecedent(range=np.arange(0, 100, 1), name="current drugs")
X.low = scaler.fit_transform(np.arange(0, 35, 1).reshape(-1, 1))
X.medium = scaler.fit_transform(np.arange(30, 50, 1).reshape(-1, 1))
X.high = scaler.fit_transform(np.arange(45, 100, 1).reshape(-1, 1))
X.view() # plot the X antecedent


Y = Antecedent(range=np.arange(0, 100, 1), name="drug sales over the past month") 
Y.very_few = scaler.fit_transform(np.arange(0, 20, 1).reshape(-1, 1))
Y.few = scaler.fit_transform(np.arange(15, 35, 1).reshape(-1, 1))
Y.medium = scaler.fit_transform(np.arange(30, 50, 1).reshape(-1, 1))
Y.many = scaler.fit_transform(np.arange(45, 65, 1).reshape(-1, 1))
Y.a_lot = scaler.fit_transform(np.arange(60, 100, 1).reshape(-1, 1))
Y.view() # plot the Y antecedent


Z = Antecedent(range=np.arange(0, 100, 1), name="drug sales in current season over the past year")
Z.very_few = scaler.fit_transform(np.arange(0, 20, 1).reshape(-1, 1))
Z.few = scaler.fit_transform(np.arange(15, 35, 1).reshape(-1, 1))
Z.medium = scaler.fit_transform(np.arange(30, 50, 1).reshape(-1, 1))
Z.many = scaler.fit_transform(np.arange(45, 65, 1).reshape(-1, 1))
Z.a_lot = scaler.fit_transform(np.arange(60, 100, 1).reshape(-1, 1))
Z.view() # plot the Z antecedent

























