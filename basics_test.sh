#!/bin/bash

echo 'running test file basics_test.sh'

echo "checking python files' adherance to PEP8 style guide"

pycodestyle style.py

pycodestyle get_column_stats.py

pycodestyle basics_test.py

echo 'testing exception for FileNotFoundError'

python get_column_stats.py --file_name test.txt --column_number 2

echo 'testing a file of random integers'

(for i in `seq 1 100`; do
    echo "$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM";
done )> data.txt

python get_column_stats.py --file_name data.txt --column_number 2

echo 'testing exception for IndexError, column does not exist'

python get_column_stats.py --file_name data.txt --column_number 5

echo 'testing a file of 1s'

V=1
(for i in `seq 1 100`; do
    echo "$V\t$V\t$V\t$V\t$V";
done )> data.txt

python get_column_stats.py --column_number 2 --file_name data.txt

V='a'
W=1
(for i in `seq 1 100`; do
    echo "$V\t$W\t$V\t$W\t$V";
done )> data.txt

echo 'testing file with strings in a non-specified column'

python get_column_stats.py --file_name data.txt --column_number 1

echo 'testing exception for ValueError, column contains non integers'

python get_column_stats.py --file_name data.txt --column_number 2

echo 'tests complete'
