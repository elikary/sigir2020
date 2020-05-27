from __future__ import division
import numpy as np
from common_variables import user_column, item_colum, rating_column, threshold


def precision(tp, denominator):
    return tp/denominator
    
def antiprecision(fp, denominator):
    return fp/denominator

def recall(tp, relevants):
    if relevants == 0:
        return 0
    return tp/relevants

def fallout(fp, nonrelevants):
    if nonrelevants == 0:
        return 0
    return fp/nonrelevants

def count_positive_hits(data, column, threshold):
    ratings = get_ratings_set(data)
    return data[data[column].isin([i for i in ratings if i >threshold])][column].count()

def count_negative_hits(data, column, threshold):
    ratings = get_ratings_set(data)
    return data[data[column].isin([i for i in ratings if i <=threshold])][column].count()

def get_ratings_set(data):
    return data[rating_column].unique()

def get_test_ratings_rec(recommendation, testdata):
    recommendation = set_new_index(recommendation, user_column, item_colum)
    testdata = set_new_index(testdata, user_column, item_colum)
    recommendation[rating_column] = testdata[rating_column]
    return recommendation

def get_topk(data, k):
    return data.groupby(user_column).head(k).reset_index(drop=True)

def set_new_index(df, col1, col2):
    df.set_index(df[col1].map(str) +  '_' +df[col2].map(str), inplace=True)
    return df

def get_number_users(data):
    return data[user_column].unique()

def findUserData(data, u):
    return data.loc[data[user_column]== u] 

def metrics_one_user(rec_user, user_test, k): 
    tp_user = count_positive_hits(rec_user, rating_column, threshold)
    fp_user = count_negative_hits(rec_user, rating_column, threshold) 
    
    relevants_user = count_positive_hits(user_test, rating_column, threshold)
    nonrelevants_user = count_negative_hits(user_test, rating_column, threshold)

    return recall(tp_user, relevants_user), precision(tp_user,k), \
            fallout(fp_user, nonrelevants_user), antiprecision(fp_user, k)


def metrics_all_users(recommendation, testdata, k):
    recall_list = []
    fallout_list = []
    precision_list = []
    antiprecision_list = []
    
    users_test = get_number_users(testdata) 
    
    for u in users_test:
        
        recommendation_user = findUserData(recommendation, u)
        testdata_user = findUserData(testdata, u)
        
        recall, precision, fallout, antiprecision = metrics_one_user(recommendation_user, testdata_user, k)
        
        recall_list.append(recall)
        fallout_list.append(fallout)
        precision_list.append(precision)
        antiprecision_list.append(antiprecision)
        

    recall = np.mean(recall_list)
    fallout = np.mean(fallout_list)
    precision = np.mean(precision_list)
    antiprecision = np.mean(antiprecision_list)
  
    return [recall, precision, fallout, antiprecision]
    

def full_metrics(recommendation, testdata, k):
    
    recommendation = get_test_ratings_rec(recommendation, testdata) # match ratings test with rec totaldatset
    return metrics_all_users(recommendation, testdata, k)
       
    
def condensed_metrics(recommendation, testdata, k):
    
    recommendation = get_test_ratings_rec(recommendation, testdata) # match ratings test with rec totaldatset       
    condensed_recommendation =recommendation[recommendation.rating.notnull()]    
    rec_at_k = get_topk(condensed_recommendation, k)
    return metrics_all_users(rec_at_k, testdata, k)

    
    

    
    
    

    
    
    
    
    
    
    
    

