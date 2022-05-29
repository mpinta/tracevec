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
1. **Training word embedding models** (_using [Gensim](https://radimrehurek.com/gensim/) topic modelling library_)
2. **Clustering** (_Doc2Vec vectors into clusters_)
3. **Classification** (_of the electrical device type using Doc2Vec vectors_)
4. **Prediction** (_of the next electricity consumption category using Word2Vec vectors_)
5. **RNN Forecasting** (_the next electricity consumption category using RNN with GRU_)

First, prepare your Pip or Anaconda environment and make sure you have all of the above dependencies installed. Then open the `tracevec.ipynb` notebook file, which stores and describes all the results of our training and model analysis. You can also run and modify the code yourself, as it is fully equipped with the descriptive comments. You can find our `Word2Vec` and `Doc2Vec` models in the `models` directory (_skip the model part training if you don’t want to create new ones_).

## Datasets
All data sets required to run the code are included in the repository. If you are running code without the included data sets, it is only necessary to clone the [tracebase](https://github.com/areinhardt/tracebase) repository, which represents projects main data set, into the `datasets` directory. All the other modified data sets (_consumptions, samples, forecast-train and forecast-test_) are gradually created by the notebook code itself. The tracebase data set is not our property and is used only as a depencency (_submodule_) - we appreciate the work done by the authors. Make sure to initialize the submodule with:
```
$ git submodule init
$ git submodule update
```

## Publications
The code was originally used in the following publications:
```
Pintarič Matic, (2022).
S strojnim učenjem podprta analiza vzorcev vektorizirane porabe električne energije.
Maribor: University of Maribor, Faculty of Electrical Engineering and Computer Science.
```

#### Acknowledgements
_Contains information from the tracebase data set, which is made available at  [http://www.tracebase.org](http://www.tracebase.org/)  under the Open Database License (ODbL)._
