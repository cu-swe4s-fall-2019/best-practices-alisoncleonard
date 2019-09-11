import math
import argparse
import sys


def main():
    parser = argparse.ArgumentParser(description='calc mean and stdev of'
                                     'a column', prog='get_column_stats')

    parser.add_argument('--file_name', type=str,
                        help='Name of the file', required=True)

    parser.add_argument('--column_number', type=int,
                        help='The column number', required=True)

    args = parser.parse_args()

    file_name = args.file_name
    col_num = args.column_number

    try:
        f = open(file_name, 'r')
    except FileNotFoundError:
        print('Could not find ' + file_name)
        sys.exit(1)
    except PermissionError:
        print('Could not open ' + file_name)
        sys.exit(1)

    V = []

    for l in f:
        A = [int(x) for x in l.split()]
        V.append(A[col_num])

    mean = sum(V)/len(V)

    stdev = math.sqrt(sum([(mean-x)**2 for x in V]) / len(V))

    print('mean:', mean)
    print('stdev:', stdev)


if __name__ == '__main__':
    main()
