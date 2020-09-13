class A:
    def method(self):
        print('This belongs to class A')

class B(A):
    def method(self):
        print('This belongs to class B')
    pass
        
class C(A):
    def method(self):
        print('This belongs to class C')
    pass
        
class D(B,C):
    def method(self):
        print('This belongs to class D')
    pass

d = D()
d.method()