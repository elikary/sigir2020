#### System Requirements
Java JDK: 1.8 or above (the software was tested with openJDK Runtime Environment (build 1.8.0_222-b10)).
Maven: tested with version 3.6.0

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
First download the `sigir2020` folder into your `home` directory/folder. `sigir2020` contains 2 folders:
- `librec 2.0.0`
- `FP_metrics`

For recommendation execution go to `librec-2.0.0/bin` and run the following command:

    for i in 1 2 3 4 5; do ./run_cross movielens1M 3706 $i; done

+ `run_cross` script runs recommendation using 5-fold cross_validation.
+ `3706` is the size of the list (big size for condensed metrics only, despite of evaluating at top k)
+ `$i` is the number of fold

The results per each fold will be stored in the `librec/result/movielens1M/fold$i` directory
By default, librec returns the results as files into folders, to bring the files outside the folders, run the following command:

    for i in 1 2 3 4 5; do ./movefolders_cv movielens1M $i; done

The final folder organization should be as follows:
 `librec-2.0.0/result/movielens1M/fold$i/<algorithm name>`