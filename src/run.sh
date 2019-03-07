#! /bin/bash
#
# run.sh
# Copyright (C) 2019 mohdanishaikh <mohdanishaikh@mohdanishaikh-Inspiron-7573>
#
SCRIPT=`basename ${BASH_SOURCE[0]}`

CLASSIFIER=""
SAVE_MODEL=0
DEV_DIR_NAME=""
TEST_DIR_NAME=""

# Set fonts for Help.
NORM=`tput sgr0`
BOLD=`tput bold`
REV=`tput smso`

# Help function
function HELP {
  echo -e \\n"Help documentation for ${BOLD}${SCRIPT}.${NORM}"\\n
  echo -e "${REV}Basic usage:${NORM} ${BOLD}$SCRIPT -d <dev_data_dir_name> -t <test_data_dir_name> -c [svm|regression|random|decision] [-s]${NORM}"\\n
  echo "Command line switches are optional. The following switches are recognized."
  echo "${REV}-c${NORM}  --The classifier to train and test the data on, can take the values svm, regression, random and decision"
  echo "${REV}-s${NORM}  --Indicates whether to save the model or not"
  echo "${REV}-d${NORM}  --The data directory name for dev data set"
  echo "${REV}-t${NORM}  --The data directory name for test data set"
  echo -e "${REV}-h${NORM}  --Displays this help message. No further functions are performed"\\n
  echo -e "Examples"
  echo -e "Train, test and save model on svm : ${BOLD}$SCRIPT -d train -t test -c svm -s${NORM}"
  echo -e "Train and save model on svm : ${BOLD}$SCRIPT -d train -c svm -s${NORM}"
  echo -e "Train and test model on svm : ${BOLD}$SCRIPT -d train -t test -c svm${NORM}"
  echo -e "Train model on svm : ${BOLD}$SCRIPT -d train -c svm${NORM}"
  echo -e "Test saved model on svm : ${BOLD}$SCRIPT -t test -c svm${NORM}"
  exit 1
}

# Check the number of arguments. If none are passed, print help and exit.
NUMARGS=$#
echo -e \\n"Number of arguments: $NUMARGS"
if [ $NUMARGS -eq 0 ]; then
  HELP
fi

### Start getopts code ###

#Parse command line flags
#If an option should be followed by an argument, it should be followed by a ":".
#Notice there is no ":" after "h". The leading ":" suppresses error messages from
#getopts. This is required to get my unrecognized option code to work.

while getopts :c:sd:t:eh FLAG; do
  case $FLAG in
    c)
      CLASSIFIER=$OPTARG
      ;;
    s)
      SAVE_MODEL=1
      ;;
    d)
      DEV_DIR_NAME=$OPTARG
      ;;
    t)
      TEST_DIR_NAME=$OPTARG
      ;;
    h)  #show help
      HELP
      ;;
    \?) #unrecognized option - show help
      echo -e \\n"Option -${BOLD}$OPTARG${NORM} not allowed."
      HELP
      ;;
  esac
done

shift $((OPTIND-1))  #This tells getopts to move on to the next argument.

function combine_features {
  candidates_dir=$1
  labels_dir=$2
  features_dir=$3
  candidates_file="${candidates_dir}/candidates.csv"
  suffixes_file="${candidates_dir}/suffixes.csv"
  prefixes_file="${candidates_dir}/prefixes.csv"
  labels_file="${labels_dir}/labels.csv"
  features_file="${features_dir}/features.csv"
  pushd $features_dir
    feature_files=`ls | tr "\n" " "`
    paste -d',' $candidates_file $prefixes_file $suffixes_file $feature_files > ${features_file}
  popd
}

function combine_candidates_labels {
  candidates_dir=$1
  labels_dir=$2
  candidates_file="${candidates_dir}/candidates.csv"
  suffixes_file="${candidates_dir}/suffixes.csv"
  prefixes_file="${candidates_dir}/prefixes.csv"
  labels_file="${labels_dir}/labels.csv"
  pushd $candidates_dir
    echo "candidates" > $candidates_file
    echo "prefixes" > $prefixes_file
    echo "suffixes" > $suffixes_file
    for i in *.txt
    do
      cat $i >> $candidates_file
      cat "${i}.pre" >> $prefixes_file
      cat "${i}.suf" >> $suffixes_file
    done
  popd
  pushd $labels_dir
    echo "labels" > $labels_file
    for i in *.txt
    do
      cat $i >> $labels_file
    done
  popd
}

PROJECT_ROOT_DIR=$(dirname $(cd `dirname $0` && pwd))
PROJECT_SRC_DIR="${PROJECT_ROOT_DIR}/src"
PROJECT_DATA_DIR="${PROJECT_ROOT_DIR}/data"
PROJECT_MODELS_DIR="${PROJECT_ROOT_DIR}/models"
PROJECT_LOGS_DIR="${PROJECT_ROOT_DIR}/logs"
LOG_FILE="${PROJECT_LOGS_DIR}/${CLASSIFIER}.log"
if [ ! -d "${PROJECT_LOGS_DIR}" ]
then
  mkdir ${PROJECT_LOGS_DIR}
fi
if [ ! -z ${DEV_DIR_NAME} ]
then
  dev_dir="${PROJECT_DATA_DIR}/${DEV_DIR_NAME}"
  dev_candidates_dir="${dev_dir}/candidates"
  dev_labels_dir="${dev_dir}/labels"
  dev_features_dir="${dev_dir}/features"
fi
if [ ! -z ${TEST_DIR_NAME} ]
then
  test_dir="${PROJECT_DATA_DIR}/${TEST_DIR_NAME}"
  test_candidates_dir="${test_dir}/candidates"
  test_labels_dir="${test_dir}/labels"
  test_features_dir="${test_dir}/features"
fi
if [ ! -z ${DEV_DIR_NAME} ] && [ ! -z ${CLASSIFIER} ]
then
  echo "Cleaning ${dev_dir} directory candidates, labels and features..."
  pushd ${dev_dir}
    rm -rf ${dev_candidates_dir}
    rm -rf ${dev_labels_dir}
    rm -rf ${dev_features_dir}
  popd
  echo "Cleaning ${test_dir} directory candidates, labels and features..."
  pushd ${test_dir}
    rm -rf ${test_candidates_dir}
    rm -rf ${test_labels_dir}
    rm -rf ${test_features_dir}
  popd
  pushd ${PROJECT_SRC_DIR}
    echo "Preprocessing and generating features for ${DEV_DIR_NAME}..."
    python preprocess.py -d ${DEV_DIR_NAME}
    combine_candidates_labels "${dev_candidates_dir}" "${dev_labels_dir}"
    python features.py -d ${DEV_DIR_NAME}
    combine_features "${dev_candidates_dir}" "${dev_labels_dir}" "${dev_features_dir}"
    if [ ! -z ${TEST_DIR_NAME} ]
    then
      echo "Preprocessing and generating features for ${TEST_DIR_NAME}..."
      python preprocess.py -d ${TEST_DIR_NAME}
      combine_candidates_labels "${test_candidates_dir}" "${test_labels_dir}"
      python features.py -d ${TEST_DIR_NAME}
      combine_features "${test_candidates_dir}" "${test_labels_dir}" "${test_features_dir}"
    fi
    if [ ${SAVE_MODEL} -eq 1 ] && [ ! -z ${TEST_DIR_NAME} ]
    then
      echo "Training, testing and saving ${CLASSIFIER} model..."
      python classifiers.py -d ${DEV_DIR_NAME} -t ${TEST_DIR_NAME} -c ${CLASSIFIER} -s > ${LOG_FILE}
    elif [ ${SAVE_MODEL} -eq 1 ]
    then
      echo "Training and saving ${CLASSIFIER} model..."
      python classifiers.py -d ${DEV_DIR_NAME} -c ${CLASSIFIER} -s > ${LOG_FILE}
    elif [ ! -z ${TEST_DIR_NAME} ]
    then
      echo "Training and testing ${CLASSIFIER} model..."
      python classifiers.py -d ${DEV_DIR_NAME} -t ${TEST_DIR_NAME} -c ${CLASSIFIER} > ${LOG_FILE}
    else
      echo "Training ${CLASSIFIER} model..."
      python classifiers.py -d ${DEV_DIR_NAME} -c ${CLASSIFIER} > ${LOG_FILE}
    fi
    echo "Execution completed, logs available at ${LOG_FILE}..."
  popd
elif [ ! -z ${TEST_DIR_NAME} ] && [ ! -z ${CLASSIFIER} ] && [ $SAVE_MODEL -eq 0 ]
then
  echo "Testing pre-saved ${CLASSIFIER} model..."
  python classifiers.py -t ${TEST_DIR_NAME} -c ${CLASSIFIER} > ${LOG_FILE}
  echo "Execution completed, logs available at ${LOG_FILE}..."
fi
exit 0
