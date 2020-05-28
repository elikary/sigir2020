#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Elisa Mena-Maldonado
"""

import pandas as pd
import common_variables as cmv


def load_data(path, data_set_name, file_name, separator, cols, head):
    print('------loading ' + file_name + ' ------ ' + '\n')
    
    try:
        data_df = pd.read_csv(path + data_set_name +'/'+ file_name ,sep=separator, names=cols, encoding='latin-1', header = head)
        print('done!')                
        return data_df
        
    except FileNotFoundError as e:
        print(e)
 

       
def concat_allfolds(data_set):
        
    eval_files = []
    
    for f in cmv.folds:

        eval_data = load_data(cmv.evaluation_result_path, data_set, data_set +'_fold'+ str(f) +'.csv', ',', 0)
        print(data_set + ' fold' + str(f))
        eval_files.append(eval_data)

    eval_all = pd.concat(eval_files)
    print(eval_all.head())
    return eval_all
 
def compute_mean_allfolds(eval_all, k, algorithms, data_set):
    
    eval_final = pd.DataFrame(columns= eval_all.columns)
    
    for a in algorithms:
    
        eval_all_at_k = eval_all.loc[(eval_all['cutoff']==k) & \
                                     (eval_all['algorithm']==a)]
        all_means = eval_all_at_k.mean()
        
        all_means = all_means.append(pd.Series([a,data_set], index=['algorithm','dataset']))
        eval_final = eval_final.append(all_means, ignore_index=True)
        
    print(eval_final.head())
    q = cmv.evaluation_result_path + data_set  + '/' +  data_set + '_' + str(k) + '.csv'
    print(q)
    eval_final.to_csv(q, header=True, index=None, sep=',', mode='w+')
        
def main():

    for d in cmv.data_sets:
        compute_mean_allfolds(concat_allfolds(d), cmv.k, cmv.algorithms, d)

if __name__ == "__main__":
    main()    
   
    
    
    
    
    
    
    
    
    
    
    
    