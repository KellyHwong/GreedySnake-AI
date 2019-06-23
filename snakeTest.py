#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06-08 20:54:50
# @Author  : Kelly Hwong (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from snake import *  # TODO fix: will import main
from utils import read_config
from SnakeAI import SnakeAI


def main():
    startx = random.randint(5, CELLWIDTH - 6)
    starty = random.randint(5, CELLHEIGHT - 6)
    # 以这个点为起点，建立一个长度为3格的贪吃蛇（数组）
    wormCoords = [(startx, starty),
                  (startx - 1, starty),
                  (startx - 2, starty)]
    snake = Snake(dim=(WORLD_WIDTH, WORLD_HEIGHT),
                  cells=wormCoords, direction=RIGHT)
    ai = SnakeAI(snake=snake)
    apple = getRandomLocation()
    game = SnakeGame(snake=snake, apple=apple, ai=ai)

    game.pygame.display.set_caption('Greedy Snake AI')  # 设置窗口的标题
    game.showStartScreen()  # 显示开始画面

    while True:
        # 这里一直循环于开始游戏和显示游戏结束画面之间，
        # 运行游戏里有一个循环，显示游戏结束画面也有一个循环
        # 两个循环都有相应的return，这样就可以达到切换这两个模块的效果
        # 你不会多线程？ by
        game.run()  # 运行游戏
        game.showGameOverScreen()  # 显示游戏结束画面


if __name__ == '__main__':
    main()
