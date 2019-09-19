"""
Calculate the mean and standard deviation of a column of integers


    * mean - returns the mean of a list of integers

    * stdev - returns the standard deviation of a list of integers

    * main - uses the functions mean and stdev to print the mean and standard
    deviation of a specified column of integers from an input text file
"""

import math
import argparse
import sys
import random


def mean(int_list):
    """
    Compute the mean of a list of integers

    Parameters
    -----------
    int_list: A list of integers

    Returns
    --------
    The mean of int_list
    """
    try:
        if int_list == []:
            print('An empty list does not have a mean')
            return None
        else:
            return sum(int_list)/len(int_list)
    except TypeError:
        print('argument for mean(int_list) must be a list of integers')
        raise TypeError
        sys.exit(1)


def stdev(int_list):
    """
    Compute the population standard deviation of a list of integers

    Parameters
    -----------
    int_list: A list of integers

    Returns
    --------
    The population standard deviation of int_list
    """
    try:
        if int_list == []:
            print('An empty list does not have a standard deviation')
            return None
        else:
            list_mean = mean(int_list)
            return math.sqrt(sum([(list_mean-x)**2 for x in int_list]) /
                             len(int_list))
    except TypeError:
        print('argument for stdev(int_list) must be a list of integers')
        raise TypeError
        sys.exit(1)


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
    colunn_mean
        The mean of the column values

    column_stdev
        The standard deviation of the column values

    Prints the output:
    mean: column_mean
    stdev: column_stdev
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

    column_mean = mean(V)
    column_stdev = stdev(V)

    print('mean:', column_mean)
    print('stdev:', column_stdev)


if __name__ == '__main__':
    main()
