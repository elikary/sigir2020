## Recommendation
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

### Running recommendation
First download the `sigir2020` folder into your `home` directory/folder. `sigir2020` contains 2 folders:
- [librec 2.0.0](https://github.com/elikary/sigir2020/tree/master/FP_metrics)
- [FP_metrics](https://github.com/elikary/sigir2020/tree/master/librec-2.0.0)

For recommendation execution go to `librec-2.0.0/bin` and run the following command:

    for i in 1 2 3 4 5; do ./run_cross cm100k_observed 10 $i; done

+ `run_cross` script runs recommendation using 5-fold cross_validation.
+ `10` is the size of the list 
+ `$i` is the number of fold

The results per each fold will be stored in the `librec/result/cm100k_observed/fold$i` directory
By default, librec returns the results as files into folders, to bring the files outside the folders, run the following command:

    for i in 1 2 3 4 5; do ./movefolders_cv cm100k_observed $i; done

The final folder organization should be as follows:
 `librec-2.0.0/result/cm100k_observed/fold$i/<algorithm name>`
 
 For instance, `librec-2.0.0/result/cm100k_observed/fold1/mostpopular`
 
 NOTE: To run scripts in unix systems, you need to assign the right persmissions to each file.

    chmod +x run_cross
    chmod +x movefolders_cv
 
 #### System Requirements
 Java JDK: 1.8 or above (the software was tested with openJDK Runtime Environment (build 1.8.0_222-b10)).
 Maven: tested with version 3.6.0