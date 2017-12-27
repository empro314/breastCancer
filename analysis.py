import numpy as np
import pandas as pd
import matplotlib as mpl

input = pd.read_csv("data/dataCorr/dataCorr.csv", sep=';')

#mpl.style.use('default')

#input["radius_mean"].hist()

input["texture_mean"].hist()

