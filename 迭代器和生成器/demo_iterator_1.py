# -*- coding: UTF-8 -*-

# 将迭代器写在可迭代对象中

# 定义一个迭代器

class myRange(object):
    """
    myRange是可迭代对象
    """
    def __init__(self, start=0, end=10):
        self.start = start
        self.end = end
        self.index = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.end:
            temp = self.index
            self.index += 1
            return temp
        else:
            raise StopIteration()

ret = myRange(1, 5)
for x in ret:
    print(x)

print('=====')
for y in ret:
    print(y)
# 使用iter()方法可以获取可迭代对象的迭代器：
# ret_iterator = iter(myRange(1, 5))
# while True:
#     try:
#         x = ret_iterator.__next__()
#         print(x)
#     except StopIteration:
#         break
