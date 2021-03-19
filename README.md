# Agreement and Disagreement between True and False-Positive Metrics in Recommender Systems Evaluation
Source code used for the results reported in the [SIGIR2020 paper](http://marksanderson.org/publications/my_papers/sigir2020.pdf)

> E. Mena-Maldonado, R. Cañamares, [P. Castells](http://ir.ii.uam.es/castells), Y. Ren and [M.Sanderson](http://marksanderson.org). Agreement and Disagreement between True and False-Positive Metrics in Recommender Systems Evaluation. 43rd ACM International Conference on Research and Development in Information Retrieval (SIGIR 2020). ACM, Virtual Event, China.

Paper DOI (https://doi.org/10.1145/3397271.3401096)

**Extended version of this work:** [TOIS PAPER](https://github.com/elikary/tois2021)

## Sotware Required
This project contains two modules:
- **Recommendation:** we used (an edited version) of Librec 2.0.0 library to run the algorithms of our experiments (See [librec-2.0.0](https://github.com/elikary/sigir2020/tree/master/librec-2.0.0) folder)
- **Evaluation:** we created some scripts in Python to do evaluation in our experiments (See [FP_metrics](https://github.com/elikary/sigir2020/tree/master/FP_metrics) folder)

We have included instructions (README files) on how to run each module, please refer to each folder for more information.

## Datasets 
For convinience we have uploaded binarized versions of the datasets used for all the experiments presented in the paper.  Please see the folder:
`sigir2020/librec-2.0.0/data`
- MOVIELENS 1M (Observed) Train and (Observed) test
- CM100K (Observed) Train and (Observed and True) tests
- CM100K SYNTHETIC (Observed) Train and (Observed and True) tests
- YAHOO! R3 (Observed) Train and (Observed and True) tests


## OS support
The code was tested on Linux

        NAME="Red Hat Enterprise Linux Server"
        VERSION="7.7 (Maipo)"
        
Can possibly run on OSX however this has not been tested yet.











