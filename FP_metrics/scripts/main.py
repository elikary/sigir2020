#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Elisa Mena-Maldonado

"""

import pandas as pd
from evaluation import full_metrics, condensed_metrics
import common_variables as cmv


def load_data(path, data_set_name, file_name, separator, cols):
    print('------loading ' + file_name + ' ------ ' + '\n')
    
    try:
        data_df = pd.read_csv(path + data_set_name +'/'+ file_name ,sep=separator, names=cols, encoding='latin-1')
        print('done!')                
        return data_df
        
    except FileNotFoundError as e:
        print(e)
 
    
def compute_evaluation(data_set_name, num_fold, iscondensed):
    
    print(data_set_name)

    result_list = []
    
    test = load_data(cmv.data_path, data_set_name + '/fold'+ str(num_fold), cmv.test_file_name + '.txt', '\t', cmv.cols)
    
    for a in cmv.algorithms:
        recommendation = load_data(cmv.recommendation_path, data_set_name + '/fold' + str(num_fold), a, ',', cmv.recommendation_cols)
        recommendation_at_k = recommendation.groupby(cmv.user_column).head(cmv.k).reset_index(drop=True)
        if iscondensed == True:
            result_list.append([a, data_set_name] + full_metrics(recommendation_at_k, test, cmv.k) + \
                           condensed_metrics(recommendation, test, cmv.k) + [cmv.k])
        else:
            result_list.append([a, data_set_name] + full_metrics(recommendation_at_k, test, cmv.k) + [cmv.k])

        print('Finished processing metrics@'+ str(cmv.k) + '\n')

    results = pd.DataFrame(result_list)
    
    if iscondensed == True:
        results.columns = cmv.result_cols_condensed 
    else:
        results.columns = cmv.result_cols
    
    q = cmv.evaluation_result_path + data_set_name  + '/' + data_set_name + '_fold'+ str(num_fold) + '.csv'
    print(q)
    print (results.head(5))
    results.to_csv(q, header=True, index=None, sep=',', mode='w+')


def main():

     for d in cmv.data_sets:
         for f in cmv.folds:
             iscondensed = False if d!= 'movielens1M' else True

             compute_evaluation(d, f, iscondensed)

if __name__ == "__main__":
    main()


