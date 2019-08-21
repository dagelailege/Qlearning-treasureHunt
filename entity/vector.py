# -*- coding: utf-8 -*-

"""
author = ‘wuzhiheng‘
time   = '2019-04-11 11:06'
"""
import abc
import hashlib
"""
定义动作和状态的形式
"""


class Vector(metaclass=abc.ABCMeta):

    def __init__(self):
        pass

    def __repr__(self):
        pass

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __getattribute__(self, item):
        pass

    def __eq__(self, other):
        pass

    def __ne__(self, other):
        pass

    def __hash__(self):
        pass


class RectangleVector(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "vector({}, {})".format(self.x, self.y)

    def __add__(self, other):
        return RectangleVector(self.x+other.x, self.y+other.y)

    def __sub__(self, other):
        return RectangleVector(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.x or self.y != other.y

