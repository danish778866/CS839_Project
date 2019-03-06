#! /bin/bash
#
# run.sh
# Copyright (C) 2019 mohdanishaikh <mohdanishaikh@mohdanishaikh-Inspiron-7573>
#
# Distributed under terms of the MIT license.
#

SCRIPT=`basename ${BASH_SOURCE[0]}`
PROJECT_ROOT_DIR=$(dirname $(cd `dirname $0` && pwd))
LABELS_DIR="${PROJECT_ROOT_DIR}/data/labels"
CANDIDATES_DIR="${PROJECT_ROOT_DIR}/data/candidates"
FEATURES_DIR="${PROJECT_ROOT_DIR}/data/features"

CANDIDATES_FILE="${CANDIDATES_DIR}/candidates.csv"
SUFFIXES_FILE="${CANDIDATES_DIR}/suffixes.csv"
PREFIXES_FILE="${CANDIDATES_DIR}/prefixes.csv"
LABELS_FILE="${LABELS_DIR}/labels.csv"
FEATURES_FILE="${FEATURES_DIR}/features.csv"

COMBINE_FEATURES=0
COMBINE_CANDIDATES=0

# Set fonts for Help.
NORM=`tput sgr0`
BOLD=`tput bold`
REV=`tput smso`

# Help function
function HELP {
  echo -e \\n"Help documentation for ${BOLD}${SCRIPT}.${NORM}"\\n
  echo -e "${REV}Basic usage:${NORM} ${BOLD}$SCRIPT -d <hadoop path> -s <spark path> -t <task number>${NORM}"\\n
  echo "Command line switches are optional. The following switches are recognized."
  echo "${REV}-c${NORM}  --Indicates to combine the candidate files"
  echo "${REV}-f${NORM}  --Indicates to combine the features file"
  echo -e "${REV}-h${NORM}  --Displays this help message. No further functions are performed."\\n
  echo -e "Example: ${BOLD}$SCRIPT -c -f"
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

while getopts cfh FLAG; do
  case $FLAG in
    c)
      COMBINE_CANDIDATES=1
      ;;
    f)
      COMBINE_FEATURES=1
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

if [ $COMBINE_CANDIDATES -eq 1 ]
then
  if [ -f ${CANDIDATES_FILE} ]
  then
    rm -vf ${CANDIDATES_FILE}
  fi
  if [ -f ${PREFIXES_FILE} ]
  then
    rm -vf ${PREFIXES_FILE}
  fi
  if [ -f ${SUFFIXES_FILE} ]
  then
    rm -vf ${SUFFIXES_FILE}
  fi
  if [ -f ${LABELS_FILE} ]
  then
    rm -vf ${LABELS_FILE}
  fi
  pushd $CANDIDATES_DIR
    echo "candidates" > $CANDIDATES_FILE
    echo "prefixes" > $PREFIXES_FILE
    echo "suffixes" > $SUFFIXES_FILE
    for i in *.txt
    do
      cat $i >> $CANDIDATES_FILE
      cat "${i}.pre" >> $PREFIXES_FILE
      cat "${i}.suf" >> $SUFFIXES_FILE
    done
  popd
  pushd $LABELS_DIR
    echo "labels" > $LABELS_FILE
    for i in *.txt
    do
      cat $i >> $LABELS_FILE
    done
  popd
fi

if [ $COMBINE_FEATURES -eq 1 ]
then
  if [ -f ${FEATURES_FILE} ]
  then
    rm -vf ${FEATURES_FILE}
  fi
  pushd $FEATURES_DIR
    feature_files=`ls | tr "\n" " "`
    paste -d',' $CANDIDATES_FILE $PREFIXES_FILE $SUFFIXES_FILE $feature_files > ${FEATURES_FILE}
  popd
fi
