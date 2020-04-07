'''
Created on Dec 9, 2019

@author: prnsoft
'''

import argparse
from test.bisect import parse_args
parser = argparse.ArgumentParser()
parser.add_argument("square", help="display a square of a given number")
args = parser.parse_args()
print(int(args.square)**2)


if __name__ == '__main__':
    pass