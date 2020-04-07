'''
Created on Dec 20, 2019

@author: prnsoft
'''
def baz():
    print("[mod3] baz()")
    
class Baz:
    pass

# from pkg.sub_pkg1.submod1 import foo
# foo()

from .. import sub_pkg1
print(sub_pkg1)

from ..sub_pkg1.submod1 import foo
foo()