#!/usr/bin/python
# -*- coding: utf-8 -*-


########################################################################################################################
# 字典常被用来组织结构化数据，判断value类型，配合不同处理，可以迭代地对结构化数据进行处理
########################################################################################################################
def aggregate(iterable):
    """
    有序聚合结构相同的字典

    data = [{'month': '2017-11', 'userTotal': 100}, {'month': '2017-12', 'userTotal': 101}]
    print aggregate(data)

    >> {'userTotal': [100, 101], 'month': ['2017-11', '2017-12']}
    """
    target = dict()
    assert len(filter(lambda x: isinstance(x, dict), iterable)) == len(iterable), 'Only aggregate dict.'
    for d in iterable:
        for k, v in d.items():
            if isinstance(v, (int, long, float, basestring)):
                target.setdefault(k, []).append(v)
            elif isinstance(v, list):
                temp = target.setdefault(k, [])
                temp += v
            elif isinstance(v, dict):
                target[k] = aggregate(v)
            else:
                pass
    return target


def count(self, d):
    """统计可迭代对象的长度"""
    target = {}
    for key, value in d.items():
        if isinstance(value, (list, tuple, set)):
            target[key] = len(value)
        elif isinstance(value, dict):
            target[key] = self.count(value)
        elif isinstance(value, int):
            target[key] = value
        else:
            pass
    return target


########################################################################################################################
# dict/tuple/list/custom object都可以用来组织结构化数据
# 通过sorted()函数，可以实现通过结构化数据的一个属性，指定排序方法，对结构化数据进行排序
########################################################################################################################
sorted([dict(a=3), dict(b=2), dict(c=4)], key=lambda d: d.values()[0])
