"""
@author: Elisa Mena-Maldonado
"""

import pandas as pd
import common_variables as cmv


def load_data(path, data_set_name, file_name, separator, head):
    try:
        data_df = pd.read_csv(path + data_set_name +'/'+ file_name ,sep=separator, encoding='latin-1', header = head)
        return data_df
        
    except FileNotFoundError as e:
        print(e)


def remove_optimals(df):
    return df.loc[~df['algorithm'].isin(cmv.optimals)]
    
    
def retrieve_nicks(series):
    values = []
    for a in  series:
        if a in cmv.nick_names:
            values.append(cmv.nick_names[a])
    return values

