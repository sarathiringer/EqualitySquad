import os
import pandas as pd

parentDirectory = os.path.dirname(os.path.dirname(__file__))
path = os.path.join(parentDirectory, 'Data')   

pd.set_option('display.max_columns', None)

file = "\output_data.csv"
input_df = pd.read_csv(path + file)

print(input_df.head())