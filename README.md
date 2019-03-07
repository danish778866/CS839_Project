# CS839_Project

python preprocess.py -d test
./run.sh -c -d test
python features.py -d test
./run.sh -d test -f
python preprocess.py -d train
./run.sh -c -d train
python features.py -d train
./run.sh -d train -f
python classifiers.py -d train -t test -c svm -s
python classifiers.py -t test -c svm

