# -*- coding: utf-8 -*-

"""
author = ‘wuzhiheng‘
time   = '2019-04-11 23:46'
"""

import numpy as np
from entity.agent import RectangleAgent
from entity.treasureMap import RectangleTreasureMap
from entity.environment import RectangleEnvironment
from entity.vector import RectangleVector


def main():
    graph_init = np.array([[0, 0, 0, -1, 0],
                      [0, 0, 1, 0, 0],
                      [-1, -1, 0, -1, 0],
                      [0, -1, 0, 0, 0],
                      [0, 0, 0, 0, 0]])
    graph = RectangleTreasureMap(graph=graph_init)
    robot = RectangleAgent(treasuremap=graph)
    env = RectangleEnvironment(a=robot)
    # 学习阶段
    learn_times = 2000
    # gamma = 0.5
    for i in range(learn_times):
        print("==================================================================")
        print("start learn: {}".format(i))
        robot.state = robot.rand_start()
        print("{}".format(robot.state))
        while 0 <= robot.state.x < robot.treasuremap.graph.shape[0] and \
                0 <= robot.state.y < robot.treasuremap.graph.shape[1] and \
                robot.treasuremap.graph[robot.state.x][robot.state.y] != -1 and \
                robot.treasuremap.graph[robot.state.x][robot.state.y] != 1:
            action = robot.strategy()
            print("action: {}".format(action))

            reward = env.get(robot, action)
            print("reward: {}".format(reward))
            if (robot.state + action) not in robot.states:
                next_sa = 0
            else:
                next_sa = max(robot.qtable[robot.states.index(robot.state + action)])
            robot.qtable[robot.states.index(robot.state)][robot.treasuremap.actions.index(action)] =  \
                0.5*robot.qtable[robot.states.index(robot.state)][robot.treasuremap.actions.index(action)] + \
                0.5 * (reward + 0.5*next_sa)
            robot.state = robot.state+action
            print("{}".format(robot.state))
    print(robot.qtable)

    # 运行阶段
    tests = [RectangleVector(0, 4), RectangleVector(2, 4),
             RectangleVector(3, 4), RectangleVector(4, 4),
             RectangleVector(4, 3), RectangleVector(3, 0),
             RectangleVector(0, 0), RectangleVector(1, 0),
             RectangleVector(0, 1)]
    i = 0
    robot.show_init()
    for state in tests:#robot.states:
        i += 1
        robot.state = state
        if robot.treasuremap.graph[robot.state.x][robot.state.y] == -1:
            continue
        print("==================================================================================")
        print("start run: {}".format(i))
        print(robot.state)
        while 0 <= robot.state.x <= robot.treasuremap.graph.shape[0] and \
                0 <= robot.state.y <= robot.treasuremap.graph.shape[1] and \
                robot.treasuremap.graph[robot.state.x][robot.state.y] != -1 and \
                robot.treasuremap.graph[robot.state.x][robot.state.y] != 1:
            robot.show_update(robot.state)
            action = robot.treasuremap.actions[np.argmax(robot.qtable[robot.states.index(robot.state)])]
            robot.state = robot.state+action
            print("{}".format(robot.state))
        robot.show_update(robot.state)
    robot.show_clear()
    return


if __name__ == '__main__':
    main()

