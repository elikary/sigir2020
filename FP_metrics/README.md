## Evaluation
After the recommendations per each algorithm are returned by librec, the next step is the evaluation.

To execute evaluation on all datasets run:

    $ cd sigir2020/FP_metrics/scripts
    $ python main.py

After the main script run, you will see the results per each fold in `~/sigir2020/FP_metrics/evaluation/` as `<dataset-name>/<dataset-name_fold$i.csv>`. (See the image below)

Next, to compute the folds average per each dataset run:

    $ python cross_validation.py
    
The results will be saved in `FP_metrics/evaluation/` as `<dataset-name>/<dataset-name_k.csv>`. For instance `FP_metrics/evaluation/cm100k_observed/cm100_observed_10.csv`. (See the image below)

![](https://github.com/elikary/sigir2020/blob/master/images/folds.png)

### System Requirements

The recommended way to setup a working python environment is to use Anaconda distribution https://www.continuum.io/downloads.
Here is also a list of the required packages:

- Python 3.7.1 
- Pandas
- Numpy
- Scipy
- Matplotlib
- Jupyter Notebook