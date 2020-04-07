'''
Created on Dec 20, 2019

@author: prnsoft
'''
import pkgutil
import sys
import test


def a1_func():
    print("running a1_func()")
# search_path = ['.'] # set to None to see all modules importable from sys.path
# all_modules = [x[1] for x in pkgutil.iter_modules(path=search_path)]
# print(all_modules)
print(sys.path[0])