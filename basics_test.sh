#!/bin/bash

test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

echo 'running test file basics_test.sh'

echo "checking python files' adherance to PEP8 style guide"

pycodestyle style.py

pycodestyle get_column_stats.py

pycodestyle basics_test.py

echo 'testing exception for FileNotFoundError'

run main python get_column_stats.py --file_name test.txt --column_number 2
assert_in_stdout 'Could not find test.txt'
assert_no_stderr
assert_exit_code 1

echo 'testing a file of random integers'

A=$RANDOM
B=$RANDOM
C=$RANDOM
D=$RANDOM
E=$RANDOM

#(for i in `seq 1 100`; do
#    echo "$A\t$B\t$C\t$D\t$E";
#done )> data.txt

#run main python get_column_stats.py --file_name data.txt --column_number 2
#assert_in_stdout 'mean: '

#python get_column_stats.py --file_name data.txt --column_number 2

echo 'testing exception for IndexError, column does not exist'

run main python get_column_stats.py --file_name data.txt --column_number 5
assert_in_stdout 'Column number 5 does not exist'
assert_no_stderr
assert_exit_code 1

echo 'testing a file of 1s'

V=1
(for i in `seq 1 100`; do
    echo "$V\t$V\t$V\t$V\t$V";
done )> data.txt

run main python get_column_stats.py --file_name data.txt --column_number 2
assert_in_stdout 'mean: ' 1.0, 'stdev: ' 0.0
assert_no_stderr
assert_exit_code 0

V='a'
W=1
(for i in `seq 1 100`; do
    echo "$V\t$W\t$V\t$W\t$V";
done )> data.txt

echo 'testing file with strings in a non-specified column'

run main python get_column_stats.py --file_name data.txt --column_number 1
assert_in_stdout 'mean: ' 1.0, 'stdev: ' 0.0
assert_no_stderr
assert_exit_code 0

echo 'testing exception for ValueError, column contains non integers'

run main python get_column_stats.py --file_name data.txt --column_number 2
assert_in_stdout 'Column contains non integer values, unable to process'
assert_no_stderr
assert_exit_code 1

echo 'tests complete'
