# [CS839 Data Science Project Stage1](https://danish778866.github.io/DataScience/stage_1.html)

## Building and Running

### Clone Repository
```
> git clone https://github.com/danish778866/CS839_Project.git
> cd CS839_Project/stage_1
```

### Install Dependencies
```
> pip install -U scikit-learn
> pip install -U nltk
> pip install -U gensim
> python
> import nltk
> nltk.download('wordnet') # Download NLTK Wordnet Corpus
```

### Combine word2vec Google Model
```
> cd models/third_party
> cat word2vec_google_* > GoogleNews-vectors-negative300.bin
> md5sum GoogleNews-vectors-negative300.bin # Verify the md5sum to be 023bfd73698638bdad5f84df53404c8b
```

### Run
```
> src/run.sh -h # Get help text
```

## Organization
The organization of this stage is as follows:
* `README.md`: This README file.
* `src`: The folder containing the source code for stage 1.
* `data`: The folder containing data retrieved and labeled for stage 1.
* `fold_logs`: The folder containing cross validation logs.
* `logs`: The folder containing accuracy logs for different classifiers.
* `models`: The folder containing models that were trained on the train data
* set.
* `report.pdf`: The stage 1 report.
