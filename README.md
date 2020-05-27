# Agreement and Disagreement between True and False-Positive Metrics in Recommender Systems Evaluation
Source code used for the results reported in the [SIGIR2020 paper](http://marksanderson.org/publications/my_papers/sigir2020.pdf)

Paper DOI (https://doi.org/10.1145/3397271.3401096)

> E. Mena-Maldonado, R. Cañamares, [P. Castells](http://ir.ii.uam.es/castells), Y. Ren and [M.Sanderson](http://marksanderson.org). Agreement and Disagreement between True and False-Positive Metrics in Recommender Systems Evaluation. 43rd ACM International Conference on Research and Development in Information Retrieval (SIGIR 2020). ACM, Virtual Event, China.

## Sotware Required
This project contains two modules:
- **Recommendation:** we used Librec 2.0 library to run the algorithms of our experiments (See **librec-2.0.0** folder)
- **Evaluation:** we created some scripts in Python to run evaluation in our experiments (See **FP_metrics** folder)

### OS support
The code was tested on Linux

        NAME="Red Hat Enterprise Linux Server"
        VERSION="7.7 (Maipo)"
        
Can possibly run on OSX however this has not been tested yet.

## Datasets 
For convinience we have uploaded the datasets used for all the experiments presented in the paper.  Please see the folder:
`sigir2020/librec-2.0.0/data`
- MOVIELENS 1M (Observed) Train and (Observed) test
- CM100K (Observed) Train and (Observed and True) tests
- YAHOO (Observed) Train and (Observed and True) tests












