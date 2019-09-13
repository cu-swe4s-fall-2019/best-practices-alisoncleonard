# best-practices
## Software Engineering for Scientists Homework 1

# Project Description

This project tests our ability to format software development projects using
best practices. The project contains 3 main files:

1. style.py - a python file containing useless functions, formatted to conform
to the PEP8 style

summary of changes: formatted to conform to PEP8 style guide
based on changes indicated by pycodestyle

2. get_column-stats.py - a python file that takes an input file and column
number and returns the mean and standard deviation of that column

summary of changes: added docstrings, used argparse to handle
input arguments, put code inside a __main__ function, included try/except
statements to handle possible exceptions and added exit codes

3. basics_test.sh - a bash shell containing functional tests for
get_column_stats.py

summary of changes: added tests for unknown file, file containing non-integer
data, and column index out of range, added text explaining what tests are
running

# How to do math using *get_column_stats.py*

get_column_stats.py takes two required arguments: a text file containing
columns of integers (--file_name) and an integer specifying which column
to operate on (--column_number). This script returns the mean and standard
deviation of the integers in the specified column.

To process the column 2 of the file data.txt using get_column_stats.py, the
following code can be run from the command line:
'''
python get_column_stats.py --file_name test.txt --column_number 2
'''

Arguments and handled using argparse and can be called in either order.

If 'data.txt' contained the columns:

1 4 6 3 4
3 4 2 8 5
0 4 6 7 3
5 6 2 6 4

then the script would return the output:
'''
mean: 4.0
stdev: 2.0
'''

# How to install software


1. Ensure that conda is installed in your environment
If '$ conda' gives an error, install conda as required by your operating system

2. Update and configure conda
'''
$ conda update --yes conda
$ conda config --add channels bioconda
$ echo ". $HOME/miniconda3/etc/profile.d/conda.sh" >> $HOME/.bashrc
'''

3. Install python and required libraries
'''
$ conda install --yes python=3.6
$ conda install -y pycodestyle

4. Access software on [GitHub]
(https://github.com/cu-swe4s-fall-2019/best-practices-alisoncleonard)
