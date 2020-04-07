'''
Created on Dec 23, 2019

@author: prnsoft
'''

class Purchase:
    def __init__(self, basket, buyer):
        self.basket = basket
        self. buyer = buyer
        
    def __len__(self):
        return len(self.basket)
    
purchase = Purchase(['pen', 'book', 'pencil'], 'Python')
print(len(purchase))

class A:
    def __init__(self, a):
        self.a = a
        
    def __add__(self, o):
        return self.a + o.a
    
ob1 = A(1)
ob2 = A(2)
ob3 = A("Geeks")
ob4 = A("For")

print(ob1 + ob2)
print(ob3 + ob4)

class Polynomial:
    
    def __init__(self, *coefficients):
        self.coefficients = coefficients[::-1]
        
    def __call__(self, x):
        res = 0
        for index, coeff in enumerate(self.coefficients):
            res += coeff * x** index
        return res

# a constant function
p1 = Polynomial(42)

# a straight Line
p2 = Polynomial(0.75, 2)

# a third degree Polynomial
p3 = Polynomial(1, -0.5, 0.75, 2)

for i in range(1, 10):
    print(i, p1(i), p2(i), p3(i))

if __name__ == '__main__':
    pass