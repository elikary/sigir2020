# Agreement and Disagreement between True and False-Positive Metrics in Recommender Systems Evaluation
Source code used for the results reported in the [SIGIR2020 paper](http://marksanderson.org/publications/my_papers/sigir2020.pdf)

Paper DOI (https://doi.org/10.1145/3397271.3401096)

> E. Mena-Maldonado, R. Cañamares, [P. Castells](http://ir.ii.uam.es/castells), Y. Ren and [M.Sanderson](http://marksanderson.org). Agreement and Disagreement between True and False-Positive Metrics in Recommender Systems Evaluation. 43rd ACM International Conference on Research and Development in Information Retrieval (SIGIR 2020). ACM, Virtual Event, China.

## Sotware Required
This project contains two modules:
- **Recommendation:** we used Librec 2.0 library to run the algorithms of our experiments (See **librec-2.0.0** folder)
- **Evaluation:** we coded evaluation process using Python (See **FP_metrics** folder)

### OS support
The code was tested on Linux

        NAME="Red Hat Enterprise Linux Server"
        VERSION="7.7 (Maipo)"
        
Can possibly run on OSX however this has not been tested yet.

### Recommendation
We used the recommendation library [Librec-2.0.0](https://www.librec.net/). In this library there is a range of algorithms to produce recommendations.  
To run our experiments we included some extra algorithms to test the optimal ranking functions for Precision and Anti-Precision

Here is the list of the new included algorithms:

- Optimal Observed AntiPrecision
- Optimal Observed Precision
- Optimal True AntiPrecision
- Optimal True Precision
- Optimal True AntiPrecision restricted to test
- Optimal True Precision restricted to test

Please refer to `librec-core.src.main.java.recommender.baseline` to see their implementations.

#### Running recommendation
First download the `sigir2020` folder into your `home` directory/folder

For recommendation execution go to `librec-2.0.0/bin` and run the following command:

    for i in 1 2 3 4 5; do ./run_cross movielens1M 3706 $i; done 

The `run_cross` script runs recommendation using 5-fold cross_validation.

`3706` is the size of the list (big size for condensed metrics only, despite of evaluating at top k)

`$i` is the number of fold 

The results per each fold will be stored in the `librec/result/movielens1M/fold$i` directory
By default, librec returns the results as files into folders, to bring the files outside the folders, run the following command:

    for i in 1 2 3 4 5; do ./movefolders_cv movielens1M $i; done

#### Evaluation

For the evaluation we developed a package that contains all the methods necessary to run evaluation on each of the datasets we used.





