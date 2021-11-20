# tracevec
Learning word embedding models (_Word2Vec and Doc2Vec_) based on the electrical consumption of various home appliances.

## Requirements
* Python 3.8.10+
* Pip / Anaconda
* Jupyter Notebook

### Other necessary dependencies are:
`numpy`, `scipy`, `torch`, `pandas`, `seaborn`, `matplotlib`, `scikit_learn`, `gensim` and `matplotlib_venn`

Dependencies and their version details are listed in the `requirements.txt` file. They can be easily installed with the `setup.py` script:
```
$ git clone https://github.com/mpinta/tracevec
$ cd tracevec
$ python setup.py install
```

## Usage
The project consists of five connecting parts, which are:
1. Training word embedding models
2. Clustering
3. Classification
4. Prediction
5. RNN Forecasting

Prepare your Pip or Anaconda environment and make sure you have all of the above dependencies installed. Then run the `tracevec.ipynb` notebook file, which stores and describes all the results of our training and model analysis. You can also restart or modify the code yourself, as it is fully equipped with the descriptive comments. Our `Word2Vec` and `Doc2Vec` models have also been added to the `models` directory, so you can skip model training part if you don't want to create new ones.

## Datasets
All data sets required to run the code are included in the repository. If you are running code without the included data sets, it is only necessary to clone the [tracebase repository](https://github.com/areinhardt/tracebase), which represents projects main data set, into the `datasets` directory. All the other modified data sets (`consumptions`, `samples`, `forecast-train` and `forecast-test`) are gradually created by the notebook code itself.

The **tracebase** data set is not our property and is used only as a depencency. For easier access to the data, its repository is also added as a submodule. We appreciate the work done by the authors.

#### Acknowledgements
_Contains information from the tracebase data set, which is made available at  [http://www.tracebase.org](http://www.tracebase.org/)  under the Open Database License (ODbL)._
