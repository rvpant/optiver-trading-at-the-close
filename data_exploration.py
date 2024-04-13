import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data_df = pd.read_csv('train.csv')
data_df.iloc[:50].to_csv('train_top_50.csv')
print(data_df.columns)