# -*- coding: utf-8 -*-

"""
author = ‘wuzhiheng‘
time   = '2019-04-10 23:25'
"""
import abc
from entity.agent import RectangleAgent
import numpy as np
from entity.vector import RectangleVector


class Environment(metaclass=abc.ABCMeta):

    def __init__(self):
        self.rewards = None
        pass

    @abc.abstractmethod
    def get(self, action, treasuremap):
        pass


class RectangleEnvironment(Environment):

    def __init__(self, a: RectangleAgent):
        self.rewards = np.zeros(shape=(len(a.states), len(a.treasuremap.actions)
                                       ))
        for state in a.states:
            for action in a.treasuremap.actions:
                next_state = state + action
                if next_state.x >= a.treasuremap.graph.shape[0] or next_state.x < 0 or \
                        next_state.y >= a.treasuremap.graph.shape[1] or next_state.y < 0 or \
                        a.treasuremap.graph[next_state.x][next_state.y] == -1:
                    self.rewards[a.states.index(state)][a.treasuremap.actions.index(action)] = -1
                elif a.treasuremap.graph[next_state.x][next_state.y] == 1:
                    self.rewards[a.states.index(state)][a.treasuremap.actions.index(action)] = 1
                else:
                    self.rewards[a.states.index(state)][a.treasuremap.actions.index(action)] = 0
        return

    def get(self, a: RectangleAgent, action: RectangleVector):
        # print(self.rewards)
        # print(a.state, action)
        return self.rewards[a.states.index(a.state)][a.treasuremap.actions.index(action)]

