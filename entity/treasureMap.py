# -*- coding: utf-8 -*-

"""
author = ‘wuzhiheng‘
time   = '2019-04-10 22:47'
"""
import abc
import numpy as np
from entity.vector import RectangleVector


class TreasureMap(metaclass=abc.ABCMeta):
    """
    表示一张藏宝图的抽象类
    """

    def __init__(self, graph):
        self.graph = graph
        self.actions = None
        pass

    @abc.abstractmethod
    def __repr__(self) -> str:
        return str(self.graph)

    @abc.abstractmethod
    def show(self):
        pass


class RectangleTreasureMap(TreasureMap):
    """
    矩形藏宝图，藏宝图是一个np数组，1表示宝藏位置，-1表示陷阱位置，0表示正常路径
    """
    def __init__(self, graph: np.array):
        self.actions = [RectangleVector(-1, 0), RectangleVector(1, 0),
                        RectangleVector(0, -1), RectangleVector(0, 1)]
        self.graph = graph

    def __repr__(self) -> str:
        return self.graph

    def show(self):
        pass



