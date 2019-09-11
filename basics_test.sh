#!/bin/bash

pycodestyle style.py

pycodestyle get_column_stats.py

(for i in `seq 1 100`; do
    echo "$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM";
done )> data.txt

python get_column_stats.py --file_name data.txt --column_number 2


V=1
(for i in `seq 1 100`; do
    echo "$V\t$V\t$V\t$V\t$V";
done )> data.txt

python get_column_stats.py --column_number 2 --file_name data.txt

# test if file is empty
# test if file not ints
# test if call column outside of range

# add exit codes for failed tests

#(for i in `seq 1 100`; do
#    echo -e "$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM";
#done )> data.txt
