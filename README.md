# CS839 Data Science Project

## Group members
1. [Mohammed Danish Shaikh](https://github.com/danish778866)
2. [Somya Arora](https://github.com/srora)
3. [Swati Mishra](https://github.com/mishra-swati)

## Building and Running
```
> git clone https://github.com/danish778866/CS839_Project.git
> cd CS839_Project
> src/run.sh -h # Get help text
```

## Problem
The problem statements for each stage of this project can be found [here](https://sites.google.com/site/anhaidgroup/courses/cs-838-spring-2019/project-description)

## Organization
The organization of this repository is as follows:
* `README.md`: This README file.
* `build.sbt`: The build file for building with `sbt`.
* `stage_1`: The stage\_1 folder containing the following parts:
  - `src`: The folder containing the source code for stage 1.
  - `data`: The folder containing data retrieved and labeled for stage 1.
  - `fold_logs`: The folder containing cross validation logs.
  - `logs`: The folder containing accuracy logs for different classifiers.
  - `models`: The folder containing models that were trained on the train data
    set.
  - `report.pdf`: The stage 1 report.
