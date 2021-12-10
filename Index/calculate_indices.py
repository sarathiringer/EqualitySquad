import os
import pandas as pd
import numpy as np

parentDirectory = os.path.dirname(os.path.dirname(__file__))
path = os.path.join(parentDirectory, 'Data')   

pd.set_option('display.max_columns', None)

file = "\input_data.csv"
input_df = pd.read_csv(path + file)


def missing_to_nan(data, variable):
    data[variable].loc[data[variable] == '..'] = np.nan
    data[variable].loc[data[variable] == '-'] = np.nan


def object_to_float(data, variable):
    data[variable] = data[variable].astype(str).astype(float)


def adjust_table(table_name, list_vars):
    print(list_vars)
    for var in list_vars:
        print(var)
        missing_to_nan(table_name, var)
        object_to_float(table_name, var)

def describe(data):
    des1 = data.describe()
    des2 = data.isnull().sum().to_frame(name='missing').T
    des = pd.concat([des1, des2])
    #print(des)

vars = ['n_sickcase_per1000',
       'n_sickcase_per1000_f', 'n_sickcase_per1000_m', 'avg_sickdays',
       'avg_sickdays_f', 'avg_sickdays_m', 'n_emp', 'n_emp_f', 'n_emp_m',
       'stw_pay_quota_2014', 'stw_pay_quota_2015', 'stw_pay_quota_2016',
       'stw_pay_quota_2017', 'stw_pay_quota_2018', 'uw_pay_quota_2014',
       'uw_pay_quota_2015', 'uw_pay_quota_2016', 'uw_pay_quota_2017',
       'uw_pay_quota_2018']

for var in vars:
    input_df[var].loc[input_df[var] == '..'] = np.nan
    input_df[var] = input_df[var].astype(str).astype(float)

def calculate_indicies(input_df: pd) -> pd:

    # Health - relative
    input_df["index_health"] = input_df['avg_sickdays_m']/input_df['avg_sickdays_f']

    # Unpaid work - relative

    # Power & Influence - relative
    input_df["index_power"] = (input_df["stw_pay_quota_2017"] + input_df["uw_pay_quota_2017"])/200

    #Pay gap: Unexplainable differences in pay between men and women - relative
    input_df["index_pay"] = input_df["stw_pay_quota_2017"]/100

    # Distribution - relative
    input_df["index_distribution"] = input_df['n_emp_f']/input_df['n_emp_m']

    #Combined index
    input_df['index_total_geometric'] = np.sqrt(input_df["index_health"] * input_df["index_power"] * input_df["index_pay"] * input_df["index_distribution"])
    input_df['index_total_aritmetic'] = (input_df["index_health"] + input_df["index_power"] + input_df["index_pay"] + input_df["index_distribution"])/4
    
    return input_df

output_df = calculate_indicies(input_df)
"""
Condense output data
"""
"""
keep_vars = ['occupation_level4_number', 'occupation_level4', 'n_sickcase_per1000',
       'n_sickcase_per1000_f', 'n_sickcase_per1000_m', 'avg_sickdays',
       'avg_sickdays_f', 'avg_sickdays_m', 'n_emp', 'n_emp_f', 'n_emp_m',
       'stw_pay_quota_2014', 'stw_pay_quota_2015', 'stw_pay_quota_2016',
       'stw_pay_quota_2017', 'stw_pay_quota_2018', 'uw_pay_quota_2014',
       'uw_pay_quota_2015', 'uw_pay_quota_2016', 'uw_pay_quota_2017',
       'uw_pay_quota_2018', 'index_health', 'index_pay', 'index_distribution', 'index_power', 'index_total_geometric', 'index_total_aritmetic']
"""

"""
keep_vars = ['occupation_level4',
       'avg_sickdays_f', 'avg_sickdays_m', 'n_emp', 'n_emp_f', 'n_emp_m',
       'stw_pay_quota_2017', 'uw_pay_quota_2017',
       'index_health', 'index_pay', 'index_distribution', 'index_power', 'index_total_geometric', 'index_total_aritmetic']
"""

#output_df = out_df[keep_vars]

output_df.to_csv(path + '\output_data.csv')