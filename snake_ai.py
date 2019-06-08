#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06-08 20:58:32
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from snake import UP, DOWN, LEFT, RIGHT


class SnakeAI(object):
    """Implement a snake AI class

    Please pass into a snake class reference first

    Note:
        NULL

    Args:
        snake (Snake): The snake instance reference.

    Attributes:
        msg (str): Human readable string describing the exception.

    """

    def __init__(self, snake):
        self.snake = snake

    def predict(self):
        """Prediction function. Return which direction the snake should go for next step.

        Args:
            self

        Returns:
            direction: Direction for the next step.
        """

        # 会根据当前蛇🐍的状态，预测下一步怎么走
        # 当前cells位置，apple位置，direction
        # 输出(next)direction
        direction = RIGHT
        return direction


def main():
    pass


if __name__ == "__main__":
    main()
