"""Calculate the mean and standard deviation of a column of integers

    * main - returns the mean and standard deviation of integers from a
    specified column from an input file
"""

import math
import argparse
import sys


def main():
    """
    Compute the mean and standard deviation of a column of integers.

    Parameters
    ----------
    --filename: Name of the file
        The input file to read, containing integers in columns

    --column_number: The column number
        An integer specifing which column number to compute

    Returns
    --------
    mean
        The mean of the column values

    stdev
        The standard deviation of the column values
    """
    parser = argparse.ArgumentParser(description='calc mean and stdev of '
                                     'a column', prog='get_column_stats')

    parser.add_argument('--file_name', type=str,
                        help='Name of the file', required=True)

    parser.add_argument('--column_number', type=int,
                        help='The column number', required=True)

    args = parser.parse_args()

    file_name = args.file_name
    col_num = args.column_number

    try:
        file = open(file_name, 'r')
    except FileNotFoundError:
        print('Could not find ' + file_name)
        sys.exit(1)
    except PermissionError:
        print('Could not open ' + file_name)
        sys.exit(1)

    V = []

    for line in file:
        try:
            A = [x for x in line.split()]
            V.append(int(A[col_num]))
        except ValueError:
            print('Column contains non integer values, unable to process')
            sys.exit(1)
        except IndexError:
            print('Column number ' + str(col_num) + ' does not exist')
            sys.exit(1)

    mean = sum(V)/len(V)

    stdev = math.sqrt(sum([(mean-x)**2 for x in V]) / len(V))

    print('mean:', mean)
    print('stdev:', stdev)


if __name__ == '__main__':
    main()
