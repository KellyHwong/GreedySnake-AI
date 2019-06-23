#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06-11 20:48:04
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import random
import sys
import time
# import pygame
from pygame.locals import *
from constant import *
from SnakeAI import SnakeAI

# 特性 类的常量经过初始化后就不应该更改

# 游戏常量，世界大小
FPS = 5  # 屏幕刷新率（在这里相当于贪吃蛇的速度）
WINDOWWIDTH = 640  # 屏幕宽度
WINDOWHEIGHT = 480  # 屏幕高度
CELLSIZE = 20  # 小方格的大小

# 断言，屏幕的宽和高必须能被方块大小整除
assert WINDOWWIDTH % CELLSIZE == 0, "Window width must be a multiple of cell size."
assert WINDOWHEIGHT % CELLSIZE == 0, "Window height must be a multiple of cell size."

# 横向和纵向的方格数
CELLWIDTH = int(WINDOWWIDTH / CELLSIZE)
CELLHEIGHT = int(WINDOWHEIGHT / CELLSIZE)

WORLD_WIDTH = CELLWIDTH
WORLD_HEIGHT = CELLHEIGHT

GAME_MODE = "GAME_MODE"
AI_MODE = "AI_MODE"

# 定义几个常用的颜色
# R G B
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARKGREEN = (0, 155, 0)
DARKGRAY = (40, 40, 40)
BGCOLOR = BLACK


class Snake(object):
    """Implement a snake algorithm level class

    Please firstly init a cells list for the snake
    For printing/visualizing the snake, write a interface

    Note:
        NULL

    Args:
        dim (list): Dimensions of the snake world.
        cells (list): Coordinates of the snake.

    Attributes:
        msg (str): Human readable string describing the exception.
        code (int): Exception error code.

    """

    def __init__(self, dim, cells, direction=RIGHT):
        self.dim = dim
        self.cells = cells
        self.direction = direction

    def eat_apple(self, apple) -> bool:
        if self.cells[0][0] == apple[0] and self.cells[0][1] == apple[1]:
            return True  # 不移除蛇的最后一个尾巴格
        else:
            del self.cells[-1]  # 移除蛇的最后一个尾巴格
            return False

    def move(self):
        # 根据方向，添加一个新的蛇头，以这种方式来移动贪吃蛇
        if self.direction == UP:
            new_head = (self.cells[0][0], self.cells[0][1] - 1)
        elif self.direction == DOWN:
            new_head = (self.cells[0][0], self.cells[0][1] + 1)
        elif self.direction == LEFT:
            new_head = (self.cells[0][0] - 1, self.cells[0][1])
        elif self.direction == RIGHT:
            new_head = (self.cells[0][0] + 1, self.cells[0][1])
        # 插入新的蛇头在数组的最前面
        self.cells.insert(0, new_head)

    def alive(self):
        # 检查贪吃蛇是否撞到撞到边界
        if self.cells[0][0] == -1 or self.cells[0][0] == CELLWIDTH or self.cells[0][1] == -1 or self.cells[0][1] == CELLHEIGHT:
            return False  # game over
        # 检查贪吃蛇是否撞到自己
        for cell in self.cells[1:]:
            if cell[0] == self.cells[0][0] and cell[1] == self.cells[0][1]:
                return False  # game over
        return True


class SnakeGame(object):
    """Implement a snake pygame GUI level class

    Please firstly init a cells list for the snake
    For printing/visualizing the snake, write a interface

    Note:
        NULL

    Args:
        dim (list): Dimensions of the snake world.
        cells (list): Coordinates of the snake.

    Attributes:
        msg (str): Human readable string describing the exception.
        code (int): Exception error code.

    """

    def __init__(self, snake, apple=(0, 0), mode=GAME_MODE, ai=None):
        self.snake = snake
        self.apple = apple
        self.mode = mode
        self.ai = ai
        self.pygame = __import__("pygame")
        self.pygame.init()  # 初始化pygame
        # 定义全局变量 # Fix
        # global FPSCLOCK, DISPLAYSURF, self.BASICFONT
        self.FPSCLOCK = self.pygame.time.Clock()  # 获得pygame时钟
        self.DISPLAYSURF = self.pygame.display.set_mode(
            (WINDOWWIDTH, WINDOWHEIGHT))  # 设置屏幕宽高
        self.BASICFONT = self.pygame.font.Font(
            'PAPYRUS.ttf', 18)  # self.BASICFONT

    def turn(self):
        pass

    def run(self):
        while True:  # 游戏主循环
            for event in self.pygame.event.get():  # 事件处理
                if event.type == QUIT:  # 退出事件
                    self.terminate()
                elif event.type == KEYDOWN:  # 按键事件
                    # 用户按键
                    if self.ai is None:
                        # 如果按下的是左键或a键，且当前的方向不是向右，就改变方向，以此类推
                        if (event.key == K_LEFT or event.key == K_a) and self.snake.direction != RIGHT:
                            self.snake.direction = LEFT
                        elif (event.key == K_RIGHT or event.key == K_d) and self.snake.direction != LEFT:
                            self.snake.direction = RIGHT
                        elif (event.key == K_UP or event.key == K_w) and self.snake.direction != DOWN:
                            self.snake.direction = UP
                        elif (event.key == K_DOWN or event.key == K_s) and self.snake.direction != UP:
                            self.snake.direction = DOWN
                    else:  # AI Mode
                        self.snake.direction = self.ai.predict()
                    if event.key == K_ESCAPE:
                        self.terminate()

            if not self.snake.alive():
                return -1
            if self.snake.eat_apple(self.apple):
                self.apple = getRandomLocation()  # 重新随机生成一个apple
            self.snake.move()

            self.DISPLAYSURF.fill(BGCOLOR)  # 绘制背景
            self.drawGrid()
            self.drawWorm()
            self.drawApple()
            self.drawScore(len(self.snake.cells) - 3)  # 绘制分数（分数为贪吃蛇数组当前的长度-3）
            self.pygame.display.update()  # 更新屏幕
            self.FPSCLOCK.tick(FPS)  # 设置帧率

    def drawGrid(self):  # 绘制所有的方格
        for x in range(0, WINDOWWIDTH, CELLSIZE):  # draw vertical lines
            self.pygame.draw.line(self.DISPLAYSURF, DARKGRAY,
                                  (x, 0), (x, WINDOWHEIGHT))
        for y in range(0, WINDOWHEIGHT, CELLSIZE):  # draw horizontal lines
            self.pygame.draw.line(self.DISPLAYSURF, DARKGRAY,
                                  (0, y), (WINDOWWIDTH, y))

    def drawWorm(self):
        for coord in self.snake.cells:  # 根据 cells 数组绘制贪吃蛇
            x = coord[0] * CELLSIZE
            y = coord[1] * CELLSIZE
            wormSegmentRect = self.pygame.Rect(x, y, CELLSIZE, CELLSIZE)
            self.pygame.draw.rect(self.DISPLAYSURF, DARKGREEN, wormSegmentRect)
            wormInnerSegmentRect = self.pygame.Rect(
                x + 4, y + 4, CELLSIZE - 8, CELLSIZE - 8)
            self.pygame.draw.rect(self.DISPLAYSURF, GREEN,
                                  wormInnerSegmentRect)

    def drawApple(self):  # 根据 coord 绘制 apple
        x = self.apple[0] * CELLSIZE
        y = self.apple[1] * CELLSIZE
        appleRect = self.pygame.Rect(x, y, CELLSIZE, CELLSIZE)
        self.pygame.draw.rect(self.DISPLAYSURF, RED, appleRect)

    def drawScore(self, score):  # 绘制分数
        scoreSurf = self.BASICFONT.render('Score: %s' % (score), True, WHITE)
        scoreRect = scoreSurf.get_rect()
        scoreRect.topleft = (WINDOWWIDTH - 120, 10)
        self.DISPLAYSURF.blit(scoreSurf, scoreRect)

    def showStartScreen(self):  # 显示开始画面
        self.DISPLAYSURF.fill(BGCOLOR)
        titleFont = self.pygame.font.Font('PAPYRUS.ttf', 100)
        titleSurf = titleFont.render('Wormy!', True, GREEN)
        titleRect = titleSurf.get_rect()
        titleRect.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)
        self.DISPLAYSURF.blit(titleSurf, titleRect)
        self.drawPressKeyMsg()
        self.pygame.display.update()
        while True:
            if self.checkForKeyPress():
                self.pygame.event.get()  # clear event queue
                return

    def showGameOverScreen(self):
        # 显示游戏结束画面
        gameOverFont = self.pygame.font.Font('PAPYRUS.ttf', 50)
        gameSurf = gameOverFont.render('Game', True, WHITE)
        overSurf = gameOverFont.render('Over', True, WHITE)
        gameRect = gameSurf.get_rect()
        overRect = overSurf.get_rect()
        gameRect.midtop = (WINDOWWIDTH / 2, WINDOWHEIGHT /
                           2-gameRect.height-10)
        overRect.midtop = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)

        self.DISPLAYSURF.blit(gameSurf, gameRect)
        self.DISPLAYSURF.blit(overSurf, overRect)
        self.drawPressKeyMsg()
        self.pygame.display.update()
        self.pygame.time.wait(500)
        self.checkForKeyPress()  # clear out any key presses in the event queue

        while True:
            if self.checkForKeyPress():
                self.pygame.event.get()  # clear event queue
                return

    def drawPressKeyMsg(self):  # 绘制提示消息
        pressKeySurf = self.BASICFONT.render(
            'Press a key to play.', True, DARKGRAY)
        pressKeyRect = pressKeySurf.get_rect()
        pressKeyRect.topleft = (WINDOWWIDTH - 200, WINDOWHEIGHT - 30)
        self.DISPLAYSURF.blit(pressKeySurf, pressKeyRect)

    def checkForKeyPress(self):  # 检查按键是否有按键事件
        if len(self.pygame.event.get(QUIT)) > 0:
            self.terminate()
        keyUpEvents = self.pygame.event.get(KEYUP)
        if len(keyUpEvents) == 0:
            return None
        if keyUpEvents[0].key == K_ESCAPE:
            self.terminate()
        return keyUpEvents[0].key

    def terminate(self):  # 退出
        self.pygame.quit()
        sys.exit()


def getRandomLocation():  # 随机生成一个坐标位置
    return (random.randint(0, CELLWIDTH - 1), random.randint(0, CELLHEIGHT - 1))
