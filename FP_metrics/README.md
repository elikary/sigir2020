## Evaluation

For the evaluation stage we developed some scripts to run evaluation on each of the datasets we used.
To run the evaluation scripts go to `sigir2020/FP_metrics` and run the following command:

    python main.py

NOTE: To run scripts in unix systems, you need to assign the right persmissions to each file.

    chmod +x <scriptname>

After the main script was run, you will see the results per each fold in `FP_metrics/evaluation/` as `<dataset-name>/<dataset-name_fold$i.csv>`
For instance `FP_metrics/evaluation/cm100k_observed/cm100_observed_fold1.csv`

Figure here!

Now to compute the average per each fold, you need to run:

    python cross_validation.py
    
The results will be saved in `FP_metrics/evaluation/` as `<dataset-name>/<dataset-name_k.csv>`
For instance `FP_metrics/evaluation/cm100k_observed/cm100_observed_10.csv`

### System Requirements

The recommended way to setup a working python environment is to use Anaconda distribution https://www.continuum.io/downloads.
Here is also a list of the required packages:

- Python 3.7.1 
- Pandas
- Numpy
- Scipy
- Matplotlib
- Jupyter Notebook