
# -*- coding: UTF-8 -*-

# 迭代器
# 什么是迭代器：
# 通过迭代器，使我们访问集合的是变得方便。我们使用for...in...的方式访问一个集合的时候，就是使用迭代器完成的
# 如果没有迭代器，我们只能使用while循环

# 可迭代的对象：可以使用for循环来遍历的对象就是可迭代对象，常见的可迭代对象：list、tuple、set、str、dict、以及生成器
# 如果一个对象有__iter__这个方法，并且这个方法会返回一个迭代器对象，这种对象就是可迭代对象

from collections import Iterable, Iterator
# 列表是可迭代对象
ret = isinstance([1, 2, 3], Iterable)
print(ret)
ret = isinstance('abc', Iterable)
print(ret)
ret = isinstance(123, Iterable)
print(ret)

# 使用iter函数来构造一个可迭代对象

class Myrange(object):
    def __iter__(self):
        pass

ret = isinstance(Myrange(), Iterable)
print(ret)

# 迭代器：
# 1、在python2中，实现了next方法和__iter__方法，并且在这个方法中返回了值的对象，叫做迭代器对象
# 2、在python3中，实现了__next__方法和__iter__方法，并且这个方法返回了值的对象，叫做迭代器对象
# 3、如果迭代器没有返回值了，那么在next或者__next__中抛出一个StopIteration异常

# 判断一个对象是否是迭代器对象
class MyRange(object):
    def __iter__(self):
        pass

    def __next__(self):
        pass

ret = isinstance(MyRange(), Iterator)
print(ret)


# 自定义一个可使用for循环遍历的类->myRange

# 定义一个迭代器
class myRangeIterator(object):

    def __init__(self, start=0, end=10):
        self.index = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.end:
            temp = self.index
            self.index += 1
            return temp
        else:
            raise StopIteration()


class myRange(object):
    """
    myRange是可迭代对象
    """
    def __init__(self, start=0, end=10):
        self.start = start
        self.end = end

    def __iter__(self):
        # 这个方法要返回一个迭代器对象
        return myRangeIterator(self.start, self.end)

for x in myRange(1, 5):
    print(x)

# 使用iter()方法可以获取可迭代对象的迭代器：
ret_iterator = iter(myRange(1, 5))
while True:
    try:
        x = ret_iterator.__next__()
        print(x)
    except StopIteration:
        break
