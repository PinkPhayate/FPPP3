# FaultPronePredictionProject(V3)

This repository works to get product metrics and process metrics in order to [predict FP-module.](https://github.com/PinkPhayate/FP-Predict)

### Environment

+ macOS
+ Python 3.5.1([Python2 ver](https://github.com/PinkPhayate/FPPP))
+ some modules

### Input

+ current version
+ source files from previous version
+ source files from current version (predicted version)

### Product Metrics

+ LOC    number of total line
+ TChar  number of total character
+ CL     number of code line
+ TComm  number of comment line
+ MChar  number of comment characters
+ DChar  number of code characters

-- Working now --


### Process Metrics

+ measure 8 metrics written in article[1]

### Execution
1. put target source code in 'target' directory.

for example...

```
MainDir
  |-README.md
  |-src
  |-test-data
  |-target
        |-previous-version
                  |-source codes
        |- current-version
                  |-source codes
```
2. operate python command below in terminal
  + param1: root directory having target source codes
  + param2: directory name having target file in current version
  + param3: directory name having target file in previous version

for example...
```python
python -B ./src/main.py target current-version previous-version
```

### Reference

[1]Nagappan N, Ball T. Use of Relative Code Churn Measures to Predict. Proc. 27th Int. Conf. on Softw. Eng., ICSE’5, 2005, pp284-282.
