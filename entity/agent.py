# -*- coding: utf-8 -*-

"""
author = ‘wuzhiheng‘
time   = '2019-04-10 23:06'
"""
import abc
from entity.vector import RectangleVector
from entity.treasureMap import RectangleTreasureMap
import numpy as np
from random import randint, choice
import random
import tkinter as tk
import time


class Agent(metaclass=abc.ABCMeta):

    def __init__(self):
        self.state = None
        self.qtable = None

    @abc.abstractmethod
    def set_state(self, state):
        pass

    @abc.abstractmethod
    def strategy(self):
        """
        选择动作的策略
        :return:
        """
        pass

    @abc.abstractmethod
    def rand_start(self):
        pass

    @abc.abstractmethod
    def show_init(self):
        pass

    @abc.abstractmethod
    def show_update(self):
        pass


class RectangleAgent(Agent):

    def __init__(self, treasuremap: RectangleTreasureMap):
        self.state = None
        self.treasuremap = treasuremap
        self.states = self.all_states()
        self.qtable = np.zeros(shape=(len(self.states), len(self.treasuremap.actions)))
        for state in self.states:
            for action in self.treasuremap.actions:
                self.qtable[self.states.index(state)][self.treasuremap.actions.index(action)] = 0.0
        return

    def all_states(self):
        states = []
        for i in range(self.treasuremap.graph.shape[0]):
            for j in range(self.treasuremap.graph.shape[1]):
                states.append(RectangleVector(i, j))
        return states

    def set_state(self, state):
        self.state = state

    # epsilon-greedy epsilon概率随机选择，1-epsilon选择最优的路径
    def strategy(self) -> RectangleVector:
        epsilon = 0.3
        r = random.random()
        if r < epsilon:
            return choice(self.treasuremap.actions)
        else:
            # print(self.state)
            # print(self.qtable[self.states.index(self.state)])
            return self.treasuremap.actions[np.argmax(self.qtable[self.states.index(self.state)])]

    def rand_start(self):
        s = RectangleVector(randint(0, self.treasuremap.graph.shape[0]-1),
                            randint(0, self.treasuremap.graph.shape[1]-1))
        return s

    def show_init(self):
        self.root = tk.Tk()
        self.root.geometry("900x700")
        self.cv = tk.Canvas(self.root, bg='white', height=800, width=600)
        self.cv.pack()
        for i in range(self.treasuremap.graph.shape[0]):
            for j in range(self.treasuremap.graph.shape[1]):
                row = 10 + i * 100
                col = 100 + j * 100
                if self.treasuremap.graph[i][j] == 1:
                    self.cv.create_rectangle(row, col, 100 + row, 100 + col, fill="yellow", tag="treasure")
                elif self.treasuremap.graph[i][j] == -1:
                    self.cv.create_rectangle(row, col, 100 + row, 100 + col, fill="black", tag="trap")
                else:
                    self.cv.create_rectangle(row, col, 100 + row, 100 + col)
        self.cv.create_rectangle(10, 100, 110, 200, fill="red", tag="robot")
        return

    def show_update(self, s: RectangleVector):
        time.sleep(.5)
        row = 10 + 100 * s.x
        col = 100 + 100 * s.y
        self.cv.coords("robot", (row, col, 100 + row, 100 + col))
        self.cv.update()

    def show_clear(self):
        self.cv.quit()
        self.root.quit()
        return




