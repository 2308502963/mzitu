#书上的面向对象章节的
'''
class HelloClass:
    """一个简单的类实例"""
    i=123456
    def f(self):
        return "hello world"
#实例化类
x=HelloClass()
print("类的i属性的值:",x.i)
print("类的方法:",x.f())
'''
'''
class Complex:
    def __init__(self,age,sex):
        self.r=age
        self.i=sex
    def info(self):
        if(self.r>18):
            print("这个孩子成年了")
        else:
            print("你还没有成年")
    def __del__(self):
        if(self.i=="男"):
            print("对象已被删除")
        else:
            print("对象也被删除")
x=Complex(20,"女")
print(x.r,x.i)
x.info()
del Complex
'''
'''
class Test:
    def prt(self):
        print(self)#地址
        print(self.__class__)#当前的类
t=Test()
t.prt()
'''

'''
class People:
    #定义基本属性
    name=""
    age=0
    #定义私有属性，私有属性在类外部无法直接进行访问
    __weight=0
    #定义构造方法
    def __init__(self,name,age,weight):
        self.name=name
        self.age=age
        self._weight=weight
    def speak(self):
        print("%s说：我%d岁了"%(self.name,self.age))
p=People("莫冉",20,50)
p.speak()

class Speaker():
    #定义基本属性
    name=""
    topic=""
    #定义构造方法
    def __init__(self,name,topic):
        self.name=name
        self.topic=topic
    def speak(self):
        print("我叫%s,我是一个演说家，我演讲的主题是%s"%(self.name,self,topic))

class Student(People):
    grade=0
    def __init__(self,name,age,weight,grade):
        People.__init__(self,name,age,weight)
        self.grade=grade
    #重写父类方法
    def speak(self):
        print("%s说，我今年%d岁了，我在读%d年级了"%(self.name,self.age,self.grade))
s=Student("莫冉",20,50,18)
s.speak()

class Sample(Student,Speaker):
    a=""
    def __init__(self,name,weight,age,grade,topic):
        Student.__init__(self,name,age,weight,grade)
        Speaker.__init__(self,name,topic)
    def speak(self):
        print("我叫%s,我今年%d岁了，我的体重是%d,我读%d年级了,我今天演讲的主题是%s"%(self.name,self.age,self._weight,self.grade,self.topic))
test=Sample("莫冉",50,20,18,"python")
test.speak()#方法名相同，默认调用继承的类的前面的方法???????好像不对
'''
'''
#方法的重载
class Parent:#定义父类
    def myMethod(self):
        print("这是父类")
class Child(Parent):
    def myMethod(self):
        print("这是子类")
c=Child()#子类的实例
c.myMethod()#子类调用重写方法
super(Child,c).myMethod()
'''

